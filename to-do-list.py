from tkinter import Menu
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("to-do-list.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def menu():
    results = db.collection('project').get()

    for result in results:
        data = result.to_dict()
        print(f"{result.id} : {data}")
    print("1. Add Project")
    print("2. Delete Project")
    print("3. Update Project")
    print("4. Quit")
    option = input("Please idicate choice: ")
    if option == "1":
        add_project()
    elif option == "2":
        delete_project()
    elif option == "3":
        update_project()
    elif option == "4":
        exit()


def add_project():
    name = input("Enter project name: ")
    order = input("Enter task order number: ")
    task = input("Enter task: ")
    db.collection('project').document(name).update({order : task})
    menu()

def delete_project():
    name = input("Enter project name: ")
    order = input("Enter task order number: ")
    db.collection('project').document(name).update({order : firestore.DELETE_FIELD})
    menu()

def update_project():
    name = input("Enter project name: ")
    order = input("Enter task order number: ")
    task = input("Enter task: ")
    db.collection('project').document(name).set({order : task})
    menu()

menu()
