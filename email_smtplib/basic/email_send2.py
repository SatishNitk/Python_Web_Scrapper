from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPException,SMTPAuthenticationError


host = "smtp.gmail.com"
port = 587
email  = "hungrygupta@gmail.com"
password = "satishkumar"
from1 = "hungrygupta@gmail.com"
to_list = ["hungrygupta@gmail.com"]
try:
	email_obj = SMTP(host, port)
	email_obj.ehlo()
	email_obj.starttls()
	email_obj.ehlo()	
	email_obj.login(email,password)
	plain_text = "just a simple text message"
	html_txt = """
	<html>
	<body>
	<h1>
	This paragraph
	contains a lot of lines
	in the source code,
	but the browser 
	ignores it.
	</h1>
	</body>
	</html>
	         """
	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "Hello there"
	the_msg['From'] = from1
	part1 =  MIMEText(plain_text, "plain")
	part2 = MIMEText(html_txt, "html")
	the_msg.attach(part1)
	the_msg.attach(part2)
	print(the_msg.as_string())
	email_obj.sendmail(from1,to_list,the_msg.as_string())
except SMTPException:
	print("exception occured in sending rmail check once whole code")


