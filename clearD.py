# These strange_variables just create new files which are required for this project to work properly
strange_variable1 = open("emails.txt", 'a')
strange_variable2 = open("emails(verified).txt", 'a')
strange_variable3 = open("SendMailData.txt", 'a')
strange_variable4 = open("Emailno.txt", 'a')
strange_variable4.write('0')
del strange_variable1, strange_variable2, strange_variable3, strange_variable4
SMD = open("SendMailData.txt",'a')
EM  = open("Emailno.txt",'w')
SMD.truncate(0)
EM.write(str(0))
print("Command executed successfully")
