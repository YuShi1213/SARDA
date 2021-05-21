#根据图像整体置信度得分将相应的图像排序
import os
import random
file_path = r'D:\shiyu\code\SARDA\conf_av.txt'
#读取置信度得分和相应图片编号构造字典
conf_av = open(file_path)
num = 0
conf_av_value = []
conf_av_key = []
for line in conf_av:
    line = str(line).replace("\n","")
    if (num % 2) ==0:
        conf_av_value.append(float(line))
    else:
        conf_av_key.append(line[-19:-4])
    num += 1
conf_av_dict = dict(zip(conf_av_key,conf_av_value))
#根据字典中图片的value排序
sort_dict = sorted(conf_av_dict.items(),key = lambda kv:(kv[1],kv[0]),reverse=True)
print(len(sort_dict))
#写入train.txt
num_sort = 0
write_file_name = r'D:\shiyu\code\SARDA\conf_av_related\train.txt'
write_file = open(write_file_name, "w")
train_sort = []
for key in sort_dict:
    if num_sort<220:
        train_sort.append(key[0])
        print(key[1])
    num_sort+=1
#random.shuffle(train_sort)
for i in range(len(train_sort)):
    write_file.write(train_sort[i] + '\n')
write_file.close