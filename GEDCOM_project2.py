#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from _ast import Tuple
from datetime import date
import fileToDicts

import pandas as pd
from dateutil.relativedelta import relativedelta
from pandas.compat import parse_date

File = open('Khalid_GEDCOM.txt')

# In[ ]:
# Create a dict to store data
info = {
    'FAM': {},
    'INDI': {}

}

# These are the fields that we need to track as per the first part of the assigment. Had to drop date to make collection function work.
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


def createCollection(line, currenttracker):
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
    if line[2] == 'FAM':
        info['FAM'][line[1]] = {}
        currenttracker = line[1]
        return currenttracker
    elif line[1] == 'DIV' or line[1] == 'MARR':
        info['FAM'][currenttracker][line[1]] = " ".join(line[2:])
    elif line[1] == 'WIFE' or line[1] == 'HUSB' or line[1] == 'CHIL':
        info['FAM'][currenttracker][line[1]] = line[2]
    elif line[2] == 'INDI':
        info['INDI'][line[1]] = {}
        currenttracker = line[1]
        return currenttracker
    elif line[1] in typelist and currenttracker in info['INDI']:
        info['INDI'][currenttracker][line[1]] = " ".join(line[2:])
    return currenttracker


# In[2]:


New_file = open("Gedcome_khalid_project02.txt", "w")

# In[3]:


Lines = File.readlines()

# In[4]:


L1_tags = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHILL', 'DIV']
L0_tags_1 = ['INDI', 'FAM']
L0_tags_2 = ['HEAD', 'TRLR', 'NOTE']
L2_tags = ['DATE']
date_type = ['BIRT', 'MARR', 'DEAT', 'DIV']

# In[5]:
x = 0

for line in Lines:
    # print (line)

    line = line.strip()

    New_file.write("-->{}".format(line))
    New_file.write('\n')
    line = line.split(" ")
    if len(line) > 2:
        currenttracker = createCollection(line, currenttracker)
    elif line[1] in date_type:
        Nline = Lines[x + 1].strip().split(' ')
        Nline[1] = line[1]
        currenttracker = createCollection(Nline, currenttracker)

    # print (line)
    level = line[0]
    # print (level)
    tags = line[1]
    # print (tags)
    arguments = line[2:]
    # print (arguments)
    arg_ = " ".join(arguments)

    if level == '1':
        if tags in L1_tags:
            new = 'Y'
            New_file.write(
                "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(arguments) + '\n')
            New_file.write('\n')
        else:
            new = 'N'
            New_file.write(
                "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(arguments) + '\n')
            New_file.write('\n')

    if level == '2':
        if tags in L2_tags:
            new = 'Y'
            New_file.write(
                "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(arguments) + '\n')
            New_file.write('\n')
        else:
            new = 'N'
            New_file.write(
                "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(arguments) + '\n')
            New_file.write('\n')
    if level == '3':
        new = 'N'
        New_file.write(
            "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(arguments) + '\n')
        New_file.write('\n')
    if level == '0':

        if arg_ in L0_tags_1:
            new = 'Y'
            New_file.write(
                "<--" + "".join(level) + "|" + "".join(arguments) + "|" + "".join(new) + "|" + "".join(tags) + '\n')
            New_file.write('\n')
        else:
            if tags in L0_tags_2:
                new = 'Y'
                New_file.write(
                    "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(arguments) + '\n')
                New_file.write('\n')
            else:
                new = 'N'
                New_file.write(
                    "<--" + "".join(level) + "|" + "".join(tags) + "|" + "".join(new) + "|" + "".join(arguments) + '\n')
                New_file.write('\n')
    x += 1
New_file.close()

indivs_columns = ['ID', 'NAME', 'GENDER', 'BIRTHDAY', 'AGE', 'AGE_in_days', 'ALIVE', 'DEATH', 'CHILD', 'SPOUSE']
fams_columns = ['ID', 'MARRIED', 'DIVORCED', 'HUSBAND ID', 'HUSBAND NAME', 'WIFE ID', 'WIFE NAME', 'CHILDREN']


def parseFileToDFs(filename: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    indivs, families = fileToDicts.parseFile(filename)
    indivs_df = pd.DataFrame(indivs)
    families_df = pd.DataFrame(families)

    if indivs_df.empty:
        indivs_df = pd.DataFrame(columns=indivs_columns)
    else:
        # Add missing columns
        for col in indivs_columns:
            if col not in indivs_df.columns:
                indivs_df[col] = pd.np.nan
        # Calculate age
        indivs_df['AGE'] = [None if pd.isna(birth) else
                            relativedelta(date.today() if pd.isna(death) else parse_date(death),
                                          parse_date(birth)).years
                            for birth, death in zip(indivs_df['BIRTHDAY'], indivs_df['DEATH'])]
        indivs_df['AGE_in_days'] = [None if pd.isna(birth) else
                                    ((date.today() if pd.isna(death) else parse_date(death).date()) - parse_date(
                                        birth).date()).days
                                    for birth, death in zip(indivs_df['BIRTHDAY'], indivs_df['DEATH'])]
        # Calculate alive
        indivs_df['ALIVE'] = [pd.isna(death) or parse_date(death).date() > date.today()
                              for death in indivs_df['DEATH']]
        # Reorder columns
        indivs_df = indivs_df[indivs_columns]

    if families_df.empty:
        families_df = pd.DataFrame(columns=fams_columns)
    else:
        # Add missing columns
        for col in fams_columns:
            if col not in families_df:
                families_df[col] = pd.np.nan
        # Reorder columns
        families_df = families_df[fams_columns]

    return indivs_df, families_df

# In[ ]:


# In[ ]:
