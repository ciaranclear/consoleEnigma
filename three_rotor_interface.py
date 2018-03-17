

class Three_rotor_interface(object):

	def __init__(self):

		super(Three_rotor_interface, self).__init__()


	def menu_select_one_rotor(self):

		self.menu_print_active_rotor_types()
		position = self.menu_get_position()
		rotors = self._rotor_group.get_rotors_list()
		self.menu_select_a_rotor(rotors, position)
		self.menu_print_active_rotor_types()


	def menu_select_all_rotors(self):

		rotors = self._rotor_group.get_rotors_list()
		for position in self._rotor_group._active_rotors_dict:
			self.menu_print_active_rotor_types()
			self.menu_select_a_rotor(rotors, position)
		self.menu_print_active_rotor_types()