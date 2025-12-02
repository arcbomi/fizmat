import re
import json
import os

html_content = """
<a href="https://ibb.co.com/c68NKw4"><img src="https://i.ibb.co.com/jywL9zn/A22.png" alt="A22" border="0"></a>
"""

# 使用正则表达式提取 src
src_pattern = r'src="([^"]+)"'
src_list = re.findall(src_pattern, html_content)

# 创建字典列表
data_list = []
for src in src_list:
    # 提取文件名（去掉路径和扩展名）
    file_name = os.path.splitext(os.path.basename(src))[0]  # 例如 "A22"
    
    data_item = {
        "group": "geometry",  # 这里可以根据需要调整
        "download_page": f"https://pub-6b4913ff96fe4b018ce574d6efc28d60.r2.dev/{file_name}.pdf",
        "name": file_name,  # 使用文件名作为名称
        "preview_page": "https://cataas.com/cat",  # 示例预览页面
        "image": src
    }
    data_list.append(data_item)

# 输出 JSON
json_output = json.dumps(data_list, indent=4, ensure_ascii=False)
print(json_output)
