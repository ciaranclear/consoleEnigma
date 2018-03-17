

class Four_rotor_interface(object):

	def __init__(self):

		super(Four_rotor_interface, self).__init__()


	def menu_select_fourth_rotor(self):

		position = 4
		rotors = self._rotor_group.get_fourth_rotors_list()
		self.menu_select_a_rotor(rotors, position)
		self.menu_print_active_rotor_types()


	def menu_select_non_fourth_rotor(self):

		rotors = self._rotor_group.get_non_fourth_rotors_list()
		for i in range(3):
			position = i+1
			self.menu_select_a_rotor(rotors, position)
			self.menu_print_active_rotor_types()


	def menu_select_one_rotor(self):

		self.menu_print_active_rotor_types()
		position = self.menu_get_position()
		if position >= 0 and position <= 3:
			rotors = self._rotor_group.get_non_fourth_rotors_list()
			self.menu_select_a_rotor(rotors, position)
		elif position == 4:
			self.menu_select_fourth_rotor()


	def menu_select_all_rotors(self):

		self.menu_print_active_rotor_types()
		self.menu_select_non_fourth_rotor()
		self.menu_select_fourth_rotor()