# -*- coding: utf-8 -*-

# Copyright (C) 2013-2014 Avencall
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

import pika


class BusConfig(object):

    DEFAULT_HOST = pika.connection.Parameters.DEFAULT_HOST
    DEFAULT_PORT = pika.connection.Parameters.DEFAULT_PORT
    DEFAULT_VIRTUAL_HOST = pika.connection.Parameters.DEFAULT_VIRTUAL_HOST
    DEFAULT_USERNAME = pika.connection.Parameters.DEFAULT_USERNAME
    DEFAULT_PASSWORD = pika.connection.Parameters.DEFAULT_PASSWORD

    def __init__(self,
                 host=DEFAULT_HOST,
                 port=DEFAULT_PORT,
                 virtual_host=DEFAULT_VIRTUAL_HOST,
                 username=DEFAULT_USERNAME,
                 password=DEFAULT_PASSWORD):
        self.host = host
        self.port = int(port)
        self.virtual_host = virtual_host
        self.username = username
        self.password = password

    def to_connection_params(self):
        return pika.ConnectionParameters(host=self.host,
                                         port=self.port,
                                         virtual_host=self.virtual_host,
                                         credentials=self.pika_credentials)

    @property
    def pika_credentials(self):
        return pika.PlainCredentials(self.username, self.password)

    @property
    def amqp_url(self):
        return 'amqp://%(username)s:%(password)s@%(host)s:%(port)s/%(virtual_host)s' % self

    def __getitem__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]


default_config = BusConfig()
