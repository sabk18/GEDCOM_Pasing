#user story 10
import unittest
import datetime
from datetime import datetime, timedelta


class MarriageAfterFourteen(unittest.TestCase):


    def test_checkifdateshavecorrectformat(self):
        result = testDates('false','incorrect')
        self.assertFalse(result)

    def test_checkifdatesarethesame(self):
        result = testDates(datetime.now(), datetime.now())
        self.assertFalse(result)

    def test_checkifmarriageisless(self):
        result = testDates(datetime.now(), datetime.now() - timedelta(days=14*365))
        self.assertFalse(result)

    def test_checkifmarriageismore(self):
        result = testDates(datetime.now(), datetime.now() + timedelta(days=14*365))
        self.assertTrue(result)

    def test_ifinputisnull(self):
        result = testDates(None, datetime.now() + timedelta(days=1))
        self.assertFalse(result)


def testDates(birth, marriage):
    if not isinstance(birth,datetime) or not isinstance(marriage, datetime):
        return False

    if marriage > birth :
        return True
    else:
        return False

def s10test(info,file):
    for indiv in info['INDI']:
        birth_date= info['INDI'][indiv]['BIRT']
<<<<<<< Updated upstream
        # bad smell 1 no marr date for any INDI id
        #if 'MARR' in info['INDI']:
        #    marriage_date= info['INDI'][indiv]['MARR']
        #    if not testDates(marriage_date):
        #        file.write("Error at MARR Date at INDI ID {0} ".format(indiv))
=======
        #bad smell 1 because there is no marriage info for individuals
        if 'MARR' in info['INDI']:
            marriage_date= info['INDI'][indiv]['MARR']
            if not testDates(marriage_date):
                file.write("Error at MARR Date at INDI ID {0} ".format(indiv))
>>>>>>> Stashed changes
        if not testDates(birth_date):
            file.write("Error at Birth Date at INDI ID{0}".format(indiv))
    for fam in info['FAM']:
        for fam in info['FAM']:
            if 'MARR' in info['FAM'][fam]:
                marriage_date= info['FAM'][fam]['MARR']
                if not testDates(marriage_date):
                    file.write("Error at MARR Date at FAM ID {0}".format(fam))
<<<<<<< Updated upstream
                # bad smell 2 no info about birth date in FAM id
                #if not testDates(birth_date):
                #    file.write("Error at Birth Date at FAM ID{0}".format(fam))
=======
                if not testDates(birth_date):
                    file.write("Error at Birth Date at FAM ID{0}".format(fam))
>>>>>>> Stashed changes
    return file

if __name__ == '__main__':
    unittest.main()
