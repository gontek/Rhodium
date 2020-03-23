# Copyright 2015-2016 David Hadka
#
# This file is part of Rhodium, a Python module for robust decision making and
# exploratory modeling.
#
# Rhodium is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Rhodium is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Rhodium.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import division, print_function, absolute_import

import os
import sys
import unittest
from ..cache import *

class TestCache(unittest.TestCase):
    
    def testSimpleCache(self):
        cache("testValue", 5)
        value=cache("testValue", 10) # Should return the cached value of 5
        self.assertEquals(5, value)
        
    def testFileCache(self):
        setup_cache(file="test.dat")
        cache("testValue", 5)
        self.assertTrue(os.path.exists("test.dat"))
        
    def testClearCache(self):
        cache("tempValue", 5)
        setup_cache(clear=True)
        value = cache("tempValue", 10)
        self.assertEquals(10, value)
        
    def testFunction(self):
        self.testFunction_called=False
        
        def fun():
            self.testFunction_called=True
            return 5
        
        value=cache("testFun", fun)
        self.assertEquals(True, self.testFunction_called)
        self.assertEquals(5, value)
        self.testFunction_called=False
        
        value=cache("testFun", fun)
        self.assertEquals(False, self.testFunction_called)
        self.assertEquals(5, value)
        
    def testCachedFunction(self):
        self.testCachedFunction_called=False
        
        @cached
        def fun():
            self.testCachedFunction_called=True
            return 5
        
        value=fun()
        self.assertEquals(True, self.testCachedFunction_called)
        self.assertEquals(5, value)
        self.testCachedFunction_called=False
        
        value=fun()
        self.assertEquals(False, self.testCachedFunction_called)
        self.assertEquals(5, value)
            
