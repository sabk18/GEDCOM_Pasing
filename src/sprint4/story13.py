from tabulate import tabulate
import unittest
import datetime
from datetime import datetime
from datetime import date



class BirthSpacingValidator(unittest.TestCase):

    def testNull(self):
        self.assertFalse(getDays(None))


def getDays(date):
    try:
        return ((datetime.today()-datetime.strptime(date, '%d %b %Y'))).days
    except:
        return 0


def s13_run(info, file, test=False):

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
        sibs = sorted(fams[fam], key=lambda i: i['DAYS'], reverse=True)
        for sib in sibs:
            for sib2 in sibs:
                if sib != sib2:
                    if not sib['DAYS'] > sib2['DAYS'] + timedelta(days=8*30) or sib['DAYS'] <= sib2['DAYS'] + timedelta(days=2)  :
                        table.append([sib['ID'], info['INDI'][sib['ID']]['NAME'],sib2['ID'], info['INDI'][sib2['ID']]['NAME']])
        print(table)
        file.write(tabulate(table, headers=['PERSON 1 ID' ,'PERSON 1 NAME','PERSON 2 ID','PERSON 2 NAME' ], tablefmt="grid"))
    return file


if __name__ == '__main__':
    unittest.main()
