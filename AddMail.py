# These strange_variables just create new files which are required for this project to work properly

strange_variable1 = open("emails.txt", 'a')
strange_variable2 = open("emails(verified).txt", 'a')
strange_variable3 = open("SendMailData.txt", 'a')
strange_variable4 = open("Emailno.txt", 'a')
strange_variable4.write('0')
del strange_variable1, strange_variable2, strange_variable3, strange_variable4
while True:
    emails = list()
    file = open("emails.txt")
    fil = open("emails.txt", "a")
    for mail in file:
        emails.append(mail)
    email = input("Enter your E-mail ID\n") + '\n'
    if email == "done\n":
        break
    if email in emails:
        print("You are already in the mailing list")
    elif email not in emails:
        print("You are added to the mailing list")
        fil.write(email)
splitted = list()
unver = open("emails.txt")
ver = open("emails(verified).txt", "a")
for email in unver:
    splitted[:] = email
    if "@" in splitted and "." in splitted:
        my_email = str()
        for char in splitted:
            my_email = my_email + char
            my_email = my_email.lower()
        ver.write(my_email)
