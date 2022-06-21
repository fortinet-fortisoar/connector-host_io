""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import _check_health, _run_operation

logger = get_logger('host_io')


class HostIO(Connector):

    def execute(self, config, operation, params, **kwargs):
        logger.info('host_io: In execute() Operation: [{}]'.format(operation))
        try:
            params.update({"operation": operation})
            return _run_operation(config, params)
        except Exception as err:
            logger.error('host_io: {}'.format(err))
            raise ConnectorError('host_io: {}'.format(err))

    def check_health(self, config):
        return _check_health(config)
