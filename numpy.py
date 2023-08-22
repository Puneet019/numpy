

# In[22]:


import csv


# In[23]:


import numpy as np


# In[24]:


data=[]

with open(r"C:\Users\Dell\Downloads\MER.csv",'r') as csvfile:
    file_reader=csv.reader(csvfile,delimiter=",")
    for row in file_reader:
        data.append(row)
        
data=np.array(data)        


# In[25]:


data


# In[26]:


#1
print("shape:",data.shape)
print("dimension:",data.ndim)
print("type:",type(data))


# In[27]:


#2
q2=data[0:10,3:4]
q2


# In[28]:


#3 
#first row of the data tells about header/title
header=data[::8218,0:6]
header


# In[29]:


#4 Print the data contained in column 2 and 3 from row 1 till row 20
q4=data[0:20,1:3]
q4


# In[30]:


#5 Print the data present in only the first three and the last three rows of all the columns in a single output.
array_start = data[:3,:]
array_start


# In[31]:


array_end = data[-3:,:]
array_end


# In[32]:


#ans5
np.vstack((array_start, array_end))


# In[33]:


#6 Sort the data on the basis of net amount of electricity generated irrespective of the source.

q6=np.sort(data[:,2:3],axis=0)
print(q6)


# In[34]:


#7 Find the total amount of electricity generated using coal and nuclear between
#1949-1990.( In this dataset, rows containing monthly data express date in the format
#'YYYYMM'. Rows containing annual data express the date in the format 'YYYY13'.)


# In[35]:


coal_mask_array = np.array(([x[-2:] == '13' for x in data[:,1]])) 


coal_mask_array = data[coal_mask_array]
coal_mask_array


# In[36]:


newcoal_data = coal_mask_array[coal_mask_array[:,4] == 'Electricity Net Generation From Coal, All Sectors' ] 
newcoal_datas=newcoal_data[:42]
newcoal_datas


# In[37]:


coal_energy = newcoal_datas[:,2].astype(float)
coal_energy


# In[38]:


coal_ener=(coal_energy.sum())
coal_ener


# In[39]:


nuclear_data = coal_mask_array[coal_mask_array[:,4] == 'Electricity Net Generation From Nuclear Electric Power, All Sectors' ] 
nuclear_datas=nuclear_data[:42]
nuclear_datas


# In[40]:


nuclear_energy = nuclear_datas[:,2].astype(float)
nuclear_energy


# In[41]:


nuclear_ener=(nuclear_energy.sum() )
nuclear_ener


# In[42]:


#ans7
total=(nuclear_ener+coal_ener)
print("total energy produced from coal and nuclear is:",total)


# In[43]:


#8 Print all the unique sources of Energy generation present in the dataset.
print(" unique sources of Energy generation are:")
q8=np.unique(data[1:,4:5])
print(q8)



# In[51]:


#9 Print all the details(annual) where the energy source is Wind Energy. Use the concept of masking to filter the data.
mask_array = (data[:,4] == 'Electricity Net Generation From Wind, All Sectors')
mask_array


# In[52]:


wind_data = data[mask_array]
wind_data


# In[54]:


#ans9
wind_data = wind_data[wind_data[:,2] != 'Not Available']
wind_data


# In[115]:


#10 Print the Total Energy generated in the USA till date.


# In[59]:


mask_arr=(data[:,2] != 'Not Available')
mask_arr


# In[60]:


total_data = data[mask_arr]
total_data


# In[61]:


tot_energy = total_data[1:,2].astype(float)
tot_energy


# In[71]:


#ans10
print(f'Total energy generated in the USA s is {tot_energy.sum()} Gigawatt-hours')
tot_energys=tot_energy.sum()


# In[ ]:


#11 Print the average annual energy generated from wind in the USA and also the standard 
#deviation present in the energy generation.


# In[55]:


wind_energy = wind_data[1:,2].astype(float)
wind_energy


# In[56]:


#ans11
print(f'The average annual energy generated from wind is {np.mean(wind_energy)} Gigawatt-hours, '
      f'with a standard deviation of { np.std(wind_energy)}')


# In[21]:


#12 What and when was the maximum annual energy generated?


# In[63]:


#ans12
print(f'The highest recorded annual energy generated  is {tot_energy.max()} Gigawatt-hours')
index = tot_energy.argmax() #this method returns the index of the maximum value in the array
print(f'The highest energy generation occured in the year {total_data[index,1][:-2]}')
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[76]:


def index_energy_data(data, startyear, energy_label):
    """returns a NumPy array containing only rows with the specified energy_label in column 4, 
    that also contain energy data, and that also contain annual totals after the specified start year """
    
    output = data[((data[:,4] == energy_label))]
    output = output[((output[:,2] != 'Not Available'))]
    output = output[np.array(([x[-2:] == '13' and int(x[:4]) >= startyear for x in output[:,1]]))]
    
    energy = output[:,2].astype(float)
    dates = np.array([int(j[:4]) for j in output[:,1]])  # Taking the first four digits of each entry in column 1 gives us the year
    
    return energy, dates


# In[80]:


wind_energys, dates = index_energy_data(data, 1984, energy_label = 'Electricity Net Generation From Wind, All Sectors')
dates


# In[105]:


wind_frac = 100 * energy_wind / energy_total
solar_frac = 100 * energy_solar / energy_total
combined_frac = 100 * (energy_solar + energy_wind) / energy_total


# In[69]:


np.array(([x[0:4]<='1990'  for x in data[1:,1]])) 


# In[79]:


wind_frac=100*wind_energys / tot_energys
wind_frac


# In[72]:


wind_energys=wind_energy.sum()



# In[ ]:
