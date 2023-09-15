import os
import shutil
import random

# 训练集、验证集和测试集的比例分配
test_percent = 0.1
valid_percent = 0.4
train_percent = 0.5

# 标注文件的路径
image_path = 'JPEGImages'
label_path = 'labels'

images_files_list = os.listdir(image_path)
labels_files_list = os.listdir(label_path)
print('images files: {}'.format(images_files_list))
print('labels files: {}'.format(labels_files_list))
total_num = len(images_files_list)
print('total_num: {}'.format(total_num))

test_num = int(total_num * test_percent)
valid_num = int(total_num * valid_percent)
train_num = int(total_num * train_percent)

# 对应文件的索引
test_image_index = random.sample(range(total_num), test_num)
valid_image_index = random.sample(range(total_num), valid_num)
train_image_index = random.sample(range(total_num), train_num)

for i in range(total_num):
    print('src image: {}, i={}'.format(images_files_list[i], i))
    if i in test_image_index:
        # 将图片和标签文件拷贝到对应文件夹下
        shutil.copyfile('JPEGImages/{}'.format(images_files_list[i]), 'test/images/{}'.format(images_files_list[i]))
        shutil.copyfile('labels/{}'.format(labels_files_list[i]), 'test/labels/{}'.format(labels_files_list[i]))
    elif i in valid_image_index:
        shutil.copyfile('JPEGImages/{}'.format(images_files_list[i]), 'valid/images/{}'.format(images_files_list[i]))
        shutil.copyfile('labels/{}'.format(labels_files_list[i]), 'valid/labels/{}'.format(labels_files_list[i]))
    else:
        shutil.copyfile('JPEGImages/{}'.format(images_files_list[i]), 'train/images/{}'.format(images_files_list[i]))
        shutil.copyfile('labels/{}'.format(labels_files_list[i]), 'train/labels/{}'.format(labels_files_list[i]))