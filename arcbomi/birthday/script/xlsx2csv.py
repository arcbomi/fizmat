import pandas as pd
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
# 加载 Excel 文件
file_path = 'a.xlsx'
excel_file = pd.ExcelFile(file_path)

# 用于统计失败次数
failure_count = 0

# 用于存储最终数据
output_data = []

# 遍历每个工作表并处理
for sheet_name in excel_file.sheet_names:
    # 读取工作表的第3列和第4列
    df = excel_file.parse(sheet_name).iloc[:, [2, 3]]
    
    # 确保第 3 列的值是字符串，然后删除换行符和引号
    df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.replace(r'[\n\r"]', '', regex=True)
    # 删除括号及括号内的内容
    df.iloc[:, 0] = df.iloc[:, 0].str.replace(r'\s*\(.*?\)', '', regex=True)
    #删除连续空格
    df.iloc[:, 0] = df.iloc[:, 0].str.replace(r'\s+', ' ', regex=True).str.strip()
    # 删除包含 NaN 的行
    df.dropna(inplace=True)
    # 只保留第二列**包含**数字的行
    df = df[df.iloc[:, 1].astype(str).str.contains(r'\d', regex=True, na=False)]



    # 处理日期列
    def parse_date(date_str):
        global failure_count  # 允许在函数中修改全局变量 failure_count
        if isinstance(date_str, str):
            date_str = date_str.replace(' ', '')
        # 尝试处理日月年格式
        try:
            return pd.to_datetime(date_str, format='%d.%m.%Y').strftime('%m-%d')
        except:
            pass
        # 如果上面的失败，尝试月日年格式
        try:
            return pd.to_datetime(date_str, format='%m/%d/%Y').strftime('%m-%d')
        except:
            pass
        try:
            return pd.to_datetime(date_str, format='%m.%d.%Y').strftime('%m-%d')
        except:
            pass
        # 如果都失败了，返回原始值并增加失败计数
        failure_count += 1
        print('error from:'+str(date_str))
        return None

    # 应用日期格式化
    df.iloc[:, 1] = df.iloc[:, 1].apply(parse_date)
    df.dropna(subset=[df.columns[1]], inplace=True)
    
 # 删除所有空格
    df['Sheet Name'] = sheet_name.replace(" ", "")


    # 存储数据
    for _, row in df.iterrows():
        output_data.append([row.iloc[1], row.iloc[0], row['Sheet Name']])

# 保存为 CSV 文件
output_df = pd.DataFrame(output_data, columns=['birthday', 'name', 'class'])
# 按照 'birthday' 列排序 (按月份-日期排序)
output_df.sort_values(by='birthday', inplace=True)
output_df.to_csv('output.csv', index=False, encoding='utf-8')

# 打印失败次数
print(f"\nNumber of failures (original value returned): {failure_count}")
print("Data saved to output.csv")
