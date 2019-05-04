
host = "smtp.gmail.com"
port = 587
email  = "hungrygupta@gmail.com"
password = ""
from1 = "hungrygupta@gmail.com"
to = ["hungrygupta@gmail.com"]
from smtplib import SMTP, SMTPException,SMTPAuthenticationError

email_obj = SMTP(host, port)
email_obj.ehlo()
email_obj.starttls()
email_obj.ehlo()
try:
	email_obj.login(email,password)
	email_obj.sendmail(from1,to,"hi there this is satish kumar gupta this side")
except 	SMTPAuthenticationError:
	print("email or password is incorrect, please check once")
except Exception:
    print "there is some problem , Exception occure"	

email_obj.quit()
print("sucess ...")