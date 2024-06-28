# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:26:14 2024

@author: caplinje

Factory functions for creating agnosticInput compliant datasets from numpy arrays

"""
import xarray as xr
import numpy as np

# project imports
import inputNamingConventions as inc


def buildBathymetricDS(bathymetricData:np.ndarray,
                       rangeCoordinate:np.ndarray,
                       azimuthCoordinate:np.ndarray=None,
                       depthUnits='NR',
                       rangeUnits='NR',
                       azimuthUnits='NR',
                       startCoord = 'NR',
                       endCoord = 'NR',
                       dataSource = 'NR'
                       )->xr.core.dataset.Dataset:
    """Construct a bathymetry dataset based on inputNamingConventions"""
    
    bathAttrs =    {inc.UNITS:depthUnits,
                    inc.LONG_NAME:f'bathymetric depth ({depthUnits})',
                    inc.DATA_SOURCE:dataSource,
                    inc.START_COORD:startCoord,
                    inc.END_COORD:endCoord,
                    inc.IS_NULL:0}

    bathRangeAttrs = {inc.UNITS:rangeUnits}

    
    
    if not azimuthCoordinate:
        bathymetry = xr.DataArray(data=bathymetricData,coords={inc.bathRangeDatum:rangeCoordinate},name=inc.bathDatum)
        bathymetry.attrs = bathAttrs
        bathymetry[inc.bathRangeDatum].attrs = bathRangeAttrs   
        return bathymetry.to_dataset()
    
    else:
        bathAzimuthAttrs = {inc.UNITS:azimuthUnits}
        bathymetry = xr.DataArray(data=bathymetricData,coords={inc.bathRangeDatum:rangeCoordinate,inc.bathAzimuthDatum:azimuthCoordinate},name=inc.bathDatum)
        bathymetry.attrs = bathAttrs
        bathymetry[inc.bathRangeDatum].attrs = bathRangeAttrs  
        bathymetry[inc.bathAzimuthDatum].attrs = bathAzimuthAttrs
        
        return bathymetry.to_dataset()
        
    
def buildSSpDS(sspData:np.ndarray,
                       depthCoordinate:np.ndarray,
                       ssUnits='NR',
                       depthUnits='NR',
                       dataSource='NR',
                       timeOfYear='NR',
                       geoCoordinate='NR'
                       )->xr.core.dataset.Dataset:
    """Construct an SSP dataset based on inputNamingConventions"""   
    
    sspAttrs =     {inc.UNITS:ssUnits,
                    inc.LONG_NAME:f'water column sound speed ({ssUnits})',
                    inc.DATA_SOURCE:dataSource,
                    inc.TIME_OF_YEAR:timeOfYear,
                    inc.COORD:geoCoordinate,
                    inc.IS_NULL:0}

    sspDepthAttrs = {inc.UNITS:depthUnits}
    
    ssp = xr.DataArray(data=sspData,coords={inc.sspDepthDatum:depthCoordinate},name=inc.sspDatum)
    ssp.attrs = sspAttrs
    ssp[inc.sspDepthDatum].attrs = sspDepthAttrs
    return ssp.to_dataset()
                       

def buildSeabedDS(Cp:np.ndarray,
                  alpha_p:np.ndarray,
                  density:np.ndarray,
                  depth:np.ndarray,
                  Cs=None,
                  alpha_s=None,
                  frequency=None,
                  Cunits = 'NR',
                  alphaUnits = 'NR',
                  densityUnits = 'NR',
                  depthUnits = 'NR',
                  frequencyUnits = 'NR',
                  frequencyInfo = 'NR',
                  dataSource = 'NR'
                  )->xr.core.dataset.Dataset:
    """Construct an seabed dataset based on inputNamingConventions"""  
    
    # fill nans if shear properties aren't given
    if not Cs:
        Cs = np.zeros_like(Cp)*np.nan
        alpha_s = np.zeros_like(Cp)*np.nan
        

    seabeds = []
    datas = [Cp,Cs,alpha_p,alpha_s,density]
    units = [Cunits,Cunits,alphaUnits,alphaUnits,densityUnits]
    long_names = [f'compressional sound speed ({Cunits})',
                  f'shear sound speed ({Cunits})',
                  f'compressional attenuation ({alphaUnits})',
                  f'shear attenutation ({alphaUnits})',
                  f'sediment density ({densityUnits})']   
    if not frequency:
        for i in range(5):
            seabed = xr.DataArray(data=datas[i],coords={inc.seabedDepthDatum:depth},name=inc.seabedDatums[i])
            seabeds.append(seabed)
        
        allVars = xr.merge(seabeds)
        
    else:
        for i in range(5):
            seabed = xr.DataArray(data=datas[i],coords={inc.seabedDepthDatum:depth,inc.seabedFrequencyDatum:frequency},name=inc.seabedDatums[i])
            seabeds.append(seabed)
        
        allVars = xr.merge(seabeds)        
        allVars[inc.seabedFrequencyDatum].attrs = {inc.Units:frequencyUnits}
        
    allVars[inc.seabedDepthDatum].attrs = {inc.UNITS:depthUnits}
    
    for i in range(5):
        seabedAttrs =  {inc.UNITS:units[i],
                        inc.LONG_NAME:long_names[i],
                        inc.DATA_SOURCE:dataSource,
                        inc.FREQUENCY_INFO:frequencyInfo,
                        inc.IS_NULL:0}
        allVars[inc.seabedDatums[i]].attrs = seabedAttrs
        
    return allVars


def buildSourceDS(levels:np.ndarray,
                  frequencies:np.ndarray,
                  frequencyUnits='NR',
                  refRange='NR',
                  description='NR',
                  dataSource='NR'
                  )->xr.core.dataset.Dataset:
    
    sourceAttrs =      {inc.UNITS:'dB (rel. 1 uPa)',
                        inc.LONG_NAME:'reference level associated with source (dB rel 1 uPa)',
                        inc.DATA_SOURCE:'NR',
                        inc.SOURCE_REF_RANGE: refRange,
                        inc.SOURCE_DESC: description,
                        inc.IS_NULL:0}
            
    source = xr.DataArray(data=levels,coords={inc.sourceFrequencyDatum:frequencies},name=inc.sourceDatum)
    source.attrs = sourceAttrs
    source[inc.sourceFrequencyDatum].attrs = {inc.UNITS:frequencyUnits}  
    #bathymetry.azimuth.attrs = inc.bathAzimuthAttrsDefault
    return source.to_dataset()
        
































