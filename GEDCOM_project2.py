#!/usr/bin/env python
# coding: utf-8

# In[ ]:


File = open('Khalid_GEDCOM.txt')

# In[ ]:
# Create a dict to store data
info={
    'FAM':{},
    'INDI':{}

 }

 # These are the fields that we need to track as per the first part of the assigment. Had to drop date to make collection function work.
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
    'HEAD',
    'TRLR',
    'NOTE']

currenttracker='';

def createCollection(line,currenttracker):
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
        currenttracker=line[1]
        return currenttracker
    elif line[1] == 'DIV' or line[1] == 'MARR':
        info['FAM'][currenttracker][line[1]] = " ".join(line[2:])
    elif line[1] == 'WIFE' or line[1] == 'HUSB' or line[1] == 'CHIL':
        info['FAM'][currenttracker][line[1]] = line[2]
    elif line[2] == 'INDI':
        info['INDI'][line[1]] = {}
        currenttracker=line[1]
        return currenttracker
    elif line[1] in typelist and currenttracker in info['INDI']:
        info['INDI'][currenttracker][line[1]] = " ".join(line[2:])
    return currenttracker





# In[2]:


New_file = open("Gedcome_khalid_project02.txt","w")


# In[3]:


Lines = File.readlines()


# In[4]:


L1_tags = ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHILL','DIV']
L0_tags_1 =['INDI','FAM']
L0_tags_2 =['HEAD','TRLR','NOTE']
L2_tags =['DATE']
date_type =['BIRT','MARR','DEAT','DIV']

# In[5]:
x=0

for line in Lines:
#print (line)

    line = line.strip()

    New_file.write("-->{}".format(line))
    New_file.write('\n')
    line = line.split(" ")
    if len(line)>2:
        currenttracker=createCollection(line,currenttracker)
    elif line[1] in date_type:
        NewLine = Lines[x+1].strip().split(' ')
        NewLine[1] = line[1]
        currenttracker=createCollection(Newline,currenttracker)



    #print (line)
    level = line[0]
    #print (level)
    tags = line[1]
    #print (tags)
    arguments =line[2:]
    #print (arguments)
    arg_ = " ".join(arguments)

    if level == '1':
        if tags in L1_tags:
            new = 'Y'
            New_file.write("<--"+ "".join(level) + "|" + "".join(tags) + "|" +"".join(new)+ "|" + "".join(arguments)+'\n')
            New_file.write('\n')
        else:
            new ='N'
            New_file.write("<--"+ "".join(level) + "|" + "".join(tags) + "|" +"".join(new)+ "|" + "".join(arguments)+'\n')
            New_file.write('\n')

    if level == '2':
        if tags in L2_tags:
            new = 'Y'
            New_file.write("<--"+ "".join(level) + "|" + "".join(tags) + "|" +"".join(new)+ "|" + "".join(arguments)+'\n')
            New_file.write('\n')
        else:
            new ='N'
            New_file.write("<--"+ "".join(level) + "|" + "".join(tags) + "|" +"".join(new)+ "|" + "".join(arguments)+'\n')
            New_file.write('\n')
    #if level == '3':
       # new = 'N'
        #New_file.write("<--"+ "".join(level) + "|" + "".join(tags) + "|" +"".join(new)+ "|" + "".join(arguments)+'\n')
       # New_file.write('\n)
    #level 3 doesn't exist so it can just be treated as invalid input --> last part of the if statement
    if level =='0':

        if arg_ in L0_tags_1:
            new ='Y'
            New_file.write("<--"+ "".join(level) + "|" + "".join(arguments) + "|" +"".join(new)+ "|" + "".join(tags)+'\n')
            New_file.write('\n')
        else:
            if tags in L0_tags_2:
                new = 'Y'
                New_file.write("<--"+ "".join(level) + "|" + "".join(tags) + "|" +"".join(new)+ "|" + "".join(arguments)+'\n')
                New_file.write('\n')
            else:
                new = 'N'
                New_file.write("<--"+ "".join(level) + "|" + "".join(tags) + "|" +"".join(new)+ "|" + "".join(arguments)+'\n')
                New_file.write('\n')
    else:
        new = 'Invalid Input'
        New_file.write("<--"+ "".join(level) + "|" + "".join(tags) + "|" +"".join(new)+ "|" + "".join(arguments)+'\n')
                New_file.write('\n')
    x+=1
New_file.close()


# In[ ]:




# In[ ]:
