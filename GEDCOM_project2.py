#!/usr/bin/env python
# coding: utf-8

# In[ ]:


File = open('Khalid_GEDCOM.txt')


# In[2]:


New_file = open("Gedcome_khalid_project02.txt","w")


# In[3]:


Lines = File.readlines()


# In[4]:


L1_tags = ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHILL','DIV']
L0_tags_1 =['INDI','FAM']
L0_tags_2 =['HEAD','TRLR','NOTE']
L2_tags =['DATE']


# In[5]:


for line in Lines:  
#print (line)

    line = line.strip()
    New_file.write("-->{}".format(line))
    New_file.write('\n')
    line = line.split(" ")
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
    if level == '3':
        new = 'N' 
        New_file.write("<--"+ "".join(level) + "|" + "".join(tags) + "|" +"".join(new)+ "|" + "".join(arguments)+'\n')
        New_file.write('\n')
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
New_file.close()


# In[ ]:





# In[ ]:




