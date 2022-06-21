""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
from connectors.core.connector import get_logger, ConnectorError
import requests
import json

logger = get_logger('host_io')


class HostIO(object):

    def __init__(self, config):
        self.token = config.get('token')
        self.url = config.get('server').strip()
        if not self.url.startswith('https://'):
            self.url = 'https://' + self.url
        if self.url[-1] == '/':
            self.url = self.url[:-1]
        self.headers = {'accept': 'application/json'}

    def make_rest_call(self, endpoint, method='GET', data=None, headers=None, health_check=False):
        url = '{0}{1}token={2}'.format(self.url, endpoint, self.token)
        logger.info('host_io: Final url to make rest call is: {}'.format(url))
        if data:
            logger.info('host_io: Converting the data: {} into an equivalent JSON object.'.format(data))
            data = json.dumps(data)
            logger.info('host_io: After converting into a JSON object: {}'.format(data))
        try:
            logger.info('host_io: Making a request with {0} method, {1} data and {2} as headers.'.format(method, data, headers))
            response = requests.request(method, url, data=data, headers=headers)
            if response.status_code in [200]:
                if health_check:
                    return {'status': 'Success'}
                try:
                    logger.info('host_io: Converting the response into JSON format after returning with status code: {}'.format(response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.info('host_io: Failed to convert the response into JSON format. The response details are: {}'.format(response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('host_io: Failed with response {}'.format(response))
                raise ConnectorError({'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception('host_io: {}'.format(e))
            raise ConnectorError('host_io: {}'.format(e))

    def get_dns_domain_details(self, params):
        domain_name = params.get('dns_domain')
        endpoint = '/api/dns/{0}?'.format(domain_name)
        logger.info('host_io: Endpoint is: {}'.format(endpoint))
        return self.make_rest_call(endpoint=endpoint)

    def get_all_domains(self, params):
        field = params.get('field')
        value = params.get('value')
        limit = params.get('limit')
        page = params.get('page')
        endpoint = '/api/domains/{0}/{1}?limit={2}&page={3}&'.format(field, value, str(limit), str(page))
        logger.info('host_io: Endpoint is: {}'.format(endpoint))
        return self.make_rest_call(endpoint=endpoint)

    def get_full_domains_data(self, params):
        domain_name = params.get('domain_name')
        endpoint = '/api/full/{0}?'.format(domain_name)
        logger.info('host_io: Endpoint is: {}'.format(endpoint))
        return self.make_rest_call(endpoint=endpoint)

    def get_related_domains(self, params):
        domain_name = params.get('domain_name')
        endpoint = '/api/related/{0}?'.format(domain_name)
        logger.info('host_io: Endpoint is: {}'.format(endpoint))
        return self.make_rest_call(endpoint=endpoint)

    def get_web_domain_details(self, params):
        domain_name = params.get('web_domain')
        endpoint = '/api/web/{0}?'.format(domain_name)
        logger.info('host_io: Endpoint is: {}'.format(endpoint))
        return self.make_rest_call(endpoint=endpoint)


def _run_operation(config, params):
    operation = params['operation']
    hc_object = HostIO(config)
    command = getattr(HostIO, operation)
    response = command(hc_object, params)
    return response


def _check_health(config):
    try:
        hi_obj = HostIO(config)
        server_config = hi_obj.make_rest_call(endpoint='/api/full/google.com?', health_check=True)
        if server_config['status'] == 'Failure':
            logger.exception('host_io: Authentication Error, Check URL and API Token.')
            raise ConnectorError('host_io: Authentication Error, Check URL and API Token.')
    except Exception as Err:
        logger.exception('host_io: Health Check Error:{}'.format(Err))
        raise ConnectorError('host_io: Health Check Error:{}'.format(Err))
