
import mod_python.apache

from base64 import b64decode
# WebOb
from webob import Request, Response


class ModPythonRequest(object):

    def __init__(self, environ):
        self.request = Request(environ, charset='utf8')
        self.response = Response()

    def add_common_vars(self):
        raise NotImplementedError()

    def add_handler(self):
        raise NotImplementedError()

    def allow_methods(self):
        raise NotImplementedError()

    @property
    def content_length(self):
        return self.response.content_length

    @content_length.setter
    def content_length(self, value):
        self.response.content_length = value

    @property
    def content_type(self):
        return self.response.content_type

    @content_type.setter
    def content_type(self, value):
        self.response.content_type = value

    def document_root(self):
        raise NotImplementedError()

    def get_basic_auth_pw(self):
        auth = self.request.authorization
        if auth:
            mechanism, token = auth.strip.split()
            if mechanism == 'Basic':
                return b64decode(token).split(':')[-1]

    def get_config(self):
        raise NotImplementedError()

    def get_remote_host(self, type=None, str_is_ip=None):
        return self.request.remote_addr

    def get_options(self):
        raise NotImplementedError()

    def internal_redirect(self):
        raise NotImplementedError()

    def log_error(self, message, level=None):
        try:
            print >> self.request.environ['wsgi.errors'], message
        except KeyError:
            raise NotImplementedError()

    def requires(self):
        raise NotImplementedError()

    def read(self, len_=-1):
        return self.request.body.read(len_)

    def readline(self, len_=-1):
        return self.request.body.readline(len_)

    def readlines(self, sizehint=-1):
        raise NotImplementedError()

    def register_cleanup(self, callable, data=None):
        raise NotImplementedError()

    def sendfile(self, path, offset, len_):
        raise NotImplementedError()

    def send_http_header(self):
        pass

    @property
    def uri(self):
        return self.request.path

    def write(self, string, flush=1):
        self.response.app_iter.append(string)

    def flush(self):
        pass

    def set_content_length(self, len_):
        self.response.content_length = len_

