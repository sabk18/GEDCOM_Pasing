import unittest
from datetime import datetime, timedelta, date


class marrDateValidator(unittest.TestCase):


    def test_isdate(self):
        result = s7test({'INDI':{1:{'BIRT':'10 FEB 2020'}}}, 'TEST')
        self.assertTrue(result)




def s7test(info, file):
    for ind in info['INDI']:
        today = date.today() 
        birthDate = datetime.strptime(info['INDI'][ind]['BIRT'] , '%d %b %Y')
        age = today.year - birthDate.year - ((today.month, today.day) < 
            (birthDate.month, birthDate.day))
        if age >= 150:
            if file=='TEST':
                return False
            file.write(
                    'Issue with {0} | Age is over 150\n '.format(fam))
        if file=="TEST":
            return True

    return file


if __name__ == '__main__':
    unittest.main()
