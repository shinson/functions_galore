def nested_list(csv_file):
"""Separate csv by new line then seperate each item in the list using the while loup so that each line becomes a list within a list"""
	final_list = []
	with open(csv_file, "r") as list_file:
		list_file = list_file.read().split("\n")
	x = 1
	while x < len(list_file):
		final_list.append(list_file[x].split(","))
		x += 1
	return final_list
		

print nested_list("employees.csv")
