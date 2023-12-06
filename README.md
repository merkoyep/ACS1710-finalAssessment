This assignment is a Python/Flask application that performs CRUD operations with a database.
## Decisions I made
- I decided to sort the todos based on my personal preference of ranking based on priority. Luckily, the names of the priorities I chose were already in alphabetical order which is helpful! Otherwise I would have assigned each priority a number and sorted that way.

## Todo:
- [x] Create a new folder named: templates

- [x] Create a new file: app.py

In app.py add the following:

- [x] from flask import Flask, render_template, request, url_for, redirect
- [x] from pymongo import MongoClient
- [x] from bson.objectid import ObjectId

- [x] Add a route
This route will be the main "home" page for the app.


- [x] Set some environment variables
- [x] Set these environment variables to help with testing and development.

- [x] Add some styles
Your form is pretty bland. Some styles will help!

- [x] Create a new folder: static


- [x] In templates/index.html add a link to your stylesheet. Add the following in the <head> of the document:


- [x] Handle the form submit and create new todo items


- [x] Displaying todo items
In this step you'll request records from your database and display them on the page.

- [x] Edit the home page route:

- [x] The new line finds all of the records in the todos collection. This should return a list of objects.

- [x] Next pass the list of todos to the template when you render it.

- [x] Before you can see the todos you'll need to turn that list of todos into HTML. Edit templates/index.html. Add the following below the form:


- [x] Deleting todos
Todos are great but, when they are completed it would be good to remove them from the list.


- [x] Write a route to handle this new form action

- [x] Next, you used the .delete_one() method of the todos collection to delete a single record. To Identify the record you needed to include an object/dictionary that includes the _id of the record you want to delete. Notice that the value for the _id is passed to the ObjectId() function. Object ids are more than the string id value. This function takes the id string and turns it into valid Object id that Mongo can work with.


Stretch Challenges

- [x] 1 Add a new priority level
- [x] Add a new radio button to the list of priorities. Currently the list shows: Important, and Unimportant. It might be good to have a "normal" or "very important" priority level.

- [x] Add a new radio button with a new value. Give it a matching label.

- [x] Test your work by adding a new todo item with the new priority.

- [x] 2 Style priorities
It would be helpful if users could spot important priority todos at a glance. Adding some color would heklp with this.

Currrently the todo priority string is displayed in a p tag that has a class name matching the priority value. You can style this name in your style sheet. Add a class for each priority name. Something like:

- [x] 3 Sort your todos
Important! This app is running all of it's application logic on the serverside. The browser isn't doing any work. This gives us two possiblities to handling sorted todos.

- [x] 4 Completion
It might be good if we had a list that showed all of the todo items but could also show which were complete and which were not. This way we could avoid questions like: "did I feed the cat?"

To solve this challenge you need to add a new property to your todo items: complete. This can be a boolean value if your todos are completed True, or not complete False. Or it could be a string if todos might be "not complete", "in progress", and "complete". You decide.

Follow these steps:

- [x] Add a new field for your todos: complete. Figure all todos are Not complete when they are created. You can just add this field and it's default value to the todo that is initially created.

- [x] Display the completion status in your template.

- [x] To mark a todo as complete follow the same pattern as was used with the delete, form, and route.

- [x] In order to update a record you'll need to call: todos.update_one(filter, new_values). This method takes two parameters: filter, use this to identify which records to update, and new_values, an object/dictionary with the properties and values to updated.

- [x] 5 Add a date to each todo
It would be good if each todo stored the date it was added to the list. This might help organize how we complete and prioritize our tasks!
