import os
import tkinter as tk
from tkinter import filedialog, messagebox
from zip_process import find_and_extract_files_flat
from file_process import find_and_copy_files


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


def browse_input_file():
    """打开文件选择对话框，选择查找的文件"""
    file_path = filedialog.askopenfilename(title="选择查找的文件", filetypes=[("所有文件", "*.*")])
    input_file_entry.delete(0, tk.END)  # 清空当前内容
    input_file_entry.insert(0, file_path)  # 将选中的文件路径显示在文本框里


def browse_output_dir():
    """打开文件夹选择对话框，选择输出目录"""
    folder_path = filedialog.askdirectory(title="选择导出文件夹")
    output_dir_entry.delete(0, tk.END)  # 清空当前内容
    output_dir_entry.insert(0, folder_path)  # 将选中的文件夹路径显示在文本框里


def process_files():
    """根据用户输入，调用相应的处理函数"""
    input_path = input_file_entry.get().strip()
    output_path = output_dir_entry.get().strip()
    file_input = file_format_entry.get().strip()
    keyword_input = keyword_entry.get().strip()

    # 转换输入为列表
    file_extensions = [ext.strip() for ext in file_input.split(',')] if file_input else None
    keywords = [kw.strip() for kw in keyword_input.split(',')] if keyword_input else None

    if not input_path or not output_path:
        messagebox.showwarning("警告", "请输入完整的文件路径和导出文件夹！")
        return

    # 判断输入路径类型并调用相应处理函数
    try:
        if is_target_file(input_path):
            find_and_extract_files_flat(input_path, output_path, file_extensions, keywords)
            messagebox.showinfo("完成", "压缩包文件处理完毕！")
        else:
            find_and_copy_files(input_path, output_path, file_extensions, keywords)
            messagebox.showinfo("完成", "普通文件处理完毕！")
    except Exception as e:
        messagebox.showerror("错误", f"处理文件时发生错误: {str(e)}")


# 创建主窗口
root = tk.Tk()
root.title("文件处理工具")

# 设置窗口大小
root.geometry("800x400")

# 输入文件路径
tk.Label(root, text="查找文件路径:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
input_file_entry = tk.Entry(root, width=40)
input_file_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="浏览", command=browse_input_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# 输出文件夹路径
tk.Label(root, text="导出文件夹路径:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
output_dir_entry = tk.Entry(root, width=40)
output_dir_entry.grid(row=1, column=1, padx=10, pady=10)
browse_output_button = tk.Button(root, text="浏览", command=browse_output_dir)
browse_output_button.grid(row=1, column=2, padx=10, pady=10)

# 查找文件格式
tk.Label(root, text="查找目标文件格式 (如 .jpg, .txt)：").grid(row=2, column=0, padx=10, pady=10, sticky="e")
file_format_entry = tk.Entry(root, width=40)
file_format_entry.grid(row=2, column=1, padx=10, pady=10)

# 查找关键字
tk.Label(root, text="文件名包含的关键字:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
keyword_entry = tk.Entry(root, width=40)
keyword_entry.grid(row=3, column=1, padx=10, pady=10)

# 处理文件按钮
process_button = tk.Button(root, text="开始处理", command=process_files)
process_button.grid(row=4, column=1, padx=10, pady=20)

# 启动主循环
root.mainloop()
