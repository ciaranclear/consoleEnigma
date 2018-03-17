from validator import Validator

class Shorting_bar(object):

	def __init__(self, character = None):

		self._validator = Validator()
		self._device_type = "SHORTING_BAR"
		self._character = character
		self._connected = False
		if character:
			self._character = self._validator.valid_character(character)
			self._connected = True
		super(Shorting_bar, self).__init__()

	# PUBLIC METHODS ------------------------------------------------------------------

	def pin_connected_to(self, pin_type):
		"""pin_connected_to takes a pin_type as an argument but \
		is not used as this is a polymorphic method. Returns the \
		character the shorting bar is connected to"""

		return self._character


	def get_device_type(self):
		"""get_device_type returns this device type"""

		return self._device_type


	def get_device_id(self):
		"""get_device_id returns a string with the device type \
		and character"""

		return "{0}_{1}".format(self._device_type, self._character)


	def connect_shorting_bar(self, character):
		"""connect_shorting_bar takes a character as an argument. \
		If the character is valid the shorting bar is connected to \
		that character and connected is set as True"""

		character = self._validator.valid_character(character)
		self._character = character
		self._connected = True


	def disconnect_shorting_bar(self):
		"""disconnect_shorting_bar sets character to None and \
		sets connected to False"""

		self._character = None
		self._connected = False


	def valid_device(self):
		"""valid_device returns the connected status of the shorting bar"""

		return self._connected


if __name__ == "__main__":

	shorting_bar = Shorting_bar('a')
	print(shorting_bar.pin_connected_to("SM"))
	print(shorting_bar.get_device_type())
	shorting_bar.connect_shorting_bar('b')
	print(shorting_bar.pin_connected_to("SM"))
	print(shorting_bar.get_device_type())
	print(shorting_bar.valid_device())