import smtplib, os, datetime, getpass
# These strange_variables just create new files which are required for this project to work properly

strange_variable1 = open("emails.txt", 'a')
strange_variable2 = open("emails(verified).txt", 'a')
strange_variable3 = open("SendMailData.txt", 'a')
strange_variable4 = open("Emailno.txt", 'a')
strange_variable4.write('0')
del strange_variable1, strange_variable2, strange_variable3, strange_variable4
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
logemail = input('Enter the email from which you want to send the mail followed by "Confirm":\n')
if not logemail.endswith("Confirm"):
  while True:
    logemail = input('Enter the email from which you want to send the mail followed by "Confirm":\n')
    if logemail.endswith("Confirm"):
      break
logemail = logemail[:len(logemail)-7].strip()
# Clearing the "Confirm" word from logemail
logpass = getpass.getpass('Enter the password for <{}> account followed "Confirm":\n'.format(logemail))
if not logpass.endswith("Confirm"):
    while True:
        logpass = getpass.getpass('Enter the password for <{}> account followed by "Confirm":\n'.format(logemail))
        if logpass.endswith("Confirm"):
            break
logpass = logpass[:len(logpass)-7].strip()
# Clearing the "Confirm" word from logpass
server.login(logemail,logpass)
emails = open("emails(verified).txt")
subject = input('Enter the subject of the email followed by "Confirm":\n')
if not subject.endswith("Confirm"):
  while True:
    subject = input('Enter the subject of the email followed by "Confirm":\n')
    if subject.endswith("Confirm"):
      break
bodies = list()
body = input('Enter the body of the email followed by "Confirm":\n')
if not body.endswith("Confirm"):
  bodies.append(body.strip())
  while True:
    body = input()
    if not body.endswith("Confirm"):
        bodies.append(body.strip())
    else:
        bodies.append(body.strip()[:-7].strip())
        break
else:
    bodies.insert(0,body.strip()[:-7].strip())
body = "\n".join(bodies)
# Clearing the "Confirm" word from the subject
subject = subject[:len(subject)-7].strip()
message = "Subject: {}\n\n{}".format(subject, body)
for email in emails :
  server.sendmail(logemail, email , message)
server.quit()
def get_to_mails(to_emails):
    return_string = ''
    for email in to_emails:
        return_string += "<{}>{}".format(email.strip(),"\n+(" "*11)")
    return return_string.strip()
emails = open("emails(verified).txt")
to_Emails = [email for email in emails]
count = open('Emailno.txt').read()
counts = int(''.join([character for character in count if character.isnumeric()]))
countfile = open("Emailno.txt",'w')
countfile.write(str(counts+1))
print()
my_body = []
for count in range(body.count('\n')+1):
    if not count==0:
        my_body.append(" "*11 + body.split('\n')[count])
    else:
        my_body.append(body.split('\n')[count])
my_body="\n".join(my_body)
data = ""

data += ("Email #{}".format(counts+1)+'\n')
data += ("DATE    :  {}".format(datetime.datetime.now().strftime("%d/%b/%Y %I:%M:%S%p")) + '\n')   # Long Date
data += ("FROM    :  <{}>".format(logemail) + "\n")
data += ("TO      :  {}".format(get_to_mails(to_Emails) + "\n"))
data += ("SUBJECT :  {}".format(subject) + "\n")
data += ("BODY    :  {}".format(my_body) + "\n\n")
SMD=open("SendMailData.txt", 'a')
SMD.write(data)
print('Sent email log is stored in the file {}'.format(os.getcwd()+r"\SendMailData.txt"))
