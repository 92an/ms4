## Table of Content

- [Deployment:](#Deployment)
    - [Preperation:](#Preperation)
    - [Deployment with Heroku CLI:](#Deployment-with-Heroku-CLI)
    - [Deployment with Github Automatic Deployment:](#Deployment-with-Github-Automatic-Deployment)
    - [More Information:](#More-Information)
- [Technologies Used:](#technologies-used)
    - [Languages:](#languages)
    - [Libraries and Frameworks:](#libraries-and-frameworks)
    - [Tools](#tools)
- [Project Purpose:](#project-purpose)
- [User Stories:](#user-stories)
- [Admin functionality:](#Admin-functionality)
- [Design:](#Design)
- [Future Features:](#Future-Features) 
- [Testing:](#Testing)
    - [Validation:](#Validation)
        - [HTML:](#HTML)
        - [CSS:](#CSS)
        - [CSS:](#JS)
    - [Responsive Testing:](#Responsive-Testing)
    - [Functionality:](#Functionality)
- [Bugs:](#Bugs)
    - [username responsive profile in navigation:](#username-responsive-profile-in-navigation)
    - [categories stopped functioning after first filter:](#categories-stopped-functioning-after-first-filter)
- [References:](#References)
    - [inspiration:](#inspiration)
    - [Images:](#Images)
    - [Logo:](#Logo)

# Deployment:

The deployment of this project is done on heroku and 
the code is written using gitpod.


## Preperation:

1. Log in to Heroku and create a "New App" with a unique name

2. Before deployment we have to inform heroku what dependencies 
our project has in a txt file called requirements. To do this use the
line of code below. 

```
pip3 freeze --local > requirements.txt
```
3. The next step is to create a Procfile using the following command.
```
echo web: python run.py > Procfile
```
4. Push these files to github.

5. The key value pairs that are hidden in the "env.py" file 
need to be specified in the settings field. In Heroku go to
settings and reveal "config vars" then specify the keys there.

## Deployment with Heroku CLI: 

1. Install Heroku CLI.

2. log in to Heroku using the following command.

```
$ heroku login
```
3. (if working on a computer locally) clone repository. 
```
$ heroku git:clone -a econhub
$ cd econhub
```
4. To implement changes to the code and pushing them to Heroku
use the following lines of code.
```
$ git add .
$ git commit -m "Commit comments here!"
$ git push heroku master
```


## Deployment with Github Automatic Deployment:

1. Go to the GitHub tab in the deploy section on Heroku.

2. Type in you GitHub username and the corresponding repository that you want to deploy.

3. Enable automatic deployment.

4. Select the Branch you want to deploy, and click on the deploy branch button.

## More Information:

For any additional information please refer to the deployment 
documentation which can be found [here](https://devcenter.heroku.com/categories/deployment)

How to clone git reposirtories can be found [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

# Technologies Used:

## Languages:
* HTML5
* CSS3 
* Javascript
* Python
    * For dependencies I refer to the requirements.txt file
* Jinja Templating language
* django

## Libraries and Frameworks:
* Bootstrap
* Jquery
* Django
* Font Awesome

## Tools
* Gitpod
* Git
* Github
* Heroku
* Chrome Dev Tools

# Project Purpose:

Simple artstore, with the aim of inspiring amateur artists

# Target Audience:

* Art Enthusiasts
* Artists
* People looking for art to decorate their home

# User stories:

### See excel file

# Design

Simple black and white layout to not create visual overload when looking at artwork.
This is the case as most art can have rather explosive colors, therefore I was going for a more
neutral look in the website as to not draw away the focal point.


# Testing

## Validation


## Responsive Testing
Done on google chrome only and is the recomended browser

* Mobile S 320px
* Mobile M 375px
* Mobile L 425px
* Tablet 768px
* Laptop 1024px
* Laptop L 1440px


|Design Test|Mobile S|Mobile M|Mobile L|
|-----------|:--------:|:--------:|:--------:|
|homepage.html|poor|ok|ok|
|terms.html|poor|ok|ok|
|chattrooms.html|poor|ok|ok|
|micro_chatt.html|poor|ok|ok|
|macro_chatt.html|poor|ok|ok|
|political_chatt.html|poor|ok|ok|
|student_chatt.html|poor|ok|ok|
|register.html|poor|ok|ok|
|login.html|poor|ok|ok|
|profile.html|poor|ok|ok|
|add_terms.html|poor|ok|ok|
|categories.html|poor|ok|ok|
|add_categories.html|poor|ok|ok|

<p>&nbsp;</p>

|Design Test|Tablet|Laptop|Laptop L|
|-----------|:------:|:------:|:--------:|
|homepage.html|ok|ok|ok|
|terms.html|ok|ok|ok|
|chattrooms.html|ok|ok|ok|
|micro_chatt.html|ok|ok|ok|
|macro_chatt.html|ok|ok|ok|
|political_chatt.html|ok|ok|ok|
|student_chatt.html|ok|ok|ok|
|register.html|ok|ok|ok|
|login.html|ok|ok|ok|
|profile.html|ok|ok|ok|
|add_terms.html|ok|ok|ok|
|categories.html|ok|ok|ok|
|add_categories.ok|ok|ok|ok|

<p>&nbsp;</p>

Tested device formats:

* Moto G4
* Galaxy S5
* Pixel 2
* Pixel 2 XL
* iPhone 5/SE
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* iPad Pro
* Surface Duo
* Galaxy Fold

**NOTE that is is not ideal to operate on the smalest screen.
Though functional the is some overflow issue and is rather impractical
on smaller screens. Though since it is expeted that the user is someone
working on a laptop, or studying mobile devices are not the main device
that the use might use.

## Functionality

|Function|status|
|-----------|:------:|
|Menubar is dynamically changing based on who is logged in|ok|
|Only admin can see category section|ok|
|Only admin can see all tasks in profile section to delete or edit|ok|
|Users can only see their own terms in their profile to delete or edit|ok|
|Register user function works|ok|
|Login function works|ok|
|Log out works|ok|
|Forms have a cancel button to return|ok|
|Terms can be added to the dictionary in the profile section|ok|
|Terms can be updated in the dictionary in the profile section|ok|
|Terms can be deleted from the dictionary in the profile section|ok|
|Terms can read in the dictionary|ok|
|User can enter chattrooms|ok|
|User can leave chattrooms|ok|
|User can communicate in chattrooms|ok|
|Admin can alter all terms|ok|
|Admin can add categories|ok|
|Admin can delete categories|ok|

# References:

## inspiration

simple art store

## Images

Image by <a href="https://pixabay.com/users/pexels-2286921/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1836478">Pexels</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1836478">Pixabay</a>
Image by <a href="https://pixabay.com/users/geralt-9301/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3256055">Gerd Altmann</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3256055">Pixabay</a>
Image by <a href="https://pixabay.com/users/vem777-12826491/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4286332">Valeriu Marin</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4286332">Pixabay</a>
Image by <a href="https://pixabay.com/users/ractapopulous-24766/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2561511">JL G</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2561511">Pixabay</a>
Image by <a href="https://pixabay.com/users/tsukiko-kiyomidzu-1850874/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2196323">Alexandra Haynak</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2196323">Pixabay</a>
Image by <a href="https://pixabay.com/users/nika_akin-13521770/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4804818">Nika Akin</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4804818">Pixabay</a>
Image by <a href="https://pixabay.com/users/prawny-162579/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5984279">Prawny</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5984279">Pixabay</a>


