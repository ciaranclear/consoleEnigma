from stecker_cable import Stecker_cable

class Stecker_cable_enigma_logic(object):

	def __init__(self):
		
		super(Stecker_cable_enigma_logic, self).__init__()


	def stecker_plug_already_connected(self, character):
		"""stecker_plug_already_connected takes a character as an argument. If \
		that plugboard character has a stecker plug connected to it returns True \
		else returns False"""
		
		character = self._validator.valid_character(character)
		if self._plugboard.get_connected_device(character) == "STECKER_PLUG":
			return True
		else:
			return False


	def connect_stecker_cable(self, character1, character2):
		"""connect_stecker_cable takes two characters as an argument. If both \
		characters are valid any device currently connected to each character \
		is disconnected. A stecker cable object is initialized. The stecker \
		plug objects are attained and an plug_id assigned to each of them. \
		Each plug is then connected to its plugboard character"""
		
		character1 = self._validator.valid_character(character1)
		character2 = self._validator.valid_character(character2)
		self.disconnect_stecker_cable(character1)
		self.disconnect_stecker_cable(character2)
		stecker_cable = Stecker_cable()
		plugs = stecker_cable.get_plugs()
		plug1 = plugs["P1"]
		plug2 = plugs["P2"]
		self._plugboard.connect_plug(character1, plug1)
		self._plugboard.connect_plug(character2, plug2)


	def disconnect_stecker_cable(self, character):
		"""disconnect_stecker_cable takes a character as an argument. If the \
		character is valid then the corresponding plugs character is attained \
		and both plugboard characters are disconnected"""

		character = self._validator.valid_character(character)
		connected_character = self._plugboard.connected_to(character, "LG")
		self._plugboard.disconnect_plug(character)
		self._plugboard.disconnect_plug(connected_character)


	def number_of_connected_plugs(self):
		"""number_of_connected_plugs counts the number of plugboard \
		characters connected to a stecker plug and returns that number"""

		plugboard_dict = self._plugboard.get_plugboard_dict()
		connected = 0
		for character in plugboard_dict:
			if plugboard_dict[character]["CONNECTED_DEVICE"] == "STECKER_PLUG":
				connected += 1
		return connected


	def get_connected_characters(self):
		"""get_connected_characters returns a list of lists. Each sub list \
		contains a character pair of connected plugboard characters"""

		plugboard_dict = self._plugboard.get_plugboard_dict()
		character_pair_list = []
		visited_chars = []
		for character in plugboard_dict:
			character_pair = []
			if plugboard_dict["CONNECTED_DEVICE"] == "STECKER_PLUG" and\
				character not in visited_chars:
				connected_char = plugboard_dict[character]["LG"]
				if connected_char:
					visited_chars.append(connected_char)
				character_pair.append(character)
				character_pair.append(connected_char)
				character_pair_list.append(character_pair)
		return character_pair_list