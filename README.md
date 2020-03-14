# BoostYourCP
 A webapp to increase coding culture in our college.
 
  ## what all it uses??
  - Phython, Diango ,Postgresql, Rest API , icalender, 
  - Cron jobs
   - Heroku web hosting,Scraping
  -Html, CSS (Bootstrap)
 
 ## Features
 
 - Sends icalender files via mail. So, that user can add reminders about the upcoming coding contests on codechef and codeforces.
 - Provides API access to upcoming contests.
 - We will also be extenting it to a coding portal will have alot of interesting features.
 - project is completely made in Django. 
 - Hosted at Heroku

 
 
## Link 
https://boostyourcp.herokuapp.com/


## How it works

1. Scraps the required data from coding sites daily,uses Cron Job scheduler.
2. We are using api of codeforces to get desired data.
3. Then we Send email using a python cron script, to send mail.
4. Have to make a user id on the app to use it.
5. Can select from what all sites, user wants to participate.



Note : Limited scraping is permitted. 
We are using cron jobs daily, not on user request . So no problem of getting blocked for scraping.
This is quit optimised  way of doing this and no effect on user experience.

## Have a glance 


front-end of website             |  mails that we will get
:-------------------------:|:-------------------------:
![](https://i.imgur.com/sPsjDM3.png) |  ![](https://i.imgur.com/owOh3Am.jpg)

















	
    
