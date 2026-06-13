---
name: 语料索引库建立维护pipeline
description: Index_builder是一个，为了支持“BM25检索和向量检索的混合检索”，而以query的历史数据和各类字典为数据，在用户参与人工审核情况下，来建立，维护，改善语料索引库的一个python项目。**是建立索引，而不是去进行检索**。为了创建，测试完善这个项目，使用了低压电气柜的装配制造过程中的缺陷原始数据，以“电气柜制造缺陷意图分类与匹配系统”的索引库建立为目标开始项目。
author: Guo Fei
---

# 1. 项目目录结构

[节点链接](documents/project_files_index.md)

# 2. 工作流程与节点

## 完整工作流概览



## 节点 从原始查询数据raw.csv生成queries_raw.jsonl
[节点链接](documents/节点raw处理.md)


## 节点 构建 intent_catalog 字段
[节点链接](documents/catalog构建.md)


## 节点 BM25算法将query分配到intent进行试算测试
[节点链接](documents/BM25试算.md)


## 节点 试算测试结果人工审核
[节点链接](documents/人工审核.md)


## 节点 输入与循环
[节点链接](documents/输出与循环.md)




# 4. 测试用数据讲解
目前 intent_catalog.jsonl分大品类
- 二次线
- 元器件
- 铜排
- 机械/电气连接
- 钣金结构
- 标记标识
- 外观
- 防护
- 构型图纸
- 清洁5S
- 工艺记录


## 应用场景

该项目面向**电气设备制造业**的质量检查场景，具体应用于：
- **缺陷记录自动分类**：将生产巡检中记录的各类缺陷描述自动归类到标准缺陷库
- **质检数据标准化**：将非结构化的自然语言缺陷描述标准化为结构化数据
- **减少人工标注工作量**：通过"自动分配 + 人工审核"的混合模式提升效率


## 核心技术思路

1. **最终输出字段键值要支持双路检索架构**：
   - **BM25关键词检索**：基于词频和逆文档频率的传统检索方法，擅长精确匹配
   - **向量语义检索**：基于嵌入向量的语义相似度检索，擅长语义理解（当前为占位实现）

2. **结果融合策略**：
   - 使用 **RRF (Reciprocal Rank Fusion)** 算法融合两路检索结果
   - 通过阈值和边距策略决定最终分配意图

部分模块仍为简单占位实现，可进一步扩展：
- Tokenizer可接入真实分词库（如jieba）
- DummyEmbedder可替换为真实预训练语言模型（如BGE、Sentence-Transformers等）
- 可接入FAISS索引提升向量检索效率


python -m src.main.run_prepare_catalog_pipeline
然后：


python -m src.main.run_assign_query_to_intent
人工审核后：


python -m src.main.run_collect_catalog_feedback --reviewed-only
如果想重新用 LLM 补齐扩展字段：


python -m src.main.run_enrich_intent_catalog --llm
python -m src.main.run_build_intent_fields
目前唯一未完成项
实际数据文件还没生成：


data/raw/intent_seed.jsonl
data/processed/intent_catalog_enriched.jsonl
data/published/intent_catalog.jsonl
原因是你要求取消 pip 安装，我已停止安装流程。等你自己装好 requirements 后，运行：





intent端修改完成，开始query端。
1.先查看”1.query的使用与处理.md“里的 ”## 字段定义“，修改对应的schema和scripts。
2.参考临时文件夹下的preprocesss_lexical.py，src下创建脚本，完成从raw.csv这个query原始数据，依赖dict下的辞典，生成querise_raw.jsonl, 新增其他键值。




