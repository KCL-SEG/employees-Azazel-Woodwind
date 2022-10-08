"""Tests for the solution of your exercise."""
"""DO NOT CHANGE THIS FILE!"""

from employee import *
import re

def test_billie():
    assert billie.get_pay() == 4000
    string = str(billie)
    regex = '^Billie works on a monthly salary of 4000.\s+Their total pay is 4000.$'
    assert re.match(regex, string)

def test_charlie():
    assert charlie.get_pay() == 2500
    string = str(charlie)
    regex = '^Charlie works on a contract of 100 hours at 25/hour.\s+Their total pay is 2500.$'
    assert re.match(regex, string)

def test_renee():
    assert renee.get_pay() == 3800
    string = str(renee)
    regex = 'Renee works on a monthly salary of 3000 and receives a commission for 4 contract\(s\) at 200/contract.\s+Their total pay is 3800.'
    assert re.match(regex, string)

def test_jan():
    assert jan.get_pay() == 4410
    string = str(jan)
    regex  = 'Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract\(s\) at 220/contract.\s+Their total pay is 4410.'
    assert re.match(regex, string)

def test_robbie():
    assert robbie.get_pay() == 3500
    string = str(robbie)
    regex = '^Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.\s+Their total pay is 3500.$'
    assert re.match(regex, string)

def test_ariel():
    assert ariel.get_pay() == 4200
    string = str(ariel)
    regex = '^Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.\s+Their total pay is 4200.$'
    assert re.match(regex, string)
