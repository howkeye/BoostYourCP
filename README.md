# BoostYourCP

This project is completely made in Django. 
Due to internet issues in the workspace suring Hackathon, we are not able to deploy our Django project.
We will soon be adding link of our project.

1. Clone the repo in a local folder.

2. Create the virtual environment and install the all requirements avaliable in req.txt.
  We have used conda package manager, so req.txt is for conda. For,pip install respective packages.

3. Go to desired location and make database using migration feature of Django. Use these commands -
	'''
	python3 manage.py makemigrations
	python3 manage.py migrate
	'''

4. Start your local django server
	python3 manage.py runserver

5. Open your locally hosted app, by clicking on link in terminal.

6. Tada...You have started the project, now you can easily access all its features.

7. To access the database, create a superuser from terminal.
	python3 manage.py createsuperuser

8. Use your details, to access the database  by following link ‘localhost:port/admin’ in main page.

#Other features:
Some features like cron jobs can easily be done by uploading it in django server.
You can do it manually by  
1. For sending mail : ‘localhost:port/send’  has python3 function to send contest reminders.
         So, just open this page  and  ..TaDa .. You send alarms via mail.

2.For daily fetching of Contest details : ‘localhost:port/codechef’ &&  ‘localhost:port/codeforces’ .  
 	So, just open this page  and  ..TaDa .. You updated your contest Data.
	
3. We have other cron jobs to do operations like leaderboard update and usr rating fenching.
 U can check urls.py and respective mapped functions to know about them  or wait for a couple of days....we will be updating it.

Limited scraping is permitted. 
We are using cron jobs daily, not on user request . So no problem of getting blocked for scraping.
This is quit optimised  way of doing this and no effect on user experience.






	
    
