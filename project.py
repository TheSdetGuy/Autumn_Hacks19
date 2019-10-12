import pandas as pd
import numpy as np
    
def search(i,d):
    #banking
   
    if d is 1:
        dataset = pd.read_csv('Police.csv',error_bad_lines = False)
        keys = dataset.iloc[:,0:1].values
        keys = np.reshape(keys, (1,np.product(keys.shape)))
        data = dataset.iloc[:,1:].values
        if i in keys:
            r , c = np.where(keys == i)
            r = int(r)
            c= int(c)
            returndata = dataset.iloc[c:c+1,:]
            return returndata
        else:
            return "sorry this id does not exist"
    if d is 2:
        dataset = pd.read_csv('Health.csv',error_bad_lines = False)
        keys = dataset.iloc[:,0:1].values
        keys = np.reshape(keys, (1,np.product(keys.shape)))
        data = dataset.iloc[:,1:].values
        if i in keys:
            r , c = np.where(keys == i)
            r = int(r)
            c= int(c)
            returndata = dataset.iloc[c:c+1,:]
            return returndata
        else:
            return "sorry this id does not exist"
    if d is 3:
        dataset = pd.read_csv('Bank.csv',error_bad_lines = False)
        keys = dataset.iloc[:,0:1].values
        keys = np.reshape(keys, (1,np.product(keys.shape)))
        data = dataset.iloc[:,1:].values
        if i in keys:
            r , c = np.where(keys == i)
            r = int(r)
            c= int(c)
            returndata = dataset.iloc[c:c+1,:]
            return returndata
        else:
            return "sorry this id does not exist"

    
print(search('RVJ82',3))