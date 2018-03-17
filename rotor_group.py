from rotor import*
from validator import Validator

class Rotor_group:

	def __init__(self):

		self._validator = Validator()
		super(Rotor_group, self).__init__()

	# PUBLIC METHODS ------------------------------------------------------------------

	def deselect_rotor_type(self, rotor):
		"""deselect_rotor_type takes a rotor type as an argument and if the \
		rotor type is valid and that rotor is an active rotor it will be \
		deselected and returns True. If the rotor type is not active returns \
		False. If the rotor type is not valid a ValueError is raised"""

		if self.valid_rotor_type(rotor):
			for position in self._active_rotors_dict:
				if self._active_rotors_dict[position]:
					if self._active_rotors_dict[position].rotor_type() == rotor:
						self.deselect_rotor_position(position)
						return True
			return False
		else:
			raise RotorTypeError(rotor)


	def deselect_rotor_position(self, position):
		"""deselect_rotor_position takes a position as an argument. If the \
		position is a valid rotor position then the rotor at that position \
		is deselected and returns True. If position is not valid ValueError \
		is raised"""

		if self.valid_position(position):
			self._active_rotors_dict[position] = None
			return True
		else:
			raise ValueError("{} is not a valid rotor position".format(position))


	def rotor_type(self, position):
		"""rotor_type takes a position as an argument. If position is valid \
		and there is an active rotor at that position then that rotors type \
		is returned. If there is no active rotor at that position returns \
		None. If the position is invalid ValueError is raised"""

		if self.valid_position(position):
			if self._active_rotors_dict[position]:
				return self._active_rotors_dict[position].rotor_type()
			else:
				return None
		else:
			raise ValueError("{} is not a valid rotor position".format(position))


	def inactive_rotors_list(self):
		"""inactive_rotors_list returns a list of all rotor types that \
		are inactive"""

		active_rotors = self.active_rotors_list()

		inactive_rotors = []
		for rotor in self._rotors_dict:
			rotor_type = self._rotors_dict[rotor].rotor_type()
			if rotor_type not in active_rotors:
				inactive_rotors.append(rotor_type)

		return inactive_rotors


	def active_rotors_list(self):
		"""active_rotors_list returns a list of all rotor types that \
		are active"""

		active_rotors = []
		for position in self._active_rotors_dict:
			rotor_type = self.rotor_type(position)
			if rotor_type:
				active_rotors.append(rotor_type)

		return active_rotors


	def active_rotors_dictionary(self):
		"""active_rotors_dictionary returns a dictionary with key value \
		pairs of the rotor position and the rotor type at that position"""

		active_rotors = {}
		for position in self._active_rotors_dict:
			active_rotors[position] = self.rotor_type(position)

		return active_rotors


	def get_rotors_list(self):
		"""get_rotors_list returns a list of all the rotor types"""

		return self._rotors_list


	def get_rotor_settings_list(self):
		"""get_rotor_settings_list returns a list with all the rotor \
		settings. If a rotor position has no active rotor then the \
		setting value is None"""

		rotor_settings = []
		for i in range(self._rotor_group_size):
			position = i+1
			if self._active_rotors_dict[position]:
				setting = self._active_rotors_dict[position].get_rotor_setting()
				rotor_settings.append(setting)
			else:
				rotor_settings.append(None)

		return rotor_settings


	def change_rotor_setting(self, position, setting):
		"""change_rotor_setting takes a position and a setting as an argument. \
		If position is valid and the setting is a valid ring character and \
		there is an active rotor at that rotor position then that rotors \
		setting is set to the argument setting and returns True. If there \
		is no active rotor at that rotor position returns False. If the \
		position is not valid a ValueError is raised"""

		if self.valid_position(position):
			setting = self._validator.valid_character(setting)
			if self._active_rotors_dict[position] and \
				self._active_rotors_dict[position].valid_ring_character(setting):
				self._active_rotors_dict[position].set_rotor_setting(setting)
				return True
			else:
				return False
		else:
			raise ValueError("{} is not a valid rotor position".format(position))


	def get_ring_settings_list(self):

		ring_settings = []
		for i in range(self._rotor_group_size):
			position = i+1
			if self._active_rotors_dict[position]:
				ring_setting = self._active_rotors_dict[position].get_ring_setting()
				ring_settings.append(ring_setting)
			else:
				ring_settings.append(None)

		return ring_settings


	def change_ring_setting(self, position, setting):
		"""change_ring_setting takes a position and a setting as an argument. \
		If position is valid and the setting is a valid ring character and \
		there is an active rotor at that rotor position then that rotors \
		ring setting is set to the argument setting and returns True. If there \
		is no active rotor at that rotor position returns False. If the \
		position is not valid a ValueError is raised"""

		if self.valid_position(position):
			setting = self._validator.valid_character(setting)
			if self._active_rotors_dict[position] and \
				self._active_rotors_dict[position].valid_ring_character(setting):
				self._active_rotors_dict[position].set_ring_setting(setting)
				return True
			else:
				return False
		else:
			raise ValueError("{} is not a valid rotor position".format(position))


	def valid_rotors_group(self):
		"""valid_rotors_group returns True if every rotor position has an \
		active rotor els returns False"""

		for position in self._active_rotors_dict:
			if not self._active_rotors_dict[position]:
				return False
		return True


	def valid_position(self, position):
		"""valid_position takes a position as an argument. If position \
		is an integer and has a value between one and the number of rotor \
		positions in the machine returns True else returns False"""

		if isinstance(position, int) and position > 0 and \
			position <= self._rotor_group_size:
			return True
		else:
			return False


	def valid_rotor_type(self, rotor_type):
		"""valid_rotor_type takes a rotor_type as an argument. If the rotor \
		type is in the rotors dict returns True else returns False"""

		for rotor in self._rotors_dict:
			if rotor == rotor_type:
				return True
		return False


	def valid_ring_setting(self, position, setting):

		if self.valid_position(position):
			return self._active_rotors_dict[position].valid_ring_character(setting)
		else:
			raise ValueError("Invalid rotor position")


	def rotor_ring_character_type(self, position):

		if self.valid_position(position):
			return self._active_rotors_dict[position].ring_character_type()
		else:
			raise ValueError("Invalid rotor position")


	def get_rotor_dict(self, position):
		"""get_rotor_dict takes a rotor position as an argument. Returns \
		the rotor dictionary for that rotor position or None if no rotor \
		has been selected at that position. If position is not valid a \
		ValueError is raised"""

		if self.valid_position(position):
			if self._active_rotors_dict[position]:
				return self._active_rotors_dict[position].get_rotor_dict()
			else:
				return None
		else:
			raise ValueError("{} is not a valid rotor position".format(position))


	def output_to_reflector(self, index):

		for i in range(0, self._rotor_group_size):
			index = self._active_rotors_dict[i+1].output_to_reflector(index)
		return index


	def output_from_reflector(self, index):

		for i in range(self._rotor_group_size, 0, -1):
			index = self._active_rotors_dict[i].output_from_reflector(index)
		return index

	# PRIVATE METHODS -----------------------------------------------------------------

	def _rotor_turnover(self):

		if self._active_rotors_dict[2].turnover():
			self._active_rotors_dict[2].keyed_rotor()
			self._active_rotors_dict[3].keyed_rotor()
		if self._active_rotors_dict[1].keyed_rotor():
			self._active_rotors_dict[2].keyed_rotor()


	def _set_rotors_dict(self):

		for rotor in self._rotors_list:
			rotor_characters = ROTOR_DICT[rotor][0]
			ring_characters = EQUIPMENT_DICT["RING_CHARACTERS"][self._machine_type]
			turnover_characters = ROTOR_DICT[rotor][1]
			self._rotors_dict[rotor] = Rotor(rotor_characters, ring_characters,
												turnover_characters, rotor)