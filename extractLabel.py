import os
import shutil

# 指定文件夹路径
folder_path = "E:/pycharm/coco2017_person/images/train2017"  # 替换为你的文件夹路径

source_path = "E:/pycharm/coco2017_person/labels/train2017"  # 替换为你的文件夹路径
target_path = "E:/pycharm/coco2017_person/target"  # 替换为你的文件夹路径

# 获取文件夹中的所有文件和文件夹名
file_and_folder_names = os.listdir(folder_path)

# # 打印结果
# print("文件夹中的所有文件和文件夹名：")
# for name in file_and_folder_names:
#     print(name)


# 遍历文件名
for name in file_and_folder_names:
    # 获取完整的文件路径
    full_path = os.path.join(folder_path, name)

    # 判断是否为文件
    if os.path.isfile(full_path):
        # print(f"文件名：{name}")
            # 在这里可以对文件进行操作，例如拷贝、重命名等
            
            # 构造新的文件名
        new_filename = name[:-len(".jpg")] + ".txt"

            # 构造完整的旧文件路径和新文件路径
        old_file_path = os.path.join(source_path, new_filename)
        new_file_path = os.path.join(target_path, new_filename)


        shutil.copy2(old_file_path, new_file_path)

    else:
        print(f"文件夹名：{name}")