# The Boathouse Restaurant Website

Restaurant Website. Currently allows customers to order a takeaway from a set menu and view their previous order. Staff are able to set the menu and also view orders. End goal is to build a fully functioning website for this restraurant with both a front end and back end created by me, including additional features such as; a table booking system and the ability for staff to assign bills to a table.

## What's Available To Do In This Version?

Glad you asked! In this version there are two groups a user can belong too; Customer, and Staff.

Customers can sign up with their email to the Boathouse restaurant which allows them to order from any combination of a starter, main, or dessert and delivery options. They can also view their previous orders which will give a status update to meals between ordering and delivery. (Try it for yourself)

Staff are able to edit the menu by adding an deleting menu items including the price. They can also view all in progress customers orderes and give status updates to them. Unfortunately, It's not possible for you to assign yourself as a member of staff. Luckily, I've created an account for you to have a go at these features:

    Username: Ann.Chovy@boathouse.co.uk

    Password: Takeaway123


## Feature Roadmap

--- Sprint 1 --

- Inital working backend of the website includes; model and main urls --- COMPLETE

- Functions to allow staff to delete menu items --- COMPLETE

- Login and security --- COMPLETE

- Front end design work and implementation --- (look into javascript and frameworks React/ Bootstrap) ONGOING

-- Sprint 2 --

- Customers can order more then one item of each course and more then one of the same item --- (look into formsets and javascript)

- Email noticifcations

- Customers can cancel orders after checkout out. Canceled orders and orders in basket to auto delete after a certain time

- Reduce number of conformation pages so updates happen from list view --- (javascript/ AJAX)

- Allow customers to book a table for a certain times

- Front end redesign and improvements

## Running The App

Running the Server:

    In command lines navigate to directory; boathouse/takeaway
   
    Enter the command; python manage.py runserver
   
    This will require installation of Python and the Django framework. Full requirements in requirments.txt
   
 The project is also hosted here: https://benjihills.pythonanywhere.com/
     



