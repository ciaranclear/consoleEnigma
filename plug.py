from validator import Validator

class Plug(object):

	def __init__(self, device_type, plug_id, device, character = None):
		self.validator = Validator()
		self._device_type = device_type
		self._plug_id = plug_id
		self._character = character
		self._device = device
		self._connected = False
		if character:
			self._character = self.validator.valid_character(character)
			self._connected = True
		super(Plug, self).__init__()

	# PUBLIC METHODS -----------------------------------------------------------------

	def pin_connected_to(self, pin_type):
		"""pin_connected_to takes a pin_type and returns the \
		corresponding letter it is connected to through the device"""

		return self._device.connected_to(self._plug_id, pin_type)


	def plug_connected_to(self):
		"""plug_connected_to returns the letter this plug is connected to"""

		return self._character


	def connect_plug(self, character):
		"""connect_plug takes a letter as an argument. sets this \
		plugs letter as letter and sets connected to True"""

		character = self.validator.valid_character(character)
		self._character = character
		self._connected = True


	def plug_is_connected(self):
		"""plug_is_connected returns True if plug is connected \
		or returns False if plug is not connected"""

		return self._connected


	def disconnect_plug(self):
		"""disconnect_plug sets this plugs letter \
		to None and sets connected to False"""

		self._character = None
		self._connected = False


	def valid_device(self):
		"""valid_device calls the valid device method in the \
		device object"""

		return self._device.valid_device()


	def set_device(self, device):
		"""set_device takes an object as an argument \
		and sets it as this plugs connected device"""

		self._device = device


	def get_device_type(self):
		"""get_device_type returns device type"""

		return self._device_type

	get_plug_type = get_device_type


	def get_device_id(self):
		"""get_plug_id returns this plugs id"""

		return self._plug_id

	get_plug_id = get_device_id


class Test_device(object):

	def __init__(self):
		super(Test_device, self).__init__()

	def connected_to(self, plug_id, pin_type):
		return "connected to " + plug_id + " " + pin_type

	def valid_device(self):
		return "valid device"


if __name__ == "__main__":

	plug_id = "01"
	pin_type = "LG"
	device_type = "test device"
	device = Test_device()
	plug = Plug(device_type, "test plug", device, "A")
	print(plug.get_device_id())
	print(plug.get_device_type())
	print(plug.valid_device())
	print(plug.plug_is_connected())
	print(plug.plug_connected_to())
	print(plug.pin_connected_to("SM"))