#!/usr/bin/env python3
'''
This is the command interface for the mailroom.  Now that I know that donor
manipulations work correctly (At least according to pytest.  I mean, I wrote
the tests so the likelihood of human error here is high, you know?).
'''
import os
import datetime
'''
Module imports
'''
class MailBox:
    '''
    Sending mail and directory writing functions
    '''
    @staticmethod
    def letter_template(donor, total, count):
        '''
        This is the template for the mail to write to screen and file
        '''
        date = datetime.datetime.now().strftime('%B %d, %Y')
        template = f'{date} \n'\
        f'\nHello {donor}, \n' \
        f'\n'\
        f'We are writing to thank you for you generous donation\n'\
        f'to our foundation.  Your contributions for the year \n'\
        f'total ${total:,.2f} in {count} disbursements.'\
        f'\n'\
        f'\n'\
        f'Again, the foundation thanks you for your support, \n'\
        f'and we hope to remain in contact with you in this new \n'\
        f'year.\n'\
        f'\n'\
        f'Sincerely, \n'\
        f'Ecumenical Slobs LLC \n'
        return template


    @staticmethod
    def mail_send(donor_tools, donor):
        '''
        This function now contains both the terminal and the file mails.  It
        acts on an individual donor, and allows another function to loop all.
        '''
        path = os.getcwd()
        directory = path + '/donors/' + donor + '/'
        filename = donor + ' - ' \
                    + datetime.datetime.now().strftime('%s') + '.txt'

        MailBox.mail_format(donor_tools[donor].name, \
        sum(donor_tools[donor].donations), len(donor_tools[donor].donations), \
        directory, filename)
        '''
        Sending to file creation below
        '''
        print(MailBox.letter_template(donor_tools[donor].name, \
        sum(donor_tools[donor].donations), len(donor_tools[donor].donations)))
        '''
        Printing to terminal
        '''

    @staticmethod
    def mail_send_all(donor_tools):
        '''
        This function now contains the loop for all mails.
        '''
        for k in donor_tools:
            MailBox.mail_send(donor_tools, k)


    @staticmethod
    def mail_send_one(donor_tools, donor):
        '''
        This should send a single mail, however there's an iteration for some
        reason, filing this as a bug that I'll need to address in the future.
        '''
        if donor in donor_tools:
            MailBox.mail_send(donor_tools, donor)


    @staticmethod
    def mail_format(donor_name, donor_total, donor_count, directory, filename):
        '''
        This is the formating for the mail print and file.  This allows us to
        have both files and terminal output for single donors as well as multiple
        '''
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(directory + filename, 'w+') as outfile:
            outfile.write('{}\n'.format(MailBox.letter_template\
            (donor_name, donor_total, donor_count)))
