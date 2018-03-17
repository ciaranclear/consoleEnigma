from settings import NUMBERS_DICT

class Keyboard(object):

	def __init__(self):

		super(Keyboard, self).__init__()


	def keyboard_input(self, character):
		"""keyboard_input takes a character as an argument. If the \
		character is an alphabetic character the uppercase of that \
		character is returned. If the character is numeric its \
		alphabetic equivilant is looked up in the numbers dictionary \
		and returned. If the character is not alphanumeric None is \
		returned"""

		if character.isalnum():
			if character.isalpha():
				return character.upper()
			elif character.isdigit():
				return NUMBERS_DICT[character]
		else:
			return None


if __name__ == "__main__":

	numbers = [0,1,2,3,4,5,6,7,8,9]
	keyboard = Keyboard()
	for number in numbers:
		print(keyboard.keyboard_input(str(number)))