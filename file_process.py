import os
import shutil

def find_and_copy_files(src_dir, dest_dir, file_extensions=None, keywords=None):
    # 检查目标文件夹是否存在，如果不存在则创建
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 遍历源文件夹中的文件
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()

            # 进行多条件判断
            if file_extensions and file_ext not in file_extensions:
                continue  # 如果文件扩展名不在给定的扩展名列表中，则跳过

            if keywords and not any(keyword.lower() in file.lower() for keyword in keywords):
                continue  # 如果文件名不包含任何关键字，则跳过

            # 生成目标文件路径
            dest_file = os.path.join(dest_dir, file)

            # 直接复制并覆盖目标文件
            shutil.copy(file_path, dest_file)
            print(f"文件 {file} 已复制并覆盖到 {dest_dir}")

    print("所有符合条件的文件已经完成复制！")
