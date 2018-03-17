from display_enigma import Display_enigma
from formater import Formater
from settings import*

class Display_uhr_enigma(Display_enigma):

	def __init__(self):

		super(Display_uhr_enigma, self).__init__()


	def print_machine(self):
		"""print_machine calls the functions required to print an enigma
		machine that has an uhr box"""

		self._print_machine_heading()
		self._print_machine_summary()
		self.print_uhr_box()
		self.print_plugboard()
		self.print_rotor_group()


	def print_uhr_box(self):
		"""print_uhr_box calls the functions required to print the uhr box"""

		self._print_uhr_box_heading()
		self._print_uhr_box_setting()
		self._print_number_of_connected_plugs()
		self._print_number_of_disconnected_plugs()
		self._print_plugs_heading()
		self._print_blank_columns_line()
		self._print_uhr_plug_connections()
		self._print_padded_string()


	def _print_uhr_box_heading(self):
		"""_print_uhr_box_heading prints the uhr box heading in a padded string"""
		
		uhr_box_heading = Formater.pad_string("[UHR BOX]", '*', self._display_width)
		print(uhr_box_heading)


	def _print_uhr_box_setting(self):
		"""_print_uhr_box_setting prints the current uhr box setting"""

		current_setting = self._uhr_box.get_uhr_box_setting()
		print("\nCURRENT UHR BOX SETTING = {}".format(current_setting))


	def _print_number_of_connected_plugs(self):
		"""_print_number_of_connected_plugs prints the number of plugs
		connected to the plugboard"""

		connected = len(self._uhr_box.connected_uhr_plugs_list())
		print("NUMBER OF CONNECTED PLUGS = {}".format(connected))


	def _print_number_of_disconnected_plugs(self):
		"""_print_number_of_disconnected_plugs prints the numbe of
		unconnected uhr plugs"""

		disconnected = len(self._uhr_box.available_uhr_plugs_list())
		print("NUMBER OF DISCONNECTED PLUGS = {}\n".format(disconnected))


	def _print_plugs_heading(self):
		"""_print_plugs_heading prints the column headings for each plug
		pin type for A type and B type plugs"""

		print("{0}{2}{1}{3}{1}{4}{1}{5}".format(" " * 5, "  |  ",
					  "A PLUGS LARGE PINS", "A PLUGS SMALL PINS",
					  "B PLUGS LARGE PINS", "B PLUGS SMALL PINS"))


	def _print_blank_columns_line(self):
		"""_print_blank_columns_line prints a line of column seperators"""

		print("{0}{1}{1}{1}".format(" " * 3, (" " * 22) + "|"))


	def _print_uhr_plug_connections(self):
		"""_print_uhr_plug_connections prints a row for each plug number
		in tha range of 01 to 10. Each row contains four substrings. Each
		substring contains a plug pin id, the plugboard character it is
		connected to, the corresponding plug pin id it is connected to and
		the corresponding plugboard character it is connected to"""

		uhr_dict = self._uhr_box.get_uhr_box_dict()
		plugs_dict = uhr_dict["CONNECTIONS"]["PLUGS"]
		for i in range(10):
			plug_number = i+1
			string_num = Formater.left_pad_string(str(plug_number), "0", 2)
			sub_strings = []
			sub_strings = self._get_sub_strings(string_num, plugs_dict)
			print("{0}  {1} | {2} | {3} | {4}".format(string_num,
				sub_strings[0], sub_strings[1], sub_strings[2], sub_strings[3]))


	def _get_sub_strings(self, string_num, plugs_dict):
		"""_get_sub_string takes two digit string and a plugs_dict. This function
		returns a list with the four sub strings for each pin type"""

		plug_pin_types = ["ALG", "ASM", "BLG", "BSM"]
		sub_strings = []
		for plug_pin_type in plug_pin_types:
			plug_pin_id = "{0}{1}".format(string_num, plug_pin_type)
			plug_id = plug_pin_id[0:3]
			plug_dict = plugs_dict[plug_id]
			connection_string = self._uhr_plug_connection_string(plug_pin_id, plug_dict)
			sub_strings.append(connection_string)
		return sub_strings


	def _uhr_plug_connection_string(self, plug_pin_id, plug_dict):
		"""_uhr_plug_connection_string takes a plug_pin_id string and a
		plug dict. This function assembles each sub string"""
		
		character = plug_dict["CHAR"]
		connected_pin_id = plug_dict[plug_pin_id]["CONNECTED_PIN_ID"]
		connected_pin_character = plug_dict[plug_pin_id]["CONNECTED_CHAR"]
		if not character:
			character = '-'
		if not connected_pin_character:
			connected_pin_character = '-'
		connection_string = "{0}-({1})->{2}-({3})".format(plug_pin_id, character,
									   connected_pin_id, connected_pin_character)
		return connection_string


	def _print_plugboard_summary(self):
		"""_print_plugboard_summary prints the """
		
		connections_list = []
		connections_list.append("\nPLUGBOARD       ")
		if self._uhr_box.uhr_box_disconnected():
			connections_list.append("No connections")
		else:
			connections_list = self._get_connections_list(connections_list)
		plugboard_string = Formater.list_to_string(connections_list)
		print(plugboard_string)


	def _get_connections_list(self, connections_list):

		ordered_characters = self._make_ordered_keys_string()
		plugboard_dict = self._plugboard.get_plugboard_dict()
		connections_list = self._get_connections(ordered_characters,
								   connections_list, plugboard_dict)
		if len(connections_list) > 11:
			next_line_space = "\n{}".format(" " * 16)
			connections_list.insert(11, next_line_space)
		return connections_list


	@staticmethod
	def _get_connections(character_list, connections_list, dictionary):

		for character in character_list:
			if dictionary[character]["CONNECTED_DEVICE"] == "UHR_BOX_PLUG":
				plug_id = dictionary[character]["CONNECTED_DEVICE_ID"]
				connection_string = "{0}->{1} ".format(character, plug_id)
				connections_list.append(connection_string)
		connections_list.sort()
		return connections_list


	def print_plugboard(self):

		self._print_plugboard_heading()
		self._print_plugboard_rows()
		self._print_padded_string()


	def _print_plugboard_rows(self):
		
		characters = ENIGMA_LAYOUT
		first_row = characters['FIRST_ROW']
		second_row = characters["SECOND_ROW"]
		third_row = characters["THIRD_ROW"]
		self._print_row("ROW ONE", first_row, " ")
		self._print_horizontal_dashed_row()
		self._print_row("ROW TWO", second_row, "     ")
		self._print_horizontal_dashed_row()
		self._print_row("ROW THREE", third_row, " ")


	def _print_row(self, row_title, character_list, offset):

		pin_row = self._row_title_string(row_title)
		pin_row += offset
		for character in character_list:
			pin_row += character + "LG " + character + "SM "
		print(pin_row)
		self._print_virtical_dashed_row(offset, len(character_list)*2)
		self._print_plug_id_row(character_list, offset)


	def _print_horizontal_dashed_row(self):

		print("-" * 88)


	def _print_virtical_dashed_row(self, offset, repeat):

		line = "{0}{1}{2}{3}".format(" " * 15,"|",offset + " ","|   " * repeat)
		print(line)


	def _print_plug_id_row(self, character_list, offset):

		plug_row = self._row_title_string("PLUG ID")
		plug_row += offset
		for character in character_list:
			device_type = self._plugboard.get_connected_device(character)
			if device_type == "UHR_BOX_PLUG":
				plug_id = self._plugboard.get_connected_device_id(character)
				plug_row += " ({})  ".format(plug_id)
			else:
				plug_row += " |___|  "
		print(plug_row)