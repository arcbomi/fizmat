import os

# 设置要处理的目录
directory = r'C:\Users\windm\me\New folder'

# 遍历指定目录中的所有文件
for root, dirs, files in os.walk(directory):
    for filename in files:
        # 检查文件名中是否包含 .pdf_compressed
        if '.pdf_compressed' in filename:
            # 创建新的文件名，去掉 .pdf_compressed
            new_filename = filename.replace('.pdf_compressed', '')
            # 构建完整的旧文件路径和新文件路径
            old_file_path = os.path.join(root, filename)
            new_file_path = os.path.join(root, new_filename)

            # 重命名文件
            os.rename(old_file_path, new_file_path)

            print(f"Renamed: {old_file_path} to {new_file_path}")
