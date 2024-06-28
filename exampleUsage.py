# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:26:30 2024

@author: jim
"""
import xarray as xr
import numpy as np
import pandas as pd
import datasetFactories as dfact
from uAcousticEnvDS import envDS


## Build single transect data set from various datatypes
bath = xr.load_dataset('testData/singleTrans.netcdf',decode_times=False)
ssps = xr.load_dataset('testData/SSPs.netcdf',decode_times=False)
# select single SSP profile from SSP dataset, and drop NANs
ssp = ssps.isel(lon=0,lat=0).dropna(dim='depth')
# load example source spectra
spectraDF = pd.read_csv('testData/impactSpectra.csv',header=None,names=['f','L'])

## use dataset factories to create datasets for each input according to conventions
bathymetry = dfact.buildBathymetricDS(bath.depth_m.data, bath.range_m.data,depthUnits='m',rangeUnits='m')
SSP = dfact.buildSSpDS(ssp.C.data, ssp.depth.data,ssUnits='m/s',depthUnits='m')
source = dfact.buildSourceDS(spectraDF['L'].values, spectraDF['f'].values,frequencyUnits='Hz',refRange='750',description='Impact')

## instantiatie envDS class, note seabed is not included at this step
data = envDS(bathymetry=bathymetry,ssp=SSP,source=source)

## to add data after instantiation, use xarrays merge functionality:
seabed = dfact.buildSeabedDS([1755], [.88], [1.5], [0],)
merged = xr.merge([seabed,data.Dataset])

## add description

data.addDescription('pile driving example dataset')

##show complete dataset

print(data.Dataset)

## show subsets
print('---------Bathymetry----------')
print(data.Dataset.bath)

## save and load

data.save('testData/pileEx.nc')

loadedData = envDS().read('testData/pileEx.nc')

print(data.Dataset)

