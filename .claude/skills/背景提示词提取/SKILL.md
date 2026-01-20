---
name: 主场景、副场景背景提示词提取
description: 为仙侠/修真小说场景生成背景图像提示词。主场景基于氛围、事件状态、季节等多维度变化，副场景是主场景的局部细节特写。当用户想要基于小说分镜或场景描述为AI图像生成工具（Midjourney、Stable Diffusion等）创建场景描述时使用。输出高质量中文仙侠风格提示词，包含恰当的光照、氛围和构图细节。
---

# 仙侠小说背景提示词生成器

此技能为中文仙侠/修真小说生成高质量的背景图像提示词。所有提示词都指定干净的背景，不包含人物、文本或UI元素，适合AI图像生成工具。

## 何时使用此技能

**触发条件：**
- 用户提到为小说/漫画创建场景背景
- 用户想要用于Midjourney、Stable Diffusion或其他AI图像生成器的提示词
- 用户需要修真/仙侠场景的视觉描述
- 用户正在制作分镜或场景规划

**此技能的功能：**
- 分析场景信息（位置、氛围、事件状态）
- 生成详细的中文仙侠风格图像提示词
- 确保提示词指定：无人物、无文本、无UI元素
- 创建基于多维度变化的主场景（氛围、事件状态、季节、视角、特殊现象）
- 生成主场景的副场景（局部特写、细节衍生）
- 保持一致的修真/仙侠美学

## 输入格式

接受任何格式的场景信息。提取以下关键元素：

**必需：**
- `location`：场景位置（如"青云宗外门弟子房"、"主殿"、"练功场"）

**可选但有帮助：**
- `visual_effects.environment`：环境细节（雾、山、天气）
- `visual_effects.lighting`：具体光照描述
- `visual_effects.color_palette`：色彩基调或氛围

输入示例：
```json
{
  "shot_id": "EP01-S001",
  "location": "青云宗外门弟子房",
  "visual_effects": {
    "environment": "窗外云雾缭绕,远处青山如黛",
    "lighting": "自然光从窗户斜射,柔和昏暗",
    "color_palette": "暖色调,晨光金"
  }
}
```

## 输出格式

生成符合以下JSON结构的数据:

```json
{
  "scenes": [
    {
      "id": "scene-XXX",
      "name": "地点名称-氛围状态",
      "location_type": "室内/室外/特殊空间",
      "atmosphere": "氛围状态",
      "main_prompt": "完整的英文图像生成提示词",
      "main_prompt_cn": "完整的中文图像生成提示词",
      "sub_scenes": [
        {
          "name": "副场景名称",
          "prompt": "副场景的英文提示词",
          "prompt_cn": "副场景的中文提示词"
        }
      ],
      "tags": ["标签1", "标签2", ...],
      "usage_count": 数字,
      "description": "中文场景描述"
    }
  ],
  "metadata": {
    "version": "版本号",
    "created_date": "创建日期",
    "total_scenes": "场景总数",
    "description": "整体描述"
  }
}
```

### 提示词构建指南

在实际生成提示词时，按照以下结构组装：

**基础格式：**
```
Chinese xianxia style, [场景描述], [光照], [色彩], [修真氛围], [质量修饰符], 无人物、无文本、无UI元素
```

**组成部分说明：**

**1. 风格前缀**（始终包含）
- `Chinese xianxia style` - 确立修真美学

**2. 场景描述**
- 室内：建筑细节、家具、房间特征
- 室外：自然环境、建筑、地形
- 特殊空间：神秘元素、阵法、屏障

**3. 光照**
根据氛围和事件状态匹配相应的光照关键词：

| 氛围/状态 | 光照关键词 | 色调 |
|------|-------------------|------------|
| 宁静祥和 | soft natural light, gentle illumination, warm glow | warm, soft, peaceful |
| 肃穆庄严 | strong directional light, dramatic shadows, golden beams | high contrast, solemn |
| 神秘莫测 | ethereal glow, mystical light, bioluminescence | dreamy, otherworldly |
| 压迫凝重 | dark ambient light, shadows, dim lighting | dark, moody, tense |
| 灵动飘逸 | bright spiritual light, radiating energy, luminous | bright, ethereal |
| 日常状态 | natural daylight, soft ambient light | natural, balanced |
| 修炼状态 | flowing spiritual light, energy glow, inner radiance | mystical, energized |
| 突破时刻 | brilliant light, pillar of light, heavenly phenomenon | dramatic, divine |
| 战斗之后 | fading light, ember glow, damaged environment | somber, aftermath |
| 仪式进行 | ritual flames, ceremonial light, altar illumination | sacred, ceremonial |

**4. 修真关键词**（每个提示词使用2-3个）

*建筑：*
- cultivation sect, pavilion, altar, mountain gate, secret realm
- ancient temple, meditation hall, training ground, scripture pavilion

*自然：*
- sea of clouds, spiritual energy, ancient trees, mysterious mist
- mountain peaks, floating islands, spiritual spring, mystical forest

*效果：*
- magical formations, glowing runes, spiritual herbs, treasure light
- barrier, ethereal glow, mystical aura, cultivation atmosphere

*氛围：*
- ethereal, ancient, mysterious, solemn, peaceful, dangerous
- transcendent, otherworldly, mystical

**5. 质量修饰符**（始终包含）
- `high quality, detailed, 8k resolution`

**6. 排除项**（始终包含）
- `no people, no text, no UI elements, no characters, no writing, no symbols`

## 场景类型检测

根据位置关键词确定场景类型：

**室内**
关键词：房、殿、堂、阁、室、屋

描述示例：
- 简陋木屋：`humble wooden room in cultivation sect, simple wooden furniture, wooden bed, wooden table, paper window`
- 宏伟大殿：`grand main hall of cultivation sect, ornate pillars, stone floor, ceremonial altar, spiritual symbols`
- 修炼室：`cultivation training room, meditation cushions, wooden floor, incense burner, tranquil atmosphere`

**室外**
非室内、非特殊空间的默认类型

描述示例：
- 山门：`majestic mountain gate of cultivation sect, stone stairs, ancient architecture, mountain peaks in background`
- 庭院：`open courtyard plaza in cultivation sect, stone pavement, traditional buildings surrounding, open sky`
- 山区：`secluded mountain area behind sect, ancient trees, stone path, spiritual energy gathering spots`

**特殊空间**
关键词：秘境、异空间、结界、虚空

描述示例：
- `mystical space, [位置], glowing runes, magical barrier, spiritual energy, ethereal atmosphere`

## 生成主场景

1. **识别唯一组合**：每个（位置 + 氛围/状态）组合应生成一个唯一的主场景
2. **确定场景类型**：根据位置关键词归类为室内/室外/特殊
3. **构建描述**：选择适当的场景描述模板
4. **添加光照和色彩**：匹配氛围和事件状态
5. **包含修真元素**：添加2-3个相关的修真关键词
6. **应用质量和排除项**：始终附加质量修饰符和排除术语

## 生成主场景变体

主场景应该基于多种维度进行变化，而不仅仅是简单的时间区分：

**1. 氛围与情绪变化**
- 宁静祥和：适合日常修行、冥想
- 肃穆庄严：适合宗门大典、重要仪式
- 神秘莫测：适合秘境探索、奇遇
- 压迫凝重：适合危机时刻、战斗前奏
- 灵动飘逸：适合顿悟、突破时刻

**2. 事件状态变化**
- 日常状态：平静无事的常规场景
- 修炼状态：灵气流动、阵法激活
- 突破时刻：天象异变、光柱冲天
- 战斗之后：破坏痕迹、能量残留
- 仪式进行：法阵运转、符文闪烁

**3. 季节与时节变化**
- 春季：新生萌芽、花开、生机勃勃
- 夏季：繁茂葱郁、热烈、雷雨前夕
- 秋季：落叶飘零、萧瑟、金黄色调
- 冬季：银装素裹、寂静、寒冷氛围
- 特殊时节：宗门大典、论道大会、试炼开启

**4. 视角与构图变化**
- 全景俯视：展现整体环境布局
- 仰视宏伟：突出建筑的庄严高大
- 平视沉浸：身临其境的日常视角
- 特写聚焦：强调关键元素的细节

**5. 特殊现象变化**
- 灵气浓郁：可见灵气流动、光点闪烁
- 天象异变：异象环生、奇光异彩
- 禁制触发：结界显现、符文流转
- 宝物出世：霞光万道、瑞气千条

**主场景变体示例：**
*基础位置：*"青云宗外门弟子房"
*主场景变体：*
- "青云宗外门弟子房-清晨日常"（宁静晨光、日常状态）
- "青云宗外门弟子房-修炼突破"（灵气涌动、突破时刻）
- "青云宗外门弟子房-雨夜肃杀"（雷雨交加、危机氛围）
- "青云宗外门弟子房-冬日萧瑟"（雪花飘落、寒冷寂静）

## 生成副场景（细节衍生）

副场景是基于对应主场景的局部特写或细节展开，展示主场景中的具体元素：

**1. 局部特写**
- 家陈设细节：古朴桌案、蒲团、香炉
- 建筑细节：雕梁画栋、窗棂花纹、石质纹理
- 自然细节：花草叶片、水波纹路、树皮肌理
- 器物细节：法器表面、符箓纹理、阵法纹路

**2. 角度微调**
- 同一主场景的不同角度呈现
- 从近景到中景的变化
- 从高处俯瞰与低处仰视的对比

**3. 细节变化**
- 主场景中某个元素的细微变化
- 光影投射的不同效果
- 季节在细节上的体现

**副场景示例：**
*主场景：*"青云宗外门弟子房-清晨日常"
*副场景：*
- "木桌案上的修炼典籍"（特写桌上散放的书籍）
- "窗纸透进来的晨光投影"（特写窗户光影效果）
- "青瓷香炉的袅袅轻烟"（特写香炉烟雾细节）
- "床榻旁的佩剑与法器"（特写武器道具摆放）

## 提示词示例

### 室内场景 - 宁静日常
```
Chinese xianxia style, humble wooden room in cultivation sect, simple wooden furniture, wooden bed, wooden table, soft natural light through paper window, misty mountains visible outside window, warm golden lighting, peaceful cultivation atmosphere, high quality, detailed, 8k resolution, no people, no text, no UI elements
```

### 室外场景 - 肃穆庄严
```
Chinese xianxia style, majestic mountain gate of cultivation sect, stone stairs, ancient architecture, mountain peaks in background, strong directional light, dramatic shadows, golden beams, solemn cultivation atmosphere, high quality, detailed, 8k resolution, no people, no text, no UI elements
```

### 特殊空间 - 神秘莫测
```
Chinese xianxia style, mystical secret realm, glowing magical formations, blue runes on stone floor, ethereal barrier, ethereal glow, bioluminescence, spiritual energy gathering spots, mysterious cultivation atmosphere, high quality, detailed, 8k resolution, no people, no text, no UI elements
```

## 质量检查清单

生成提示词后，验证：

- [ ] 所有提示词包含"Chinese xianxia style"
- [ ] 所有提示词包含"no people, no text, no UI elements"
- [ ] 所有提示词包含质量修饰符："high quality, detailed, 8k resolution"
- [ ] 主场景基于多维度变化（氛围、事件状态、季节、视角、特殊现象）
- [ ] 副场景是对应主场景的局部特写或细节衍生
- [ ] 主场景变化丰富，不局限于简单的白天/黑天区分
- [ ] 光照和色彩与氛围、事件状态匹配
- [ ] 修真关键词使用得当
- [ ] 场景类型（室内/室外/特殊）正确识别
- [ ] 描述具体详细，不泛泛而谈

## 使用技巧

**用于小说插图：**
- 为常用位置生成主场景
- 为不同情绪创建氛围/状态变体
- 使用特写强调重要细节

**用于AI动画/漫画：**
- 首先批量生成所有主场景
- 为不同情感节拍创建变体
- 在相似位置之间保持一致性

**用于场景规划：**
- 使用提示词在写作前可视化场景
- 生成多个变体以探索美学选项
- 为同一位置测试不同氛围

## 重要提示

1. **一致性**：对相关位置使用相似的术语和关键词
2. **无现代元素**：严格保持仙侠/修真美学（除非另有说明）
3. **质量优于数量**：最好有较少、精心制作的提示词，而不是许多通用的提示词
4. **具体细节**：包含具体的视觉元素（不仅仅是"美丽的风景"）
5. **强制排除**：始终明确排除人物、文本和UI元素

## 示例工作流程

**用户请求：**"为每一章的分镜生成背景提示词"

**响应：**
1. 读取分镜文件以提取场景
2. 识别所有唯一的（位置 + 基础氛围/状态）组合
3. 对于每个组合：
   - 确定场景类型（室内/室外/特殊）
   - 基于多维度生成主场景变体（氛围、事件状态、季节、视角、特殊现象）
   - 为每个主场景生成2-3个副场景（局部特写、细节衍生）
4. 输出格式为JSON或markdown，包含：
   - 场景ID
   - 场景名称
   - 位置类型
   - 变化维度（氛围/事件/季节/视角）
   - 主提示词
   - 副场景列表（基于主场景的细节特写）
   - 标签
   - 描述
5. 验证所有质量检查清单项通过

---

**记住：**目标是生成干净、有氛围的背景图像，捕捉中国仙侠修真世界的精髓。每个提示词都应将观看者带入一个神秘的、古代的武术和精神修炼领域。
