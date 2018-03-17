from validator import Validator
from shorting_bar import Shorting_bar

class Plugboard(object):

	def __init__(self):

		self._validator = Validator()
		self._characters = [chr(i) for i in range(65, 91)]
		self._plugboard_dict = {}
		self.clear_plugboard()
		super(Plugboard, self).__init__()

	# PUBLIC METHODS ------------------------------------------------------------------

	def clear_plugboard(self):
		"""clear_plugboard creates a new dictionary object \
		and self steckers each plugboard character with a shorting \
		bar object. The new dictionary is then set as the plugboard"""

		new_dict = {}
		for character in self._characters:
			new_dict[character] = Shorting_bar(character)
		self._plugboard_dict = new_dict


	def try_connect_plug(self, character, plug):
		"""try_connect_plug takes a character and a plug object \
		as an argument. If the character is valid and that plugboard \
		character is available then the plug object will be connected \
		to that character and the plug object stored in the plugboard \
		dict. If connection succesful returns True else returns False"""

		character = self._validator.valid_character(character)
		if self._plugboard_dict[character].get_device_type() == "SHORTING_BAR":
			plug.connect_plug(character)
			self._plugboard_dict[character] = plug
			return True
		else:
			return False


	def connect_plug(self, character, plug):
		"""connect_plug takes a character and a plug object as an \
		argument. If the character is valid any device currently \
		connected to that plugboard character is disconnected and \
		the plug object is connected to that character and stored \
		in the plugboard dict"""

		character = self._validator.valid_character(character)
		self.disconnect_plug(character)
		plug.connect_plug(character)
		self._plugboard_dict[character] = plug
		return True


	def disconnect_plug(self, character):
		"""disconnect_plug takes a character as an argument. If \
		the character is valid and that plugboard character is not \
		connected to a shorting bar then the connected device \
		will be disconnected. A shorting bar object will then \
		be connected to that plugboard character. If a device was \
		disconnected returns True else returns False"""

		character = self._validator.valid_character(character)
		if self._plugboard_dict[character].get_device_type() != "SHORTING_BAR":
			self._plugboard_dict[character].disconnect_plug()
			self._plugboard_dict[character] = Shorting_bar(character)
			return True
		else:
			return False


	def get_connected_device(self, character):
		"""get_connected_device takes a character as an argument. \
		If character is valid returns the connected device type \
		connected to that plugboard character"""

		character = self._validator.valid_character(character)
		return self._plugboard_dict[character].get_device_type()


	def get_connected_device_id(self, character):
		"""get_connected_device_id takes a character as an argument. \
		If character is valid returns the device id of the connected \
		device"""

		character = self._validator.valid_character(character)
		return self._plugboard_dict[character].get_device_id()


	def connected_to(self, character, pin_type):
		"""connected_to takes a character and a pin_type as an argument. \
		If character is valid and the pin_type is valid returns the \
		corresponding character that the pin is connected to. If pin_type \
		is not valid a ValueError is raised"""

		character = self._validator.valid_character(character)
		if self._validator.valid_pin_type(pin_type):
			return self._plugboard_dict[character].pin_connected_to(pin_type)
		else:
			raise ValueError("{} is not a valid pin type".format(pin_type))


	def valid_plugboard(self):
		"""valid_plugboard calls the valid_device method on each connected \
		device on the plugboard. If all connected devices are valid returns \
		True else returns False"""

		for character in self._characters:
			if not self._plugboard_dict[character].valid_device():
				return False
		return True


	def get_plugboard_dict(self):
		"""get_plugboard_dict returns a dictionary with key value pairs \
		of plugboard characters and a character dictionary. Each character \
		dictionary contains key value pairs for each pins corresponding \
		character and the connected device type"""

		plugboard_dict = {}
		for character in self._plugboard_dict:
			plugboard_dict[character] = self._character_dict(character)
		return plugboard_dict

	# PRIVATE METHODS ----------------------------------------------------------------

	def _character_dict(self, character):
		"""_character_dict takes a character as an argument and returns a \
		dictionary with key value pairs for each pins corresponding \
		character and the connected device type"""

		character_dict = {}
		character_dict["SM"] = self._plugboard_dict[character].pin_connected_to("SM")
		character_dict["LG"] = self._plugboard_dict[character].pin_connected_to("LG")
		character_dict["CONNECTED_DEVICE"] = \
		self._plugboard_dict[character].get_device_type()
		character_dict["CONNECTED_DEVICE_ID"] = \
		self._plugboard_dict[character].get_device_id()
		return character_dict


if __name__ == "__main__":

	plugboard = Plugboard()