#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

#define our brooklyn dataframe and main statistics
brooklyn = pd.read_csv('brooklyn.csv')
brooklyn['one_bedroom'] = brooklyn.bedrooms.apply(lambda x: 'one_bedroom' if x == 1 else None)
average_brooklyn_rent = np.mean(brooklyn['rent'])
brooklyn['rent price vs avg'] = brooklyn.rent.apply(lambda x: 'Above avg rent' if x > 3327 else 'below avg rent')
brooklyn_rent_sd = np.std(brooklyn['rent'])
brooklyn_rent_median = np.median(brooklyn['rent'])
#printing the main statistics of the brooklyn dataframe
try: 
    print('The average price of rent in Brooklyn is $' + str(round(average_brooklyn_rent, 2)))
except NameError: 
    print('The average price of rent in Brooklyn is not defined')
    
try: 
    print('The median price of rent in Brooklyn is $' + str(round(brooklyn_rent_median, 2)))
except NameError: 
    print('The median price of rent in Brooklyn is not defined')
    
try: 
    print('The standard deviation of rent prices in Brooklyn is $' +  str(round(brooklyn_rent_sd, 2)))
except NameError: 
    print('The standard deviation of rent prices in Brooklyn is not defined')
    
#defining our score functionn that gives each attribute a certain value out of 100
def score(row): 
    score = 0
    if row['has_elevator']  :
        score = score+ 40
    if row['has_dishwasher'] :
        score = score + 20
    if row['has_washer_dryer']: 
        score = score + 30
    if row['has_doorman']:
        score = score + 10
    return score
   
brooklyn['score'] = brooklyn.apply(score, axis = 1)

#sorting the rent of a one bedroom or studio apartment along with our score column
print(brooklyn.sort_values('score',ascending=0)[['bedrooms','bathrooms','score', 'rent','neighborhood', 'rent price vs avg']].head(40))

#print the average rent prices of 1 bedroom or studio apartments by neighborhood in brooklyn    
print('The average rent of a studio or one bedroom apartment by neighborhood:')
brooklyn_onebr = brooklyn[brooklyn['bedrooms']<=1]
neighborhood_means_onebr = brooklyn_onebr[['neighborhood', 'rent']].groupby(['neighborhood']).mean()
mean_rent_onebr_by_neighborhood = neighborhood_means_onebr.sort_values(['rent']).reset_index()
print(mean_rent_onebr_by_neighborhood)


# In[5]:


#define our manhattan dataframe and main statistics
manhattan = pd.read_csv('manhattan.csv')
manhattan['one_bedroom'] = manhattan.bedrooms.apply(lambda x: 'one_bedroom' if x == 1 else None)
average_manhattan_rent = np.mean(manhattan['rent'])
manhattan['rent price vs avg'] = manhattan.rent.apply(lambda x: 'Above avg rent' if x > 5138 else 'below avg rent')
manhattan_rent_sd = np.std(manhattan['rent'])
manhattan_rent_median = np.median(manhattan['rent'])
#printing the main statistics of the manhattan dataframe
try: 
    print('The average price of rent in Manhattan is $' + str(round(average_manhattan_rent, 2)))
except NameError: 
    print('The average price of rent in Manhattan is not defined')
    
try: 
    print('The median price of rent in Manhattan is $' + str(round(manhattan_rent_median, 2)))
except NameError: 
    print('The median price of rent in Manhattan is not defined')
    
try: 
    print('The standard deviation of rent prices in Manhattan is $' +  str(round(manhattan_rent_sd, 2)))
except NameError: 
    print('The standard deviation of rent prices in Manhattan is not defined')
    
#defining our score functionn that gives each attribute a certain value out of 100
def score(row): 
    score = 0
    if row['has_elevator']  :
        score = score+ 40
    if row['has_dishwasher'] :
        score = score + 20
    if row['has_washer_dryer']: 
        score = score + 30
    if row['has_doorman']:
        score = score + 10
    return score
   
manhattan['score'] = manhattan.apply(score, axis = 1)


#print the rent prices of 1 bedroom or studio apartments by neighborhood in manhattan    

print('The average rent of a studio or one bedroom apartment by neighborhood:')
manhattan_onebr = manhattan[manhattan['bedrooms']<=1]
neighborhood_means_onebr = manhattan_onebr[['neighborhood', 'rent']].groupby(['neighborhood']).mean()
print(neighborhood_means_onebr.sort_values(['rent']))

#sorting the average rent of a one bedroom or studio apartment along with our score column
print(manhattan.sort_values('score',ascending=0)[['bedrooms','bathrooms','score', 'rent','neighborhood', 'rent price vs avg']].head(40))


# In[6]:


#define our queens dataframe and main statistics
queens = pd.read_csv('queens.csv')
queens['one_bedroom'] = queens.bedrooms.apply(lambda x: 'one_bedroom' if x == 1 else None)
average_queens_rent = np.mean(queens['rent'])
queens['rent price vs avg'] = queens.rent.apply(lambda x: 'Above avg rent' if x > 2516 else 'below avg rent')
queens_rent_sd = np.std(queens['rent'])
queens_rent_median = np.median(queens['rent'])
#printing the main statistics of the queens dataframe
try: 
    print('The average price of rent in Queens is $' + str(round(average_queens_rent, 2)))
except NameError: 
    print('The average price of rent in Queens is not defined')
    
try: 
    print('The median price of rent in Queens is $' + str(round(queens_rent_median, 2)))
except NameError: 
    print('The median price of rent in Queens is not defined')
    
try: 
    print('The standard deviation of rent prices in Queens is $' +  str(round(queens_rent_sd, 2)))
except NameError: 
    print('The standard deviation of rent prices in Queens is not defined')
    
#defining our score functionn that gives each attribute a certain value out of 100
def score(row): 
    score = 0
    if row['has_elevator']  :
        score = score+ 40
    if row['has_dishwasher'] :
        score = score + 20
    if row['has_washer_dryer']: 
        score = score + 30
    if row['has_doorman']:
        score = score + 10
    return score
   
queens['score'] = queens.apply(score, axis = 1)

#sorting the rent of a one bedroom or studio apartment along with our score column
print(queens.sort_values('score',ascending=0)[['bedrooms','bathrooms','score', 'rent','neighborhood', 'rent price vs avg']].head(40))

#print the average rent prices of 1 bedroom or studio apartments by neighborhood in queens    
print('The average rent of a one bedroom or studio apartment by neighborhood in Queens')
queens_onebr = queens[queens['bedrooms']<=1]
neighborhood_means_onebr = queens_onebr[['neighborhood', 'rent']].groupby(['neighborhood']).mean()
print(neighborhood_means_onebr.sort_values(['rent']))


# In[ ]:




