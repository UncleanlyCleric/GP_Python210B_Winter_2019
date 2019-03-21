#!/usr/bin/env python3
'''
This is the command interface for the mailroom.  Now that I know that donor
manipulations work correctly (At least according to pytest.  I mean, I wrote
the tests so the likelihood of human error here is high, you know?).
'''
import sys
from donor_models import DonorCollection
from mail_box import MailBox
'''
Module imports
'''

#pylint: disable=C0103
alms = DonorCollection()

'''
Because my sense of humor is odd, that's why.  Also setting an object
'''

class MailRoom:
    '''
    All the calls and commands will be through this class.  Manipulation of
    donor information is done in donor_models.py, and all of the execution for
    this subprogram is from mailroom_oo.py
    '''
    @staticmethod
    def list_donors():
        '''
        Lists existing donors.
        '''
        print(f"\n{'-'*15}\nList of Donors:\n{'-'*15}")
        current = alms.list_donor()
        for donor in current:
            print(donor)
        print(f"{'-'*15}\n")


    @staticmethod
    def print_report():
        '''
        I couldn't get this to work at first, however starting with an empty
        dictionary and populating it manually worked.
        '''
        headers = ['Donor Name', 'Total Given', 'Times Donated', 'Average Gift']
        print(f"'\n{'-'*80}\n{{:17}} | {{:<19}} | {{:<15}} | {{:<19}}\n{'-'*80}"\
        .format(headers[0], headers[1], headers[2], headers[3]))

        donor_data = alms.donors_dict
        for donor in donor_data:
            print('{:17} | ${:<18,.2f} | {:<15} | ${:<16,.2f}'.format\
            (donor_data[donor].name, sum(donor_data[donor].donations), \
            len(donor_data[donor].donations), sum(donor_data[donor].donations)/\
            len(donor_data[donor].donations)))
        print(f"{'-'*80}\n")


    @staticmethod
    def donor_mail_choice():
        '''
        This section allows the user to mail a donor
        '''
        donor_tools = alms.donors_dict
        MailRoom.list_donors()
        try:
            donor = str(input('Who would you like to mail (all for all): '))
            if donor == 'all':
                MailBox.mail_send_all(donor_tools)
            else:
                try:
                    donor_tools = alms.find_donor(donor)
                    MailBox.mail_send_one(donor_tools, donor)
                except KeyError:
                    print("Not found")
        except (KeyboardInterrupt, EOFError, ValueError):
            MailRoom.safe_input()


    @staticmethod
    def safe_input():
        '''
        This will be for handling keyboard exceptions
        '''
        return None


    @staticmethod
    def goodbye():
        '''
        Gracefully exits
        '''
        print('Goodbye!')
        sys.exit()


    @staticmethod
    def donor_del():
        '''
        This section allows the user to delete a donor
        '''
        try:
            MailRoom.list_donors()
            del_donor = str(input('Enter the name of the donor to remove: '))
            del alms.donors_dict[del_donor]
            MailRoom.list_donors()
        except (KeyboardInterrupt, EOFError, ValueError):
            MailRoom.safe_input()


    @staticmethod
    def donor_add():
        '''
        This section allows the user to add a donor
        '''
        try:
            MailRoom.list_donors()
            donor = str(input('Enter the name of the donor to add: '))
            alms.donor_creation(donor)
            while True:
                d_num = int(input('How many donations were made (3 or less): '))
                try:
                    d_num = int(d_num)
                except ValueError:
                    del alms.donors_dict[donor]
                    return False
                if d_num >= 3:
                    print('No more than 3 donations')
                    del alms.donors_dict[donor]
                    return False
                while d_num > 0:
                    donations = float(input('Enter their donation: '))
                    if donations < 0:
                        print('\nMust be a positive number\n')
                        continue
                    '''
                    Forcing donation to be positive
                    '''
                    alms.donors_dict[donor].donation_add(donations)
                    d_num -= 1
                break
            MailRoom.list_donors()
        except (KeyboardInterrupt, EOFError, ValueError):
            MailRoom.safe_input()

################################################################################
'''
End MailRoom
'''
################################################################################

class Menus(MailRoom):
    '''
    Menuing class, for those paying attention at home.  This is where the
    menu system resides, in case it needs tweeking.
    '''

    prompt = '\n'.join(('Welcome to mailroom 1.0!',
                        '',
                        'Please choose from below options:',
                        'list   - Display a list of donors.',
                        'report - Display a report of donation totals.',
                        'send   - Generate letters to send to donors.',
                        'add    - Add a new donor.',
                        'delete - Remove a donor',
                        'quit   - Exit.',
                        '>>> '))

    valid_input = ('report', 'quit', 'list', 'send', 'all', 'delete', 'add')


    menu_choice = {'report': MailRoom.print_report,
                   'list': MailRoom.list_donors,
                   'send': MailRoom.donor_mail_choice,
                   'add' : MailRoom.donor_add,
                   'delete': MailRoom.donor_del,
                   'quit': MailRoom.goodbye
                  }

    @staticmethod
    def main():
        '''
        The main menu and the calls to other functions.
        '''
        while True:
            try:
                response = input(Menus.prompt)
            except (KeyboardInterrupt, EOFError):
                continue
            if response not in Menus.valid_input:
                print('\nERROR: Invalid option')
                continue
            Menus.menu_choice[response]()


################################################################################
'''
End Menus
'''
################################################################################
