import id_converter, url_repository

class URLShortener(object):

    def __init__(self):
        self._url_repository = url_repository.URLRepository()
        self._id_converter_instance = id_converter.IDConverter()
        self._custom_url_storage = {}

    def shorten_url(self, long_url, custom_url=None):
        seq_id = self._url_repository.increment_id()
        if not custom_url:
            unique_id = self._id_converter_instance.create_unique_id(seq_id)
        else:
            unique_id = custom_url
            self._custom_url_storage = { custom_url : seq_id }

        self._url_repository.save_url(seq_id, long_url)
        base = URLShortener.long_url_to_short_url_base(long_url)
        return base + str(unique_id)

    @staticmethod
    def long_url_to_short_url_base(long_url):
        url_parts = long_url.split('/')
        base_url_parts = url_parts[2].split('.')
        base_url_start = '.'.join(base_url_parts[:-1])
        return '/'.join(url_parts[0:2]) + '/' + base_url_start[:-2] + '.' + base_url_start[len(base_url_start) - 2:] + '/'

    def get_long_url_from_id(self, unique_id):
        try:
            dictionary_key = self._custom_url_storage[unique_id]
            return self._url_repository.get_url(dictionary_key)
        except KeyError:
            dictionary_key = self._id_converter_instance.get_dictionary_key_from_unique_id(unique_id)
            return self._url_repository.get_url(dictionary_key)


