import os
import zipfile
import shutil


def find_and_extract_files_flat(zip_path, dest_dir, file_extensions=None, keywords=None):
    """
    从压缩包中查找符合条件的文件，并解压到目标文件夹（平铺，无嵌套文件夹）。

    :param zip_path: 压缩包路径
    :param dest_dir: 解压目标文件夹路径
    :param file_extensions: 要查找的文件扩展名列表（如 ['.txt', '.jpg']）
    :param keywords: 文件名需包含的关键字列表（如 ['data', 'report']）
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 打开压缩包
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        all_files = zip_ref.namelist()

        for file in all_files:
            # 跳过文件夹路径，仅处理文件
            if file.endswith('/'):
                continue

            # 获取文件扩展名
            file_ext = os.path.splitext(file)[1].lower()

            # 条件判断
            if file_extensions and file_ext not in file_extensions:
                continue  # 文件扩展名不匹配，跳过
            if keywords and not any(keyword.lower() in file.lower() for keyword in keywords):
                continue  # 文件名不包含关键字，跳过

            # 确保文件名唯一，避免覆盖
            base_name = os.path.basename(file)  # 去掉路径，仅保留文件名
            dest_file_path = os.path.join(dest_dir, base_name)
            counter = 1
            while os.path.exists(dest_file_path):  # 如果文件名冲突，添加序号
                base_name_no_ext, file_ext = os.path.splitext(base_name)
                dest_file_path = os.path.join(dest_dir, f"{base_name_no_ext}_{counter}{file_ext}")
                counter += 1

            # 解压文件
            with zip_ref.open(file) as source_file:
                with open(dest_file_path, 'wb') as target_file:
                    shutil.copyfileobj(source_file, target_file)

            print(f"文件 {file} 已解压为 {dest_file_path}")

    print("符合条件的文件解压完成！")


