class Item:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def __str__(self):
		return f"{self.name}: {self.description}"

	def onTake(self):
		print(f"You have picked up {self.name}.")

	def onDrop(self):
		print(f"You have dropped {self.name}.")
