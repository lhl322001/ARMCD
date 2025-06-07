import os
import shutil

# 定义源文件夹路径

# 定义目标文件夹路径
name = "real"
destination_folder = "validationSet/" + name
source_folder = "dataset/dataset/dataset/train/" + name
# 定义阈值
threshold = 10000

# 获取源文件夹中所有文件名
file_names = os.listdir(source_folder)
os.makedirs(destination_folder, exist_ok=True)
# 过滤出符合条件的文件名
test_files = [f for f in file_names if f.startswith(name)]

# 提取文件名中的数字部分，并检查是否大于阈值，如果是，则复制文件到目标文件夹
for old_file in test_files:
    # 提取文件名中的数字部分
    number = int(old_file.split("_")[1].split(".")[0])

    # 检查数字是否大于阈值
    if number >= threshold:
        # 构建复制后的文件名
        new_file = name + "_" + str(number-threshold) + ".jpg"

        # 复制文件到目标文件夹
        shutil.copyfile(os.path.join(source_folder, old_file), os.path.join(destination_folder, new_file))
