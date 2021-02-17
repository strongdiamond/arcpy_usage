
# coding: utf-8
# Import system modules
import os
import sys
import arcpy
from arcpy import env


def tiff2bit_to_8bit(in_tiff2bit,out_tiff8bit):
    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CopyRaster_management(in_tiff2bit,out_tiff8bit,"DEFAULTS","0","9","","","8_BIT_UNSIGNED")

if __name__ == '__main__':
    # env.workspace=r'D:\sd\clip'
    in_tiff2bit=r'D:\clip\mask.tif'
    out_tiff8bit =r'D:\clip\mask8bit.tif'
    tiff2bit_to_8bit(in_tiff2bit,out_tiff8bit)
