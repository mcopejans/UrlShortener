import re


class UrlValidator(object):

    URL_REGEX = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    @staticmethod
    def validate(url):
        """
        Validates url.
        :param url: Input URL.
        :return: Regex group in case url is a valid url according to URL_REGEX.
        :raises: AttributeError if url is not valid.
        """
        return UrlValidator.URL_REGEX.search(url).group()