#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyVows testing engine
# https://github.com/heynemann/pyvows

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Bernardo Heynemann heynemann@gmail.com

from pyvows import Vows

@Vows.assertion
def to_length(topic, expected):
    assert len(topic) == expected, "Expected topic(%s) to have %s of length, but it had %s" % (topic, expected, len(topic))

