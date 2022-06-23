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
        logger.info('Final url to make rest call is: {0}'.format(url))
        if headers:
            self.headers.update(headers)
        if data:
            logger.info('Converting the data: {0} into an equivalent JSON object.'.format(data))
            data = json.dumps(data)
            logger.info('After converting into a JSON object: {0}'.format(data))
        try:
            logger.info('Making a request with {0} method, {1} data and {2} as headers.'.format(method, data, self.headers))
            response = requests.request(method, url, data=data, headers=self.headers)
            if response.status_code in [200]:
                if health_check:
                    return {'status': 'Success'}
                try:
                    logger.info('Converting the response into JSON format after returning with status code: {0}'.format(response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response))
                raise ConnectorError({'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))

    def get_dns_domain_details(self, params):
        endpoint = '/api/dns/{0}?'.format(params.get('dns_domain'))
        logger.info('Endpoint is: {0}'.format(endpoint))
        return self.make_rest_call(endpoint=endpoint)

    def get_all_domains(self, params):
        field = params.get('field')
        value = params.get('value')
        limit = params.get('limit')
        page = params.get('page')
        endpoint = '/api/domains/{0}/{1}?limit={2}&page={3}&'.format(field, value, str(limit), str(page))
        logger.info('Endpoint is: {0}'.format(endpoint))
        return self.make_rest_call(endpoint=endpoint)

    def get_full_domains_data(self, params):
        endpoint = '/api/full/{0}?'.format(params.get('domain_name'))
        logger.info('Endpoint is: {0}'.format(endpoint))
        return self.make_rest_call(endpoint=endpoint)

    def get_related_domains(self, params):
        endpoint = '/api/related/{0}?'.format(params.get('domain_name'))
        logger.info('Endpoint is: {0}'.format(endpoint))
        return self.make_rest_call(endpoint=endpoint)

    def get_web_domain_details(self, params):
        endpoint = '/api/web/{0}?'.format(params.get('web_domain'))
        logger.info('Endpoint is: {0}'.format(endpoint))
        return self.make_rest_call(endpoint=endpoint)


def _run_operation(config, params):
    hc_object = HostIO(config)
    command = getattr(HostIO, params['operation'])
    response = command(hc_object, params)
    return response


def _check_health(config):
    try:
        hi_obj = HostIO(config)
        server_config = hi_obj.make_rest_call(endpoint='/api/full/google.com?', health_check=True)
        if server_config['status'] == 'Failure':
            logger.exception('Authentication Error, Check URL and API Token.')
            raise ConnectorError('Authentication Error, Check URL and API Token.')
    except Exception as Err:
        logger.exception('Health check failed with: {0}'.format(Err))
        raise ConnectorError('Health check failed with: {0}'.format(Err))
