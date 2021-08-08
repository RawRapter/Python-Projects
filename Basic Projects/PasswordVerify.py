"""
Verify Basic Program to Check if the password is correct or not
"""
#Importing getpass module
import getpass
database = {"anant.arun": "123456", "unnati.ranjan": "654321"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
#running loop until correct password is entered
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("It was Wrong!! Enter Your Password Again : ")
        break
print("User Verified!!")