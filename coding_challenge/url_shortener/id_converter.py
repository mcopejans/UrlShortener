
class IDConverter(object):

    def __init__(self):
        self._char_to_index_table = IDConverter.init_char_to_index_table()
        self._index_to_char_table = IDConverter.init_index_to_char_table()

    @staticmethod
    def init_char_to_index_table():
        char_to_index_table = {}
        for i in range(0, 26):
            start_char = 'a'
            char_to_index_table[chr(ord(start_char) + i)] = i

        for i in range(26, 52):
            start_char = 'A'
            char_to_index_table[chr(ord(start_char) + i - 26)] = i

        for i in range(52, 62):
            start_char = '0'
            char_to_index_table[chr(ord(start_char) + i - 52)] = i

        return char_to_index_table

    @staticmethod
    def init_index_to_char_table():
        index_to_char_table = []
        for i in range(0, 26):
            start_char = 'a'
            index_to_char_table.append(chr(ord(start_char) + i))

        for i in range(26, 52):
            start_char = 'A'
            index_to_char_table.append(chr(ord(start_char) + i - 26))

        for i in range(52, 62):
            start_char = '0'
            index_to_char_table.append(chr(ord(start_char) + i - 52))

        return index_to_char_table

    @staticmethod
    def convert_base_10_to_base_62_id(id):
        digits = []
        while id > 0:
            remainder = int(id % 62)
            digits.append(remainder)
            id /= 62

        return reversed(digits)

    def convert_base_62_to_base_10_id(self, id):
        base_10_id = long()
        for i, char in enumerate(id):
            base_10_i = self._char_to_index_table[char]
            base_10_id += base_10_i * pow(62, len(id) - i - 1)

        return base_10_id

    def create_unique_id(self, id):
        base_62_id = IDConverter.convert_base_10_to_base_62_id(id)
        unique_url_id = ''
        for digit in base_62_id:
            unique_url_id += self.index_to_char_table[digit]

        return unique_url_id

    def get_dictionary_key_from_unique_id(self, unique_id):
        base_62_id = ''
        for char in unique_id:
            base_62_id += char

        return self.convert_base_62_to_base_10_id(base_62_id);

    @property
    def char_to_index_table(self):
        return self._char_to_index_table

    @property
    def index_to_char_table(self):
        return self._index_to_char_table
