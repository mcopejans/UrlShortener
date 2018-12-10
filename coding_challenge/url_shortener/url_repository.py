import time


class URLRepository(object):

    def __init__(self):
        self._id = pow(62,5)
        self._urls = {}

    def increment_id(self):
        self._id += 1
        return self._id

    def save_url(self, key, long_url):
        self._urls[key] = long_url

    def get_url(self, key):
        """
        Retrieves URL from dictionary.
        :param key:
        :return:
        :raises: KeyError if key not in dictionary.
        """
        return self._urls[key]
