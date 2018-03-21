#!/usr/bin/env python

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

import time, hashlib, hmac

from bravado.requests_client import Authenticator

class APIKeyAuthenticator(Authenticator):

    def __init__(self, host, api_key, api_secret):
        super(APIKeyAuthenticator, self).__init__(host)
        self.api_key = api_key
        self.api_secret = api_secret

    def matches(self, url):
        if 'swagger.json' in url:
            return False
        return True

    def apply(self, r):
        # 5s grace period in case of clock skew
        expires = int(round(time.time()) + 5)
        r.headers['api-expires'] = str(expires)
        r.headers['api-key'] = self.api_key
        prepared = r.prepare()
        body = prepared.body or ''
        url = prepared.path_url
        r.headers['api-signature'] = self.generate_signature(self.api_secret, r.method, url, expires, body)
        return r

    def generate_signature(self, secret, verb, url, nonce, data):
        parsedURL = urlparse(url)
        path = parsedURL.path
        if parsedURL.query:
            path = path + '?' + parsedURL.query

        nonce = str(nonce)
        
        _message = verb + path + nonce + data
        message = bytes(_message.encode('utf-8'))
        
        secret = bytes(secret.encode('utf-8'))
        
        return hmac.new(secret, message, digestmod=hashlib.sha256).hexdigest()
