from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def signin( request ):
   if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = auth.authenticate(username=username,password=password)

         if user is not None:
            auth.login( request , user )
            return redirect('/Dashboard')
         else:
            messages.info( request , 'Invalid Credentials' )
            return redirect('/Signin')
   else:
      return render( request , 'Signin.html' )

def signup( request ):

   if request.method == 'POST':
         username = request.POST.get('username')
         password1 = request.POST.get('password1')
         password2 = request.POST.get('password2')
         email = request.POST.get('email')
         name = request.POST.get('name')

         if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request, 'Username Taken' ) 
               return redirect('/Signup')
            elif User.objects.filter(email=email).exists():   
               messages.info(request, 'Email already Taken' ) 
               return redirect('/Signup')
            else:
               user = User.objects.create_user( username=username , password = password1 , email = email , first_name = name )
               user.save()
               auth.login( request , user )
               return redirect( '/Dashboard' )
         else:
            messages.info( request , ' Password Mismatch ' ) 
            return redirect('/Signup')
            
   else:
      return render( request , 'Signup.html' )


def logout(request):
   auth.logout(request)
   return redirect('/')      