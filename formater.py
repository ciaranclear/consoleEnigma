
class Formater(object):

	def __init__(self):
		super(Formatter, self).__init__()


	@staticmethod
	def pad_string(string, pad_char, length):

		left_pad_length = int((length - len(string))/2)
		left_padded_string = "{0}{1}".format(pad_char * left_pad_length, string)
		rigth_pad_length = int(length - len(left_padded_string))
		new_string = "{0}{1}".format(left_padded_string, pad_char * rigth_pad_length)
		return new_string

	@staticmethod
	def right_pad_string(string, pad_char, length):

		right_pad_length = length - len(string)
		new_string = "{0}{1}".format(string, pad_char * right_pad_length)
		return new_string

	@staticmethod
	def left_pad_string(string, pad_char, length):

		left_pad_length = length - len(string)
		new_string = "{0}{1}".format(pad_char * left_pad_length, string)
		return new_string

	@staticmethod
	def list_to_string(_list):

		new_string = ""
		for char in _list:
			new_string += char
		return new_string