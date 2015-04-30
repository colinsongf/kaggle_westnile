'''
Created on Apr 29, 2015

@author: owner
'''
import pandas as pd

train_file='/home/owner/Dataset/west_Nile/train.csv'
columns=["Date","Address","Species","Block","Street","Trap","AddressNumberAndStreet","Latitude","Longitude","AddressAccuracy","NumMosquitos","WnvPresent"]
traindata=pd.read_csv(train_file,names=columns)

