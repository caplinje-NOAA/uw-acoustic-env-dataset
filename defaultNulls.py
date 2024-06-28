# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:54:56 2024

@author: caplinje

A set of functions for generating skeletal null data structures for model agnostic inputs
according to the naming convenctions defined in inputNamingConventions.py

"""
import xarray as xr

import inputNamingConventions as inc




## functions for creating skeletal null datasets of each of these components

def nullBathymetry()->xr.core.dataset.Dataset:
    bathymetry = xr.DataArray(data=[],coords={inc.bathRangeDatum:[]},name=inc.bathDatum)
    bathymetry.attrs = inc.bathAttrsDefault
    bathymetry[inc.bathRangeDatum].attrs = inc.bathRangeAttrsDefault    
    #bathymetry.azimuth.attrs = inc.bathAzimuthAttrsDefault
    return bathymetry.to_dataset()

def nullSSP()->xr.core.dataset.Dataset:
    ssp = xr.DataArray(data=[],coords={inc.sspDepthDatum:[]},name=inc.sspDatum)
    ssp.attrs = inc.sspAttrsDefault
    ssp[inc.sspDepthDatum].attrs = inc.sspDepthAttrsDefault  
    #bathymetry.azimuth.attrs = inc.bathAzimuthAttrsDefault
    return ssp.to_dataset()

def nullSeabed()->xr.core.dataset.Dataset:
    seabeds = []
    units = inc.seabedAttrsDefault['units']
    long_names = inc.seabedAttrsDefault['long_name']
    for i in range(5):
        seabed = xr.DataArray(data=[],coords={inc.seabedDepthDatum:[]},name=inc.seabedDatums[i])
        seabeds.append(seabed)
    # merge
    allVars = xr.merge(seabeds)
    # add depth attrs
    allVars[inc.seabedDepthDatum].attrs = inc.seabedDepthAttrsDefault
    # add attributes to dataset
    for i in range(5):
        allVars[inc.seabedDatums[i]].attrs = inc.seabedAttrsDefault
        allVars[inc.seabedDatums[i]].attrs['units'] = units[i]
        allVars[inc.seabedDatums[i]].attrs['long_name'] = long_names[i]
        

   
    return allVars

def nullSource()->xr.core.dataset.Dataset:
    source = xr.DataArray(data=[],coords={inc.sourceFrequencyDatum:[]},name=inc.sourceDatum)
    source.attrs = inc.sourceAttrsDefault
    source[inc.sourceFrequencyDatum].attrs = inc.sourceFrequencyAttrsDefault  
    #bathymetry.azimuth.attrs = inc.bathAzimuthAttrsDefault
    return source.to_dataset()