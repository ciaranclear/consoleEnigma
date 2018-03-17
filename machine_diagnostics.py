

class MachineDiagnostics(object):

	def __init__(self, enigma_machine):

		self.machine = enigma_machine
		super(MachineDiagnostics, self).__init__()


	def get_diagnostic_string(self):

		diagnostic_string = "INVALID\n"
		diagnostic_string += self._rotors_string()
		diagnostic_string += self._reflector_string()
		diagnostic_string += self._uhr_box_string()

		return diagnostic_string


	def _rotors_string(self):

		rotors_dict = self.machine._rotor_group.active_rotors_dictionary()
		rotor_string = ""
		for position in rotors_dict:
			if rotors_dict[position] == None:
				rotor_string += "{}R{} has no rotor selected\n".format(' ' * 15, position)
		return rotor_string


	def _reflector_string(self):

		reflector_string = ""
		if self.machine.active_reflector_type() == None:
			reflector_string = "{}No reflector selected\n".format(' ' * 15)
		return reflector_string


	def _uhr_box_string(self):

		try:
			unconnected_plugs = self.machine._uhr_box.available_uhr_plugs_list()
		except AttributeError:
			return ""
		else:
			uhr_box_string = ""
			if len(unconnected_plugs) > 0 and len(unconnected_plugs) < 20:
				for unconnected_plug in unconnected_plugs:
					uhr_box_string += "{}UHR PLUG {} is not connected\n".format(' ' * 15, unconnected_plug)

			return uhr_box_string