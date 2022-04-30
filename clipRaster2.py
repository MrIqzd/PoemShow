# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# clipRaster2.py
# Created on: 2022-04-11 15:44:00.00000
#   (generated by JCT)
# Description: 分割栅格
# ps: 要用python2.7+arcpy  或者 ArcGIS自带的python
# ---------------------------------------------------------------------------

# python27
# Import arcpy module
import arcpy
year="2016"
for i in range(9,13):
    month = str(i)
    # Local variables:
    v2019tif = "F:\\result\\"+year+"_" + month + "\\"+year+"_" + month + ".tif"
    clip16 = "F:\\result\\"+year+"_" + month + "\\clip16"
    clip16__2_ = clip16
    parallelProcessingFactor = "1"

    # Process: 分割栅格
    tempEnvironment0 = arcpy.env.parallelProcessingFactor
    arcpy.env.parallelProcessingFactor = parallelProcessingFactor
    arcpy.SplitRaster_management(v2019tif, clip16, year+"_" + month, "NUMBER_OF_TILES", "TIFF", "NEAREST", "8 16",
                                 "2048 2048", "0", "PIXELS", "", "", "", "NONE", "DEFAULT", "")# 8 16 可以修改
    arcpy.env.parallelProcessingFactor = tempEnvironment0
    print(month+" is ok" )

