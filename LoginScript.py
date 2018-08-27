Username = "unassigned" #Replace with your username of choice
Password = "unassigned" #Replace with your password of choice
#DO NOT EDIT BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING
passtrue = False
x = True
y = True
success = False #Indicates login is not successful yet
while x == True:
  e_u = raw_input("User: ")#Asks for user to enter User
  if e_u == Username:#checks if entered user matches saved user
    passtrue = True#Verifies that entered user is equal to saved user
    x = False #Breaks 
    y = True
  else:
    print("Incorrect user!")
while y == True:
  e_p = raw_input("Password for " + Username + ": ")
  if e_p == Password:
    print("Login successful!")
    success = True #Indicates login successful
    y = False
  else:
    print("Incorrect password!")
