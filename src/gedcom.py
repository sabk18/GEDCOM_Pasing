#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from tabulate import tabulate
import datetime
from datetime import date

# In[ ]:
# Create a dict to store data
info = {
    'FAM': {},
    'INDI': {}
}

# These are the fields that we need to track as per the first part of the assignment. Had to drop date to make
# collection function work.
typelist = [
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
    'HEAD',
    'TRLR',
    'NOTE']

currenttracker = '';


def create_collection(line, currenttracker):
    ''' Updates the dict and adds the values in. Structure is as follows
    info = {
        'FAM':{
            $ID:{
                'WIFE': $ID,
                'HUSB': $ID,
                'DIV': $DATE,
                'MAR': $DATE
            },
        },
        'INDI':{
            $ID:{
                'NAME': $NAME,
                'SEX': $SEC,
                'BIRT': $DATE,
                'DEAT': $DATE,
                'FAMS': $ID,
                'FAMC': $ID,
                'FAM': $ID,
            }
        }
    }'''
    global typelist
    global info
    if line[2] == 'FAM':
        info['FAM'][line[1]] = {}
        currenttracker = line[1]
        return currenttracker
    elif line[1] == 'DIV' or line[1] == 'MARR':
        info['FAM'][currenttracker][line[1]] = " ".join(line[2:])
    elif line[1] == 'WIFE' or line[1] == 'HUSB':
        info['FAM'][currenttracker][line[1]] = line[2]
    elif line[1] == 'CHIL':
        if 'CHIL' not in info['FAM'][currenttracker]:
            info['FAM'][currenttracker][line[1]] = []
        info['FAM'][currenttracker][line[1]].append(line[2])

    elif line[2] == 'INDI':
        info['INDI'][line[1]] = {}
        currenttracker = line[1]
        return currenttracker
    elif line[1] in typelist and currenttracker in info['INDI']:
        if line[1] == 'FAMC':
            if 'FAMC' not in info['INDI'][currenttracker]:
                info['INDI'][currenttracker]['FAMC'] = []
            info['INDI'][currenttracker]['FAMC'].append(" ".join(line[2:]))
        else:
            info['INDI'][currenttracker][line[1]] = " ".join(line[2:])
    return currenttracker


# In[2]:

def createoutput(file, new_file):
    global currenttracker

    # In[3]:

    lines = file.readlines()

    # In[4]:

    l1_tags = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHILL', 'DIV']
    l0_tags_1 = ['INDI', 'FAM']
    l0_tags_2 = ['HEAD', 'TRLR', 'NOTE']
    l2_tags = ['DATE']
    date_type = ['BIRT', 'MARR', 'DEAT', 'DIV']

    # In[5]:
    x = 0

    for line in lines:
        # print (line)

        line = line.strip()

        new_file.write("-->{}".format(line))
        new_file.write('\n')
        line = line.split(" ")
        if len(line) > 2:
            currenttracker = create_collection(line, currenttracker)
        elif line[1] in date_type:
            Nline = lines[x + 1].strip().split(' ')
            Nline[1] = line[1]
            currenttracker = create_collection(Nline, currenttracker)

        # print (line)
        level = line[0]
        # print (level)
        tags = line[1]
        # print (tags)
        arguments = line[2:]
        # print (arguments)
        arg_ = " ".join(arguments)

        if level == '1':
            if tags in l1_tags:
                new = 'Y'
                new_file.write(
                        "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(
                            arguments) + '\n')
                new_file.write('\n')
            else:
                new = 'N'
                new_file.write(
                        "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(
                            arguments) + '\n')
                new_file.write('\n')

        if level == '2':
            if tags in l2_tags:
                new = 'Y'
                new_file.write(
                        "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(
                            arguments) + '\n')
                new_file.write('\n')
            else:
                new = 'N'
                new_file.write(
                        "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(
                            arguments) + '\n')
                new_file.write('\n')
        if level == '3':
            new = 'N'
            new_file.write(
                    "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(arguments) + '\n')
            new_file.write('\n')
        if level == '0':

            if arg_ in l0_tags_1:
                new = 'Y'
                new_file.write(
                        "<--" + "".join(level) + "|" + "".join(arguments) + "|" + "".join(new) + "|" + "".join(
                            tags) + '\n')
                new_file.write('\n')
            else:
                if tags in l0_tags_2:
                    new = 'Y'
                    new_file.write("<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(
                            arguments) + '\n')
                    new_file.write('\n')
                else:
                    new = 'N'
                    new_file.write("<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(
                            arguments) + '\n')
                    new_file.write('\n')
        x += 1

    table = []
    for person in info['INDI']:
        row = [person,
               info['INDI'][person]['NAME'],
               info['INDI'][person]['SEX'],
               info['INDI'][person]['BIRT'], ]
        date_time_str = info['INDI'][person]['BIRT']
        date_time_obj = datetime.datetime.strptime(date_time_str, '%d %b %Y')
        row.append((date.today().year - date_time_obj.year - (
                (date.today().month, date.today().day) < (date_time_obj.month, date_time_obj.day))) + 1)
        if 'DEAT' in info['INDI'][person]:
            row.extend(['True', info['INDI'][person]['DEAT']])
        else:
            row.extend(['False', 'N/A'])
        if 'FAMC' in info['INDI'][person]:
            row.append(info['INDI'][person]['FAMC'])
        else:
            row.append('N/A')
        if 'FAMS' in info['INDI'][person]:
            row.append(info['INDI'][person]['FAMS'])
        else:
            row.append('N/A')
        table.append(row)
    print('Individaul')
    new_file.write('\nIndividaul\n')
    print(tabulate(table, headers=['ID', 'NAME', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse', ],
                   tablefmt="grid"))
    new_file.write(
            tabulate(table, headers=['ID', 'NAME', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse', ],
                     tablefmt="grid"))
    new_file.write('\nFamilies\n')
    print('Families')
    table = []
    for famId in info['FAM']:
        row = [famId]
        if 'MARR' in info['FAM'][famId]:
            row.append(info['FAM'][famId]['MARR'])
        else:
            row.append('N/A')
        if 'DIV' in info['FAM'][famId]:
            row.append(info['FAM'][famId]['DIV'])
        else:
            row.append('N/A')
        row.extend(
                [info['FAM'][famId]['HUSB'],
                 info['INDI'][info['FAM'][famId]['HUSB']]['NAME'],
                 info['FAM'][famId]['WIFE'],
                 info['INDI'][info['FAM'][famId]['WIFE']]['NAME']
                 ])
        if 'CHIL' in info['FAM'][famId]:
            row.append(info['FAM'][famId]['CHIL'])
        else:
            row.append('N/A')
        table.append(row)
    print(tabulate(table, headers=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name',
                                   'Children'], tablefmt="grid"))

    new_file.write(tabulate(table,
                            headers=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name',
                                     'Children'], tablefmt="grid"))

    return info, new_file
# In[ ]:


# In[ ]:
