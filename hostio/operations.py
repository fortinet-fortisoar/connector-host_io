""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
import requests
import json

logger = get_logger('host_io')


class Host_io(object):

    def __init__(self, config):
        self.token = config.get('token')
        self.server_url = config.get('server').strip()
        self.protocol = 'https'
        if self.server_url[-1] == '/':
            self.server_url = self.server_url[:-1]
        self.url = '{0}://{1}'.format(self.protocol.lower(), self.server_url)
        self.headers = {'accept': 'application/json'}

    def make_rest_call(self, endpoint, method='GET', data=None, headers=None, health_check=False):
        url = '{0}{1}token={2}'.format(self.url, endpoint, self.token)
        if data:
            data = json.dumps(data)
        try:
            response = requests.request(method, url, data=data, headers=headers)
            if response.status_code in [200]:
                if health_check:
                    return {'status': 'Success'}
                try:
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    return {'status': 'Failure', 'data': response_data}
            else:
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(e))

    def dns_domain(self, params):
        e_url = params.get('endpoint_url')
        endpoint = '/api/dns/{0}?'.format(e_url)
        return self.make_rest_call(endpoint=endpoint)

    def get_all_domains(self, params):
        field = params.get('field')
        value = params.get('value')
        limit = params.get('limit')
        page = params.get('page')
        endpoint = '/api/domains/{0}/{1}?limit={2}&page={3}&'.format(field, value, str(limit), str(page))
        return self.make_rest_call(endpoint=endpoint)

    def get_full_domains_data(self, params):
        e_url = params.get('endpoint_url')
        endpoint = '/api/full/{0}?'.format(e_url)
        return self.make_rest_call(endpoint=endpoint)

    def related_domain(self, params):
        e_url = params.get('endpoint_url')
        endpoint = '/api/related/{0}?'.format(e_url)
        return self.make_rest_call(endpoint=endpoint)

    def web_domain(self, params):
        e_url = params.get('endpoint_url')
        endpoint = '/api/web/{0}?'.format(e_url)
        return self.make_rest_call(endpoint=endpoint)


def _run_operation(config, params):
    operation = params['operation']
    hc_object = Host_io(config)
    command = getattr(Host_io, operation)
    response = command(hc_object, params)
    return response


def _check_health(config):
    try:
        hc_object = Host_io(config)
        server_config = hc_object.make_rest_call(endpoint='?', health_check=True)
        if server_config['status'] == 'Failure':
            logger.exception('Authentication Error, Check URL and API Token.')
            raise ConnectorError('Authentication Error, Check URL and API Token.')
    except Exception as Err:
        logger.exception('Health Check Error:{}'.format(Err))
        raise ConnectorError('Health Check Error:{}'.format(Err))
