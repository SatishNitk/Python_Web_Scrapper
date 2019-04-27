from argparse import ArgumentParser
from csv_File import DataManager
from email_send4 import MessageUser



parser = ArgumentParser(prog="email_smtplib")
parser.add_argument("--user_id", type=int)
args = parser.parse_args()
# print(args)
# print(args.user_id)
# print(DataManager().read_data(args.user_id))
# for row in DataManager().read_data():
	# print row
# print(DataManager().append_data("satish","hungrygupta@gmail.com"))
# print(DataManager().edit_data(edit_id=7))


# MessageUser().add_user("satish kumar gupta",333222.222,"hungrygupta@gmail.com")
print MessageUser().send_email()