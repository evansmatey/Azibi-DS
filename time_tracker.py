#!/usr/bin/env python
# coding: utf-8

# In[14]:


import datetime
import time 
import pandas as pd
import numpy as np


a, b, c, d ,e = (2020,7,30,10,20)


# In[2]:


x = datetime.datetime(a,b,c,d,e)
y = datetime.datetime(2020,7,31,13,10)


# In[3]:


c = y-x


# In[4]:


c = c.total_seconds()


# In[5]:


c = int(float(str(c)))


# In[6]:


c = float(c)
c = int(c)


# In[6]:


c


# In[11]:


import time
sec = 95400
ty_res = time.gmtime(sec)
res = time.strftime("%H:%M:%S",ty_res)
print(res)


# In[21]:


import datetime
sec = 1000
res = datetime.timedelta(seconds =c)
print(res)


# In[20]:


duration = datetime.timedelta(c)


# In[10]:


duration


# In[ ]:


x.time()


# In[ ]:


strr = '9/15/18/10/30/30'
strr1 = '9/15/18/17/30/30'


# In[ ]:


strr


# In[ ]:


dt = datetime.datetime.strptime(strr, '%m/%d/%y/%H/%M/%S')
dt1 = datetime.datetime.strptime(strr1, '%m/%d/%y/%H/%M/%S')


# In[12]:


def time_tracker(starttime, endtime, wageperhour = 5):
    '''
    @time_tracker is a function that can be used to calculate the money earned when working.
    this function accepts tuple objects nothing else in the form '9/15/18/10/30' month/day/year/hour/minute in this 
    order nothing else
    '''
    eyear, emon, eday, ehour, emin = endtime     #tuple unpacking the arguments 
    syear, smon, sday, shour, smin = starttime
    
    st = datetime.datetime(syear, smon, sday, shour, smin)     #convert the stings into datetime object
    et = datetime.datetime(eyear, emon, eday, ehour, emin) 
    # calculating the differences between the start time and the end time 2
    wt =  et - st 
    wts = wt.total_seconds()     # converting the total time worked into seconds for eazy calculation
    ttw = int(float(str(wts)))     # convert the total time worked in seconds into integer
    duration = datetime.timedelta(seconds = ttw)     #converting the total seconds works into a date-time format
    divider = 3600
    total_earned = float((wts/divider)* wageperhour)     #calculating the money earned and converting the value into a float
    print('you worked for {} and earned {}{:.2f}{}'.format(duration,'$',total_earned,'dollars'))     #using the .string format method
    
#Alert:
# This my addition to the code to create a CSV file...

import datetime
import time 
import csv
f = open('people.csv','a', newline = '')
start = tuple(map(int, (input('Enter the start date of the task in this order;Year,Month,Day,Hour,Minute: ').split(','))))
end = tuple(map(int, (input('Enter the end date of the task in this order;Year,Month,Day,Hour,Minute: ').split(','))))
def time_tracker(starttime, endtime, wageperhour = 5):
    '''
    @time_tracker is a function that can be used to calculate the money earned when working.
    this function accepts tuple objects nothing else in the form '9/15/18/10/30' month/day/year/hour/minute in this 
    order nothing else
    '''
    eyear, emon, eday, ehour, emin = endtime     #tuple unpacking the arguments 
    syear, smon, sday, shour, smin = starttime
    
    st = datetime.datetime(syear, smon, sday, shour, smin)     #convert the stings into datetime object
    et = datetime.datetime(eyear, emon, eday, ehour, emin) 
    # calculating the differences between the start time and the end time 2
    wt =  et - st 
    divider = 3600
    wts = wt.total_seconds()     # converting the total time worked into seconds for eazy calculation
    ttw = int(float(str(wts)))     # convert the total time worked in seconds into integer
    hr = ttw // divider             # convert to hours
    total_earned = float((wts/divider)* wageperhour)     #calculating the money earned and converting the value into a float
    print('You worked for {} hours and earned {}{:.2f}{}'.format(hr,'$',total_earned,'dollars'))     #using the .string format method
    return hr, total_earned
end_result = time_tracker(start, end)
writer =csv.writer(f)
writer.writerow(['Hours_worked', 'Salary'])
writer.writerow(end_result)

f.close()

# In[43]:


start = 2020,7,30,8,20
end =  2020,7,31,12,30
ll = [[start, end, 5]]
time_tracker(start, end, 20)


# In[44]:


def save_time_tracker_details( eyear, emon, eday, ehour, emin, syear, smon, sday, shour,
                              smin , wageperhour, totalwage, totaltime):
    
    """
    @save_time_tracker_details is a simple function that just saves the data generated form the time_tracker fuction 
    in a csv file 
    """
    
    
    


# In[45]:


ll


# In[46]:


nn = np.array(ll)['eyear', 'emon', 'eday', 'ehour', 'emin', 'syear', 'smon', 'sday', 'shour',
                              'smin' , 'wageperhour', 'totalwage', 'totaltime']


# In[39]:


coll = ['eyear', 'emon', 'eday', 'ehour', 'emin', 'syear', 'smon', 'sday', 'shour',
                              'smin' , 'wageperhour', 'totalwage', 'totaltime']


# In[41]:


data = pd.DataFrame(data=[[2020,7,30,8,20,2020,7,31,12,30,5, 124, '1 day, 4:10:20']], columns=coll)


# In[42]:


data


# In[37]:


data.reindex(columns=['eyear', 'emon', 'eday', 'ehour', 'emin', 'syear', 'smon', 'sday', 'shour',
                              'smin' , 'wageperhour', 'totalwage', 'totaltime'])


# In[38]:


data.reindex(labels=[2020,7,30,8,20,2020,7,31,12,30,5, 124, '1 day, 4:10:20'])


# In[ ]:




