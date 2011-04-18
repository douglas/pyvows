#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyvows testing engine
# https://github.com/heynemann/pyvows

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Bernardo Heynemann heynemann@gmail.com

from pyvows import Vows

@Vows.batch
class DivisionTests(Vows.Context):

    class WhenDividing42Per1(Vows.Context):

        def topic(self):
            return 42 / 1

        def WeGetANumber(self, topic):
            Vows.Assert.is_numeric(topic)

        def WeGet42(self, topic):
            Vows.Assert.are_equal(42, topic)

@Vows.batch
class Assertion(Vows.Context):

    class Equal(Vows.Context):

        def topic(self):
            return "test"

        def WeGetTest(self, topic):
            Vows.Assert.are_equal('test', topic)

        def WeDoNotGetElse(self, topic):
            Vows.Assert.not_are_equal('else', topic)

    class IsNumeric(Vows.Context):

        class WhenItIsANumber(Vows.Context):
            def topic(self):
                return 42

            def WeAssertItIsNumeric(self, topic):
                Vows.Assert.is_numeric(topic)

        class WhenItIsNotANumber(Vows.Context):
            def topic(self):
                return 'test'

            def WeAssertItIsNotNumeric(self, topic):
                Vows.Assert.not_is_numeric(topic)

