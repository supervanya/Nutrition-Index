import db

while True:
	name = input("> ")
	id = db.get_user_id(name)
	print(id)