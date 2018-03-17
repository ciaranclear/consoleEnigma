

class Validator:

	def __init__(self):
		pass


	@staticmethod
	def unique_list(_list):

		unique_set = set(_list)
		if len(_list) == len(unique_set):
			return True
		else:
			return False


	@staticmethod
	def valid_character(character):

		if character.isalnum():
			return character.upper()
		else:
			raise ValueError("{} is not an alphanumeric character".format(character))


	@staticmethod
	def valid_pin_type(pin_type):

		return True if pin_type == "LG" or pin_type == "SM" else False


	@staticmethod
	def valid_stecker_plug_id(plug_id):

		if plug_id == "P1" or plug_id == "P2":
			return True
		else:
			raise ValueError("{} is not a valid plug_id", format(plug_id))