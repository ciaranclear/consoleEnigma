from rotor import*

class Enigma_interface(object):

	def __init__(self):

		super(Enigma_interface, self).__init__()


	def menu_select_rotors(self):

		self.print_rotor_group()

		while True:
			print("Enter a number to select one of the following\
				\n1. Select One Rotor\
				\n2. Select All Rotors")

			inpt = input()

			if inpt == '1':
				self.menu_select_one_rotor()
				break
			elif inpt == '2':
				self.menu_select_all_rotors()
				break
			else:
				print("Invalid input! try again")
		self.print_rotor_group()


	def menu_select_a_rotor(self, rotor_list, position):

		while True:
			print("Enter a number to select a rotor for R{}".format(position))

			for i in range(len(rotor_list)):
				print("{0} {1}".format(i+1, rotor_list[i]))
			try:
				inpt = int(input())
			except Exception:
				pass
			else:
				if inpt >= 1 and inpt <= len(rotor_list):
					self._rotor_group.select_rotor(rotor_list[inpt-1], position)
					break
			print("Invalid input! try again")
		return


	def menu_print_active_rotor_types(self):

		active_rotors = self._rotor_group.active_rotors_dictionary()
		active_rotors_string = "Current active rotors :"
		for i in range(self._rotor_group.rotor_group_size()):
			position = i+1
			active_rotors_string += " R{} '{}' "\
				.format(position, active_rotors[position])
		print(active_rotors_string)


	def menu_select_ring_settings(self):

		self.menu_print_ring_settings()

		for i in range(self._rotor_group.rotor_group_size()):
			position = i+1
			active_rotors_dict = self._rotor_group.active_rotors_dictionary()
			while True:
				if not active_rotors_dict[position]:
					print("R{} has no rotor selected".format(position))
					break
				print("For rotor position R{} enter a {} to set the ring setting"\
					.format(position, self._required_type_string(position)))
				setting = input()
				try:
					setting = self._rotor_group.valid_ring_setting(position, setting)
				except RotorRingCharError:
					print("Invalid input! ring setting must be a {}"\
						.format(self._required_type_string(position)))
					continue
				else:
					self._rotor_group.change_ring_setting(position, setting)
					self.menu_print_ring_settings()
					break


	def menu_print_ring_settings(self):

		ring_settings = self._rotor_group.get_ring_settings_list()
		ring_settings_string = "Current ring settings :"
		for i in range(self._rotor_group.rotor_group_size()):
			position = i+1
			ring_settings_string += " R{} '{}' "\
				.format(position, ring_settings[i])
		print(ring_settings_string)


	def menu_select_rotor_settings(self):

		self.menu_print_rotor_settings()

		for i in range(self._rotor_group.rotor_group_size()):
			position = i+1
			active_rotors_dict = self._rotor_group.active_rotors_dictionary()
			while True:
				if not active_rotors_dict[position]:
					print("R{} has no rotor selected".format(position))
					break
				print("For rotor position R{} enter a {} to set the rotor setting"\
					.format(position, self._required_type_string(position)))
				setting = input()
				try:
					setting = self._rotor_group.valid_ring_setting(position, setting)
				except RotorRingCharError:
					print("Invalid input! rotor setting must be a {}"\
						.format(self._required_type_string(position)))
					continue
				else:
					self._rotor_group.change_rotor_setting(position, setting)
					self.menu_print_rotor_settings()
					break


	def menu_print_rotor_settings(self):

		current_rotor_settings = self._rotor_group.get_rotor_settings_list()
		current_settings = "Current rotor settings :"
		for setting in range(1, self._rotor_group.rotor_group_size()+1):
			current_settings += "  R{0} \"{1}\"".format(setting, current_rotor_settings[setting-1])
		print(current_settings)


	def menu_select_reflector(self):
		
		reflectors = self.get_reflectors_list()
		print("The current active reflector is {}.\nEnter a number to select a reflector"
			.format(self.active_reflector_type()))
		while True:
			for i in range(len(reflectors)):
				print("{0} {1}".format(i+1, reflectors[i]))
			try:
				inpt = int(input())
			except Exception:
				pass
			else:
				if inpt >= 1 and inpt <= len(reflectors):
					reflector = reflectors[inpt-1]
					self.set_reflector(reflector)
					break
			print("Invalid input! try again")
		print("The current active reflector is {}".format(self.active_reflector_type()))


	def plain_text_input(self):

		if self.valid_enigma():
			print("\nEnter the text you wish to encrypt. Only alpha numeric characters\
				\nwill be encrypted. All other characters will be ignored\n")

			plain_text = input()
			cypher_text = self.get_output(plain_text)
			cypher_text = self._add_whitespace(cypher_text)
			print("\n{}".format(cypher_text))
		else:
			print(self._diagnostics.get_diagnostic_string())
			print("\nEnigma machine setup is not complete")


	def menu_get_position(self):
		
		while True:
			print("\nEnter the rotor position you wish to change")
			try:
				position = int(input())
			except Exception:
				position = None
			if self._rotor_group.valid_position(position):
				return position
			print("\n{} is not a valid rotor position".format(position))


	def menu_get_letter(self, message):

		while True:
			print(message)
			character = input()
			if len(character) == 1 and character.isalpha():
					return character.upper()
			elif len(character) != 1:
				print("\nOne letter must be entered")
				continue
			else:
				print("\n{} Invalid input! try again".format(character))


	def menu_get_plug_override(self, letter):

		while True:
			print("\n{} is already has a plug connected do you want to overide it y/n"\
				.format(letter))
			inpt = input()
			if inpt.isalpha():
				if inpt.upper() == 'Y':
					return True
				elif inpt.upper() == 'N':
					return False
			print("\nInvalid input! try again")


	def _required_type_string(self, rotor_position):


		required_type = self._rotor_group.rotor_ring_character_type(rotor_position)
		if required_type == "letter":
			return "letter"
		elif required_type == "number":
			return "number between 01 and 26"


	@staticmethod
	def _add_whitespace(text):

		new_text = ""
		for i in range(len(text)):
			if i % 5 == 0 and i != 0:
				new_text += ' '
			new_text += text[i]

		return new_text