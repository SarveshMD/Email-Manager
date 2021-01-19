Hello, 
This is an email manager created with python. I don't know how to make a GUI for it, for now, It can be used only from CLI. 
Since I found it interesting, I thought of uploading it to github so that anyone  can see it. 
I will be happy if you left some suggestions for improving this.
Please leave some suggestions and issues with my project if you come across something. 
I will be really happy if you help me make this graphical. 

Purpose: 
  This project is made for adding to websites and apps of companies, when the user will be prompted for email. But, as of now, this project is just for testing, once I gain all your help and make it graphical, It can be used well. The project collects the emails of the consumers of company which uses this project in their app or website. Then it verifies the emails with some verification steps preferred by the company and then adds the email to a file. When the company has some offers or some announcements, they can use this project to send email to all of the verified emails.

Contents : 
    AddMail.py
    AddMail-OTP.py
    SendMail.py
    clearD.py
    clearE.py
    
Functions of AddMail.py
  -> It prompts the user for emails until the user enters 'done'.
  -> The email is verified for writing it to a file. The verification process goes through two steps. 
  -> Step 1: It will check if the email is already in the list.
  -> Step 2: It will be verified by checking if it has "@" and "." symbols on them.
  -> If it satisfies both these conditions, the email gets verified and will be stored in the emails(verified).txt file.
  
Functions of AddMail-OTP.py
  -> It has the same functionality as AddMail.py, with an extra verification step. 
  -> First, the email will be verified with the conditions of AddMail.py.
  -> The extra verification step is, It sends a random 6 digit OTP to the entered email. 
  -> The user will be prompted for the OTP sent to his email. 
  -> If the user enters the correct OTP, it will be considered verified. 
  
Functions of SendMail.py
  -> Prompts the sender for the "From" email and password and logs in to gmail using smtplib
  -> Prompts for the Subject. 
  -> Prompts for the body. (Only ascii characters for now. Can be upgraded with your help.)
  -> Sends the email and stores the sending history in a SendMailData.txt file. It will contain all the emails sent from SendMail.py file

Function of clearD.py
  -> It cleares the SendMailData.txt file
  
Function of clearE.py
  -> It clears the emails.txt and emails(verified).txt, which will be formed after running any program in this repository.

I hope you will help me upgrade this and work with me to develop this. Thanks a lot for reading till the end. 
