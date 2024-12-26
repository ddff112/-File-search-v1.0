import os
from zip_process import find_and_extract_files_flat
from file_process import find_and_copy_files

print("这是一个文件处理界面")
input_path = input("请输入查找的文件路径：").strip('"')
output_path = input("请输入文件导出的文件夹：").strip('"')
file_input = input("请输入查找目标文件格式（例:.jpg,.txt，多个用逗号分隔，可留空）：").strip('"')
keyword_input = input("请输入索引关键字（多个用逗号分隔，可留空）：").strip('"')

# 转换输入为列表
file_extensions = [ext.strip() for ext in file_input.split(',')] if file_input else None
keywords = [kw.strip() for kw in keyword_input.split(',')] if keyword_input else None

def is_target_file(input_path):
    """
    判断给定路径的文件是否属于.zip。

    :param input_path: 文件路径
    :return: True 表示是目标文件，False 表示不是
    """
    if input_path:  # 检查路径是否有效
        file_ext = os.path.splitext(input_path)[1].lower()  # 获取文件扩展名（小写）
        return file_ext in [".zip"]  # 判断文件扩展名是否为 .zip
    return False  # 如果路径无效，则返回 False

# 判断输入路径类型并调用相应处理函数
if is_target_file(input_path):
    find_and_extract_files_flat(input_path, output_path, file_extensions, keywords)
    print("zip文件处理完毕！")
else:
    find_and_copy_files(input_path, output_path, file_extensions, keywords)
    print("文件处理完毕！")
