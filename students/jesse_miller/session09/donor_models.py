#!/usr/bin/env python3
'''
Let's try this by following the directions.  So, this is going to be where the
donor manipulation occurs.  The goal is to compartmentalize everything so that
functions can be called by other programs if and when needed.
'''

class DonorTools:
    '''
    So this class is implemented, however I never got any of the calls to work
    in the actual program, which is disappointing.
    '''
#
    def __init__(self, name):
        self.name = name
        self.donations = [] #?  We'll try it.
#
#
    def donation_add(self, new_donation):
        '''
        This should append donations to the list
        '''
        self.donations.append(new_donation)
#
    @property
    def donation_count(self):
        '''
        Fairly obvious, counts the number of donations
        '''
        return len(self.donations)
#
#
    @property
    def donation_total(self):
        '''
        Again, obvious, adds the donations up
        '''
        return sum(self.donations)
#
#
    @property
    def donation_average(self):
        '''
        Averages the donations
        '''
        return self.donation_total / self.donation_count
#

################################################################################
'''
End DonorTools
'''
################################################################################

class DonorCollection:
    '''
    This class will handle the donors dictionary, as well as the collections.
    Some of the things we can look forward to:
    Create a donor
    Find a donor
    List donors
    Donor reports
    Data saving and reloading.
    '''
    def __init__(self):
        '''
        Initializing and building the default dict
        '''


        self.donors_dict = {}

        self.donor_creation('Robert Smith')
        self.donor_creation('JD Cronise')
        self.donor_creation('Chris Stapleton')
        self.donor_creation('Dave Lombardo')
        self.donor_creation('Randy Blythe')
        self.donor_creation('Devin Townsand')
        self.donors_dict['Robert Smith'].donation_add(435.56)
        self.donors_dict['Robert Smith'].donation_add(125.23)
        self.donors_dict['Robert Smith'].donation_add(125.23)
        self.donors_dict['JD Cronise'].donation_add(125.23)
        self.donors_dict['Chris Stapleton'].donation_add(243.87)
        self.donors_dict['Chris Stapleton'].donation_add(111.32)
        self.donors_dict['Dave Lombardo'].donation_add(62.23)
        self.donors_dict['Dave Lombardo'].donation_add(422.87)
        self.donors_dict['Dave Lombardo'].donation_add(9432.01)
        self.donors_dict['Randy Blythe'].donation_add(223.50)
        self.donors_dict['Randy Blythe'].donation_add(8120.32)
        self.donors_dict['Devin Townsand'].donation_add(431.12)
        self.donors_dict['Devin Townsand'].donation_add(342.92)
        self.donors_dict['Devin Townsand'].donation_add(5412.45)


    def donor_creation(self, donor):
        '''
        Allows for adding new donors to the db
        '''
        new_donor = DonorTools(donor)
        self.donors_dict[donor] = new_donor
        return donor


    def list_donor(self):
        '''
        Listing the contents of the db
        '''
        donor_list = []
        for donor in self.donors_dict:
            donor_list.append(donor)
        sorted_donors = sorted(donor_list)
        return sorted_donors


    def find_donor(self, current_donor):
        '''
        This will take an inputed donor name, and search for it.  If the name
        isn't found, it will then bounce the request to the creation function.
        '''
        print(", ".join(self.donors_dict.keys()))
        return self.donors_dict[current_donor]


    def delete_donor(self, current_donor):
        '''
        This should allow for the removal of a donor from the dictionary
        '''
        del self.donors_dict[current_donor]
        return self.donors_dict


################################################################################
'''
End DonorCollection
'''
################################################################################
