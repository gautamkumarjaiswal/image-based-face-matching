# image-based-face-matching
Have an image of person A and person B, check both images are of same person or not.


                            INSTALLATION INSTRUCTION TO RUN PERSON IDENTIFICATION PYTHON SCRIPT

NOTE: WE WILL CREATE VIRTUAL ENVIRONMENT AND INSTALL ALL DEPENDENCIES IN THAT SO THAT IT WILL NOT CHANGE/AFFECT YOUR ROOT DIRECTORY, JUST BY DELETEING THIS FOLDER YOU CAN DELETE ITS EXISTANCE.

Before running script set environment, it will hardly take 15 to 20 minutes.


Windows: Open windows 'cmd' typing cmd in search (not conda command window) as an administrator
Ubuntu : Open terminal



1) Download and install python from> https://www.python.org/downloads/    (if you already have then ignore this step and check its version to be sure)
2) check python version using command > python -V
3)install pip using command > python get-pip.py
4) Upgrade pip > python -m pip install -U pip
5) Install virtual environment> pip install virtualenv
6) test installation> virtualenv --version

7) make a folder named 'image_matching' in any drive of windows (in my case i made a folder in 'E' drive)

8) Now change the directroy to 'E' drive
(for example if previously it was c:\User>john then change drive by typing 'cd..' and finaly change to 'E', it will look like 'E:\')

NOTE: If you are using ubuntu, chnage the directory to 'image_matching' using terminal.

9) In 'E' drive we created a folder named 'image_matching' go inside that folder by changeing directory> E:\cd image_matching
(now this folder will be your working directory, copy the folder i have given to you to this folder)

10)create virtual environment repositery>virtualenv env
(this will create a folder with name 'env' inside working repositery 'image_matching' and inside 'env' there will be four sub folders and one license file. )

11) Run the command>env\Scripts\activate
    Ubuntu user: > source env/bin/activate

(if you are getting error, look for 'activate' file in either 'Scripts' or 'bin' folder, and give path of 'activate' file according to step 11)
(after successful run, cmd window will look like '(env) E:\image_matching>' means you have created virtual env and ready to work)


12) Now install Keras by typing: (env) E:\image_matching>pip install face_recognition
(this may take few minutes)



NOW YOU ARE READY To RUN SCRIPT

13) change directory where face_recog.py script is kept i.e go to folder 'image-based-face-matching':(env) E:\image_matching> cd image-based-face-matching
14)run the python scipt: (env) E:\image_matching\image-based-face-matching>python face_recog.py
If eveything is okay you will get output sayinh images are of same person or different person.

To Change image file:

15) Type 'idle' as shown here E:\image_matching\image-based-face-matching>idle
This will open a python IDE, go to 'file' tab (upper left) from menu and select 'open' to open 'face_recog.py' file. Follow comments to test
other image file, save using ctrl+s and run the program as step (19).




-----------------------over---------------------------------------------------------
