
typelist=[
    'INDI',
    'NAME',
    'SEX',
    'BIRT',
    'DEAT',
    'FAMS',
    'FAMC',
    'FAM',
    'MARR',
    'HUSB',
    'WIFE',
    'CHIL',
    'DIV',
    'DATE',
    'HEAD',
    'TRLR',
    'NOTE']

def checktype(linetypelist):
    try:
        if linetypelist[2] == 'FAM' or linetypelist[2] == 'INDI':
            linetype=linetypelist[2]
            arg = linetypelist[1]
        else:
            linetype=linetypelist[1]
            arg = " ".join(linetypelist[2:])
    except:
        linetype=linetypelist[1]
        arg = ''
    if linetype in typelist:
        return linetype+'|'+'Y'+'|'+arg 
    else:
        return linetype+'|'+'N'+'|'+arg 

with open('Khalid_GEDCOM.txt') as gedcom:
    for line in gedcom:
        splitline=line.strip().split()
        current = int(splitline[0])
        print ('--> {}'.format(line.strip()))
        print ('<-- {}'.format(splitline[0] +'|'+ checktype(splitline)))
