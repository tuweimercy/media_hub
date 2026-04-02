### CREATING A DJANGO APP WITH DB 
- Step 1 : set up the necessary configs for your project 
    For MediaHUB our configs are 
    a. Media files url 
    b. Templates directory 
    c. Redirect URLs 
    d. Cloudinary configs for media management 
    e. Custom auth model override 

- Step 2 : register our cloudinary credentials 
### Accounts app 
- Step 3 : set up our custom user model /schema - i.e. the table to be created on migration  
- Step 4 : install pillow for media file management i.e. the files that are not to be saved on cloudinary (pip install pillow)
- step 5 : run the migrations for the accounts app
 - python manage.py makemigrations
 - python manage.py migrate
 