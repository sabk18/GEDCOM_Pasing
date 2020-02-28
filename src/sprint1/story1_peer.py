
import unittest
import datetime
from datetime import datetime, timedelta


def testDates(input_date):

    input_date = datetime.strptime(input_date, '%d %b %Y')
    currentDate =datetime.now()
    if input_date <= currentDate:
        return True
    else:
        return False


def s1test(info, file):
    for indiv in info['INDI']:
        birth_date= info['INDI'][indiv]['BIRT']
        if 'DEAT' in info['INDI']:
            death_date= info['INDI'][indiv]['DEAT']
            if not testDates(death_date):
                file.write("Error at DEAT Date at INDI ID {0} ".format(indiv))
        if not testDates(birth_date):
            file.write("Error at Birth DATEat INDI ID{0}".format(indiv))


    for fam in info['FAM']:
        if 'MARR' in info['FAM'][fam]:
            marriage_date= info['FAM'][fam]['MARR']
            if not testDates(marriage_date):
                file.write("Error at MARR Date at FAM ID {0}".format(fam))
        if 'DIV'in info ['FAM'][fam]:
            divorce_date= info['FAM'][fam]['DIV']
            if not testDates(divorce_date):
                file.write("Error at DIV Date at FAM ID {0}".format(fam))
    return file
