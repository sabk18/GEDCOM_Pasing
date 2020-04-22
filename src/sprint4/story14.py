from tabulate import tabulate
import unittest
import datetime
from datetime import datetime
from datetime import date


<<<<<<< Updated upstream
class MultipleBirthsValidator(unittest.TestCase):
=======
class TwingValidator(unittest.TestCase):

    def testfullinput(self):
        self.assertTrue(s32_run({'INDI': {1: {'BIRT': '15 MAR 2010', 'FAMC': 2}, 2: {
                        'BIRT': '15 MAR 2010', 'FAMC': 2}}}, 1, True))

    def testdate(self):
        self.assertTrue(getDays('17 MAR 2020') < 30)

    def testlarge(self):
        self.assertTrue(getDays('15 MAR 2010') > 30)

    def testbad(self):
        self.assertFalse(getDays('14 MAR 201') > 30)
>>>>>>> Stashed changes

    def testNull(self):
        self.assertFalse(getDays(None))


def getDays(date):
    try:
        return ((datetime.today()-datetime.strptime(date, '%d %b %Y'))).days
    except:
        return 0


<<<<<<< Updated upstream
def s14_run(info, file, test=False):
=======
def s32_run(info, file, test=False):
>>>>>>> Stashed changes

    fams = {}
    for indiv in info['INDI']:
        if 'FAMC' in info['INDI'][indiv]:
            if info['INDI'][indiv]['FAMC'] not in fams:
                fams[info['INDI'][indiv]['FAMC']] = []
            fams[info['INDI'][indiv]['FAMC']].append(
                {'ID': indiv, 'DAYS': getDays(info['INDI'][indiv]['BIRT'])})

    if test:
        print(fams)
        return True
    for fam in fams:
        table = []
<<<<<<< Updated upstream
        file.write('\nMultiple Births in {0} Family\n'.format(fam))
=======
        file.write('\nTwins in {0} Family\n'.format(fam))
>>>>>>> Stashed changes
        sibs = sorted(fams[fam], key=lambda i: i['DAYS'], reverse=True)
        for sib in sibs:
            for sib2 in sibs:
                if sib != sib2:
                    if sib['DAYS'] == sib2['DAYS']:
                        table.append([sib['ID'], info['INDI'][sib['ID']]['NAME'],sib2['ID'], info['INDI'][sib2['ID']]['NAME']])
<<<<<<< Updated upstream
                for sib2 in sibs& sib3 in sibs:
                    if sib != sib3 & sib2 != sib3:
                        if sib['DAYS'] == sib3['DAYS'] & sib2['DAYS'] == sib3['DAYS']:
                            table.append([sib['ID'], info['INDI'][sib['ID']]['NAME'],sib2['ID'], info['INDI'][sib2['ID']]['NAME'],sib3['ID'], info['INDI'][sib3['ID']]['NAME']])
                    for sib2 in sibs& sib3 in sibs& sib4 in sibs:
                        if sib != sib4 & sib2 != sib4 & sib3 != sib4:
                            if sib['DAYS'] == sib4['DAYS'] & sib2['DAYS'] == sib4['DAYS']  & sib3['DAYS'] == sib4['DAYS'] :
                                table.append([sib['ID'], info['INDI'][sib['ID']]['NAME'],sib2['ID'], info['INDI'][sib2['ID']]['NAME'],sib3['ID'], info['INDI'][sib3['ID']]['NAME'],sib4['ID'], info['INDI'][sib4['ID']]['NAME']])
                        for sib2 in sibs& sib3 in sibs& sib4 in sibs& sib5 in sibs:
                            if sib != sib5 & sib2 != sib5 & sib3 != sib5 & sib4 != sib5 :
                                if sib['DAYS'] == sib5['DAYS'] & sib2['DAYS'] == sib5['DAYS'] & sib3['DAYS'] == sib5['DAYS'] & sib4['DAYS'] == sib5['DAYS']:
                                    table.append([sib['ID'], info['INDI'][sib['ID']]['NAME'],sib2['ID'], info['INDI'][sib2['ID']]['NAME'],sib3['ID'], info['INDI'][sib3['ID']]['NAME'],sib4['ID'], info['INDI'][sib4['ID']]['NAME'],sib5['ID'], info['INDI'][sib5['ID']]['NAME']])
        if sibs < 6:
            file.write('\nThere are not too many births in {0} Family at once\n'.format(fam))
        if sibs > 6:
            file.write('\nThere are too many births in {0} Family at once\n'.format(fam))
        print(table)
        file.write(tabulate(table, headers=['PERSON 1 ID' ,'PERSON 1 NAME','PERSON 2 ID','PERSON 3 NAME','PERSON 3 ID','PERSON 4 NAME','PERSON 4 ID','PERSON 5 NAME','PERSON 5 ID' ], tablefmt="grid"))
=======
        print(table)
        file.write(tabulate(table, headers=['PERSON 1 ID' ,'PERSON 1 NAME','PERSON 2 ID','PERSON 2 NAME' ], tablefmt="grid"))
>>>>>>> Stashed changes
    return file


if __name__ == '__main__':
    unittest.main()