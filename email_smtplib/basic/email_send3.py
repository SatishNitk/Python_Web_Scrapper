import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPException,SMTPAuthenticationError

host = "smtp.gmail.com"
port = 587
email  = "hungrygupta@gmail.com"
password = ""
from1 = "hungrygupta@gmail.com"
to_list = ["hungrygupta@gmail.com"]



class MessageUser:
	user_details = []
	messages = []
	email_messages = []
	base_message = """ 
    HI there {name} jk  {date} jj  ${total}
	"""
	def  add_user(self, name,amount, email=None):
		name = name[0].upper() + name[1:].lower()
		amount = "%.2f"%(amount)
		detail = {
		"name" : name,
		"amount" : amount
		}
		today  = datetime.date.today()
		date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		detail['date'] = date_text
		if email is not None:
			detail['email'] = email
		self.user_details.append(detail)

	def get_details(self):
	    return self.user_details

	def make_message(self):
		print "dd", len(self.get_details())
		if(len(self.user_details) > 0):
			for detail in self.get_details():
				name = detail['name']
				date = detail['date']
				amount = detail['amount']
				message = self.base_message
				new_msg = message.format(
				       name = name,
				       date= date,
				       total = amount
				)
				email_id = detail.get("email")
				if email_id:
					user_data = {
					  "email" : email_id,
					  "message" : new_msg
					}
					self.email_messages.append(user_data)
				else:
					self.messages.append(new_msg)
			return self.messages
		return []
			
	def send_email(self):
		self.make_message()
		print len(self.email_messages)
		if len(self.email_messages) > 0:
			for detail in self.email_messages:
				email_id = detail['email']
				user_message = detail['message']
				try:
					email_obj = SMTP(host, port)
					email_obj.ehlo()
					email_obj.starttls()
					email_obj.ehlo()	
					email_obj.login(email,password)
					the_msg = MIMEMultipart("alternative")
					the_msg['Subject'] = "Hello there"
					the_msg['From'] = from1
					the_msg['To'] = email_id
					part1 =  MIMEText(user_message, "plain")
					the_msg.attach(part1)
					print(the_msg.as_string())
					email_obj.sendmail(from1,[email_id],the_msg.as_string())
				except SMTPException:
					print "exception occured"
			return True
		return False		

user_obj = MessageUser()
user_obj.add_user("satish kumar",2222.222,"hungrygupta@gmail.com")
user_obj.add_user("satish kumar gupta",333222.222,"hungrygupta@gmail.com")
print user_obj.send_email()
