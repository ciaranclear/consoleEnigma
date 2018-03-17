from validator import Validator
from settings import *


class RotorTypeError(Exception):
    def __init__(self, rotor_type):
        super().__init__("{} is not a valid rotor type".format(rotor_type))


class RotorListRangeError(Exception):
    def __init__(self, rotor_type, list_type):
        super().__init__("{0} {1} is incorrect length, must be 26 characters in length"
                         .format(rotor_type, list_type))


class RotorListCharError(Exception):
    def __init__(self, rotor_type, list_type):
        super().__init__("{0} {1} must contain all letters or all numbers not both"
                         .format(rotor_type, list_type))


class RotorListTypeError(Exception):
    def __init__(self, rotor_type, list_type):
        super().__init__("{0} {1} elements must be of type char only"
                         .format(rotor_type, list_type))


class RotorListRepeatError(Exception):
    def __init__(self, rotor_type, list_type):
        super().__init__("{0} {1} all characters must be unique, Same char cannot be repeated"
                         .format(rotor_type, list_type))


class RotorTurnoverListError(Exception):
    def __init__(self, rotor_type):
        super().__init__("{} turnover list characters must also be in ring characters list"
                         .format(rotor_type))


class RotorRingCharError(Exception):
    def __init__(self, character, correct_char_type):
        self.required_type = None
        if correct_char_type.isalpha():
            self.required_type = "numeric"
        else:
            self.required_type = "letter"
        super().__init__("{0} is not a valid ring character. Required character must be a {1}"
                         .format(character, self.required_type))


class Rotor:
    def __init__(self, rotor_characters,
                 ring_characters,
                 turnover_characters,
                 rotor_type=None):
        """Rotor is initialized with four arguments. rotor_characters is a list of \
        the characters that define the cross wiring within the rotor. ring_characters \
        is a list of characters that are displayed around the ring of the rotor. \
        kickover_characters is a list of characters that repressent the rotor settings \
        at which the left neighbouring rotor will turnover. During initialization all \
        rotor lists are validated and if a non empty turnover list is provided then \
        turnover is set to True"""

        self.validator = Validator()
        self._rotor_type = rotor_type
        self._rotor_characters = self._validate_rotor_lists(rotor_characters, "rotor characters")
        self._ring_characters = self._validate_rotor_lists(ring_characters, "ring characters")
        self._absolute_characters = [chr(i) for i in range(65, 91)]
        self._turnover_characters = self._validate_turnover_list(turnover_characters)
        self._default_rotor_position = ring_characters[0]
        self._initial_rotor_character = rotor_characters[0]
        self.can_turnover = True
        if len(self._turnover_characters) == 0:
            self.can_turnover = False

    # PUBLIC METHODS -----------------------------------------------------------------

    def rotor_type(self):
        """rotor_type returns the rotor type"""

        return self._rotor_type

    def output_to_reflector(self, index):
        """output_to_reflector takes an index as an argument. Returns the output \
        index of the character in the rotor_characters list for the same character \
        in the absolute_characters list at the argument index"""

        char = self._rotor_characters[index]
        output_index = self._absolute_characters.index(char)
        return output_index

    def output_from_reflector(self, index):
        """output_from_reflector takes an index as an argument. Returns the output \
        index of the character in the absolute_characters list for the same character \
        in the rotor_characters list at the argument index"""

        char = self._absolute_characters[index]
        output_index = self._rotor_characters.index(char)
        return output_index

    def turnover(self):
        """turnover returns True if current ring character is a turnover character, \
        else returns False"""

        for character in self._turnover_characters:
            if character == self.get_rotor_setting():
                return True

        return False

    def rotor_inc(self):
        """rotor_inc moves all values in _ring_characters, _rotor_characters and \
        _absolute_characters one index up the list and the last character to the \
        first index of the list"""

        self.ring_characters_inc()
        self._rotor_characters_inc()
        self._absolute_characters_inc()

    def rotor_dec(self):
        """rotor_dec moves all values in _ring_characters, _rotor_characters and \
        _absolute_characters one index down the list and the first character to \
        the last index of the list"""

        self.ring_characters_dec()
        self._rotor_characters_dec()
        self._absolute_characters_dec()

    def keyed_rotor(self):
        """keyed_rotor increments rotor. Returns True if turnover else returns False"""

        if self.turnover():
            self.rotor_inc()
            return True
        else:
            self.rotor_inc()
            return False

    def set_default_rotor_position(self):
        """set_default_rotor_setting calls set_rotor_position and sets rotor \
        position to 'A' if _ring_characters are letters or '1' if _ring_characters \
        are numeric"""

        self.set_rotor_setting(self._default_rotor_position)

    def set_rotor_setting(self, character):
        """set_rotor_setting takes a character as an argument and rotates the rotor \
        position until the current rotor setting is equal to the argument character \
        and then returns the current rotor setting"""

        character = self.validator.valid_character(character)
        while self.get_rotor_setting() != character:
            self.rotor_inc()
        return self.get_rotor_setting()

    def get_rotor_setting(self):
        """get_rotor_setting returns the character at _ring_characters[0] the \
        character that would be displayed in the rotor window of an enigma machine"""

        return self._ring_characters[0]

    def set_default_rotor_settings(self):
        """set_default_rotor_settings sets rotor to default position and then sets \
        the ring setting to default"""

        self.set_default_rotor_position()
        self.set_default_ring_setting()
        return (self.get_ring_setting(), self.get_rotor_setting())

    def set_ring_setting(self, character):
        """set_ring_setting takes a character as an argument. If character is valid \
        rotor is rotated until _absolute_characters[0] is equal to _default rotor \
        position. _ring_characters are rotated until the _ring_characters[0] is \
        equal to character and then the rotor is rotated back to its original rotor \
        position"""

        try:
            character = self.valid_ring_character(character)
        except RotorRingCharError as e:
            raise e
        else:
            current_ring_setting = self._ring_characters[0]
            if self._default_rotor_position not in self._absolute_characters:
                default_rotor_position = self._convert_ring_character(self._default_rotor_position)
            else:
                default_rotor_position = self._default_rotor_position
            while self._absolute_characters[0] != default_rotor_position:
                self.rotor_inc()
            while self._ring_characters[0] != character:
                self.ring_characters_inc()
            while self._ring_characters[0] != current_ring_setting:
                self.rotor_inc()
            return character

    def get_ring_setting(self):
        """get_ring_setting gets the index of the _default_rotor_position character \
        in the _absolute_characters list and then gets the character at that index \
        in the _ring_characters list. This character is the current ring setting \
        and is returned"""

        try:
            index = self._absolute_characters.index(self._default_rotor_position)
        except ValueError:
            default_rotor_position = self._convert_ring_character(self._default_rotor_position)
            index = self._absolute_characters.index(default_rotor_position)
        ring_setting = self._ring_characters[index]
        return ring_setting

    def valid_ring_character(self, character):
        """valid_ring_character takes a character as an argument and returns \
        True if the character is in the ring_characters list else returns False"""

        try:
            character = self.validator.valid_character(character)
        except ValueError:
            raise RotorRingCharError(character, self._ring_characters[0])
        else:
            if character in self._ring_characters:
                return character
            elif "{:0>2}".format(character) in self._ring_characters:
                return "{:0>2}".format(character)
            else:
                raise RotorRingCharError(character, self._ring_characters[0])

    def ring_character_type(self):

        if self._ring_characters[0].isalpha():
            return "letter"
        else:
            return "number"

    def ring_characters_inc(self):
        """ring_characters_inc moves all the values in _ring_characters one index \
        up the list and the last value to the first index of the list"""

        self._ring_characters = Rotor._inc_list(self._ring_characters)

    def ring_characters_dec(self):
        """ring_characters_dec moves all the values in _ring_characters one index \
        down the list and the first value to the last index of the list"""

        self._ring_characters = Rotor._dec_list(self._ring_characters)

    def set_default_ring_setting(self):
        """set_default_ring_setting sets the ring setting to the same value as \
        _default_rotor_position"""

        self.set_ring_setting(self._default_rotor_position)

    def get_rotor_dict(self):
        """get_rotor_dict returns a dictionary with the rotor type, ring characters, \
        rotor characters, absolute characters and turnover characters"""

        rotor_dict = {}
        rotor_dict["ROTOR_TYPE"] = self.rotor_type()
        rotor_dict["ROTOR_SETTING"] = self.get_rotor_setting()
        rotor_dict["RING_SETTING"] = self.get_ring_setting()
        rotor_dict["RING_CHARACTERS"] = self._ring_characters.copy()
        rotor_dict["ROTOR_CHARACTERS"] = self._rotor_characters.copy()
        rotor_dict["ABSOLUTE_CHARACTERS"] = self._absolute_characters.copy()
        rotor_dict["TURNOVER_CHARACTERS"] = self._turnover_characters.copy()
        return rotor_dict

    # PRIVATE METHODS ---------------------------------------------------------------

    def _rotor_characters_inc(self):
        """_rotor_characters_inc moves all the values in rotor_characters one index \
        up the list and the last value to the first index of the list"""

        self._rotor_characters = Rotor._inc_list(self._rotor_characters)

    def _rotor_characters_dec(self):
        """_rotor_characters_dec moves all the values in rotor_characters one index \
        down the list and the first value to the last index of the list"""

        self._rotor_characters = Rotor._dec_list(self._rotor_characters)

    def _absolute_characters_inc(self):
        """_absolute_characters_inc moves all the values in absolute_characters one \
        index up the list and the last value to the first index of the list"""

        self._absolute_characters = Rotor._inc_list(self._absolute_characters)

    def _absolute_characters_dec(self):
        """_absolute_characters_dec moves all the values in absolute_characters one \
        index down the list and the first value to the last index of the list"""

        self._absolute_characters = Rotor._dec_list(self._absolute_characters)

    @staticmethod
    def _inc_list(_list):
        """_inc_list takes a list as an argument. all values in the list are moved \
        one index up the list and the last value to the first index of the list"""

        first_char = _list[0]
        new_list = list(range(26))
        new_list[0:25] = _list[1:]
        new_list[25] = first_char
        return new_list

    @staticmethod
    def _dec_list(_list):
        """_dec_list takes a list as an argument. all values in the list are moved \
        one index down the list and the first value to the last index of the list"""

        last_char = _list[-1]
        new_list = list(range(26))
        new_list[1:] = _list[0:25]
        new_list[0] = last_letter
        return new_list

    def _validate_rotor_lists(self, _list, list_type):
        """_validate_rotor_lists takes a list and a list_type string as an argument. \
        If the length of the list is not 26 RotorListRangeError is raised. If all \
        the elements are not unique RotorListRepeatError is raised. If any element \
        in the list is not an alphanumeric character RotorListTypeError is raised. \
        If all elements in the list are not alpha or not numeric RotorListCharError \
        is raised. If the list is valid a valid list with uppercase characters is \
        returned"""

        if len(_list) != 26:
            raise RotorListRangeError(self.rotor_type(), list_type)

        if not self.validator.unique_list(_list):
            raise RotorListRepeatError(self.rotor_type(), list_type)

        valid_list = []
        for i in range(len(_list)):
            if not _list[i].isalnum():
                raise RotorListTypeError(self.rotor_type(), list_type)
            elif _list[i].isalpha() and _list[0].isalpha():
                valid_list.append(_list[i].upper())
            elif _list[i].isnumeric() and _list[0].isnumeric():
                valid_list.append(_list[i])
            else:
                raise RotorListCharError(self.rotor_type(), list_type)
        return valid_list

    def _convert_turnover_list(self, turnover_characters):

        converted_list = []
        letters_list = LETTERS
        numbers_list = NUMBERS
        for character in turnover_characters:
            if character in self._ring_characters:
                converted_list.append(character)
            elif character in letters_list:
                index = letters_list.index(character)
                number = numbers_list[index]
                converted_list.append(number)
        return converted_list

    def _validate_turnover_list(self, turnover_list):
        """_validate_turnover_list takes a list as an argument. Checks that each \
        character in the turnover_list is also in the ring_characters list. If a \
        turnover character does not match any character in the ring_characters \
        list RotorTurnoverListError is raised. If list is valid a valid list \
        containing uppercase characters is returned. If turnover_list is empty \
        an empty list is returned"""

        turnover_list = self._convert_turnover_list(turnover_list)
        valid_turnover_list = []
        for turnover_char in turnover_list:
            for char in self._ring_characters:
                if turnover_char.upper() == char.upper():
                    valid_turnover_list.append(turnover_char.upper())
        if len(valid_turnover_list) != len(turnover_list):
            raise RotorTurnoverListError(self._rotor_type)
        else:
            return valid_turnover_list

    def _convert_ring_character(self, character):

        index = NUMBERS.index(character)
        default_rotor_position = LETTERS[index]
        return default_rotor_position


if __name__ == "__main__":
    rotor_type = 'Rotor 1'
    rotor_characters = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S',
                        'P', 'A', 'I', 'B', 'R', 'C', 'J']
    ring_characters_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ring_characters_numeric = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
                               '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
    turnover_characters_alpha = ['Q']
    turnover_characters_numeric = ['15']

    rotor1 = Rotor(rotor_characters, ring_characters_alpha, turnover_characters_alpha, rotor_type)
    print(rotor1.rotor_type())
    print(rotor1.get_rotor_setting())
    rotor1.keyed_rotor()
    print(rotor1.get_rotor_setting())
    print("ring setting ", rotor1.get_ring_setting())
    rotor1.set_default_rotor_position()
    print(rotor1.get_rotor_setting())
    rotor1.set_ring_setting('C')
    print("ring setting ", rotor1.get_ring_setting())
    print(rotor1.set_default_rotor_settings())

    rotor2 = Rotor(rotor_characters, ring_characters_numeric, turnover_characters_numeric, rotor_type)
    print(rotor2.rotor_type())
    print(rotor2.get_rotor_setting())
    rotor2.keyed_rotor()
    print(rotor2.get_rotor_setting())
    print("ring setting ", rotor2.get_ring_setting())
    rotor2.set_default_rotor_position()
    print(rotor2.get_rotor_setting())
    rotor2.set_ring_setting("03")
    print("ring setting ", rotor2.get_ring_setting())
    print(rotor2.set_default_rotor_settings())