from tabulate import tabulate
import unittest
import datetime
from datetime import datetime, timedelta
from datetime import date


class ageDifValidator(unittest.TestCase):

    def testfullinput(self):
        self.assertTrue(
            s34_run({'INDI': {1:{'BIRT':'17 OCT 2005'},2:{'BIRT':'17 OCT 2000'}},'FAM': {1: {'MAR': '17 OCT 2009', 'WIFE': 1, 'HUSB':2}}}, 1, True))

    def testtr(self):
        self.assertFalse(doubleAge(10,15))

    def testlarge(self):
        self.assertTrue(doubleAge(10,30))

    def testbad(self):
        self.assertFalse(doubleAge(10,11))

    def testAgeMar(self):
        self.assertTrue(ageAtMar('17 OCT 2000','19 OCT 2009')>=9)

    def testNull(self):
        self.assertFalse(doubleAge(None, None))


def doubleAge(value1, value2):
    try:
        return (value1/value2>=2 or value2/value1 >=2)
    except:
        return False
def ageAtMar(birthdate,marYear):  
    birthdate = datetime.strptime(birthdate, '%d %b %Y')           
    marDate =datetime.strptime(marYear, '%d %b %Y')
    age = marDate.year - birthdate.year  - ((marDate.month, marDate.day) < (birthdate.month, birthdate.day))
    return (age)

def s34_run(info, file, test=False):



    for fam in info['FAM']:
        wifeAge = ageAtMar(info['INDI'][info['FAM'][fam]['WIFE']]['BIRT'],info['FAM'][fam]['MAR'])
        husAge = ageAtMar(info['INDI'][info['FAM'][fam]['HUSB']]['BIRT'],info['FAM'][fam]['MAR'])
        if doubleAge(wifeAge,husAge):
            if test:
                return True
            file.write('{} Married at double the partners age'.format(fam))


    return file


if __name__ == '__main__':
    unittest.main()
