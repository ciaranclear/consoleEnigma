from rotor_group import Rotor_group
from rotor import*

class Three_rotor_group(Rotor_group):

	def __init__(self, machine_type):

		self._machine_type = machine_type
		self._rotor_group_size = 3
		self._rotors_list = EQUIPMENT_DICT["ROTORS"][self._machine_type]
		self._rotors_dict = {}
		self._active_rotors_dict = {}
		self._set_rotors_dict()
		super(Three_rotor_group, self).__init__()

	# PUBLIC METHODS ------------------------------------------------------------------

	def rotor_group_size(self):

		return self._rotor_group_size


	def select_rotor(self, rotor, position):

		if self.valid_rotor_type(rotor) and self.valid_position(position):
			self.deselect_rotor_type(rotor)
			self._active_rotors_dict[position] = self._rotors_dict[rotor]
			return True
		elif not self.valid_rotor_type(rotor):
			raise RotorTypeError(rotor)
		elif not self.valid_position(position):
			raise ValueError("{} is not a valid rotor position".format(position))


	def select_rotors(self, r1, r2, r3):

		unique_rotors = set(r1, r2, r3)
		rotors = [r1, r2, r3]
		if len(unique_rotors) != self._rotor_group_size:
			raise ValueError("A rotor can not be used in more than one position")
		for i in range(self._rotor_group_size):
			rotor = rotors[i]
			position = i+1
			self.select_rotor(rotor, position)


	def set_default_rotors(self):

		for i in range(self._rotor_group_size):
			rotor = self._rotors_list[i]
			position = i+1
			self.select_rotor(rotor, position)
