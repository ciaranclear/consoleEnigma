from settings import *
from validator import Validator
from plugboard import Plugboard
from keyboard import Keyboard
from entry_wheel import Entry_wheel
from rotor import Rotor
from reflector import Reflector
from machine_diagnostics import MachineDiagnostics


class Enigma_machine(object):

	def __init__(self):

		self._validator = Validator()
		self._plugboard = Plugboard()
		self._keyboard = Keyboard()
		self._diagnostics = MachineDiagnostics(self)
		self._ETW_list = EQUIPMENT_DICT["ENTRY_WHEELS"][self._machine_type]
		self._reflectors_list = EQUIPMENT_DICT["REFLECTORS"][self._machine_type]
		self._entry_wheel = Entry_wheel(self._ETW_list)
		self._reflectors_dict = {}
		self._active_reflector = None
		self._set_reflectors_dict()
		self.set_default_settings()
		super(Enigma_machine, self).__init__()

	# PUBLIC METHODS ------------------------------------------------------------------

	def get_entry_wheel_list(self):

		return self._ETW_list.copy()


	def get_inactive_reflectors_list(self):
		"""get_inactive_reflectors_list returns a list of all the inactive \
		reflector types"""

		inactive_reflectors = []
		if self._active_reflector:
			active_reflector_type = self._active_reflector.reflector_type()
			for reflector in self._reflector_dict:
				reflector_type = self._reflectors_dict[reflector].reflector_type()
				if reflector_type != active_reflector_type:
					inactive_reflectors.append(reflector_type)
		return inactive_reflectors


	def active_reflector_type(self):
		"""active_reflector_type returns the active reflector type"""

		if self._active_reflector:
			return self._active_reflector.reflector_type()
		else:
			return None


	def get_active_reflector_dict(self):
		"""get_active_reflector_dict returns the active reflectors \
		dictionary or returns None if there is no active reflector"""

		if self._active_reflector:
			return self._active_reflector.get_reflector_dict()
		else:
			return None


	def set_reflector(self, reflector):
		"""set_reflector takes a reflector type as an argument. If the \
		reflector type is valid that reflector is set as the active \
		reflector. If reflector type is not valid a ValueError is raised"""

		if reflector in self._reflectors_dict:
			self._active_reflector = self._reflectors_dict[reflector]
		else:
			raise ValueError("{} is not a valid reflector type".format(reflector))


	def get_reflectors_list(self):
		"""get_reflectors_list returns a list of all the reflector types"""

		return self._reflectors_list


	def get_output(self, input_string):
		"""get_output takes an input_string as an argument. If the input \
		string is not of type string then a TypeError is raised. Each \
		character in the input string is validated by the keyboard object \
		"""

		output_string = ""
		if not isinstance(input_string, str):
			raise TypeError("Input string is not of type string")
		for character in input_string:
			character = self._keyboard.keyboard_input(character)
			if character:
				self._rotor_group._rotor_turnover()
				character = self._plugboard.connected_to(character, "LG")
				character = self._rotary_group_output(character)
				character = self._plugboard.connected_to(character, "SM")
				output_string += character
		return output_string


	def valid_enigma(self):
		"""valid_enigma returns True if the plugboard, rotor group and \
		reflector are valid els returns False"""

		if self._plugboard.valid_plugboard() and \
			self._rotor_group.valid_rotors_group() and \
			self._active_reflector:
			return True
		else:
			return False


	def set_default_settings(self):
		"""set_default_settings clears the plugboard, sets default rotors \
		and sets the default reflector"""

		self.clear_plugboard()
		self._rotor_group.set_default_rotors()
		self.set_default_reflector()


	def set_default_reflector(self):
		"""set_default_reflector sets the default reflector"""

		default_reflector = EQUIPMENT_DICT["REFLECTORS"][self._machine_type][0]
		self._active_reflector = self._reflectors_dict[default_reflector]


	def clear_plugboard(self):
		"""clear_plugboard calls the clear_plugboard method in the plugboard \
		object"""

		self._plugboard.clear_plugboard()

	# PRIVATE METHODS -----------------------------------------------------------------

	def _rotary_group_output(self, character):
		"""_rotary_group_output takes a character as an argument. The \
		character is converted into an index in the entry wheel. For \
		each rotor its output index is used as the input for the next \
		rotor going to the reflector. The last rotors output is used as \
		the input towards the reflector. The output from the reflector is \
		input into the last rotor position and each rotors output index \
		is used as the input for the next rotor going towards the entry \
		wheel. The first rotors output is used as input for the entry \
		wheel and this outputs a character which is returned"""

		index = self._entry_wheel.output_to_rotor(character)

		index = self._rotor_group.output_to_reflector(index)

		index = self._active_reflector.reflector_output(index)

		index = self._rotor_group.output_from_reflector(index)

		character = self._entry_wheel.output_from_rotor(index)
		return character


	def _set_reflectors_dict(self):
		"""_set_reflectors_dict initializes each reflector with its reflector \
		type and its character list and stores them in the reflectors dict"""

		for reflector in self._reflectors_list:
			reflector_characters = REFLECTOR_DICT[reflector]
			self._reflectors_dict[reflector] = Reflector(reflector, reflector_characters)

