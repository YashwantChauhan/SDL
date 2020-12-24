# CYBER-SPHERE 
## An Intrusion Detection System based on Random Forest Classifier

## OVERVIEW
A Website based Intrusion Destection System(IDS) aimed towards reducing cost of IDS for small to mid-sized businesses. An easily accessible and reliable tool which provides solutions to all the security needs.

## TECHNOLOGIES USED
- Language : Python
- Back-end : Django 
- Front-end : HTML/CSS/Java Script , Bootstrap

## ARCHITECTURE
The Use-Cases of my Project are:
 
1. **LOGIN**
   
   1. Two Pages in this use case -> 'Login' and 'Signup'
   2. User Database of Django used to register and authenticate user.
   3. Admin can be created on the server-side ; Admin can view/modify database(s).
   4. I have created a seperate app(use case as said in Django) under 'APPS' folder for its coding and implementation.
   
2. **Upload File**

   1. File is the 'Traffic Capture File' of one's Network. The format should be i .csv , can be achieved using Wireshark features.
   2. File should contain required column/fields required for the algorithm functioning.
   3. The Webpage assosciated to this is the 'detect.html' and the coded function in the server is 'detect'.
        1. It contains a form to be filled with description, name, etc.
        2. Option for file to be uploaded from anywhere in the device
        3. Confirm button to upload it to the server.
   4. After this the user is directed to 'Result'.
   
3. **Result**

   1. The Algorithm written in the jupyter notebook named 'Model' is used.
   2. It is the Random Forest Algorithm trained on KDD'99 Cup Data saved under 'KDD'.
   3. Using 'Joblib' , the learner and scaler are saved named as 'learner' and 'scaler' in 'Model'. These are further loaded inside the Server function named as 'detect'.
   4. The Algorithm gives classification of attacks( if one is present ) and the possible solutions are searched in the databse named as 'Results.
   5. The database gives results on the basis of key tags; all databases are in 'Model.py' file in Dashb App.
   
4. **Recommendation**

   1. These are saved in 'Recommendations' Database. Can be called after results if the client wants recommended solutions.
   2. Different possible solutions are given to the clients from our Database.
   3. At last the client can choose to 'Save' their detection and results.
   
5. **History**

   1. If 'Save Changes' is opted history gets saved in 'History' Database.
   2. When client want to see his/her history the history corresponding to thier username is displayed.
   3. This is achieved using username as **Foriegn Key** between 'User' and 'History' Database.
   

## ARCHIECTURE DIAGRAM ##



<img src="https://github.com/YashwantChauhan/SDL/blob/main/IDS/static/Readme/Architecture.PNG" width="600" height="400">


## Prototype ##

<img src="https://github.com/YashwantChauhan/SDL/blob/main/IDS/static/Readme/index.PNG" width="500" height="300">
<img src="https://github.com/YashwantChauhan/SDL/blob/main/IDS/static/Readme/report1.PNG" width="500" height="350">
<img src="https://github.com/YashwantChauhan/SDL/blob/main/IDS/static/Readme/report2.PNG" width="600" height="350">

