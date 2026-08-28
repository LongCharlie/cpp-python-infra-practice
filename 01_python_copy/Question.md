题目：复现与修复 Python 浅拷贝问题

背景描述
假设你在开发一个 AI 数据的 Batch 处理系统，每个样本的数据结构如下：
data = {"id": 101, "labels": ["cat", "pet"]}
现在你需要对数据进行 Augmentation（增强），复制一份原数据并给复制后的样本添加一个新标签 "animal"，同时要求绝不能修改原始数据。

你的任务

请写出一个 Python 脚本，完成以下三部分：

Bug 复现：使用浅拷贝（例如 copy.copy() 或 .copy()）复制 data 到 data_shallow，并向 data_shallow["labels"] 中 append("animal")。打印原始数据 data，展示为什么这引发了数据污染 Bug。

修复方案一（数据重构/不可变变通）：不用深拷贝，通过重新构建字典/列表的方式（例如重新创建内层 list），修改新样本而不污染原样本 data。

修复方案二（深拷贝）：使用标准库模块真正的深拷贝方式彻底解决该问题。