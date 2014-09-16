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

from __future__ import unicode_literals

import datetime
import socket
import unittest
from mock import sentinel, patch
from .. event import NotifierEvent


UUID = '9da9906e-07f1-44c9-83be-0f738a6ec729'
PUBLISHER_ID = socket.gethostname()
PRIORITY = ('INFO',)
DATETIME = datetime.datetime.now()


class TestNotificationEvent(unittest.TestCase):

    def setUp(self):
        self.msg = {
            'priority': PRIORITY,
            'publisher_id': PUBLISHER_ID,
            'message_id': UUID,
            'name': sentinel.name,
            'datetime': DATETIME,
            'data': {}
        }

    @patch('xivo_bus.resources.notifier.event.datetime')
    @patch('xivo_bus.resources.notifier.event.uuid')
    def test_marshal(self, uuid_mock, datetime_mock):
        uuid_mock.uuid4.return_value = UUID
        datetime_mock.datetime.now.return_value = DATETIME
        command = NotifierEvent(sentinel.name,
                                data1=sentinel.data1,
                                data2=sentinel.data2)
        self.msg['data'].update({
            'data1': sentinel.data1,
            'data2': sentinel.data2
        })

        msg = command.marshal()

        self.assertEqual(msg, self.msg)

    @patch('xivo_bus.resources.notifier.event.uuid')
    def test_unmarshal(self, uuid_mock):
        uuid_mock.uuid4.return_value = UUID
        command = NotifierEvent.unmarshal(self.msg)

        self.assertEqual(command.name, sentinel.name)
        self.assertEqual(command.data, {})
        self.assertEqual(command.message_id, UUID)
        self.assertEqual(command.publisher_id, PUBLISHER_ID)
        self.assertEqual(command.priority, PRIORITY)
