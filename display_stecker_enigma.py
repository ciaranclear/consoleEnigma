from display_enigma import Display_enigma
from formater import Formater
from settings import*

class Display_stecker_enigma(Display_enigma):

	def __init__(self):
		
		super(Display_stecker_enigma, self).__init__()

	
	def print_machine(self):

		self._print_machine_heading()
		self._print_machine_summary()
		self.print_plugboard()
		self.print_rotor_group()


	def print_plugboard(self):

		self._print_plugboard_heading()
		self._print_plugboard_rows()
		self._print_padded_string()


	def _print_plugboard_rows(self):

		characters = ENIGMA_LAYOUT
		first_row = characters['FIRST_ROW']
		second_row = characters["SECOND_ROW"]
		third_row = characters["THIRD_ROW"]
		self._print_row("ROW ONE", first_row, " " * 7)
		self._print_horizontal_dashed_row()
		self._print_row("ROW TWO", second_row, " " * 11)
		self._print_horizontal_dashed_row()
		self._print_row("ROW THREE", third_row, " " * 7)


	def _print_row(self, row_title, character_list, offset):

		character_row = self._row_title_string(row_title)
		character_row += offset
		for character in character_list:
			character_row += "{}{}".format(character, " " * 7)
		print(character_row)
		self._print_virtical_dashed_row(offset, len(character_list))
		self._print_connected_character_row(character_list, offset)


	def _print_connected_character_row(self, character_list, offset):

		connected_row = self._row_title_string("CONNECTED TO")
		connected_row += offset
		for character in character_list:
			connected_char = self._plugboard.connected_to(character, "LG")
			connected_row += "{}{}".format(connected_char, " " * 7)
		print(connected_row)


	def _print_plugboard_summary(self):
		
		connections_list = []
		ordered_characters = self._make_ordered_keys_string()
		plugboard_dict = self._plugboard.get_plugboard_dict()
		connections_list = self._get_connections(ordered_characters,
									connections_list, plugboard_dict)
		if len(connections_list) == 0:
			connections_list.append("No connections")
		elif len(connections_list) > 13:
			next_line_space = "\n{}".format(" " * 16)
			connections_list.insert(13, next_line_space)
		connections_list.insert(0, "\nPLUGBOARD       ")
		plugboard_string = Formater.list_to_string(connections_list)
		print(plugboard_string)


	@staticmethod
	def _get_connections(character_list, connections_list, dictionary):

		for character in character_list:
			if dictionary[character]["CONNECTED_DEVICE"] == "STECKER_PLUG":
				connected_char = dictionary[character]["LG"]
				connection_string = "{0}{1} ".format(character, connected_char)
				connections_list.append(connection_string)
				connections_list = self._remove_duplicate_pairs(connections_list)
		return connections_list
	

	@staticmethod
	def _remove_duplicate_pairs(connections_list):

		connections_list.sort()
		non_duplicate_list = []
		for i in range(len(connections_list)):
			if i % 2 == 0:
				non_duplicate_list.append(connections_list[i])
		return non_duplicate_list


	def _print_horizontal_dashed_row(self):

		print("-" * 88)


	def _print_virtical_dashed_row(self, offset, repeat):

		line = "{0}{1}{2}{3}".format(" " * 15,"|",offset , "|       " * repeat)
		print(line)