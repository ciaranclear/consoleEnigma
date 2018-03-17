

class Uhr_box_interface(object):

	def __init__(self):

		super(Uhr_box_interface, self).__init__()


	def menu(self):
		""""menu allows the user to change the machines settings"""

		while True:
			#self.print_enigma()
			print("\n{} ENIGMA MACHINE\
				  \nenter a number for one of the following\
				  \n1. Select Rotors\
				  \n2. Select Ring Settings\
				  \n3. Select Rotor Settings\
				  \n4. Select Reflector\
				  \n5. Uhr Box Setup\
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
				self.menu_uhr_box_setup()
			elif inpt == '6':
				self.plain_text_input()
			elif inpt == '7':
				self.print_machine()
			elif inpt == '8':
				break
			else:
				print("Invalid input! try again")


	def menu_uhr_box_setup(self):
		
		while True:
			self.print_uhr_box()
			self.print_plugboard()
			print("\nEnter a number for one of the following\
				\n1. Connect Uhr Box Plug\
				\n2. Disconnect Uhr Box Plug\
				\n3. Change Uhr Box Setting\
				\n4. Clear Plugboard\
				\n5. Return To Enigma Menu")

			inpt = input()

			if inpt == '1':
				self.menu_connect_uhr_box_plug()
			elif inpt == '2':
				self.menu_disconnect_uhr_box_plug()
			elif inpt == '3':
				self.menu_change_uhr_box_setting()
			elif inpt == '4':
				self.menu_clear_plugboard()
			elif inpt == '5':
				break
			else:
				print("Invalid input! try again")


	def menu_select_uhr_box_plug(self, uhr_plug_list):

		while True:
			print("\nEnter a number to select an uhr plug")
			for i in range(len(uhr_plug_list)):
				print("{0} {1}".format(i+1, uhr_plug_list[i]))
			try:
				inpt = int(input())
			except Exception:
				pass
			else:
				if inpt >= 1 and inpt <= len(uhr_plug_list):
					return uhr_plug_list[inpt-1]
			print("Invalid input! try again")


	def menu_connect_uhr_box_plug(self):
		
		while True:
			self.print_plugboard()
			available_uhr_plugs = self._uhr_box.available_uhr_plugs_list()
			selected_plug = self.menu_select_uhr_box_plug(available_uhr_plugs)
			message = "\nEnter a plugboard letter to connect uhr plug to"
			character = self.menu_get_letter(message)
			if self.uhr_plug_already_connected(character):
				if self.menu_get_plug_override(character):
					self.disconnect_uhr_plug(character)
					self.connect_uhr_plug(selected_plug, character)
			else:
				self.connect_uhr_plug(selected_plug, character)
			if self._uhr_box.valid_uhr_box():
				print("All uhr plugs have been connected")
				break
			else:
				print("Enter y to connect another uhr plug")
				inpt = input()
				if inpt.upper() == 'Y':
					continue
				else:
					break


	def menu_disconnect_uhr_box_plug(self):
		
		while not self._uhr_box.uhr_box_disconnected():
			self.print_plugboard()
			message = "\nEnter a plugboard letter to disconnect an uhr plug"
			character = self.menu_get_letter(message)
			if self.uhr_plug_already_connected(character):
				current_plug = self._plugboard.get_connected_device_id(character)
				self.disconnect_uhr_plug(character)
				print("Uhr plug {0} has been disconnected from plugboard socket {1}"
					.format(current_plug, character))
			else:
				print("{} does not have an uhr plug connected".format(character))
			if self._uhr_box.uhr_box_disconnected():
				print("All uhr plugs have been disconnected")
				break
			else:
				print("Enter y to disconnect another uhr plug")
				inpt = input()
				if inpt.upper() == 'Y':
					continue
				else:
					break
		if self._uhr_box.uhr_box_disconnected():
			print("There are no uhr plugs connected")


	def menu_change_uhr_box_setting(self):
		
		while True:
			self.print_uhr_box()
			print("\nEnter a new setting for the uhr box. Must be a number between 0 and {}"
				.format(self._uhr_box.setting_range))
			try:
				setting = int(input())
			except Exception:
				pass
			else:
				if self._uhr_box.valid_uhr_box_setting(setting):
					self._uhr_box.set_uhr_box_setting(setting)
					break
			print("Invalid input! try again")


	def menu_clear_plugboard(self):
		
		uhr_dict = self._uhr_box.get_uhr_box_dict()
		plugs = uhr_dict["CONNECTIONS"]["PLUGS"]
		for plug in plugs:
			connected_character = plugs[plug]["CHAR"]
			if connected_character:
				self.disconnect_uhr_plug(connected_character)
		self.print_plugboard()
		print("The plugboard has been cleared")