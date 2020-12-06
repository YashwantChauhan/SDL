from django.shortcuts import render,redirect
from .forms import files_form
from .models import files,Recommend,Results,History,Contact
from django.contrib.auth.decorators import login_required
import csv
import pandas as pd
import joblib
import numpy as np

sc = joblib.load(r'Model/scaler')
clfr = joblib.load(r'Model/learner')

@login_required(login_url='logout/')
def index(request):
    return render(request , 'Dashb.html')

def logout(request):
    return redirect('/Signout')

def home(request):
    return redirect('/')

def detect(request):
    form = files_form(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        form = files_form()
        obj = files.objects.get(activated=False)
        columns = [ 'duration',
                    'protocol_type',
                    'service',
                    'flag',
                    'src_bytes',
                    'dst_bytes',
                    'land',
                    'wrong_fragment',
                    'urgent',
                    'hot',
                    'num_failed_logins',
                    'logged_in',
                    'num_compromised',
                    'root_shell',
                    'su_attempted',
                    'num_root',
                    'num_file_creations',
                    'num_shells',
                    'num_access_files',
                    'num_outbound_cmds',
                    'is_host_login',
                    'is_guest_login',
                    'count',
                    'srv_count',
                    'serror_rate',
                    'srv_serror_rate',
                    'rerror_rate',
                    'srv_rerror_rate',
                    'same_srv_rate',
                    'diff_srv_rate',
                    'srv_diff_host_rate',
                    'dst_host_count',
                    'dst_host_srv_count',
                    'dst_host_same_srv_rate',
                    'dst_host_diff_srv_rate',
                    'dst_host_same_src_port_rate',
                    'dst_host_srv_diff_host_rate',
                    'dst_host_serror_rate',
                    'dst_host_srv_serror_rate',
                    'dst_host_rerror_rate',
                    'dst_host_srv_rerror_rate',
                    'target' ]
        Attacks = ""
        jam = {}
        with open(obj.file_name.path , 'r' ) as f:
            reader = csv.reader(f)

            for i,row in enumerate(reader):
                if i==0:
                    pass
                else:
                    df = pd.DataFrame(columns=columns)
                    df.loc[0] = row
                    df.drop('num_root', axis = 1, inplace = True) 
                    df.drop('srv_serror_rate', axis = 1, inplace = True) 
                    df.drop('srv_rerror_rate', axis = 1, inplace = True) 
                    df.drop('dst_host_srv_serror_rate', axis = 1, inplace = True) 
                    df.drop('dst_host_serror_rate', axis = 1, inplace = True) 
                    df.drop('dst_host_rerror_rate', axis = 1, inplace = True) 
                    df.drop('dst_host_srv_rerror_rate', axis = 1, inplace = True) 
                    df.drop('dst_host_same_srv_rate', axis = 1, inplace = True) 
                    df.drop( 'num_outbound_cmds', axis =1 , inplace = True)
                    df.drop( 'is_host_login', axis =1 , inplace = True)

                    pmap = { 'icmp' : 0 , 'tcp' : 1 , 'udp': 2 }
                    df['protocol_type']=df['protocol_type'].map(pmap)

                    fmap = {'SF':0, 'S0':1, 'REJ':2, 'RSTR':3, 'RSTO':4, 'SH':5, 'S1':6, 'S2':7, 'RSTOS0':8, 'S3':9, 'OTH':10} 
                    df['flag'] = df['flag'].map(fmap)

                    df.drop( 'service' ,  axis = 1 , inplace = True )
                    df.drop( 'target' ,  axis = 1 , inplace = True )

                    X = df
                    Y = clfr.predict(X)
                    Y = np.array_str(Y)
                    if Y not in jam:
                        Attacks += Y + "-"
                        jam[Y] = '1'
                    


        Attacks = Attacks[:-1]           
        obj.Results = Attacks
        
        obj.save()
        return redirect('/Dashboard/results' )

    return render(request,'detect.html',{'form':form})

def results(request):
    obj = files.objects.get(activated=False)
    val = list(obj.Results.split('-'))
    s = "normal"
    context = []
    for i in val:
        if i != "['normal']":
            s = "attack"
            obj_1 = Results.objects.get(key=i)
            context.append(obj_1)
            obj_1.activated=False
            obj_1.save()

    if s=="normal":
        f = ['normal']
        obj_1 = Results.objects.get(key=f)
        context.append(obj_1)
        obj_1.activated=False
        obj_1.save()


    return render(request,'results.html' , {'val' :context , 'action' : s } )

def recommend(request):

    obj = files.objects.get(activated=False)
    val = obj.Results
    obj_2 = Recommend.objects.get(name=val)
    val_2 = obj_2.recommended_steps
    obj_2.activated = False
    obj_2.save()

    return render(request,'recommend.html' , {'val' :val_2} )


def history(request):

    if request.method=='POST':

        obj = files.objects.get(activated=False)
        obj_2 = Recommend.objects.get(activated=False)
        obj_3 = Results.objects.filter(activated=False)

        result = ""

        for i in obj_3:
            val = i.name
            result += val + ','
            i.activated = True 
            i.save()

        result = result[:-1]
        description = obj.describe
        recommendations = obj_2.recommended_steps

        obj.activated = True
        obj_2.activated = True

        obj.save()
        obj_2.save()

        history = History(result=result , description=description , recommendations=recommendations , user = request.user )

        history.save()

        return redirect('/Dashboard')

    obj = History.objects.filter(user=request.user)
    context = []

    k = obj.count()-5
    j = 0 
    for i in obj:
        if j>=k:
            context.append(i)
        else:
            j += 1

    return render(request , 'history.html' , {'context' : context })


def shistory(request):
    if request.method == 'POST':
        obj = files.objects.get(activated=False)
        obj.activated = True
        obj.save()

        obj_3 = Results.objects.filter(activated=False)
        for i in obj_3:
            i.activated = True 
            i.save()

        obj_2 = Recommend.objects.get(activated=False)
        obj_2.activated=True
        obj_2.save()


        return redirect('/Dashboard')


def contact(request):

    obj = Contact.objects.all()
    context = []

    for i in obj:
        context.append(i)

    
    return render(request , 'contact.html' , {'context':context})



