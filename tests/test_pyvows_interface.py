#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyVows testing engine
# https://github.com/heynemann/pyvows

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Bernardo Heynemann heynemann@gmail.com

from pyvows import Vows

import division_vows

def test_can_get_vows():
    assert Vows.contexts

def test_can_get_vows_by_key():
    assert 'DivisionTests' in Vows.contexts

def test_can_run_vows():
    result = Vows.ensure()

    assert result.successful
