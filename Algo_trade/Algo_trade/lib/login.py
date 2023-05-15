class _USER:
	def __init__(self , name, password , right):
		self.name = name
		self.password = password
		self.right = right
	
	def login(self):
		if(self.name != "admin"):
			exit(1)
		if(self.passwaord != "admin"):
			exit(1)
	
	def login_get_info(self):
		pass


