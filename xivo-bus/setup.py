#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from distutils.core import setup

setup(
    name='xivo-bus',
    version='0.1',
    description='XiVO BUS libraries',
    author='Avencall',
    author_email='dev@avencall.com',
    url='http://git.xivo.fr/',
    license='GPLv3',
    packages=[
        'xivo_bus',
        'xivo_bus.ctl',
        'xivo_bus.resources',
        'xivo_bus.resources.agent',
        'xivo_bus.resources.agent.command',
        'xivo_bus.resources.common',
        'xivo_bus.resources.device',
        'xivo_bus.resources.extension',
        'xivo_bus.resources.line',
        'xivo_bus.resources.user',
        'xivo_bus.resources.user_line_extension',
        'xivo_bus.resources.voicemail',
        'xivo_bus.resources.xivo',
        'xivo_bus.resources.xivo.command',
    ]
)