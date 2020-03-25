import unittest
from datetime import datetime, timedelta, date


class marrDateValidator(unittest.TestCase):


    def test_ismore(self):
        result = s8test({'INDI':{1:{'BIRT':'10 FEB 2020','FAMC':2}},'FAM':{2:{'MARR':'1 FEB 2020'}}}, 'TEST')
        self.assertFalse(result)




def s8test(info, file):
    for ind in info['INDI']:
        birthDate = datetime.strptime(info['INDI'][ind]['BIRT'] , '%d %b %Y')

        if 'FAMC' in info['INDI'][ind]:
            marrDate= datetime.strptime(info['FAM'][info['INDI'][ind]['FAMC']]['MARR'] , '%d %b %Y')
            if birthDate > marrDate:
                if file=='TEST':
                    return False
                file.write(
                    'Issue with {0} | Age is over 150\n '.format(fam))
            if file=="TEST":
                return True

    return file


if __name__ == '__main__':
    unittest.main()
