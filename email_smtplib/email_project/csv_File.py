import csv
import shutil
from tempfile import NamedTemporaryFile
import datetime

class DataManager():

	filename ="data.csv"
	temp_file = NamedTemporaryFile(delete = False)

	def get_length(self):
		with open("data.csv", "r") as csvfile:
			reader = csv.reader(csvfile)
			reader_list = list(reader)
			return len(reader_list)

	def append_data(self,name,email,date=""):
		with open(self.filename, 'a') as csvfile:
			fieldnames = ['id','name','email','date']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			next_id = self.get_length()
			if int(next_id) == 0:
				writer.writeheader()
			else:
				next_id -= 1 	
			writer.writerow(
				{
				"id": next_id + 1, 
				"name":name,
				"email":email,
				"date" : datetime.datetime.now()
				})
		return True	
	#append_data("datea.csv","satish","kr@gmail.com")

	def edit_data(self,edit_id=None, email=None,name=None,sent=None):
		with open(self.filename, "rb") as csvfile, self.temp_file:
			reader = csv.DictReader(csvfile)
			fieldnames = ['id','name','email','date']
			writer = csv.DictWriter(self.temp_file, fieldnames=fieldnames)
			writer.writeheader()
			# print("dd",self.temp_file.name)
			for row in reader:
				if edit_id is not None:
					if int(row["id"]) == 4:
						row["sent"] = "TRUE"
				elif email is not None:
					if str(row["email"] == str(email)):
						row['sent'] = "TRUE"
						row['name']  = name
				else:
					return False	
				writer.writerow({
					"id" : row["id"],
					"name" : row["name"],
					"email" : row["email"],
					"amount" :"323232",
					"date" : datetime.datetime.now(),
					"sent" : "TRUE"
					})
		shutil.move(self.temp_file.name, self.filename)
		return True
	# edit_data(email = "kr@gmail.com",name ="GUPTAKUMAR")

	def read_data(self,user_id=None, email=None):
		all_data = []
		unknown_user_id = None
		unknown_email = None
		with open(self.filename,"r") as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				if user_id is not None:
					if int(user_id) ==  int(row.get("id")):
						all_data.append(row)
						return all_data
					else:
						unknown_user_id = user_id	
	 			elif(email is not None):
	 				if str(email) == str(row.get("email")):
	 					all_data.append(row)
	 					return all_data
	 				else:
	 					unknown_email = email	
	 			else:
	 				all_data.append(row)

	 		if unknown_user_id is not None:
	 		    return "user not found with id={}".format(unknown_user_id)
	 		if unknown_email is not None:
	 		    return "user not found with email= {}".format(email)		
	 		return all_data    
	 	return None			

	# print(read_data(email="kr@gmail.com", user_id=1))