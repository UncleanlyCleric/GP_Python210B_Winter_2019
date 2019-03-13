#!/usr/bin/env python3
'''
Here we go testing again!
'''
import datetime
#import os
import pytest

from donor_models import Donor, DonorCollection
#import cli_main

'''
donor_models.py testing
'''
################################################################################
'''
We'll start with testing the Donor class
'''
def test_donor_init():
    '''
    This tests adding a donor
    '''
    donor = Donor('James Hetfield')
    assert donor.name == 'James Hetfield'
    assert donor.donations == []


def test_donor_init_error():
    '''
    Now, let's see if we can break it
    '''
    with pytest.raises(TypeError):
        #pylint: disable=E1121
        Donor('Kirk Hammett', 400)


def test_donation_add():
    '''
    Let's try to add money the right way
    '''
    donor = Donor('James Hetfield')
    donor.donation_add(400)

    assert donor.donations == [400]

    donor.donation_add(3000)
    assert donor.donations == [400, 3000]


def test_donation_count():
    '''
    Let's make sure I can count
    '''
    donor = Donor('Kirk Hammett')
    donor.donation_add(1400)
    assert donor.donation_count == 1

    donor.donation_add(2300)
    assert donor.donation_count == 2


def test_donation_total():
    '''
    Let's make sure I can add
    '''
    donor = Donor('Kirk Hammett')
    donor.donation_add(1400)
    donor.donation_add(2300)
    donor.donation_add(5400)
    assert donor.donation_total == 9100


def test_donation_avg():
    '''
    Testing if I can divide
    '''
    donor = Donor('Kirk Hammett')
    donor.donation_add(3000)
    donor.donation_add(700)
    donor.donation_add(5300)
    assert donor.donation_average == 3000


def test_letter():
    '''
    This is the one that I'm not confident over.  The formatting worries at me,
    it should work... but...
    '''
    donor = Donor('James Hetfield')
    donor.donation_add(1310)
    letter = donor.letter_template()
    date = datetime.datetime.now().strftime("%B %d, %Y")

    assert letter == f'{date} \n'\
    f'\nHello James Hetfield, \n'\
    f'\n'\
    f'We are writing to thank you for you generous donation\n'\
    f'to our foundation.  Your contributions for the year \n'\
    f'total $1,310.00 in 1 disbursements.'\
    f'\n'\
    f'\n'\
    f'Again, the foundation thanks you for your support, \n'\
    f'and we hope to remain in contact with you in this new \n'\
    f'year.\n'\
    f'\n'\
    f'Sincerely, \n'\
    f'Ecumenical Slobs LLC \n'


'''
Moving on to testing donor manipulation
'''
def test_init():
    '''
    Testing the init function
    '''
    testing = DonorCollection()
    assert testing.donors_dict == {'Robert Smith': [435.56, 125.23, 357.10],
                                   'JD Cronise': [123.12],
                                   'Chris Stapleton': [243.87, 111.32],
                                   'Dave Lombardo': [63.23, 422.87, 9432.01],
                                   'Randy Blythe': [223.50, 8120.32],
                                   'Devin Townsand': [431.12, 342.92, 5412.45],
                                  }


def test_donor_creation():
    '''
    Here, we create a donor
    '''
    testing = DonorCollection()
    testing.donor_creation('Kirk Hammett')

    assert 'Kirk Hammett' in testing.donors_dict
    assert testing.donors_dict['Kirk Hammett'].donations == []


def test_donor_list():
    '''
    Testing our listing function
    '''
    testing = DonorCollection()
    test_list = testing.list_donor()
    assert test_list == ['Chris Stapleton', 'Dave Lombardo', 'Devin Townsand', \
    'JD Cronise', 'Randy Blythe', 'Robert Smith']


def test_find_donor_exists():
    '''
    This is to test if it can find an existing donor
    '''
    testing = DonorCollection()
    assert testing.find_donor('JD Cronise') == testing.donors_dict["JD Cronise"]

def test_find_donor_nonexist():
    '''
    This tests creating a donor if one isn't already extant
    '''
    testing = DonorCollection()
    assert testing.find_donor('Kirk Hammett') == \
    testing.donors_dict['Kirk Hammett']

################################################################################
'''
cli_main.py testing
'''
################################################################################
