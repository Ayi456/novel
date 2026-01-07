# 小说创作与版本管理系统

> 使用 Claude AI 辅助小说创作，通过 Git 进行专业版本管理

## ✨ 核心特色

- **AI 驱动创作**：利用 Claude 进行小说改写、优化和创意扩展
- **Git 版本控制**：完整追踪每次修改，轻松回溯任何版本
- **多本管理**：支持多部小说同时创作，每本小说独立章节管理
- **精彩点前置**：遵循"黄金开场"原则，第一章即抓住读者注意力

## 🚀 快速开始

### 初始化项目

```bash
# 克隆项目
git clone https://cnb.cool/zha-ji/novel
cd novel

# 查看分支
git branch -a
```

### 工作流程

#### 1. 创建项目结构

```bash
# 创建多本小说的目录结构
mkdir -p novels/novel-01/chapters
mkdir -p novels/novel-02/chapters

# 或批量创建
for i in {01..05}; do
  mkdir -p novels/novel-$i/chapters
done
```

**推荐目录结构**：

```
novel/
├── novels/
│   ├── novel-01/              # 第一部小说
│   │   ├── README.md          # 小说简介、人物设定
│   │   ├── outline.md         # 大纲
│   │   └── chapters/
│   │       ├── chapter-001.md
│   │       ├── chapter-002.md
│   │       └── ...
│   ├── novel-02/              # 第二部小说
│   │   ├── README.md
│   │   ├── outline.md
│   │   └── chapters/
│   │       ├── chapter-001.md
│   │       └── ...
│   └── ...
└── README.md                  # 项目总说明
```

#### 2. 创建新小说或导入现有小说

**方式一：创建新小说**

```bash
# 进入某部小说目录
cd novels/novel-01

# 创建小说基本文件
cat > README.md << 'EOF'
# 小说标题

## 简介
[小说简介]

## 人物设定
- **主角**：[姓名] - [性格特点]
- **配角**：[姓名] - [关系]

## 世界观设定
[背景设定]
EOF

# 创建大纲
cat > outline.md << 'EOF'
# 小说大纲

## 第一卷：[卷名]
- 第1-10章：[情节概要]
- 第11-20章：[情节概要]

## 第二卷：[卷名]
...
EOF

# 创建第一章
cat > chapters/chapter-001.md << 'EOF'
# 第一章：[章节标题]

[正文内容]
EOF

# 提交初始版本
git add .
git commit -m "feat(novel-01): 创建新小说项目结构"
```

**方式二：导入现有小说**

```bash
# 如果已有完整小说文本，可以拆分章节
cd novels/novel-01

# 假设原文件为 full-novel.txt，每章以"第X章"开头
# 使用脚本拆分（需要根据实际格式调整）
awk '/^第[0-9]+章/ {close(file); file=sprintf("chapters/chapter-%03d.md", ++i)} {print > file}' full-novel.txt

# 或手动复制章节
cp /path/to/chapter-01.txt chapters/chapter-001.md
cp /path/to/chapter-02.txt chapters/chapter-002.md

# 提交初始版本
git add .
git commit -m "feat(novel-01): 导入现有小说章节"
```

#### 3. 使用 Claude 优化小说章节

#### 3. 使用 Claude 优化小说章节

**关键原则：精彩点前置**

在与 Claude 交互时，明确以下改写目标：

- ✅ 第一章开头必须出现强烈冲突或悬念
- ✅ 前3000字即展现主角困境或核心欲望
- ✅ 删除铺垫过长的背景介绍
- ✅ 用场景描写和对话推进情节

**示例 Claude 提示词（单章节优化）**：

```
请帮我改写《小说名》第X章，要求：
1. 章节开头就有吸引力（悬念/冲突/意外）
2. 字数控制在 [目标字数] 字左右
3. 保持与前后章节的衔接
4. 突出人物性格和情感变化

当前章节内容：
[粘贴章节内容]

前情提要：
[简述前面章节的关键情节]
```

**示例 Claude 提示词（跨章节优化）**：

```
请帮我优化《小说名》第X-Y章的节奏，要求：
1. 分析当前这几章的节奏问题
2. 建议哪些章节需要合并或拆分
3. 提供具体的改写方向

章节概要：
第X章：[概要]
第Y章：[概要]
```

#### 4. 版本管理最佳实践

#### 4. 版本管理最佳实践

```bash
# 单章节修改后提交
cd novels/novel-01
git add chapters/chapter-001.md
git commit -m "refactor(novel-01/ch01): 精彩点前置 - 改写开场"

# 多章节修改后提交
git add chapters/chapter-001.md chapters/chapter-002.md
git commit -m "refactor(novel-01/ch01-02): 优化前两章节奏"

# 修改某本小说的大纲
git add novels/novel-01/outline.md
git commit -m "docs(novel-01): 更新第二卷大纲"

# 重大修改前创建分支（实验不同版本）
git checkout -b experiment/novel-01-dark-ending
cd novels/novel-01/chapters
# 在分支上修改最后几章
git commit -m "experiment(novel-01): 尝试暗黑向结局"

# 满意后合并回主分支
git checkout main
git merge experiment/novel-01-dark-ending

# 或者为某章节创建多个版本
git checkout -b version/ch10-emotional
# 修改第10章为情感向
git checkout main
git checkout -b version/ch10-action
# 修改第10章为动作向
# 后续可以对比两个版本选择更好的
```

**提交信息格式规范**：

```
<type>(<scope>): <description>

示例：
feat(novel-01/ch05): 添加新章节
refactor(novel-02/ch01-03): 重写前三章
fix(novel-01/outline): 修复时间线矛盾
```

## 📝 提交信息规范

使用语义化提交信息，便于追踪修改历史：

| 类型 | 说明 | 示例 |
|------|------|------|
| `feat` | 新增章节或角色 | `feat(novel-01/ch10): 添加第十章` |
| `refactor` | 重写或优化现有内容 | `refactor(novel-01/ch02): 重写第二章对话` |
| `fix` | 修复剧情漏洞 | `fix(novel-01): 修复时间线矛盾` |
| `polish` | 语言润色 | `polish(novel-02/ch05): 优化情感描写` |
| `experiment` | 实验性修改 | `experiment(novel-01): 尝试第一人称视角` |
| `docs` | 更新大纲或设定 | `docs(novel-01): 补充人物背景设定` |

## 📚 小说结构建议

**单本小说章节规划**：

```
novel-01/
├── README.md              # 小说设定（人物、世界观）
├── outline.md             # 完整大纲
└── chapters/
    ├── chapter-001.md     # 第1章 (精彩点前置)
    │   └── 开场：强烈冲突/悬念钩子
    ├── chapter-002.md     # 第2章
    │   └── 人物展示：性格、关系、动机
    ├── chapter-003.md     # 第3章
    │   └── 触发事件：主线剧情正式开始
    ├── chapter-004-020.md # 第4-20章
    │   └── 上升阶段：困难升级、伏笔铺设
    ├── chapter-021.md     # 第21章
    │   └── 中点转折：重大发现或失败
    ├── chapter-022-040.md # 第22-40章
    │   └── 深化阶段：真相浮现、关系变化
    ├── chapter-041-048.md # 第41-48章
    │   └── 高潮对抗：最终决战
    └── chapter-049-050.md # 第49-50章（结局）
        └── 结局：收尾、留白
```

**多本小说并行创作建议**：

- 使用 Git 分支隔离不同小说的大改动
- 每本小说独立的 README.md 记录创作进度
- 优先完成一本再开新坑，避免同时写多本导致混乱

## 🔄 常用 Git 命令

```bash
# 查看修改历史
git log --oneline --graph --all

# 查看某本小说的修改历史
git log --oneline -- novels/novel-01/

# 查看某个章节的修改历史
git log -p novels/novel-01/chapters/chapter-001.md

# 比较某章节的两个版本
git diff HEAD~1 HEAD -- novels/novel-01/chapters/chapter-001.md

# 回退某章节到之前版本（保留工作区）
git checkout HEAD~1 -- novels/novel-01/chapters/chapter-001.md

# 创建标签标记重要里程碑
git tag -a novel-01-v1.0 -m "《小说1》第一稿完成"
git tag -a novel-01-draft-2 -m "《小说1》第二稿完成"

# 查看所有标签
git tag -l

# 查看某本小说的所有标签
git tag -l "novel-01-*"
```

## 💡 与 Claude 协作技巧

### 迭代式改写流程

1. **章节提交**：将单个或多个章节提交给 Claude
2. **定向优化**：每次只改写1-2个章节，保持可控
3. **立即版本控制**：每次改写后立即 git commit
4. **AB 测试**：用分支保存同一章节的不同版本，对比效果

**多章节协同优化**：

```bash
# 场景1：优化连续章节的衔接
# 同时把第5-7章发给Claude，要求优化过渡

# 场景2：批量优化某类问题
# 找出所有对话过多的章节，批量优化
grep -l "对话占比过高" novels/novel-01/chapters/*.md

# 场景3：跨章节伏笔检查
# 让Claude检查前10章埋下的伏笔在后续章节是否回收
```

### 高效提示词模板

**章节改写**：
```
改写《[小说名]》第X章，要求：
- 字数控制在 [目标字数] 字
- 突出 [情感/冲突/悬念]
- 保持人物 [A] 和 [B] 的核心特质
- 与第X-1章和第X+1章自然衔接

第X章当前内容：
[粘贴章节内容]

相关上下文：
- 前一章结尾：[简述]
- 后一章开头：[简述]
```

**多章节批量分析**：
```
分析《[小说名]》第X-Y章（共N章），请：
1. 评估整体节奏是否合理
2. 指出节奏拖沓或过快的章节
3. 建议章节合并、拆分或删减方案
4. 标注伏笔和回收情况

[粘贴多个章节的概要或全文]
```

**精彩点前置检查**：
```
分析《[小说名]》第一章是否符合"精彩点前置"原则：
1. 前3000字是否有强烈钩子（冲突/悬念/意外）？
2. 主角目标和困境是否清晰？
3. 是否有多余的背景铺垫和说明文字？
4. 开场是否能让读者产生"想继续读下去"的欲望？

给出具体改进建议和改写方向。

第一章内容：
[粘贴第一章全文]
```

## 📊 版本对比工具

推荐使用 Git GUI 工具对比版本：

- **SourceTree**（可视化分支管理）
- **GitKraken**（适合复杂分支）
- **VS Code Git 扩展**（集成编辑器）

## 🎯 创作检查清单

完成每次改写后，检查：

- [ ] 第一章前3000字是否有明确冲突/悬念？
- [ ] 对话是否推动剧情（避免闲聊式对话）？
- [ ] 场景描写是否生动（五感描写）？
- [ ] 人物动机和目标是否清晰？
- [ ] 章节之间的衔接是否自然？
- [ ] 伏笔是否在合理章节回收？
- [ ] 已提交 Git 版本控制？
- [ ] 章节命名是否规范（chapter-XXX.md）？

## 📚 相关资源

- [小说创作技巧](https://example.com)
- [精彩点前置理论](https://example.com)
- [网文写作节奏把控](https://example.com)
- [Git 版本管理进阶](https://git-scm.com/book/zh/v2)
- [Markdown 格式指南](https://example.com)

## 🤝 贡献指南

欢迎提交 Pull Request 分享你的创作技巧！

---

**开始创作吧！记住：好的故事从第一页就开始。** 🎬