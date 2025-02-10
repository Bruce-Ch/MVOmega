import pandas as pd
import json

# 读取Excel文件
df = pd.read_excel('MV城市定向.xlsx')

# 获取前两列
first_two_columns = df.iloc[:, :2]

# 将每行的前两列用空格连接起来，并用双引号包裹，形成一个列表
result_list = first_two_columns.apply(lambda row: ' '.join(row.values.astype(str)), axis=1).tolist()

# 使用json.dumps来确保输出的字符串使用双引号
print(json.dumps(result_list, ensure_ascii=False))