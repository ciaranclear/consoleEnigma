from validator import Validator
from settings import *
from plug import Plug

class Uhr_box(object):

	def __init__(self):

		self.validator = Validator()
		self._connections_A_map = UHR_BOX["CONNECTIONS_LIST"]
		self._connections_B_map = [i for i in range(len(self._connections_A_map))]
		self._default_position_char = self._connections_A_map[0]
		self.setting_range = len(self._connections_A_map)-1
		self._uhr_box_setting = 0
		self._plug_list = UHR_BOX["PLUGS_LIST"]
		self._plug_A_map = self._extend_plug_map(UHR_BOX["PLUG_A_MAP"])
		self._plug_B_map = self._extend_plug_map(UHR_BOX["PLUG_B_MAP"])
		self._uhr_plugs_dict = {}
		self._set_uhr_plugs_dict()
		super(Uhr_box, self).__init__()

	# PUBLIC METHODS -------------------------------------------------------------

	def valid_uhr_plug_id(self, plug_id):
		"""valid_uhr_plug_id takes an plug_id as an argument \
		If the plug_id is valid it is returned, If plug_id \
		is invalid a ValueError is raised"""
		
		if plug_id in self._plug_list:
			return plug_id
		else:
			raise ValueError("{} is not a valid uhr plug id".format(plug_id))


	def valid_uhr_box_setting(self, setting):
		"""valid_uhr_box_setting takes a setting as an argument. \
		If setting is an integer of a value within the range of \
		0 to the setting range True is returned else returns False"""
		
		if isinstance(setting, int) and setting <= self.setting_range and setting >= 0:
			return True
		else:
			return False


	def inc_uhr_box_setting(self):
		"""inc_uhr_box_setting increases the uhr box setting by one. \
		If the new setting exceeds the setting range then the new """
		
		if self._uhr_box_setting + 1 > self.setting_range:
			setting = 0
		else:
			setting = self._uhr_box_setting + 1
		self.set_uhr_box_setting(setting)


	def dec_uhr_box_setting(self):
		
		if self._uhr_box_setting - 1 < 0:
			setting = self.setting_range
		else:
			setting = self._uhr_box_setting - 1
		self.set_uhr_box_setting(setting)	


	def get_uhr_box_setting(self):
		
		return self._uhr_box_setting


	def set_uhr_box_setting(self, setting):

		if self.valid_uhr_box_setting(setting):
			self._uhr_box_setting = setting
			self._reset_rotor()
			self._change_rotor_setting(setting)


	def connect_uhr_plug(self, plug, character):

		plug = self.valid_uhr_plug_id(plug)
		character = self.validator.valid_character(character)
		self._uhr_plugs_dict[plug].connect_plug(character)


	def disconnect_uhr_plug(self, plug):

		plug = self.valid_uhr_plug_id(plug)
		self._uhr_plugs_dict[plug].disconnect_plug()


	def disconnect_uhr_plugs(self):

		for plug in self._plugs_list:
			self.disconnect_uhr_plug(plug)


	def get_uhr_plug(self, plug):

		plug = self.valid_uhr_plug_id(plug)
		return self._uhr_plugs_dict[plug]


	def connected_uhr_plugs_list(self):

		connected_plugs_list = []
		for plug in self._plug_list:
			if self._uhr_plugs_dict[plug].plug_is_connected():
				connected_plugs_list.append(plug)

		return connected_plugs_list


	def available_uhr_plugs_list(self):

		available_plugs_list = []
		for plug in self._plug_list:
			if not self._uhr_plugs_dict[plug].plug_is_connected():
				available_plugs_list.append(plug)

		return available_plugs_list


	def valid_uhr_box(self):

		return self.uhr_box_connected()

	valid_device = valid_uhr_box


	def uhr_box_connected(self):

		for plug in self._plug_list:
			if not self._uhr_plugs_dict[plug].plug_is_connected():
				return False

		return True


	def uhr_box_disconnected(self):

		for plug in self._plug_list:
			if self._uhr_plugs_dict[plug].plug_is_connected():
				return False

		return True


	def connected_to(self, plug, pin_type):

		plug = self.valid_uhr_plug_id(plug)
		pin = plug + pin_type
		return self.corresponding_char(pin)


	def corresponding_pin(self, pin):

		plug_type = self._get_plug_type(pin)

		corresponding_pin = ""
		if plug_type == 'A':
			terminal = self._plug_A_map[pin]
			corresponding_terminal = self._A_side_corresponding_terminal(terminal)
			corresponding_pin = self._plug_B_map[corresponding_terminal]
		elif plug_type == 'B':
			terminal = self._plug_B_map[pin]
			corresponding_terminal = self._B_side_corresponding_terminal(terminal)
			corresponding_pin = self._plug_A_map[corresponding_terminal]

		return corresponding_pin


	def corresponding_char(self, pin):

		connected_pin = self.corresponding_pin(pin)
		plug = self._get_plug_id(connected_pin)
		character = self._uhr_plugs_dict[plug].plug_connected_to()

		return character


	def get_uhr_box_dict(self):

		uhr_dict = {
					"CONNECTIONS":{
						"PLUGS": {},
						"CHARACTERS": {}
						}
					}

		for plug in self._plug_list:
			plug_dict = self._get_plug_dict(plug)
			character = self._uhr_plugs_dict[plug].plug_connected_to()
			plug_dict["CHAR"] = character
			uhr_dict["CONNECTIONS"]["PLUGS"][plug] = plug_dict

		return uhr_dict

	# PRIVATE METHODS ------------------------------------------------------------

	def _get_plug_dict(self, plug):

		plug_dict = {}
		pin_type = plug + "LG"
		pin_dict = self._get_pin_dict(pin_type)
		plug_dict[pin_type] = pin_dict
		pin_type = plug + "SM"
		pin_dict = self._get_pin_dict(pin_type)
		plug_dict[pin_type] = pin_dict
		character = self._uhr_plugs_dict[plug].plug_connected_to()
		plug_dict["CHAR"] = character

		return plug_dict


	def _get_pin_dict(self, pin_type):

		pin_dict = {}
		corresponding_pin = self.corresponding_pin(pin_type)
		character = self.corresponding_char(pin_type)
		pin_dict["CONNECTED_PIN_ID"] = corresponding_pin
		pin_dict["CONNECTED_CHAR"] = character

		return pin_dict


	def _set_uhr_plugs_dict(self):

		for plug in self._plug_list:
			self._uhr_plugs_dict[plug] = Plug("UHR_BOX_PLUG", plug, self)


	def _get_plug_id(self, pin):

		return pin[0:3]


	def _get_plug_type(self, pin):

		return pin[2]


	def _reset_rotor(self):

		setting = self._connections_A_map.index(self._default_position_char)
		self._change_rotor_setting(setting)


	def _change_rotor_setting(self, setting):

		new_connections_A_map = self._connections_A_map[setting:]
		new_connections_A_map += self._connections_A_map[0:setting]
		new_connections_B_map = self._connections_B_map[setting:]
		new_connections_B_map += self._connections_B_map[0:setting]
		self._connections_A_map = new_connections_A_map
		self._connections_B_map = new_connections_B_map


	def _A_side_corresponding_terminal(self, terminal):

		number = self._connections_A_map[terminal]
		return self._connections_B_map.index(number)


	def _B_side_corresponding_terminal(self, terminal):

		number = self._connections_B_map[terminal]
		return self._connections_A_map.index(number)


	@staticmethod
	def _extend_plug_map(plug_map):

		new_map = plug_map.copy()
		for number in plug_map:
			plug = plug_map[number]
			new_map[plug] = number

		return new_map


if __name__ == "__main__":

	uhr_box = Uhr_box()
	print("uhr box connected ", uhr_box.uhr_box_connected())
	print("uhr box disconnected ", uhr_box.uhr_box_disconnected())
	print("available plugs ", uhr_box.available_uhr_plugs_list())
	print("connected plugs ", uhr_box.connected_uhr_plugs_list())
	print("uhr box setting ", uhr_box.get_uhr_box_setting())
	print("A map ", uhr_box._connections_A_map)
	print("B map ", uhr_box._connections_B_map)
	print("01ALG connected to pin ", uhr_box.corresponding_pin("01ALG"))
	print("01ASM connected to pin ", uhr_box.corresponding_pin("01ASM"))
	print("uhr box setting ", uhr_box.get_uhr_box_setting())
	uhr_box.inc_uhr_box_setting()
	print("A map ", uhr_box._connections_A_map)
	print("B map ", uhr_box._connections_B_map)
	print("01ALG connected to pin ", uhr_box.corresponding_pin("01ALG"))
	print("01ASM connected to pin ", uhr_box.corresponding_pin("01ASM"))

	plugs = UHR_BOX["PLUGS_LIST"]

	for i in range(len(plugs)):
		plug = plugs[i]
		letter = LETTERS[i]
		uhr_box.connect_uhr_plug(plug, letter)

	uhr_dict = uhr_box.get_uhr_box_dict()
	plugs = uhr_dict["CONNECTIONS"]["PLUGS"]
	for plug in plugs:
		print(plug, plugs[plug][plug + "LG"],
			plugs[plug][plug +"SM"], plugs[plug]["CHAR"])

	uhr_box.inc_uhr_box_setting()
	print("--------------------------------------------------------------------")

	uhr_dict = uhr_box.get_uhr_box_dict()
	plugs = uhr_dict["CONNECTIONS"]["PLUGS"]
	for plug in plugs:
		print(plug, plugs[plug][plug + "LG"],
			plugs[plug][plug +"SM"], plugs[plug]["CHAR"])