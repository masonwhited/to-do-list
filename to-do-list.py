# Import necessary libraries
from tkinter import Menu  # Not used in this code snippet
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK with credentials from a JSON file
cred = credentials.Certificate("to-do-list.json")
firebase_admin.initialize_app(cred)

# Create a client instance to interact with Firestore
db = firestore.client()

# Function to display the main menu
def menu():
    """
    Displays the main menu and handles user input.
    """
    # Retrieve all documents from the 'project' collection
    results = db.collection('project').get()

    # Print the ID and data of each document
    for result in results:
        data = result.to_dict()
        print(f"{result.id} : {data}")

    # Display menu options
    print("0. Add Project")
    print("1. Delete Project")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Quit")

    # Get user input
    option = input("Please indicate choice: ")

    # Handle user input
    if option == "0":
        # Add a new project
        add_project()
    elif option == "1":
        # Delete a project
        delete_project()
    elif option == "2":
        # Add a new task to a project
        add_task()
    elif option == "3":
        # Delete a task from a project
        delete_task()
    elif option == "4":
        # Update a task in a project
        update_task()
    elif option == "5":
        # Exit the program
        exit()

# Function to add a new project
def add_project():
    """
    Adds a new project to the 'project' collection.
    """
    # Get project name from user
    name = input("Enter project name: ")

    # Get task order number and task from user
    order = input("Enter task order number: ")
    task = input("Enter task: ")

    # Create a new document in the 'project' collection
    doc = db.collection('project').document(name)

    # Set the task data in the document
    doc.set({order: task})

    # Return to the main menu
    menu()

# Function to delete a project
def delete_project():
    """
    Deletes a project from the 'project' collection.
    """
    # Get project name from user
    name = input("Enter project name: ")

    # Delete the document from the 'project' collection
    db.collection('project').document(name).delete()

    # Return to the main menu
    menu()

# Function to add a new task to a project
def add_task():
    """
    Adds a new task to a project in the 'project' collection.
    """
    # Get project name from user
    name = input("Enter project name: ")

    # Get task order number and task from user
    order = input("Enter task order number: ")
    task = input("Enter task: ")

    # Update the document in the 'project' collection
    db.collection('project').document(name).update({order: task})

    # Return to the main menu
    menu()

# Function to delete a task from a project
def delete_task():
    """
    Deletes a task from a project in the 'project' collection.
    """
    # Get project name from user
    name = input("Enter project name: ")

    # Get task order number from user
    order = input("Enter task order number: ")

    # Delete the task from the document in the 'project' collection
    db.collection('project').document(name).update({order: firestore.DELETE_FIELD})

    # Return to the main menu
    menu()

# Function to update a task in a project
def update_task():
    """
    Updates a task in a project in the 'project' collection.
    """
    # Get project name from user
    name = input("Enter project name: ")

    # Get task order number and task from user
    order = input("Enter task order number: ")
    task = input("Enter task: ")

    # Update the task in the document in the 'project' collection
    db.collection('project').document(name).set({order: task}, merge=True)

    # Return to the main menu
    menu()

# Start the program by displaying the main menu
menu()