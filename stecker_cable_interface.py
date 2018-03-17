

class Stecker_cable_interface(object):

	def __init__(self):

		super(Stecker_cable_interface, self).__init__()


	def menu(self):
		""""menu allows the user to change the machines settings"""

		while True:
			print("\n{} ENIGMA MACHINE\
				  \nenter a number for one of the following\
				  \n1. Select Rotors\
				  \n2. Select Ring Settings\
				  \n3. Select Rotor Settings\
				  \n4. Select Reflector\
				  \n5. Stecker Setup\
				  \n6. Plain Text Input\
				  \n7. Display Machine\
				  \n8. Return To Main Menu".format(self._machine_type))

			inpt = input()

			if inpt == '1':
				self.menu_select_rotors()
			elif inpt == '2':
				self.menu_select_ring_settings()
			elif inpt == '3':
				self.menu_select_rotor_settings()
			elif inpt == '4':
				self.menu_select_reflector()
			elif inpt == '5':
				self.menu_stecker_setup()
			elif inpt == '6':
				self.plain_text_input()
			elif inpt == '7':
				self.print_machine()
			elif inpt == '8':
				break
			else:
				print("Invalid input! try again")
		return


	def menu_stecker_setup(self):

		self.print_plugboard()

		while True:
			print("\nEnter a number for one of the following\
					\n1. Connect Stecker Cables\
					\n2. Disconnect Stecker Cables\
					\n3. Clear Plugboard\
					\n4. Return To Enigma Menu")

			inpt = input()

			if inpt == '1':
				self.menu_connect_stecker_cable()
			elif inpt == '2':
				self.menu_disconnect_stecker_cable()
			elif inpt == '3':
				self.menu_clear_plugboard()
			elif inpt == '4':
				break
			else:
				print("Invalid input! try again")
		return


	def menu_get_letter_pair(self):

		while True:
			print("\nEnter a pair of letters to connect on the plugboard")
			characters = input()
			if len(characters) == 2 and characters[0].isalpha() and characters[1].isalpha() and\
				characters[0].upper() != characters[1].upper():
				return characters.upper()
			elif len(characters) != 2:
				print("Two letters must be input")
				continue
			elif characters[0].upper() == characters[1].upper():
				print("Two different letters must be entered")
				continue
			else:
				print("{} Invalid input! must be two letters in the form AB".format(characters))


	def menu_connect_stecker_cable(self):

		self.print_plugboard()

		while True:
			stecker_characters = self.menu_get_letter_pair()
			character1 = stecker_characters[0]
			character2 = stecker_characters[1]
			character1_connected = self.stecker_plug_already_connected(character1)
			character2_connected = self.stecker_plug_already_connected(character2)
			if not character1_connected and not character2_connected:
				self.connect_stecker_cable(character1, character2)
			elif character1_connected or character2_connected:
				character1_overide = True
				character2_overide = True
				if character1_connected:
					character1_overide = self.menu_get_plug_override(character1)
				if character2_connected and character1_overide:
					character2_overide = self.menu_get_plug_override(character2)
				if character1_overide and character2_overide:
					self.connect_stecker_cable(character1, character2)
			self.print_plugboard()
			if self.number_of_connected_plugs() >= 26:
				print("All plugboard characters are connected")
				break
			print("Enter y to connect another stecker cable")
			inpt = input()
			if inpt.upper() == 'Y':
				continue
			else:
				break


	def menu_disconnect_stecker_cable(self):

		self.print_plugboard()

		while self.number_of_connected_plugs() != 0:
			message = "\nEnter a letter to disconnect from the plugboard"
			character = self.menu_get_letter(message)
			if self.stecker_plug_already_connected(character):
				connected_character = self._plugboard.connected_to(character, "LG")
				self.disconnect_stecker_cable(character)
				print("{0}-{1} has been disconnected from the plugboard"
					.format(character, connected_character))
			else:
				print("{} is not connected to a stecker plug".format(character))
			self.print_plugboard()
			if self.number_of_connected_plugs() == 0:
				print("There are no stecker cables connected")
				break
			print("Enter y to disconnect another stecker cable")
			inpt = input()
			if inpt.upper() == 'Y':
				continue
			else:
				break


	def menu_clear_plugboard(self):
		
		self._plugboard.clear_plugboard()
		print("\nThe plugboard has been cleared")