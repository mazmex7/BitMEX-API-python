#!/usr/bin/env python

from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient
from bravado.swagger_model import Loader

from BitMEXAPIKeyAuthenticator import APIKeyAuthenticator

# swagger spec's formats to exclude. this help to avoid warning in your console.
EXCLUDE_SWG_FORMATS = ['JSON', 'guid']

def bitmex(test=True, config=None, api_key=None, api_secret=None):
    # config options at http://bravado.readthedocs.io/en/latest/configuration.html
    if not config:
        config = {
            # Don't use models (Python classes) instead of dicts for #/definitions/{models}
            'use_models': False, 
            # bravado has some issues with nullable fields
            'validate_responses': False, 
            # Returns response in 2-tuple of (body, response); if False, will only return body
            'also_return_response': True, 

            # 'validate_swagger_spec': True, 
            # 'validate_requests': True, 
            # 'formats': [],
        }

    host = 'https://www.bitmex.com'
    if test:
        host = 'https://testnet.bitmex.com'
        
    spec_uri = host + '/api/explorer/swagger.json'
    spec_dict = get_swagger_json(spec_uri, exclude_formats=EXCLUDE_SWG_FORMATS)

    if api_key and api_secret:
        request_client = RequestsClient()
        request_client.authenticator = APIKeyAuthenticator(host, api_key, api_secret)
        return SwaggerClient.from_spec(spec_dict, origin_url=spec_uri, http_client=request_client, config=config)
    else:
        return SwaggerClient.from_spec(spec_dict, origin_url=spec_uri, http_client=None, config=config)


# exclude some format from swagger json to avoid warning in API execution.
def get_swagger_json(spec_uri, exclude_formats=[]):
    loader = Loader(RequestsClient())
    spec_dict = loader.load_spec(spec_uri)
    if not exclude_formats:
        return spec_dict

    # exlude formats from definitions
    for def_key, def_item in spec_dict['definitions'].items():
        if 'properties' not in def_item:
            continue
        for prop_key, prop_item in def_item['properties'].items():
            if 'format' in prop_item and prop_item['format'] in exclude_formats:
                prop_item.pop('format')

    # exlude formats from paths
    for path_key, path_item in spec_dict['paths'].items():
        for method_key, method_item in path_item.items():
            if 'parameters' not in method_item:
                continue
            for param in method_item['parameters']:
                if 'format' in param and param['format'] in exclude_formats:
                    param.pop('format')
    return spec_dict
