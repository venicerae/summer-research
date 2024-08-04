from collections import Counter

# 假设日志文件名为'log.txt'，并且位于脚本的相同目录下
filename = r'C:\Users\raevynnr\Desktop\close1.log'

# 初始化一个Counter对象来存储每个操作的出现次数
# 初始化一个Counter对象来存储每个操作的出现次数
operations_counter = Counter()

# 打开并读取日志文件
with open(filename, 'r') as file:
    for line in file:
        # 假设每行的格式是 时间戳 操作[,操作]... 路径
        # 我们只关心操作部分
        parts = line.split(None, 3)  # 使用None作为split的参数，它会根据任何空白字符进行分割
        if len(parts) > 2:
            operations_str = parts[2]
            # 拆分由逗号分隔的操作，并去除可能的空格
            operations = [op.strip() for op in operations_str.split(',') if op.strip()]
            # 更新计数器
            operations_counter.update(operations)

        # 打印每种操作类型的数量
for operation, count in operations_counter.items():
    print(f"{operation}: {count}")

# 打印不同操作类型的总数
print(f"Total unique operation types: {len(operations_counter)}")