import matplotlib.pyplot as plt
from collections import defaultdict
import re
from datetime import datetime

# 系统调用名称到颜色的映射（你可以选择自己喜欢的颜色）
syscall_colors = {
    'openat': 'blue',
    'read': 'green',
    'execve': 'red',
    'write': 'cyan',
    'close': 'magenta',
    'exit_group': 'yellow',
    'ioctl': 'orange',
    'mmap': 'purple',
    'clone': 'brown',
    'fsync': 'gray',
    'getpid':'teal',
}

# 正则表达式模式，用于提取PID和时间戳
pattern = re.compile(r'^(\d+)\s+(\d+:\d+:\d+)\s+(\w+)\((.*)\)\s+=\s+\d+')

# 读取和解析日志文件
data = defaultdict(lambda: defaultdict(int))

with open('C:\\Users\\raevynnr\\Desktop\\output3.txt', 'r') as file:
    for line in file:
        match = pattern.match(line)
        if match:
            pid = match.group(1)
            timestamp_str = match.group(2)
            syscall = match.group(3)
            data[timestamp_str][syscall] += 1

# 转换时间戳为datetime对象
timestamps = []
for timestamp_str in sorted(data.keys()):
    timestamps.append(datetime.strptime(timestamp_str, "%H:%M:%S"))

# 准备绘图所需的数据
syscalls = list(syscall_colors.keys())
syscall_indices = {syscall: idx for idx, syscall in enumerate(syscalls)}
colors = []

for timestamp_str, syscall_counts in sorted(data.items()):
    color_values = [syscall_counts.get(syscall, 0) for syscall in syscalls]
    colors.append(color_values)

# 绘图
fig, ax = plt.subplots(figsize=(14, 8))

for timestamp, color_values in zip(timestamps, colors):
    for syscall, color_value in zip(syscalls, color_values):
        if color_value > 0:
            # 调整颜色的透明度，使得即使是少量调用的点也能在图上明显显示
            alpha_value = min(0.2 + 0.8 * (color_value / max(color_values)), 1.0)
            ax.scatter(timestamp, syscall_indices[syscall], color=syscall_colors[syscall], alpha=alpha_value, marker='o', s=100)

# 自定义绘图样式
ax.set_yticks(range(len(syscalls)))
ax.set_yticklabels(syscalls)
ax.set_xlabel('time')
ax.set_title('syscall frequency')
ax.grid(True)

# 调整X轴的日期格式
ax.xaxis.set_major_formatter(plt.FixedFormatter([timestamp.strftime('%H:%M:%S') for timestamp in timestamps]))

plt.tight_layout()
plt.show()
