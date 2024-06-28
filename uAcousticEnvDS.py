# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 07:36:33 2024

@author: caplinje


"""
# data science imports
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'

# project imports
import inputNamingConventions as inc
import defaultNulls as defaults

bath = xr.load_dataset('testData/singleTrans.netcdf',decode_times=False)


class envDS:
    """The underwater acoustic environment DS is meant to be a complete set of inputs
    for any propagation model. The envDS incorporates bathymetry, sound speed profiles,
    seabed parameters, and source data into one xarray dataset.  Data is checked to ensure
    consistent naming conventions and reporting of metadata see exampleUsage.py for examples.
    Currently, only bathymetry is range dependent."""
    
    def __init__(self, bathymetry:xr.Dataset=defaults.nullBathymetry(),
                       ssp:xr.Dataset=defaults.nullSSP(),
                       seabed:xr.Dataset=defaults.nullSeabed(),
                       source:xr.Dataset=defaults.nullSource()):
        
        
        
        self.enforceConventions(bathymetry, 
                                [inc.bathDatum], 
                                inc.bathAttrKeys, 
                                [inc.bathRangeDatum,inc.bathAzimuthDatum],
                                [inc.BathRangeAttrKeys,inc.bathAzimuthAttrKeys])
        
        self.enforceConventions(ssp, 
                                [inc.sspDatum], 
                                inc.sspAttrKeys, 
                                [inc.sspDepthDatum],
                                [inc.sspDepthAttrKeys])       
        
        self.enforceConventions(seabed, 
                                inc.seabedDatums, 
                                inc.seabedAttrKeys, 
                                [inc.seabedDepthDatum,inc.seabedFrequencyDatum],
                                [inc.seabedDepthAttrKeys,inc.seabedFrequencyDatum])  
        
        self.enforceConventions(source, 
                                [inc.sourceDatum], 
                                inc.sourceAttrKeys, 
                                [inc.sourceFrequencyDatum],
                                [inc.sourceFrequencyAttrKeys]) 
        
        self.Dataset = xr.merge([bathymetry,ssp,seabed,source])
        
        self.Dataset.attrs[inc.IS_COMPLIANT]='True'
        return 
    
    def enforceConventions(self,dataset,variables,variableKeys,coordinates,coordinateKeys):
        # validate that data is xarray dataset
        if not type(dataset)==xr.core.dataset.Dataset:
            raise TypeError('{variable} must be an xarray dataset')
            return
        
        # check for correct coordinates and datum
        dims = list(dataset.dims)
        data_vars = list(dataset.data_vars)
        if not set(data_vars)==set(variables):
            raise ValueError(f'{variables} data set must have variable {variables}, existing vars={data_vars}')
            return
        
        # if dimensionality of data is singular, coordinate must be range
        # single transect case
        if len(dims)==1:
            if not (dims[0]==coordinates[0]):
                raise ValueError(f'{variables} data set must have coordinate {inc.bathRangeDatum}')
                return    
            
            # check coordinate keys
            if not (list(dataset[coordinates[0]].attrs.keys())==coordinateKeys[0]):
                    raise ValueError(f'{coordinates[0]} data set must have attributes {coordinateKeys[0]}')
                    return   
        # if dimensionality of data is 2D, coordinates must include range and aziumth    
        if len(dims)==2:
            if not ((coordinates[0] in dims) and (coordinates[1] in dims)):
                raise ValueError(f'2D {variables} data set must have coordinates {coordinates[0]} and {coordinates[1]}')
                return   
            
            # check multi-dimension coordinate keys
            for coordinate,keys in zip(coordinates,coordinateKeys):
                
                if not (list(dataset[coordinate].attrs.keys())==keys):
                        raise ValueError(f'{coordinate} data set must have attributes {keys}')
                        return 
            
        # check variable keys
        for variable in variables:
            if not (list(dataset[variable].attrs.keys())==variableKeys):
                    raise ValueError(f'{variables} data set must have attributes {variableKeys}')
                    return   
            

        return dataset
    
    def checkDataset(self):
        pass
        
    
    def addDescription(self, description:str):
        self.Dataset.attrs[inc.DESCRIPTION]=description
    
    def save(self, path:str):
        
        self.Dataset.to_netcdf(path)
        
    def read(self, path:str):
        
        self.Dataset = xr.open_dataset(path)
        return self
    
    def plotBathymetry(self):
        return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    