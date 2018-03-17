from formater import Formater
from settings import*

class Display_enigma(object):

	def __init__(self):

		self._display_width = 93
		super(Display_enigma, self).__init__()


	def print_rotor_group(self):

		self._print_rotor_group_heading()
		self._print_entry_wheel()
		self._print_rotors()
		self._print_reflector()


	def _print_machine_heading(self):

		string = "[{0} ENIGMA]".format(self._machine_type)
		machine_heading = Formater.pad_string(string, '*', self._display_width)
		print(machine_heading)


	def _print_machine_summary(self):
		
		self._print_summary_heading()
		self._print_rotor_string()
		self._print_rotors_summary()
		self._print_reflector_summary()
		self._print_plugboard_summary()
		self._print_machine_status_summary()
		self._print_padded_string()


	def _print_rotor_string(self):

		print("\n{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}\n".format("ROTORS", " " * 4, "POS",
															  " " * 4, "TYPE", " " * 7,
															  "ROTOR SETTING", " " * 4,
															  "RING SETTING", " " * 4,
															  "TURNOVER CHARACTERS"))


	def _print_summary_heading(self):

		string = "[MACHINE SETUP SUMMARY]"
		summary_heading = Formater.pad_string(string, '*', self._display_width)
		print(summary_heading)


	def _print_padded_string(self):

		print("\n" + Formater.pad_string('*', '*', self._display_width))


	def _print_plugboard_heading(self):

		plugboard_heading = Formater.pad_string("[PLUGBOARD]", '*', self._display_width)
		print(plugboard_heading + "\n")


	def _print_rotors_summary(self):

		for i in range(self._rotor_group._rotor_group_size):
			position = i+1
			if self._rotor_group._active_rotors_dict[position]:
				self._print_rotor_summary(position)
			else:
				self._print_empty_rotor_summary(position)


	def _print_rotor_summary(self, position):

		rd = self._rotor_group._active_rotors_dict[position].get_rotor_dict()
		turnover_characters = Formater.list_to_string(rd["TURNOVER_CHARACTERS"])
		rotor_type_string = Formater.right_pad_string(rd["ROTOR_TYPE"], " ", 9)
		print("{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}".format(" " * 11, position, " " * 5,
													  rotor_type_string, " " * 8,
													  rd["ROTOR_SETTING"], " " * 15,
													  rd["RING_SETTING"], " " * 18,
													  turnover_characters))


	def _print_empty_rotor_summary(self, position):

		print("{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}".format(" " * 11, position, " " * 5,
													  "None selected", " " * 4, '-',
													  " " * 15, '-', " " * 16, '-'))


	def _print_reflector_summary(self):

		if self._active_reflector:
			reflector_type = self._active_reflector.reflector_type()
		else:
			reflector_type = "No reflector selected"
		print("\nREFLECTOR TYPE = {}".format(reflector_type))


	def _print_machine_status_summary(self):

		if self.valid_enigma():
			status = "VALID"
		else:
			status = self._diagnostics.get_diagnostic_string()
		print("\nMACHINE STATUS {}".format(status))


	def _print_rotor_group_heading(self):

		rotor_group_heading = \
			Formater.pad_string("[ROTOR GROUP]", '*', self._display_width)
		print(rotor_group_heading)


	def _print_entry_wheel(self):

		entry_wheel_heading = \
			Formater.pad_string("[ENTRY WHEEL]", '*', self._display_width)
		print(entry_wheel_heading)
		entry_wheel_string = self._row_title_string("ENTRY WHEEL")
		entry_wheel_list = self.get_entry_wheel_list()
		for character in entry_wheel_list:
			entry_wheel_string += " {} ".format(character)
		print(entry_wheel_string + "\n")


	def _print_rotor_heading(self, position, rotor_type):
		
		rotor_position_string = "****[ROTOR {}]****".format(position)
		rotor_type_string = "(TYPE {})".format(rotor_type)
		rotor_heading = "{}{}{}".format("*" * len(rotor_type_string),
							rotor_position_string, rotor_type_string)
		rotor_heading = Formater.pad_string(rotor_heading, "*", self._display_width)
		print(rotor_heading)


	def _print_rotors(self):
		
		for i in range(self._rotor_group._rotor_group_size):
			position = i+1
			rotor_dict = self._rotor_group.get_rotor_dict(position)
			if rotor_dict:
				self._print_rotor(position, rotor_dict)
			else:
				self._print_empty_rotor(position)


	def _print_rotor(self, position, rotor_dict):
		
		rotor_type = rotor_dict["ROTOR_TYPE"]
		self._print_rotor_heading(position, rotor_type)
		self._print_absolute_character_row(rotor_dict)
		self._print_rotor_character_row(rotor_dict)
		self._print_ring_character_row(rotor_dict)
		self._print_turnover_row(position, rotor_dict)


	def _print_empty_rotor(self, position):
		
		self._print_rotor_heading(position, "NONE SELECTED")
		blank_list = ['-' for i in range(26)]
		blank_list = self._pad_rotor_string_characters(blank_list)
		self._print_rotor_group_row("CORE CHARS", blank_list)
		self._print_rotor_group_row("ROTOR CHARS", blank_list)
		self._print_rotor_group_row("RING CHARS", blank_list)
		if position <= 3:
			self._print_rotor_group_row("TURNOVER CHARS", blank_list)


	def _print_absolute_character_row(self, rotor_dict):

		absolute_characters = rotor_dict["ABSOLUTE_CHARACTERS"]
		absolute_characters = self._pad_rotor_string_characters(absolute_characters)
		self._print_rotor_group_row("CORE CHARS", absolute_characters)


	def _print_rotor_character_row(self, rotor_dict):

		rotor_characters = rotor_dict["ROTOR_CHARACTERS"]
		rotor_characters = self._pad_rotor_string_characters(rotor_characters)
		self._print_rotor_group_row("ROTOR CHARS", rotor_characters)


	def _print_ring_character_row(self, rotor_dict):

		ring_characters = self._add_ring_setting(rotor_dict)
		ring_characters = self._pad_rotor_string_characters(ring_characters)
		self._print_rotor_group_row("RING CHARS", ring_characters)


	def _print_rotor_group_row(self, row_title, character_list):

		row_title = self._row_title_string(row_title)
		character_string = Formater.list_to_string(character_list)
		row_string = row_title + character_string
		print(row_string)


	def _add_ring_setting(self, rotor_dict):

		ring_characters = rotor_dict["RING_CHARACTERS"].copy()
		ring_setting = rotor_dict["RING_SETTING"]
		for i in range(len(ring_characters)):
			character = ring_characters[i]
			if character == ring_setting:
				character = "({})".format(character)
				ring_characters[i] = character
				break
		return ring_characters


	def _print_turnover_row(self, position, rotor_dict):

		if position <= 3:
			row_title = self._row_title_string("TURNOVER CHARS")
			turnover_list = self._add_turnover_settings(rotor_dict)
			turnover_string = Formater.list_to_string(turnover_list)
			row_string = row_title + turnover_string + "\n"
			print(row_string)
		else:
			print("")


	@staticmethod
	def _add_turnover_settings(rotor_dict):

		ring_characters = rotor_dict["RING_CHARACTERS"]
		turnover_characters = rotor_dict["TURNOVER_CHARACTERS"]
		turnover_list = [" - " for i in range(len(ring_characters))]
		for turnover_character in turnover_characters: 
			for i in range(len(ring_characters)):
				if ring_characters[i] == turnover_character:
					turnover_list[i] = "|^|"
		return turnover_list


	@staticmethod
	def _pad_rotor_string_characters(character_list):

		for i in range(len(character_list)):
			character = character_list[i]
			padded_character = "{:^3}".format(character)
			character_list[i] = padded_character
		return character_list


	def _print_reflector(self):
		
		if self.active_reflector_type():
			self._print_valid_reflector()
		else:
			self._print_empty_reflector()


	def _print_reflector_heading(self, reflector_type):

		reflector_string = "[{}]".format(reflector_type)
		reflector_heading = \
			Formater.pad_string(reflector_string, '*', self._display_width)
		print(reflector_heading)


	def _print_valid_reflector(self):
		
		self._print_valid_reflector_heading()
		self._print_valid_reflector_input_row()
		self._print_valid_reflector_output_row()
		self._print_padded_string()


	def _print_valid_reflector_heading(self):

		reflector_dict = self.get_active_reflector_dict()
		reflector_type = reflector_dict["REFLECTOR_TYPE"]
		self._print_reflector_heading(reflector_type)


	def _print_valid_reflector_input_row(self):

		input_row_title = self._row_title_string("INPUT CHARS")
		input_chars_list = LETTERS.copy()
		input_chars_list = self._pad_rotor_string_characters(input_chars_list)
		self._print_rotor_group_row("INPUT CHARS", input_chars_list)


	def _print_valid_reflector_output_row(self):

		reflector_dict = self.get_active_reflector_dict()
		output_row_title = self._row_title_string("OUTPUT CHARS")
		output_chars_list = reflector_dict["REFLECTOR_CHARACTERS"]
		output_chars_list = self._pad_rotor_string_characters(output_chars_list)
		self._print_rotor_group_row("OUTPUT CHARS", output_chars_list)


	def _print_empty_reflector(self):
		
		reflector_type = "No reflector selected"
		self._print_reflector_heading(reflector_type)
		blank_list = ['-' for i in range(26)]
		blank_list = self._pad_rotor_string_characters(blank_list)
		self._print_rotor_group_row("INPUT CHARS", blank_list)
		self._print_rotor_group_row("OUTPUT CHARS", blank_list)
		self._print_padded_string()


	@staticmethod
	def _row_title_string(string):

		if isinstance(string, str):
			string += " "
			string = "{:-<15}|".format(string)
			return string
		else:
			raise TypeError("function argument must be of type string")


	def _make_ordered_keys_string(self):

		characters = ENIGMA_LAYOUT
		first_row = characters['FIRST_ROW']
		second_row = characters["SECOND_ROW"]
		third_row = characters["THIRD_ROW"]
		first_row_string = Formater.list_to_string(first_row)
		second_row_string = Formater.list_to_string(second_row)
		third_row_string = Formater.list_to_string(third_row)
		ordered_characters = "{0}{1}{2}".format(first_row_string, 
			second_row_string, third_row_string)
		return ordered_characters