import requests
import json

VERSION="0.0"

class SuchBadShibeException(Exception):
    """ Exception raised whenever the API call fails """
    pass

class DogeTransport(object):
    def __init__(self):
        self.root_url = "https://www.dogeapi.com/wow"

    def fetch(self, apikey, method, **kwargs):
        """ Handle all object methods call conversion to http call."""

        headers = {'User-Agent': 'wow-such-python/%s'%(VERSION)}

        # http parameters
        payload= {}
        payload["a"] = method

        if apikey is not None :
            payload["api_key"] = apikey

        # update parameters with method parameters
        payload.update(kwargs)
        response = requests.get(self.root_url, params = payload, headers = headers)

        if response.ok :
            return response.json()
        raise SuchBadShibeException("Problem while fetching datas")

class Doge(object):
    """ Such API client """
    def __init__(self, apikey=None):
        self.apikey = apikey
        self.transport = DogeTransport()

    def __getattr__(self, attr, *args, **kwargs):
        """ Handle all object methods call and route them to the transport class. Very meta."""
        def hook(*args, **kwargs):
            return self.transport.fetch(self.apikey, attr, **kwargs)
        return hook
