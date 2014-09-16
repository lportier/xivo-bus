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

import unittest
from xivo_bus.ctl.config import BusConfig, default_config


class TestConfig(unittest.TestCase):

    def test_to_connection_params(self):
        config = BusConfig('foobar', 42)

        params = config.to_connection_params()

        self.assertEqual(params.host, 'foobar')
        self.assertEqual(params.port, 42)

    def test_default_config(self):
        self.assertEqual(default_config.host, BusConfig.DEFAULT_HOST)
        self.assertEqual(default_config.port, BusConfig.DEFAULT_PORT)
