import random, smtplib

# IMPORTANT: Before you proceed to running this code, please make sure to replace emailID with your email ID and password with your email ID's password.
# If you don't like hard-coding your password in the code, you can put them in the environment variables. To get your password from environment variables,
# import os
# os.environ.get("password")
# Replace "password" with the variable name of password. 

# These strange_variables just create new files which are required for this project to work properly
strange_variable1 = open("emails.txt", 'a')
strange_variable2 = open("emails(verified).txt", 'a')
strange_variable3 = open("SendMailData.txt", 'a')
strange_variable4 = open("Emailno.txt", 'a')
strange_variable4.write('0')
del strange_variable1, strange_variable2, strange_variable3, strange_variable4

#################################################################################
def splwrd(wrd):
	return "".join([let for let in wrd])
###	
def gn(leng=6):
  lst=[]
  for _ in range(leng):
	lst.append(str(random.randrange(0,9)))
  OTP = "".join(lst)
  return OTP
#################################################################################

while True:
	file = open("emails.txt")
	fil  = open("emails.txt","a")
	emails = [word for word in file]
	email = input("Enter a valid E-mail ID: \n")
	if email == "done":
		break
	if email+'\n' in emails:
		print("You are already in the mailing list")
	elif email+'\n' not in emails:
		server = smtplib.SMTP_SSL('smtp.gmail.com',465)
		server.login('emailID','password')
		cpupwd = gn()
		subject = "OTP for signing up"
		body = "You have tried to sign up for our mailing list. If it was you, enter this code to get signed up. If it was not you, just ignore this email.\nSignup Code : {}\nImportant : Do not forward this mail or give this code to anyone".format(cpupwd)
		message = "Subject: {}\n\n{}".format(subject,body)
		server.sendmail('emailID',email,message)
		inppwd = input('Enter the Signup Code which was sent to <{}>. Enter "HELP" for more options\n'.format(email))
		if inppwd == "HELP":
				task = input("Enter 'ReSendOTP' to resend OTP, 'ChngMail' to change correct your email and 'Leave' to abort trying to sign up\n")
				if task == "ReSendOTP":
					cpupwd = gn()
					subject = "OTP for signing up"
					body = "You have tried to sign up for our mailing list. If it was you, enter this code to get signed up. If it was not you, just ignore this email.\nSignup Code : {}\nImportant : Do not forward this mail or give this code to anyone".format(cpupwd)
					message = "Subject: {}\n\n{}".format(subject,body)
					server.sendmail('emailID',email,message)
					inppwd = input("Enter the Signup Code which was sent to <{}>:\n".format(email))
					if inppwd == cpupwd:
						fil.write(email+'\n')
						print("Your code is correct. You are signed up")
						continue
					else:
						print("Your code is incorrect. Please try again later")
						continue
				elif task == "ChngMail":
					email = input("Enter the new email which you want the OTP to be sent:\n")
					if email+'\n' not in emails:
						cpupwd = gn()
						subject = "OTP for signing up"
						body = "You have tried to sign up for our mailing list. If it was you, enter this code to get signed up. If it was not you, just ignore this email.\nSignup Code : {}\nImportant : Do not forward this mail or give this code to anyone".format(cpupwd)
						message = "Subject: {}\n\n{}".format(subject,body)
						server.sendmail('emailID',email,message)
						inppwd = input("Enter the Signup Code which was sent to <{}>:\n".format(email))
						if inppwd == cpupwd:
							fil.write(email+'\n')
							print("Your code is correct. You are signed up")
							continue
						else:
							print("Your code is incorrect. Please try again later")
							continue
					else:
						print("The new email which you gave is already in the mailing list")
						continue
				elif task == "Leave":
					continue
		if inppwd == cpupwd:
			fil.write(email+'\n')
			print("Your code is correct. You are signed up")
			continue
		else:
			print("Your code is incorrect. You have some options which may help you.")
			task = input("Enter 'ReSendOTP' to resend OTP, 'ChngMail' to change correct your email and 'Leave' to abort trying to sign up\n")
			if task == "ReSendOTP":
				cpupwd = gn()
				subject = "OTP for signing up"
				body = "You have tried to sign up for our mailing list. If it was you, enter this code to get signed up. If it was not you, just ignore this email.\nSignup Code : {}\nImportant : Do not forward this mail or give this code to anyone".format(cpupwd)
				message = "Subject: {}\n\n{}".format(subject,body)
				server.sendmail('emailID',email,message)
				inppwd = input("Enter the Signup Code which was sent to <{}>:\n".format(email))
				if inppwd == cpupwd:
					fil.write(email+'\n')
					print("Your code is correct. You are signed up")
					continue
				else:
					print("Your code is incorrect. Please try again later")
					continue
			elif task == "ChngMail":
				email = input("Enter the new email which you want the OTP to be sent:\n")
				if email+'\n' not in emails:

					cpupwd = gn()
					subject = "OTP for signing up"
					body = "You have tried to sign up for our mailing list. If it was you, enter this code to get signed up. If it was not you, just ignore this email.\nSignup Code : {}\nImportant : Do not forward this mail or give this code to anyone".format(cpupwd)
					message = "Subject: {}\n\n{}".format(subject,body)
					server.sendmail('emailID',email,message)
					inppwd = input("Enter the Signup Code which was sent to <{}>:\n".format(email))
					if inppwd == cpupwd:
						fil.write(email+'\n')
						print("Your code is correct. You are signed up")
						continue
					else:
						print("Your code is incorrect. Please try again later")
						continue
				else:
					print("The new email which you gave is already in the mailing list")
			elif task == "Leave":
				continue
		server.quit()
unver = open("emails.txt")
ver   = open("emails(verified).txt","a")
verread = open("emails(verified).txt")
verified_emails = [word for word in verread]
for email in unver:
	splitted = splwrd(email)
	if "@" in splitted and "." in splitted:
		my_email = "".join(splitted)
		if not my_email in verified_emails:
			ver.write(my_email)
