from enigma_machine import Enigma_machine
from stecker_cable_enigma_logic import Stecker_cable_enigma_logic
from stecker_cable_interface import Stecker_cable_interface
from uhr_box_enigma_logic import Uhr_box_enigma_logic
from uhr_box_interface import Uhr_box_interface
from uhr_box import Uhr_box
from three_rotor_group import Three_rotor_group
from four_rotor_group import Four_rotor_group
from three_rotor_interface import Three_rotor_interface
from four_rotor_interface import Four_rotor_interface
from enigma_interface import Enigma_interface
from display_uhr_enigma import Display_uhr_enigma
from display_stecker_enigma import Display_stecker_enigma
from settings import*

class WEHRMACHT(Enigma_machine,
				Enigma_interface,
				Three_rotor_interface,
				Display_stecker_enigma,
				Stecker_cable_enigma_logic,
				Stecker_cable_interface):

	def __init__(self):

		self._machine_type = "WEHRMACHT"
		self._rotor_group = Three_rotor_group(self._machine_type)
		super(WEHRMACHT, self).__init__()


class KRIEGSMARINE_M3(Enigma_machine,
					  Enigma_interface,
					  Three_rotor_interface,
					  Display_stecker_enigma,
					  Stecker_cable_enigma_logic,
					  Stecker_cable_interface):

	def __init__(self):

		self._machine_type = "KRIEGSMARINE_M3"
		self._rotor_group = Three_rotor_group(self._machine_type)
		super(KRIEGSMARINE_M3, self).__init__()


class KRIEGSMARINE_M4(Enigma_machine,
					  Enigma_interface,
					  Four_rotor_interface,
					  Display_stecker_enigma,
					  Stecker_cable_enigma_logic,
					  Stecker_cable_interface):

	def __init__(self):

		self._machine_type = "KRIEGSMARINE_M4"
		self._rotor_group = Four_rotor_group(self._machine_type)
		super(KRIEGSMARINE_M4, self).__init__()


class LUFTWAFFE(Enigma_machine,
				Enigma_interface,
				Four_rotor_interface,
				Display_uhr_enigma,
				Uhr_box_enigma_logic,
				Uhr_box_interface):

	def __init__(self):

		self._machine_type = "LUFTWAFFE"
		self._rotor_group = Four_rotor_group(self._machine_type)
		self._uhr_box = Uhr_box()
		super(LUFTWAFFE, self).__init__()


class SWISS_K(Enigma_machine,
			  Enigma_interface,
			  Three_rotor_interface,
			  Display_stecker_enigma,
			  Stecker_cable_enigma_logic,
			  Stecker_cable_interface):

	def __init__(self):

		self._machine_type = "SWISS_K"
		self._rotor_group = Three_rotor_group(self._machine_type)
		super(SWISS_K, self).__init__()


if __name__ == "__main__":

	def select_machine():

		while True:
			print("ENIGMA MENU\
				  \n\nEnter a number for one of the following\
				  \n1. WEHRMACHT\
				  \n2. KRIEGSMARINE M3\
				  \n3. KRIEGSMARINE M4\
				  \n4. LUFTWAFFE\
				  \n5. SWISS K\
				  \n6. Quit\n")

			inpt = input()

			if inpt == '1':
				enigma = WEHRMACHT()
			elif inpt == '2':
				enigma = KRIEGSMARINE_M3()
			elif inpt == '3':
				enigma = KRIEGSMARINE_M4()
			elif inpt == '4':
				enigma = LUFTWAFFE()
			elif inpt == '5':
				enigma = SWISS_K()
			elif inpt == '6':
				break
			else:
				print("Invalid input! try again")
				continue

			enigma.print_machine()
			enigma.menu()

	select_machine()