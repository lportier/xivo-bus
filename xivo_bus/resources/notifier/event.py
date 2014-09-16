# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Avencall
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

from __future__ import unicode_literals

import datetime
import socket
import uuid


class NotifierEvent(object):

    def __init__(self, name, data):
        self.message_id = str(uuid.uuid4())
        self.publisher_id = socket.gethostname()
        self.priority = 'INFO',
        self.name = name
        self.data = data
        self.datetime = datetime.datetime.now()

    def marshal(self):
        return {
            'message_id': self.message_id,
            'publisher_id': self.publisher_id,
            'priority': self.priority,
            'name': self.name,
            'data': self.data,
            'datetime': self.datetime
        }

    @classmethod
    def unmarshal(cls, msg):
        return cls(msg['name'], msg['data'])
