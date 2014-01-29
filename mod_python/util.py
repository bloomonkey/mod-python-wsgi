
from cgi import parse_qs as cgi_parse_qs, parse_qsl as cgi_parse_qsl


class Field(object):

    def __init__(self, name, value):
        raise NotImplementedError()


class StringField(str):

    def __init__(self, value):
        super(StringField, self).__init__(value)

    @property
    def value(self):
        return self


class FieldStorage(object):

    def __init__(self, req, keep_blank_values=False, strict_parsing=None):
        """Constructor.

        :arg req: The request object
        :type req: mod_python_wsgi.request.ModPythonRequest
        :arg keep_blank_values: blank values in URL encoded form data should
            be treated as blank strings
        :type keep_blank_values: bool

        """
        # Parse request parameters into a single data structure
        self._multidict = req.request.params

    def __getitem__(self, key):
        return self._wrap(key, self._multidict.__getitem__(key))

    def _wrap(self, name, value):
        if hasattr(value, 'read'):
            return Field(name, value)
        elif value is not None:
            return StringField(value)

    def get(self, key, default=None):
        return self._wrap(key, self._multidict.get(key, default))

    def getlist(self, key):
        return [self._wrap(key, v) for v in self._multidict.getall(key)]

    def getfirst(self, key, default=None):
        return self.get(key, default)

    def getvalue(self, key, default=None):
        val = self.getlist(key)
        if not val:
            return default
        elif len(val) == 1:
            return val[0]
        else:
            return val

    def has_key(self, key):
        return key in self._multidict


def parse_qs(*args):
    return cgi_parse_qs(*args)


def parse_qsl(*args):
    return cgi_parse_qsl(*args)


def redirect(req, location, permanent=0, text=None):
    req.response.location = location
    if permanent:
        req.response.status = 301
    else:
        req.response.status = 307
    if text:
        req.response.body = text
