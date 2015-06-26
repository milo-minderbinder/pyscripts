import urlparse
import getpass
import requests


class REClient(object):

    def __init__(self, api_url, **kwargs):
        self.api_url = api_url
        if not self.api_url.endswith('/'):
            self.api_url += '/'
        self.default_kwargs = {}
        self.default_kwargs.update(kwargs)

    def add_defaults(self, **kwargs):
        print 'Adding default request arguments: %s' % str(kwargs.keys())
        for kwarg in kwargs:
            if kwarg in self.default_kwargs:
                if type(self.default_kwargs[kwarg]) is dict:
                    self.default_kwargs[kwarg].update(kwargs[kwarg])
                else:
                    self.default_kwargs[kwarg] = kwargs[kwarg]
            else:
                self.default_kwargs[kwarg] = kwargs[kwarg]

    def add_auth(self, username=None, password=None):
        if username is None:
            username = raw_input('Username: ')
        if password is None:
            password = getpass.getpass()
        self.add_defaults(auth=(username, password))

    def request(self, rel_path='', method='GET', *args, **kwargs):
        url = urlparse.urljoin(self.api_url, rel_path)
        kwargs.update(self.default_kwargs)
        response = requests.request(method.upper(), url, *args, **kwargs)
        if response.status_code != requests.codes.ok:
            print 'Received %d response from requested URL: %s' % \
                (response.status_code, url)
        return response

    def get(self, rel_path='', *args, **kwargs):
        return self.request(rel_path, 'GET', *args, **kwargs)

    def post(self, rel_path='', *args, **kwargs):
        return self.request(rel_path, 'POST', *args, **kwargs)