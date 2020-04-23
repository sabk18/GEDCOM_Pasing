from tabulate import tabulate
import unittest
import datetime
from datetime import datetime
from datetime import date

class MultipleBirthsValidator(unittest.TestCase):

    def testfullinput(self):
        self.assertTrue(s14_run({'INDI': {1: {'BIRT': '17 MAR 2020', 'FAMC': 2}, 2: {
                        'BIRT': '17 MAR 2010', 'FAMC': 2}}}, 1, True))

    def testdate(self):
        self.assertFalse(getDays('17 MAR 2020') < 30)

    def testlarge(self):
        self.assertTrue(getDays('17 MAR 2010') > 30)

    def testbad(self):
        self.assertFalse(getDays('17 MAR 201') > 30)

    def testNull(self):
        self.assertFalse(getDays(None))



def getDays(date):
    try:
        return ((datetime.today()-datetime.strptime(date, '%d %b %Y'))).days
    except:
        return 0


def s14_run(info, file, test=False):
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
        file.write('\nTwins in {0} Family\n'.format(fam))
        samelist=[]
        sibs = sorted(fams[fam], key=lambda i: i['DAYS'], reverse=True)
        for sib in sibs:
            for sib2 in sibs:
                if sib != sib2:
                    if sib['DAYS'] == sib2['DAYS']:
                        if sib2 not in samelist:
                            samelist.append(sib2)
        if len(samelist)>=5:
            file.write('{} Family has 5 children born on same day!!')
    return file
if __name__ == '__main__':
    unittest.main()
