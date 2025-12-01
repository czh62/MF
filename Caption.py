import json
import os

# 输入 JSON 文件所在文件夹
input_dir = "RAWJson"

# 输出 txt 文件的文件夹
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

# 遍历文件夹中的所有 json 文件
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".json"):
        json_path = os.path.join(input_dir, filename)

        # 目标 txt 文件名（修改后缀）
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        txt_path = os.path.join(output_dir, txt_filename)

        # 读取 json 文件
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"无法解析 JSON 文件: {json_path}, 错误: {e}")
                continue

        # 提取 caption
        captions = []
        for item in data:
            caption = item.get("Caption")
            if caption:
                captions.append(caption)

        # 写入 txt 文件
        with open(txt_path, "w", encoding="utf-8") as f:
            for line in captions:
                f.write(line + "\n")

        print(f"已处理并保存: {txt_path}")

print("全部字幕提取完成！")
