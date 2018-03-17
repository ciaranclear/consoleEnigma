from plug import Plug
from validator import Validator

class Stecker_cable(object):

	def __init__(self):
		self._validator = Validator()
		self._plugs = {"P1": Plug("STECKER_PLUG", "P1", self),
					   "P2": Plug("STECKER_PLUG", "P2", self)}
		super(Stecker_cable, self).__init__()

	# PUBLIC METHODS -----------------------------------------------------------------

	def get_plugs(self):
		"""get_plugs returns a dictionary with both plug objects"""

		return self._plugs


	def connected_to(self, plug_id, pin_type = None):
		"""connected_to takes a plug_id and a pin_type as an argument \
		and returns the letter the other plug is connected to"""

		if self._validator.valid_stecker_plug_id(plug_id) and \
			self._validator.valid_pin_type(pin_type):
			if plug_id == "P1":
				connected_character = self._plugs["P2"].plug_connected_to()
			elif plug_id == "P2":
				connected_character = self._plugs["P1"].plug_connected_to()
			return connected_character


	def valid_device(self):
		"""valid_device returns True if both plugs are connected \
		or returns False if either plug is not connected"""

		for plug in self._plugs:
			if not self._plugs[plug].plug_is_connected():
				return False
		return True


if __name__ == "__main__":

	letter1 = "A"
	letter2 = "B"

	stecker_cable = Stecker_cable()
	plugs = stecker_cable.get_plugs()
	plug1 = plugs["P1"]
	plug2 = plugs["P2"]
	plug1.connect_plug(letter1)
	plug2.connect_plug(letter2)
	print(plug1.pin_connected_to("SM"))
	print(plug1.pin_connected_to("LG"))
	print(plug2.pin_connected_to("SM"))
	print(plug2.pin_connected_to("LG"))
	print(stecker_cable.valid_device())
	print(plug1.valid_device())
	print(plug1.get_device_type())
	print(plug1.get_plug_id())
	plug1.disconnect_plug()
	print(stecker_cable.valid_device())
	print(plug1.pin_connected_to("SM"))
	print(plug1.pin_connected_to("LG"))
	print(plug2.pin_connected_to("SM"))
	print(plug2.pin_connected_to("LG"))