import smtplib
sender_mail="madeshwaran.anandharaj@gamil.com"
receivers_mail="parameshwari.anandharaj@gamil.com"
password=input(str("Enter your password:"))
message="""from:from madeshwaran.anandharaj@gamil.com
To: To parameshwari.anandharaj@gamil.com
subject:This is a smtp mail(just for checking). 
I send this message for just checking smptp protocol is working or not.Don't reply"""
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
# password=input("Enter a password:")
server.ehlo()
server.login(sender_mail,password)
server.sendmail(sender_mail,receivers_mail,message)
