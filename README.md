SocialAuthCustomUserModel
=========================

This is a repo to try and get some clarity on how Social Auth is meant to 
work with Django 1.5's custom user models.

At the moment this code is broken, but I can not figure out why. I have 
reduced the example to its bare minimum to make debugging simpler.

#Steps to Reproduce:#

1. Clone the repo

2. Install Django 1.5

3. Install django-social-auth (at the time of writing this was 0.7.22)

4. Edit settings.py to include your GOOGLE_OAUTH2_CLIENT_ID and 
   GOOGLE_OAUTH2_CLIENT_SECRET

5. Runserver

6. Browse to /

7. Click the "Login with Google" link.

8. Select any valid Google profile.

9. End up at /error (with nothing in messages to debug why)

