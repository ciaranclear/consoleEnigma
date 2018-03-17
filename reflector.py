

class Reflector(object):

	def __init__(self, reflector_type, reflector_characters):

		self._reflector_type = reflector_type
		self._reflector_characters = self.validate_characters(reflector_characters)
		super(Reflector, self).__init__()


	def format_character(self, character):

		if character.isalpha():
			return character.upper()
		else:
			raise ValueError("invalid input. must be a character")


	def validate_characters(self, reflector_characters):
		valid_characters = []
		for character in reflector_characters:
			valid_characters.append(self.format_character(character))
		unique = set(valid_characters)
		if len(unique) == 26:
			return valid_characters
		else:
			raise ValueError(valid_characters, " not a valid reflector list")


	def reflector_output(self, index):
		
		return self._reflector_characters.index(chr(index + 65))


	def reflector_type(self):

		return self._reflector_type


	def reflector_list(self):

		return self._reflector_list


	def get_reflector_dict(self):

		reflector_dict = {}
		reflector_dict["REFLECTOR_CHARACTERS"] = self._reflector_characters.copy()
		reflector_dict["REFLECTOR_TYPE"] = self._reflector_type
		return reflector_dict


class UKWD_reflector(Reflector):

	def __init__(self, reflector_characters):
		super().__init__("UKWD", reflector_characters)

	def change_reflector_characters(self, new_characters):

		self._reflector_characters = self.validate_characters(new_characters)


if __name__ == "__main__":

	letters = [chr(i) for i in range(65, 91)]
	letters2 = letters[::-1]
	ref_type = "REFLECTOR"
	reflector = Reflector(ref_type, letters)
	for i in range(26):
		print(reflector.reflector_output(i))
	print(reflector.reflector_type())

	reflector2 = UKWD_reflector(letters2)
	for i in range(26):
		print(reflector2.reflector_output(i))
	print(reflector2.reflector_type())