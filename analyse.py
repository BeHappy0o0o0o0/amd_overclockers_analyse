#!/usr/bin/env python
# coding: utf-8

# In[53]:


import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.ticker as ticker
from matplotlib.font_manager import FontProperties  # 导入FontProperties
font = FontProperties(fname="SimHei.ttf", size=14)  # 设置字体

def analyse(file_path):
    title_list = []
    DateTime_list = []
    GPUClock_list = []
    MemoryClock_list = []
    GPUTemperature_list = []
    FanSpeed_list = []
    FanSpeedRPM_list = []
    GPULoad_list = []
    MemoryControllerLoad_list = []
    MemoryUsed_Dedicated_list = []
    MemoryUsed_Dynamic_list = []
    GPUChipPowerDraw_list = []
    VDDCPowerDraw_list = []
    VDDCIPowerDraw_list = []
    VRMEfficiency_list = []
    VDDC_list = []
    CPUTemperature_list = []
    SystemMemoryUsed_list = []
    
    # 初始化图
    # 设置图形显示风格
    plt.style.use('ggplot')
    # 设置figure大小  像素
    plt.figure(figsize=(100, 50), dpi=200)
    # 设置y轴间隔
    ax = plt.axes()
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    # ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
    # x y 轴标签   字体大小
    plt.xlabel("时间/min", fontsize=28, fontproperties=font)
    plt.ylabel("数值范围", fontsize=28, fontproperties=font)
    
    # 读取gpuz的log文件
    with open(file_path, "r") as f:
        for l in f.readlines():
            l_list = l.replace(" ", "").replace("\n", "").split(",")
    #         print(l_list)
            if l_list[0] == "Date":
                title_list = l_list
                continue
            if len(l_list) != 18:
                continue
    #         print(l_list)
    #         print(l_list[2])
            DateTime_list.append(datetime.strptime(l_list[0], "%Y-%m-%d%H:%S:%M"))
            GPUClock_list.append(float(l_list[1]))
            MemoryClock_list.append(float(l_list[2]))
            GPUTemperature_list.append(float(l_list[3]))
            FanSpeed_list.append(l_list[4])
            FanSpeedRPM_list.append(l_list[5])
            GPULoad_list.append(l_list[6])
            MemoryControllerLoad_list.append(l_list[7])
            MemoryUsed_Dedicated_list.append(l_list[8])
            MemoryUsed_Dynamic_list.append(l_list[9])
            GPUChipPowerDraw_list.append(float(l_list[10]))
            VDDCPowerDraw_list.append(l_list[11])
            VDDCIPowerDraw_list.append(l_list[12])
            VRMEfficiency_list.append(l_list[13])
            VDDC_list.append(l_list[14])
            CPUTemperature_list.append(l_list[15])
            SystemMemoryUsed_list.append(l_list[16])

    print("开始绘图，请等待。。。")
    # print(GPUClock_list)
    plt.scatter(DateTime_list, GPUClock_list, marker="o", color="b", label="gpu频率变化")
    plt.scatter(DateTime_list, MemoryClock_list, marker="s", color="r", label="显存频率变化")
    plt.scatter(DateTime_list, GPUChipPowerDraw_list, marker="s", color="g", label="gpu功耗")
    plt.legend(prop=font)
    plt.savefig("分析图.png", dpi=200)
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("请输入需要分析的gpuz-log文件路径")
        exit()
    analyse(str(sys.argv[1]))
    print("分析结束")
    


# In[ ]:




