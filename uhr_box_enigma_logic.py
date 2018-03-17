
class Uhr_box_enigma_logic(object):

	def __init__(self):

		super(Uhr_box_enigma_logic, self).__init__()


	def uhr_plug_already_connected(self, character):

		if self._plugboard.get_connected_device(character) == "UHR_BOX_PLUG":
			return True
		else:
			return False


	def connect_uhr_plug(self, uhr_plug_id, character):

		character = self._validator.valid_character(character)
		self._uhr_box.valid_uhr_plug_id(uhr_plug_id)
		uhr_plug = self._uhr_box.get_uhr_plug(uhr_plug_id)
		self._uhr_box.connect_uhr_plug(uhr_plug_id, character)
		self._plugboard.connect_plug(character, uhr_plug)


	def disconnect_uhr_plug(self, character):

		character = self._validator.valid_character(character)
		current_plug = self._plugboard.get_connected_device_id(character)
		self._uhr_box.disconnect_uhr_plug(current_plug)
		self._plugboard.disconnect_plug(character)