# README

本项目用于**批量从 JSON 文件中提取字幕（Caption 字段）**并生成对应的文本文件。

## 项目结构说明

```
.
├── Caption.py     # 主脚本，用于从 JSON 中提取 Caption 并输出为 txt
├── RAWJson/       # 输入目录：存放原始 JSON 文件
└── data/          # 输出目录：脚本运行后生成的 txt 字幕文件
```

### 内容说明

* **RAWJson/**
  该目录中存放需要处理的 JSON 文件。每个 JSON 文件中包含若干条记录，其中含有 `"Caption"` 字段。

* **Caption.py**
  运行该脚本后，会自动遍历 `RAWJson` 目录中的所有 JSON 文件，将其中的 `"Caption"` 字段内容提取出来，并按行写入对应的 `.txt` 文件。

* **data/**
  脚本会在此目录中生成处理后的 txt 文件，每个文件对应输入目录中的一个 JSON 文件。