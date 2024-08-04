import re
import matplotlib.pyplot as plt

# 用于存储系统调用及其计数的字典
syscall_counts = {}

# 打开并读取strace输出文件
with open('E:\\summerr\\results.txt', 'r') as file:
    for line in file:
        # 使用正则表达式匹配系统调用的名称（这里假设它总是行首的单词）
        match = re.match(r'(\w+)\(', line)
        if match:
            syscall = match.group(1)
            if syscall in syscall_counts:
                syscall_counts[syscall] += 1
            else:
                syscall_counts[syscall] = 1

            # 绘制系统调用计数
plt.figure(figsize=(10, 8))
syscall_names = list(syscall_counts.keys())
syscall_counts_values = list(syscall_counts.values())

# 根据计数对系统调用进行排序（可选）
sorted_indexes = sorted(range(len(syscall_counts_values)), key=lambda k: syscall_counts_values[k], reverse=True)
sorted_syscall_names = [syscall_names[i] for i in sorted_indexes]
sorted_syscall_counts = [syscall_counts_values[i] for i in sorted_indexes]

# 打印所有横坐标（x轴）的值

print("X轴的系统调用名称:", sorted_syscall_names)
for syscall, count in syscall_counts.items():
    print(f"System call {syscall}: {count} times")
plt.bar(sorted_syscall_names, sorted_syscall_counts, color='skyblue')
plt.xlabel('System Calls')
plt.ylabel('Count')
plt.title('System Call Frequency')
plt.xticks(rotation=45, ha="right")  # 旋转x轴标签以便阅读
plt.tight_layout()  # 自动调整子图参数, 使之填充整个图像区域
plt.show()