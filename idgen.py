#Author: Juan Plasencia
#Printing the greetings 
print("Hello, please enter the following information: \n")
#Asking information
name = input("First name: ")
lname = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job = input("Job tittle: ")
idnum = input("ID Number: ")
hcolor = input("Hair color: ")
ecolor = input("Eye color: ")
month = input("Started Month: ")
training = input("Do you complete advanced training?(Yes/No): ")
#Printing the ID card outputs
print("\nThe ID Card is:\n----------------------------------")
#1 Simple outputs
print(f"{lname.upper()}, {name.capitalize()}\n{job.title()}\nID: {idnum}\n\n{email.lower()}\n{phone}\n")
#2 Outputs maked it so that the second columns align, regardless of how many letters are in the responses.
print("{:<20}{:<20}".format(f"Hair: {hcolor.capitalize()}", f"Eyes: {ecolor.capitalize()}"))
print("{:<20}{:<20}".format(f"Month: {month.capitalize()}", f"Training: {training.capitalize()}"))
print("----------------------------------")