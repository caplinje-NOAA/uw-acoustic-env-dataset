# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:50:33 2024

@author: caplinje

# naming conventions for model agnostic data structures
# version 1.0

"""
# Attribute keys

UNITS = 'units'
LONG_NAME = 'long_name'
DATA_SOURCE = 'data_source'
START_COORD = 'starting coordinates'
END_COORD = 'ending coordinates'
IS_NULL = 'isNull'
TIME_OF_YEAR ='time_of_year'
COORD = 'representative loc., [lat,lon]'
FREQUENCY_INFO = 'frequency info'
SOURCE_REF_RANGE = 'range (m)'
SOURCE_DESC = 'source description'
IS_COMPLIANT = 'isCompliant'
DESCRIPTION = 'description'


# conventions associated with bathymetry 
bathDatum = 'bath'
bathRangeDatum = 'range'
bathAzimuthDatum = 'azimuth'

bathAttrsDefault =      {UNITS:'m',
                         LONG_NAME:'bathymetric depth (m)',
                         DATA_SOURCE:'NR',
                         START_COORD:'NR',
                         END_COORD:'NR',
                         IS_NULL:1}

bathRangeAttrsDefault = {UNITS:'m'}

bathAzimuthAttrsDefault = {UNITS:'degrees rel. N'}

bathAttrKeys = list(bathAttrsDefault.keys())
BathRangeAttrKeys = list(bathRangeAttrsDefault.keys())
bathAzimuthAttrKeys = list(bathAzimuthAttrsDefault.keys())

# conventions associated with sound speed profile
sspDatum = 'Cw'
sspDepthDatum = 'depth_wc' # depth in water column

sspAttrsDefault =       {UNITS:'m/s',
                         LONG_NAME:'water column sound speed (m/s)',
                         DATA_SOURCE:'NR',
                         TIME_OF_YEAR:'NR',
                         COORD:'NR',
                         IS_NULL:1}

sspDepthAttrsDefault = {UNITS:'m'}

sspAttrKeys = list(sspAttrsDefault.keys())
sspDepthAttrKeys = list(sspDepthAttrsDefault.keys())

# conventions associated with seabed
seabedDatums = ['Cp','Cs','alpha_p','alpha_s','density']
seabedDepthDatum = 'depth_sb' # depth below seabed 
seabedFrequencyDatum = 'frequency'

seabedAttrsDefault =    {UNITS:['m/s','m/s','dB/wl','dB/wl','g/cm3'],
                         LONG_NAME:['compressional sound speed (m/s)','shear sound speed (m/s)','compressional attenuation (dB/wl)','shear attenutation (dB/wl)','sediment density (g/cm3)'],
                         DATA_SOURCE:'NR',
                         FREQUENCY_INFO:'NR',
                         IS_NULL:1}

seabedDepthAttrsDefault = {UNITS:'m'}
seabedFrequencyAttrsDefault = {UNITS:'hz'}

seabedAttrKeys = list(seabedAttrsDefault.keys())
seabedDepthAttrKeys = list(seabedDepthAttrsDefault.keys())
seabedFrequencyAttrKeys = list(seabedFrequencyAttrsDefault.keys())

# conventions associated with reference levels

sourceDatum = 'level'
sourceFrequencyDatum = 'frequency'

sourceAttrsDefault =    {UNITS:'dB (rel. 1 uPa)',
                         LONG_NAME:'reference level associated with source (dB rel 1 uPa)',
                         DATA_SOURCE:'NR',
                         SOURCE_REF_RANGE: 0.0,
                         SOURCE_DESC: 'generic sound source',
                         IS_NULL:1}

sourceFrequencyAttrsDefault = {UNITS:'hz'}
sourceAttrKeys = list(sourceAttrsDefault.keys())
sourceFrequencyAttrKeys = list(sourceFrequencyAttrsDefault.keys())


