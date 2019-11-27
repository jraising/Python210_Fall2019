#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:47:06 2019

@author: jraising
"""
import os.path
from mailroom4 import letter
from mailroom4 import report
# Mock data to use
donor = {'Tester' : [653784.49, 1000.50]
          }

# Mock data to compare
expectedReport = 'Donor Name                         Total Given                   Num Gifts             Average Gift             ------------------------------------------------------------------------------------------------------\nTester                               654784.99                         2                 327392.49\n'
def test_letter():
    letter(donor)
    assert os.path.isfile("Tester.txt") is True
    
def test_report():
    generatedReport = report(donor)
    assert (generatedReport == expectedReport) is True
    
    
    
    
    
    
    
    
