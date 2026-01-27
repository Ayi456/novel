---
name: 分镜字段扁平化
description: 将分镜中的结构化字段（如 visual_effects、characters 等）合并为可读的一段话描述，同时保留可选的结构化字段用于后续自动处理。适用于生成图像提示词、人工校对与快速阅读。
---

# 分镜字段扁平化技能

此技能用于把分镜中的**结构化信息**合并为**一段话**，提升可读性与生成提示词的直接性，并可选择保留原字段以便后续自动抽取。

## 何时使用此技能

**触发条件：**
- 用户希望“合并 visual_effects 为一段话”
- 用户希望 characters 更简洁（如“顾玄：画面中央,躺在床上”）
- 需要便于快速生成图像/分镜提示词

## 核心规则

1) **优先保留结构化字段**
- 保留 `environment / lighting / color_palette / special_effects`
- 保留 `position / action / expression / costume`

2) **新增 summary/description 字段**
- `visual_effects.summary`：合并环境/光线/色调/特效
- `characters[].description`：合并人物位置与动作

3) **扁平化不替代结构化**
- 扁平化用于阅读与提示词生成
- 结构化字段用于检索、批量处理、自动化

## 输入格式

接受完整分镜或单个镜头对象：

```json
{
  "shot_id": "EP01-S001",
  "visual_effects": { "environment": "...", "lighting": "...", "color_palette": "...", "special_effects": "..." },
  "characters": [{ "name": "顾玄", "position": "...", "action": "..." }]
}
```

## 输出格式（示例）

```json
{
  "shot_id": "EP01-S001",
  "visual_effects": {
    "environment": "窗外云雾缭绕,远处青山如黛,晨光微亮",
    "lighting": "自然光从窗户斜射,柔和昏暗",
    "color_palette": "暖色调,晨光金",
    "special_effects": "无",
    "summary": "窗外云雾缭绕，远处青山如黛，晨光微亮；自然光从窗户斜射，柔和昏暗；暖色调，晨光金。"
  },
  "characters": [
    {
      "name": "顾玄",
      "position": "画面中央",
      "action": "躺在床上",
      "description": "画面中央，顾玄躺在床上"
    }
  ]
}
```

## 扁平化模板

### visual_effects.summary
```
{environment}；{lighting}；{color_palette}；{special_effects}
```
如 `special_effects` 为“无”，可省略。

### characters[].description
```
{position}，{name}{action}
```
如果已有 costume/expression，可加括号补充：
```
{position}，{name}{action}（{expression}，{costume}）
```

## 质量检查清单

- [ ] summary/description 不改变原意
- [ ] 保留结构化字段（除非用户要求删除）
- [ ] 语句简洁，不重复堆叠
- [ ] 适合直接作为提示词片段使用

## 使用提示

- 需要“只读版”时优先使用 summary/description
- 需要自动化处理时使用结构化字段
- 若用户明确要求“彻底扁平化”，再移除结构字段
