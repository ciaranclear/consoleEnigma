from rotor_group import Rotor_group
from rotor import*

class Four_rotor_group(Rotor_group):

	def __init__(self, machine_type):

		self._machine_type = machine_type
		self._rotor_group_size = 4
		self._rotors_list = EQUIPMENT_DICT["ROTORS"][self._machine_type]
		self._rotors_dict = {}
		self._active_rotors_dict = {}
		self._set_rotors_dict()
		super(Four_rotor_group, self).__init__()

	# PUBLIC METHODS ------------------------------------------------------------------

	def rotor_group_size(self):

		return self._rotor_group_size


	def select_rotor(self, rotor, position):

		if self.valid_rotor_type(rotor) and self.valid_position(position):
			if position < self._rotor_group_size and not self.valid_fourth_rotor(rotor):
				self.deselect_rotor_type(rotor)
				self._active_rotors_dict[position] = self._rotors_dict[rotor]
				return True
			elif position == self._rotor_group_size and self.valid_fourth_rotor(rotor):
				self._active_rotors_dict[position] = self._rotors_dict[rotor]
				return True
			else:
				raise Exception("{0} is not a valid rotor position for {1}".format(position, rotor))
		elif not self.valid_rotor_type(rotor):
			raise RotorTypeError(rotor)
		elif not self.valid_position(position):
			raise ValueError("{} is not a valid rotor position".format(position))


	def select_rotors(self, r1, r2, r3, r4):

		unique_rotors = set(r1, r2, r3, r4)
		rotors = [r1, r2, r3, r4]
		if len(unique_rotors) != self._rotor_group_size:
			raise ValueError("A rotor can not be used in more than one position")
		for i in range(self._rotor_group_size):
			rotor = rotors[i]
			position = i+1
			self.select_rotor(rotor, position)


	def set_default_rotors(self):

		position = 1
		rotors_set = 0
		fourth_rotor_not_set = True
		for rotor in self._rotors_list:
			if position < self._rotor_group_size and not self.valid_fourth_rotor(rotor):
				self.select_rotor(rotor, position)
				position += 1
				rotors_set += 1
			elif fourth_rotor_not_set and self.valid_fourth_rotor(rotor):
				self.select_rotor(rotor, self._rotor_group_size)
				rotors_set += 1
				fourth_rotor_not_set = False
			if rotors_set == self._rotor_group_size:
				return


	def get_fourth_rotors_list(self):

		fourth_rotors_list = []
		for rotor in self._rotors_dict:
			if not self._rotors_dict[rotor].can_turnover:
				fourth_rotors_list.append(rotor)
		return fourth_rotors_list


	def get_non_fourth_rotors_list(self):

		non_fourth_rotors_list = []
		for rotor in self._rotors_dict:
			if self._rotors_dict[rotor].can_turnover:
				non_fourth_rotors_list.append(rotor)
		return non_fourth_rotors_list


	def valid_fourth_rotor(self, rotor):

		if self.valid_rotor_type(rotor):
			return not self._rotors_dict[rotor].can_turnover
		else:
			raise RotorTypeError(rotor)