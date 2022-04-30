# processing data
主要是做毕设gtnnwr相关时数据处理函数
主要gtnnwr代码没有传

```
clipRaster2.py
Description: 分割栅格
```

```
raster_input.py
Description: 将切割好的栅格文件转成csv格式
```

```
csv_merge.py
Description: 代码跑出预测的xls文件合成一个csv，以便后续处理
```

```
raster_output.py
Description: 将csv转换成栅格
```

```
extract_statistics.py
Description: 批量提取tif的像元平均值、最值、标准差等
```

```
calculate_GWR.py
Description: 对OLR\GWR\GTWR的结果进行十折的分类，同时按照折计算相关统计参数
PS：前提是要在文件下面建立1-10的文件夹，可以makedirs，这里没写
```

```
TIFtoJPG.py
Description: 批量对tif进行符号系统渲染，导出为jpg，但是没有经纬度和图例，比例信息
```
