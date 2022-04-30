# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# TIFtoJPG.py
# Created on: 2022-04-23 00:13:01.00000
#   (generated by JCT)
# Description: 批量对tif进行符号系统渲染，导出为jpg，但是没有经纬度和图例，比例信息
# ---------------------------------------------------------------------------

import arcpy

bb_lyr = "C:\\Users\\DELL\\Desktop\\tmp\\example.lyr" # 符号系统的模版样式，要lyr格式的

path_gen="F:\\result\\"#读取tif目标路径
blank_mxd_path = "C:\\Users\\DELL\\Desktop\\pic\\blank.mxd"# 一个空的mxd文件
target_path="C:\\Users\\DELL\\Desktop\\pic\\res_jpg\\" #转换后的jpg路径
file_name="result20220406070531.tif"

for year in range(2015,2019):
    for month in range(1, 13):
        # 导入mxd文件，也就是arcmap的保存文件
        mxd = arcpy.mapping.MapDocument(blank_mxd_path)
        df = arcpy.mapping.ListDataFrames(mxd)[0]  # dataframe没具体意义
        tif_path = path_gen + str(year) + "_" + str(month) + "\\" + file_name
        # 创建raster对象
        raster = arcpy.Raster(tif_path)
        arcpy.MakeRasterLayer_management(raster, 'rasterLayer')
        layer = arcpy.mapping.Layer("rasterLayer")  # make layer
        arcpy.ApplySymbologyFromLayer_management(layer, bb_lyr)  # 符号系统
        arcpy.mapping.AddLayer(df, layer, "AUTO_ARRANGE")  # add layer
        # arcpy.ApplySymbologyFromLayer_management(layer, bb_lyr)

        df = arcpy.mapping.ListDataFrames(mxd)[0]

        file_target = target_path + str(year) + "_" + str(month) + ".jpg"
        # 导出图片命令
        arcpy.mapping.ExportToJPEG(mxd, file_target, df, df_export_width=794, df_export_height=1123)
        print(str(year) + "_" + str(month) + " is finished!")
        del mxd, df




