# -*- coding: utf-8 -*-

# Copyright (C) 2012-2014 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import logging
import sys

from kombu import BrokerConnection, Exchange, Producer

from xivo_bus.ctl.config import default_config
from xivo_bus.ctl.marshaler import Marshaler

logger = logging.getLogger(__name__)


class BusProducerError(Exception):

    def __init__(self, error):
        Exception.__init__(self, error)
        self.error = error


class BusProducer(object):

    def __init__(self, config=default_config):
        self._config = config
        self._marshaler = Marshaler()
        self._connection = None
        self._channel = None
        self._exchange = None
        self._producer = None

    def connect(self, exchange_name, exchange_type, exchange_durable):
        logger.info('Connecting to broker %s', self._config.amqp_url)
        if self.connected:
            raise Exception('already connected')
        self._connection = BrokerConnection(self._config.amqp_url)
        try:
            self._connection.connect()
        except Exception as e:
            logger.error('Failed to connect to AMQP transport %s: %s', self._config.amqp_url, e)
            sys.exit(1)

        self._channel = self._connection.channel()
        self._exchange = Exchange(name=exchange_name,
                                  type=exchange_type,
                                  channel=self._channel,
                                  durable=exchange_durable)
        self._producer = Producer(exchange=exchange_name,
                                  channel=self._channel)

        logger.info('Connected to broker %s', self._config.amqp_url)

    @property
    def connected(self):
        return self._connection is not None

    def close(self):
        logger.info('Disconnecting to broker %s', self._config.amqp_url)
        if not self.connected:
            return

        self._connection.release()
        self._connection.close()
        self._connection = None
        self._channel = None
        self._exchange = None
        self._producer = None

    def publish_event(self, routing_key, event, serializer=None):
        if not self.connected:
            raise Exception('connect before to send..')
        body = self._marshaler.marshal_command(event)
        self._producer.publish(body,
                               declare=[self._exchange],
                               exchange=self._exchange,
                               routing_key=routing_key,
                               serializer=serializer)
