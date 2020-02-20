import unittest
from datetime import datetime, timedelta


class marrDateValidator(unittest.TestCase):

    marrDate = datetime.now()
    divDate = datetime.now()

    def test_isdate(self):
        result = testDates('false', 'nope')
        self.assertFalse(result)

    def test_same(self):
        result = testDates(datetime.now(), datetime.now())
        self.assertFalse(result)

    def test_less(self):
        result = testDates(datetime.now(), datetime.now() - timedelta(days=1))
        self.assertFalse(result)

    def test_more(self):
        result = testDates(datetime.now(), datetime.now() + timedelta(days=1))
        self.assertTrue(result)

    def test_isNull(self):
        result = testDates(None, datetime.now() + timedelta(days=1))
        self.assertFalse(result)


def testDates(marr, div):
    if not isinstance(marr, datetime) or not isinstance(div, datetime):
        return False
    if marr < div:
        return True
    else:
        return False


def test(info, file):
    for fam in info['FAM']:
        if 'MARR' in info['FAM'][fam] and 'DIV' in info['FAM'][fam]:
            if not testDates(info['FAM'][fam]['MARR'],   info['FAM'][fam]['DIV']):
                write.file(
                    'Issue with {0} Family Marrige and Divorce Dates\n '.format(fam))
    return file


if __name__ == '__main__':
    unittest.main()
