
# coding: utf-8
import os
import sys
import arcpy
from arcpy import env
# from arcpy.sa import *
from arcpy.sa import ExtractByMask

######################################################################
def batch_clip_raster(inRaster,inMaskData,savepath):
    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")
    cursor = arcpy.SearchCursor(inMaskData)
    for row in cursor:
        mask = row.getValue("Shape")
        name = row.getValue("name")  # name the output layer by COUNTRY_NA field
        print(name.encode('gbk'))
        outExtractByMask = ExtractByMask(inRaster,mask)
        outExtractByMask.save(os.path.join(savepath,name.encode('gbk')+'.tif'))
        print(os.path.join(savepath,name.encode('gbk')+'.tif'))
if __name__ == '__main__':
    inRaster=r'D:\whole\s2b_20190520_center1015_zero.dat'
    inMaskData =r'D:\area\xxx.shp'
    savepath=r'D:\focus\clip'
    batch_clip_raster(inRaster,inMaskData,savepath)
