import unittest
import datetime
from datetime import datetime, timedelta


class BirthBeforeMarriage(unittest.TestCase):
    def test_checkifmarriageisless(self):
        result = testDates(datetime.now(), datetime.now() - timedelta(days=1))
        self.assertFalse(result)

def testDates(birth, marriage):
    if not isinstance(birth,datetime) or not isinstance(marriage, datetime):
        return False

    if marriage > birth :
        return True
    else:
        return False

def s2test(info,file):
    for indiv in info['INDI']:
        birth_date= info['INDI'][indiv]['BIRT']
        if 'MARR' in info['INDI']:
            marriage_date= info['INDI'][indiv]['MARR']
            if not testDates(marriage_date):
                file.write("Error at MARR Date at INDI ID {0} ".format(indiv))
        if not testDates(birth_date):
            file.write("Error at Birth Date at INDI ID{0}".format(indiv))
    for fam in info['FAM']:
        for fam in info['FAM']:
            if 'MARR' in info['FAM'][fam]:
                marriage_date= info['FAM'][fam]['MARR']
                if not testDates(marriage_date):
                    file.write("Error at MARR Date at FAM ID {0}".format(fam))
                if not testDates(birth_date):
                   file.write("Error at Birth Date at FAM ID{0}".format(fam))
    return file

if __name__ == '__main__':
    unittest.main()
