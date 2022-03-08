# The Boathouse Restaurant Website

Restaurant Website. Currently allows customers to order a takeaway from a set menu and view their previous order. Staff are able to set the menu and also view orders. End goal is to build a fully functioning website for this restraurant with both a front end and back end created by me, including additional features such as; a table booking system and the ability for staff to assign bills to a table.

# What's Available To Do In This Version?

Glad you asked! In this version there are two groups a user can belong too; Customer, and Staff.

Customers can sign up with their email to the Boathouse restaurant which allows them to order from any combination of a starter, main, or dessert and delivery options. They can also view their previous orders which will give a status update to meals between ordering and delivery. (Try it for yourself)

Staff are able to edit the menu by adding an deleting menu items including the price. They can also view all in progress customers orderes and give status updates to them. Unfortunately, It's not possible for you to assign yourself as a member of staff. Luckily, I've created an account for you to have a go at these features:

    Username: Ann.Chovy@boathouse.co.uk

    Password: Takeaway123


# Feature Roadmap

--- Sprint 1 --

Inital working backend of the website includes; model and main urls --- COMPLETE

Functions to allow staff to delete menu items --- COMPLETE

Login and security --- COMPLETE

Front end design work and implementation --- (look into javascript and frameworks React/ Bootstrap) ONGOING

-- Sprint 2 --

Customers can order more then one item of each course and more then one of the same item --- (look into formsets and javascript)

Email noticifcations

Customers can cancel orders after checkout out. Canceled orders and orders in basket to auto delete after a certain time

Reduce number of conformation pages so updates happen from list view --- (javascript/ AJAX)

Allow customers to book a table for a certain times

Front end redesign and improvements

# Running The App

Running the Server:

    In command lines navigate to directory; boathouse/takeaway
   
    Enter the command; python manage.py runserver
   
    This will require installation of Python and the Django framework. Full requirements in requirments.txt
   
 The project is also hosted here: https://benjihills.pythonanywhere.com/
     
# New to Django

Hi Gousto, thanks for checking out my current project and I hope you enjoy it! Feel free add, change, and delete as much as you like. Also sorry about the mess I'm currently putting the front end on so things are a bit jumbled around (e.g. logout button keeps escaping the banner) but should be fully working. I noticed that Django isn't part of your tech stack, so I thought I'd lend a hand in case you were wondering where best to go to look at my work. Django handles some of the work for me so places you can go where the work is 100% my own are;

menu/models.py ----- These models allow me to interact with the sqlite database, by allowing be to create data table, fields, how that data is stored and manipulated.

menu/views.py ----- The view function dictates how the models interact with the webpages via controlling the web request and web responses. 

menu/urls.py ----- sets up the url for where a webpage will be located and which view function it is attached to that web page.

menu/forms.py ----- Uses Django's in built classes to quickly define forms to be used in my templates

menu/templates ----- This folder houses most of the front end work and where I write the html for the app. This are then related back to the relavent view where they can be displayed on the appropriate web page via urls.py through views. From templates I'm also able to call functions {% %} and variables {{ }}.

takeaway/statics ---- contains all the css and images I've used so far in the project 



