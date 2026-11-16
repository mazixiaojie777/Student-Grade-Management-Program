<div align="center">
  <img src="assets/brand-icon.jpg" width="88" height="88" alt="学生成绩管理系统图标">
  <h1>学生成绩管理系统</h1>
  <p>Python 命令行版 + 单文件 Web 可视化版，业务规则完全一致</p>
</div>

## 项目简介

本项目是一个面向教学演示与学生信息管理的学生成绩管理系统，提供两套实现：

- **Python 命令行版**：使用 Python 标准库实现，数据保存在本地 `score.txt`。
- **Web 可视化版**：单文件 `index.html`，内置全部样式与脚本，支持表格、统计图表、成绩排名与名单弹窗，数据保存在浏览器 `localStorage`。

两套实现共用同一套业务规则：学号唯一、成绩必须为数字、支持学生录入 / 查询 / 修改 / 删除 / 展示 / 保存。

## 功能特性

- **学生录入**：学号唯一校验，重复学号会提示「该学号已存在！」
- **成绩录入**：成绩必须为数字，支持小数，非法输入会提示「成绩必须输入数字！」
- **成绩查询**：按学号查询，Web 版支持按学号或姓名模糊查询
- **修改成绩**：按学号定位学生，仅修改成绩
- **删除学生**：删除前二次确认，删除后不可恢复
- **展示全部**：表格展示学号、姓名、成绩、等级
- **数据保存**：Python 版保存至 `score.txt`，Web 版自动保存至 `localStorage`
- **统计分析**：学生总数、平均分、最高分、最低分、及格率
- **可视化图表**：分数段人数分布柱状图、等级分布、及格率环形图
- **成绩排名**：按成绩降序排列，同分同名次，前三名高亮
- **学生名单弹窗**：点击「学生总数」卡片查看完整名单，支持关闭 / 收起

## 目录结构

```text
student-grade-management/
├── .editorconfig                  # 编辑器统一配置
├── .gitignore                     # Git 忽略规则
├── LICENSE                        # MIT 开源协议
├── README.md                      # 项目说明
├── index.html                     # Web 可视化版（单文件，可直接打开）
├── assets/
│   └── brand-icon.jpg             # 项目图标（README 展示用）
├── data/
│   └── score.example.txt          # 示例数据（可复制为 score.txt）
├── docs/
│   └── 使用说明.md                 # 详细使用文档
└── src/
    └── python/
        └── student_grade_management.py   # Python 命令行版源码
```

## 快速开始

### 环境要求

- Python 3.8 及以上（仅使用标准库，无需安装第三方依赖）
- 现代浏览器（Chrome / Edge / Firefox / Safari 等）

### 运行 Python 命令行版

在仓库根目录执行：

```bash
python src/python/student_grade_management.py
```

程序会在**当前工作目录**读取 / 写入 `score.txt`。可先复制示例数据：

```bash
# macOS / Linux
cp data/score.example.txt score.txt

# Windows PowerShell
Copy-Item data/score.example.txt score.txt
```

启动后按照菜单输入序号即可：

```text
1. 添加学生
2. 查询学生
3. 修改成绩
4. 删除学生
5. 显示全部
6. 保存数据
0. 退出系统
```

### 运行 Web 可视化版

直接用浏览器打开 `index.html` 即可，无需安装依赖或启动服务器。

- 数据自动保存在当前浏览器的 `localStorage` 中
- 点击顶部「保存数据」可手动保存
- 清除浏览器站点数据会同时清除已录入的学生数据

### 部署到 GitHub Pages（可选）

1. 将仓库推送到 GitHub；
2. 进入仓库 **Settings → Pages**；
3. **Source** 选择 `Deploy from a branch`，分支选择 `main`，目录选择 `/(root)`；
4. 保存后访问生成的 Pages 地址即可在线使用 Web 版。

## 数据格式

`score.txt` 每行一条学生记录，字段使用英文逗号分隔：

```text
学号,姓名,成绩
2024001,张三,88
2024002,李四,92.5
2024003,王五,76
```

- 成绩为数字，支持小数与负数（与原程序规则一致）
- 空行会被自动忽略
- 文件编码为 UTF-8

## 成绩等级规则

| 等级 | 分数区间 |
| --- | --- |
| 优秀 | 90 分及以上 |
| 良好 | 80 ~ 89.99 分 |
| 中等 | 70 ~ 79.99 分 |
| 及格 | 60 ~ 69.99 分 |
| 不及格 | 60 分以下 |

## 业务规则

- 学号必须唯一，重复添加会被拒绝
- 成绩必须是合法数字，非法输入不会写入数据
- 修改与删除均按学号定位，找不到时提示「没有找到该学生！」
- Python 版与 Web 版的计算规则（平均分、及格率、等级、排名）保持一致

## 文档

- [详细使用说明](docs/使用说明.md)
- [示例数据](data/score.example.txt)

## 开源协议

本项目基于 [MIT License](LICENSE) 开源。
