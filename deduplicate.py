def make_list(file):
"""opens file  reads it and separates each email into a list format"""
	with open(file, "r") as emails_file:
		list_emails = emails_file.read().split("\n")
	return list_emails

def find_duplicates(events, happy_hour):
"""Appends each email that is in both lists into a new list"""
	double = []
	for emails in events:
		if emails in happy_hour:
			double.append(emails)
	return double
		
#maks a list of emails for each event	
events = make_list("events.txt")
happy_hour = make_list("happy_hour.txt")

#list/ set takes out duplicates and makes one list with all the emails of both events
print "These are all the emails:"
for each_email in list(set(events + happy_hour)):
	print each_email

#Prints results of duplicate emails from the new list derived from the function
print "These are the emails that came to both events:"
for each_email in find_duplicates( events, happy_hour ):	
	print each_email
