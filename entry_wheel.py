from validator import Validator

class Entry_wheel(object):

	def __init__(self, ETW_list):

		self._validator = Validator()
		self._ETW_list = self._validate_ETW_list(ETW_list)
		super(Entry_wheel, self).__init__()

	# PUBLIC METHODS ------------------------------------------------------------------

	def output_to_rotor(self, character):

		character = self._validator.valid_character(character)
		return self._ETW_list.index(character)


	def output_from_rotor(self, index):

		if isinstance(index, int) and index <= 25 and index >= 0:
			return self._ETW_list[index]
		else:
			raise ValueError("{} is not a valid index".format(index))

	# PRIVATE METHODS ----------------------------------------------------------------

	def _validate_ETW_list(self, ETW_list):

		valid_characters = []
		for character in ETW_list:
			character = self._validator.valid_character(character)
			valid_characters.append(character)
		unique = set(valid_characters)
		if len(unique) == 26:
			return valid_characters
		else:
			raise ValueError("{} not a valid entry wheel list".format(valid_characters))


if __name__ == "__main__":

	letters = [chr(i) for i in range(65, 91)]
	letters2 = [chr(i) for i in range(65, 90)]
	letters2.append('Y')
	entry_wheel = Entry_wheel(letters)

	for letter in letters:
		print(entry_wheel.output_to_rotor(letter))

	for i in range(26):
		print(entry_wheel.output_from_rotor(i))

	try:
		entry_wheel2 = Entry_wheel(letters2)
	except ValueError:
		print("entry wheel list is not valid")