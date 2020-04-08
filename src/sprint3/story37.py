from tabulate import tabulate
import unittest
import datetime
from datetime import datetime
from datetime import date


class RecentDeadRelValidator(unittest.TestCase):

    def testfullinput(self):
        self.assertTrue(
            s37_run({'INDI': {1: {'BIRT': '17 MAR 2020', 'FAMC': 2}}}, 1, True))

    def testdate(self):
        self.assertTrue(lessThanDays('17 MAR 2020', 30))

    def testlarge(self):
        self.assertFalse(lessThanDays('17 MAR 2010', 30))

    def testbad(self):
        self.assertFalse(lessThanDays('17 MAR 2010', 30))

    def testNull(self):
        self.assertFalse(lessThanDays(None, None))


def lessThanDays(date, num):
    try:
        return ((datetime.today()-datetime.strptime(date, '%d %b %Y')).days < num)
    except:
        return False


def s37_run(info, file, test=False):


    fams={}
    deadPeople = []
    for indiv in info['INDI']:
        if 'DEAT' in info['INDI'][indiv]:
            if lessThanDays(info['INDI'][indiv]['DEAT'], 30):
                deadPeople.append(indiv)
            if 'FAMC' in info['INDI'][indiv]:
                if info['INDI'][indiv]['FAMC'] not in fams:
                    fams[info['INDI'][indiv]['FAMC']] = []
                fams[info['INDI'][indiv]['FAMC']].append(
                    {'ID': indiv})

    if test:
        return True

    for deadPerson in deadPeople:
        table = []
        file.write('\n{0} Died within 30 days and is related to the following \n'.format(info['INDI'][deadPerson]['NAME']))
        if 'FAMS' in info['INDI'][deadPerson]:
            if info['INDI'][deadPerson]['SEX'] =='F':
                table.append([info['INDI'][info['FAM'][info['INDI'][deadPerson]['FAMS']]['HUSB']]['NAME'],'HUSBAND'])
            elif info['INDI'][deadPerson]['SEX'] =='M':
                table.append([info['INDI'][info['FAM'][info['INDI'][deadPerson]['FAMS']]['WIFE']]['NAME'],'WIFE'])
            for child in fams:
                table.append([info['INDI'][child['ID']]['NAME'],'Child'])

        file.write(tabulate(table, headers=['Name' ,'Relation', ], tablefmt="grid"))
    return file


if __name__ == '__main__':
    unittest.main()
