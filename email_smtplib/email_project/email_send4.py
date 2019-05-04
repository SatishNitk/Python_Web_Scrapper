import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPException,SMTPAuthenticationError
from utils.util import TemplateFormat
from csv_File import DataManager



host = "smtp.gmail.com"
port = 587
email  = "hungrygupta@gmail.com"
password = ""
from1 = "hungrygupta@gmail.com"
to_list = []



class MessageUser:
	user_details = []
	messages = []
	email_messages = []
	base_message = ""

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
		user_list = DataManager().read_data()
		if(len(user_list) > 0):
			for user in user_list:
				name = user['name']
				date = user['date']
				email =  user['email']
				new_msg  = TemplateFormat().get_final_html_template(name, date)
				if email:
					user_data = {
					  "email" : email,
					  "message" : new_msg
					}
					self.email_messages.append(user_data)
				else:
					print "email is not available"
					# self.messages.append(new_msg)
			return self.messages
		return []
			
	def send_email(self, Subject="Billing.."):
		self.make_message()
		if len(self.email_messages) > 0:
			# print "lll",self.email_messages
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
					the_msg['Subject'] =Subject
					the_msg['From'] = from1
					the_msg['To'] = email_id
					part1 =  MIMEText(user_message, "html")
					the_msg.attach(part1)
					print(the_msg.as_string())
					email_obj.sendmail(from1,[email_id],the_msg.as_string())
				except SMTPException:
					print "exception occured"
			return True
		return False		

# user_obj = MessageUser()
# user_obj.add_user("satish kumar",2222.222,"hungrygupta@gmail.com")
# user_obj.add_user("satish kumar gupta",333222.222,"hungrygupta@gmail.com")
# print user_obj.send_email()
