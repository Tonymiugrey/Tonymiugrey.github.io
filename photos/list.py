import os
import datetime
from urllib.parse import quote

def get_time_from_filename(filename):
    print(filename)
    # 根据文件名中的时间信息返回一个datetime对象
    # 这里假设文件名中时间的格式为YYYY-MM-DD
    if filename not in [".DS_Store", "list.py", "index.md", "output.txt"]:
        date_str = filename.split('-')[-1].split(".")[0]  # 假设文件名中使用下划线分隔，时间在第二个部分
        return datetime.datetime.strptime(date_str, "%Y%m%d%H%M%S")

def generate_report(directory_path, output_file):
    # 获取目录中所有文件
    files = [f for f in os.listdir(directory_path) if f not in [".DS_Store", "list.py", "index.md", "output.txt"] and os.path.isfile(os.path.join(directory_path, f))]
    
    # 根据文件名中的时间排序文件列表
    sorted_files = sorted(files, key=get_time_from_filename, reverse=True)
    
    path_name = directory_path.split("source")[-1]

    # 生成报告文件
    with open(directory_path+output_file, 'w') as report_file:
        for file_name in sorted_files:
            encoded_file_name = quote(file_name)
            print(f"{'https://cdn.jsdelivr.net/gh/Tonymiugrey/miuGrey.com.cn'+path_name+encoded_file_name}\n")
            report_file.write(f"![]({'https://cdn.jsdelivr.net/gh/Tonymiugrey/miuGrey.com.cn'+path_name+encoded_file_name})\n")

# 调用函数并传递目录路径和输出文件名
#generate_report('source/photos/1ii/photo/', 'output.txt')
#generate_report('source/photos/5d2/photo/', 'output.txt')
generate_report('source/photos/a6000/photo/', 'output.txt')
#generate_report('source/photos/macau/photo/', 'output.txt')
#generate_report('source/photos/s10/photo/', 'output.txt')
generate_report('source/photos/s23u/photo/', 'output.txt')
generate_report('source/photos/singapore/photo/', 'output.txt')
#generate_report('source/photos/xr/photo/', 'output.txt')
