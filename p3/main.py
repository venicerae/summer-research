import re
import matplotlib.pyplot as plt
import os
import matplotlib.cm as cm
import seaborn as sns
  # 导入彩虹颜色映射
from matplotlib.colors import Normalize  # 导入Normalize用于颜色归一化

# 设置 seaborn 的默认风格和调色板


# 定义文件类型分类
file_type_categories = {
    "multimedia": ['.mp3', '.wav', '.aac', '.flac', '.ogg',
                   '.mp4', '.avi', '.mkv', '.mov', '.flv', '.webm',
                   '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff',
                   '.m3u', '.m3u8', '.pls', '.xspf',
                   '.mp4v', '.m4v', '.m4a', '.aac', '.3gp', '.3g2',
                   '.mts', '.m2ts', '.ts',
                   '.mkv', '.ogm',
                   '.flac', '.ape',
                   '.mxf',
                   '.m4b',
                   '.aac', '.ac3', '.dts',
                   '.pdf', '.swf', '.avi', '.mov', '.wmv', '.rm', '.ra', '.rv'],

    "productivity": ['.txt', '.md',
                     '.odt', '.ods', '.odp', '.docx', '.xlsx', '.pptx',
                     '.pdf',
                     '.rtf',
                     '.csv', '.tsv',
                     '.json', '.xml', '.yaml', '.yml',
                     '.html', '.htm', '.xhtml',
                     '.scss', '.sass', '.less', '.css',
                     '.js', '.ts', '.jsx', '.tsx',
                     '.ttf', '.otf', '.woff', '.woff2', '.svg',
                     '.zip', '.tar.gz', '.rar',
                     '.bak', '.bak2', '.bak3',
                     '.gpg', '.enc', '.key'],

    "plist": ['.plist', '.xml'],

    "sqlite": ['.db', '.sqlite', '.sqlite3', '.db3', '.sqlite-shm', '.sqlite-wal'],

    "strings": ['.dic',
                '.res',
                '.theme',
                '.xlb', '.xlc',
                '.properties',
                '.lang', '.po', '.pot', '.mo',
                '.strings', '.srt', '.sub'],

    "others": ['.dat', '.bin',
               '.aff',
               '.ht',
               '.tmp', '.temp',
               '.log',
               '.so', '.dll', '.dylib',
               '.sod', '.soe',
               '.bak', '.old',
               '.cache', '.tmpfiles',
               '.conf', '.cfg', '.ini', '.deb', '.rpm', '.pkg']
}
sns.set(style="whitegrid")
current_palette = sns.color_palette("muted", n_colors=len(file_type_categories))  # 获取当前类别的颜色

# 初始化一个字典来存储每个分类及其计数
category_counts = {category: [] for category in file_type_categories}
total_counts = []

# 获取所有文件
input_files = [
    r'C:\Users\raevynnr\Desktop\start.txt',
    r'C:\Users\raevynnr\Desktop\search.txt',
    r'C:\Users\raevynnr\Desktop\play.txt',
    r'C:\Users\raevynnr\Desktop\stop.txt',
    r'C:\Users\raevynnr\Desktop\like.txt',
    r'C:\Users\raevynnr\Desktop\delete.txt',
    r'C:\Users\raevynnr\Desktop\close.txt',
   ]

# 读取每个文件并统计文件类型计数
for file_path in input_files:
    file_name = os.path.basename(file_path)

    # 初始化计数字典
    file_counts = {category: 0 for category in file_type_categories}
    total_count = 0

    # 读取文件内容
    with open(file_path, 'r') as file:
        data = file.readlines()

    # 统计文件类型出现次数
    for line in data:
        match = re.match(r'.*openat\(.*"([^"]+)",.*', line)
        if match:
            opened_file_name = match.group(1)
            for category, extensions in file_type_categories.items():
                for extension in extensions:
                    if opened_file_name.endswith(extension):
                        file_counts[category] += 1
                        total_count += 1
                        if category == others:
                            print(line)

    # 记录总计数和分类计数
    total_counts.append(total_count)
    for category in file_type_categories:
        category_counts[category].append(file_counts[category])

# 计算百分比
percentages = {category: [] for category in file_type_categories}
for category in file_type_categories:
    for i in range(len(input_files)):
        if total_counts[i] > 0:
            percentages[category].append((category_counts[category][i] / total_counts[i]) * 100)
        else:
            percentages[category].append(0)

# 绘制柱状图
# 绘制柱状图
# 绘制柱状图
labels = [os.path.splitext(os.path.basename(file))[0] for file in input_files]
x = range(len(input_files))

fig, ax = plt.subplots(figsize=(10, 6))

bottom = [0] * len(input_files)

for i, category in enumerects = ax.bar(x, percentages[category], bottom=bottom, label=category, color=color, alpha=0.9)

# 在每个堆叠柱状图上方显示百分比
for rect in rects:
    height = rect.get_height()
    ax.annotate(f'{height:.1f}%', xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points", ha='center', va='bottom', fontsize=8)
rate(file_type_categories):
    # 使用 seaborn 调色板中的颜色
    color = current_palette[i % len(current_palette)]  # 循环使用颜色，以防类别数超过调色板颜色数
    ax.bar(x, percentages[category], bottom=bottom, label=category, color=color,
           alpha=0.9)  # alpha 参数控制颜色的透明度，实现淡彩色效果
    bottom = [j + k for j, k in zip(bottom, percentages[category])]

for i in range(len(input_files)):
    ax.text(i, bottom[i], str(total_counts[i]), ha='center', va='bottom')  # 注意：这里假设 total_counts 索引与 labels 匹配


ax.set_xlabel('Input Files')
ax.set_ylabel('Percentage')
ax.set_title('File Type Access Percentage by Input File')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha="right")  # 添加 rotation 和 ha 参数来改善标签的显示
ax.legend()

plt.tight_layout()  # 自动调整子图参数, 使之填充整个图像区域
plt.show()