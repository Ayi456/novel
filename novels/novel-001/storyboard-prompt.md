# 特效仙人的多元宇宙之旅 - 分镜生成提示词

## 使用说明

本文件用于根据小说章节内容自动生成分镜脚本。分镜输出为数组格式,每个元素代表一个镜头,包含详细的视觉、听觉和执行信息。

---

## 分镜数组格式规范

每个分镜镜头应包含以下字段：

```typescript
interface StoryboardShot {
  // 基础信息
  shot_id: string;              // 镜头编号 (例: "EP01-S001")
  chapter_number: number;       // 章节编号 (1-36)
  scene_number: number;         // 场景编号 (从1开始)

  // 时长控制
  duration: number;             // 镜头时长(秒)

  // 镜头类型
  shot_type: string;            // 镜头类型: 远景/全景/中景/近景/特写/大特写/俯视/仰视/航拍/跟踪/摇镜/推拉/跟随/主观视角/上帝视角

  // 场景描述
  location: string;             // 场景地点 (例: "青云宗外门弟子房" / "山门广场" / "后院空地")
  time_of_day: string;          // 时间 (例: "清晨" / "正午" / "黄昏" / "夜晚")

  // 画面构图
  composition: {
    camera_position: string;    // 机位描述 (例: "房间角落,面向床榻" / "山门侧前方,仰角30度")
    camera_movement: string;    // 镜头运动 (例: "缓慢推近" / "从左至右摇摄" / "环绕拍摄" / "固定镜头")
    framing: string;            // 构图方式 (例: "三分法" / "中心构图" / "黄金分割" / "对称构图")
    focus_type: string;         // 焦点类型 (例: "主体清晰,背景虚化" / "全景深" / "焦点从前景转移至背景")
  };

  // 人物信息
  characters: Array<{
    name: string;               // 人物名称
    position: string;           // 在画面中的位置 (例: "画面中央,躺在床上" / "左侧,站立")
    action: string;             // 动作描述 (例: "猛然坐起,环顾四周" / "负手而立,45度角望天")
    expression: string;         // 表情 (例: "困惑" / "震惊" / "淡定" / "狂喜")
    costume: string;            // 服装 (例: "粗布麻衣" / "白衣,衣袂飘飘" / "布衣少女")
    props?: string;             // 道具 (例: "铁剑" / "《青云炼气诀》书册")
  }>;

  // 视觉特效
  visual_effects: {
    environment: string;        // 环境特效 (例: "窗外云雾缭绕,远处青山如黛" / "乌云密布,电蛇游走")
    lighting: string;           // 光线 (例: "自然光从窗户斜射" / "昏暗油灯光线" / "金色光芒璀璨夺目")
    color_palette: string;      // 色调 (例: "暖色调" / "冷色调" / "高对比度" / "柔和光线")
    special_effects?: string;   // 特殊特效 (例: "周身金光大盛,雷电游走" / "飞剑拖出长长的光尾" / "半透明系统界面浮现在眼前")
  };

  // 声音设计
  audio: {
    dialogue?: string;          // 对话内容
    narration?: string;         // 旁白内容
    internal_monologue?: string;// 内心独白
    background_music: string;   // 背景音乐 (例: "轻快悠扬" / "紧张悬疑" / "恢弘大气" / "幽默搞笑")
    sound_effects: string[];    // 音效列表 (例: ["木门吱呀声"] / ["雷声轰隆" / "风声呼啸"] / ["系统机械音" / "飞剑破空声"])
    volume_level: string;       // 音量 (例: "对话为主,音效为辅" / "音效突出,压过背景音")
  };

  // 剪辑节奏
  editing: {
    transition_to_next: string; // 转场方式 (例: "直接切" / "淡出" / "淡入" / "叠化" / "划像" / "快速闪切")
    pacing: string;             // 节奏 (例: "舒缓" / "紧张" / "中等" / "快速")
    purpose: string;            // 镜头目的 (例: "建立场景" / "展示人物困惑" / "强调特效震撼" / "制造笑点")
  };

  // 注释说明
  notes: {
    production_note: string;    // 制作备注 (例: "需要CG制作系统界面" / "实景拍摄+后期特效" / "需要特效化妆")
    reference_style?: string;   // 参考风格 (例: "传统仙侠风" / "现代修仙轻喜剧" / "赛博朋克未来感")
    difficulty_level: string;   // 制作难度 (例: "简单" / "中等" / "复杂" / "需要大量特效")
  };
}
```

---

## 核心视觉风格

### 整体基调
- **风格定位**: 现代修仙轻喜剧
- **视觉特色**: 传统仙侠场景 + 现代系统特效 + 幽默反差
- **色彩体系**:
  - 正常场景: 自然色调,偏暖色系
  - 特效场景: 金色/银色/雷电蓝等高对比度
  - 系统界面: 半透明蓝白色,科技感

### 特效分级
1. **初级特效** (10-50积分)
   - 金色光晕,基础雷电
   - 飞剑光尾
   - 透明界面浮现

2. **中级特效** (50-200积分)
   - 大规模雷电
   - 绝对防御屏障
   - 天魔威压黑气

3. **高级特效** (200+积分)
   - 规则修改类效果
   - 世界壁垒破碎
   - 虚空对抗

---

## 主要人物视觉设定

### 顾玄 (特效仙人)
- **年龄**: 18岁外观
- **外貌**: 俊美如谪仙,白衣飘逸
- **服装**: 粗布麻衣(初期) → 白衣(后期)
- **特征**:
  - 表面: 高冷淡然,仙风道骨
  - 内心: 吐槽狂魔,慌得一批
- **标志性动作**:
  - 45度角望天
  - 负手而立
  - 强行镇定拍尘土

### 陆尘 (天命之子)
- **年龄**: 16-17岁外观
- **外貌**: 眉宇间透着倔劲
- **服装**: 布衣少女(初期) → 弟子服
- **特征**:
  - 纯真善良
  - 崇拜顾玄
  - 执着勤奋
- **特殊体质**: 药灵体(隐藏),对雷灵力亲和

### 李道玄 (青云宗掌门)
- **年龄**: 须发花白的老者
- **外貌**: 仙风道骨,但表情丰富
- **特征**:
  - 睡觉流口水
  - 爱吹牛
  - 护犊子

---

## 章节分镜生成要点

### 第一章: 穿越与系统 (参考章节)

**关键场景拆分**:

1. **开场场景** (陌生环境醒来)
   - 镜头节奏: 缓慢,困惑感
   - 色调: 昏暗,晨光微亮
   - 重点: 展现主角困惑和记忆融合

2. **系统激活** (半透明界面浮现)
   - 镜头节奏: 中等
   - 特效重点: 界面浮现,机械音响起
   - 幽默元素: 顾玄的吐槽反应

3. **第一次特效尝试** (金光大盛)
   - 镜头节奏: 快速,震撼
   - 特效重点: 金色光芒,雷电游走
   - 音效: "噗"的一声消失(反差)

4. **御剑飞行** (含特效版)
   - 镜头节奏: 航拍 + 跟拍
   - 特效重点: 飞剑光尾,周身光晕
   - 画面: 宛如流星划过天际

5. **山门登场** (狗啃泥摔落)
   - 镜头节奏: 先震撼后搞笑
   - 反差设计: 仙气飘飘 → 积分耗尽 → 狗啃泥
   - 音效: 全场寂静 → 哄堂大笑

6. **招收弟子** (陆尘登场)
   - 镜头节奏: 温情
   - 重点: 展现陆尘的倔强和顾玄的认可

7. **展现实力** (吸收雷霆)
   - 镜头节奏: 紧张刺激
   - 特效重点: 雷霆吸收,反向射出
   - 反转: 系统自动防御(内心慌乱)

8. **化解危机** (天魔威压)
   - 镜头节奏: 压抑 → 释放
   - 特效重点: 黑气缭绕,恐怖威压
   - 重点: "滚"字的力量

### 第二章: 雷淬师弟 (参考章节)

**关键场景拆分**:

1. **主殿入门** (破旧主殿)
   - 镜头节奏: 幽默
   - 视觉重点: 四面漏风的破屋子 vs 庄重仪式

2. **后院教学** (引气入体失败)
   - 镜头节奏: 缓慢,尴尬
   - 重点: 陆尘的执着 vs 无灵根的现实

3. **雷劫降临** (意外触发)
   - 镜头节奏: 紧张
   - 特效重点: 乌云密布,电蛇游走
   - 危机: 陆尘走火入魔

4. **引雷淬体** (误打误撞)
   - 镜头节奏: 震撼
   - 特效重点: 落雷,老槐树化为焦炭
   - 反转: 顾玄手上缠绕电弧

5. **真相误解** (强行挽尊)
   - 镜头节奏: 幽默
   - 重点: 掌门加戏,陆尘崇拜,顾玄内心崩溃

---

## 通用分镜生成规则

### 镜头节奏控制

**舒缓场景** (日常、对话、思考):
- 时长: 5-10秒/镜头
- 镜头运动: 缓慢推拉或固定
- 转场: 淡入淡出

**紧张场景** (战斗、危机、特效):
- 时长: 2-5秒/镜头
- 镜头运动: 快速切换,动态跟拍
- 转场: 直接切或闪切

**幽默场景** (搞笑、反差):
- 时长: 3-7秒/镜头
- 镜头运动: 夸张视角
- 转场: 突然切或定格

### 特效场景制作要点

1. **特效前后对比**
   - 前: 正常画面
   - 后: 特效爆发
   - 反差: 强调视觉冲击

2. **积分耗尽设计**
   - 特效忽明忽暗
   - "接触不良"灯泡效果
   - "噗"的一声全灭

3. **系统界面呈现**
   - 半透明蓝白界面
   - 文字清晰易读
   - 浮现在人物眼前或画面一角

### 音效设计要点

**对话场景**:
- 对话清晰为主
- 背景音轻柔
- 适当环境音

**特效场景**:
- 音效突出
- 轰鸣声、雷电声
- 系统机械音

**幽默场景**:
- 突然静音(尴尬时刻)
- 音效卡点(摔跤时"咚")
- 反差音效(仙气音乐突然切断)

---

## 章节模板生成示例

### 第一章部分分镜示例

```json
[
  {
    "shot_id": "EP01-S001",
    "chapter_number": 1,
    "scene_number": 1,
    "duration": 8,
    "shot_type": "特写",
    "location": "青云宗外门弟子房",
    "time_of_day": "清晨",
    "composition": {
      "camera_position": "床榻正上方,俯视",
      "camera_movement": "缓慢拉远",
      "framing": "中心构图",
      "focus_type": "主体清晰,周围环境逐渐入画"
    },
    "characters": [
      {
        "name": "顾玄",
        "position": "画面中央,躺在床上",
        "action": "缓缓睁眼,眼神迷茫,然后猛地坐起",
        "expression": "困惑 → 震惊",
        "costume": "粗布麻衣"
      }
    ],
    "visual_effects": {
      "environment": "窗外云雾缭绕,远处青山如黛,晨光微亮",
      "lighting": "自然光从窗户斜射,柔和昏暗",
      "color_palette": "暖色调,晨光金",
      "special_effects": "无"
    },
    "audio": {
      "dialogue": "",
      "narration": "",
      "internal_monologue": "这是……哪里？",
      "background_music": "轻柔神秘,缓慢引入",
      "sound_effects": ["鸟鸣声", "木床轻微嘎吱声"],
      "volume_level": "环境音为主,营造陌生感"
    },
    "editing": {
      "transition_to_next": "直接切",
      "pacing": "舒缓",
      "purpose": "建立开场场景,展现主角困惑"
    },
    "notes": {
      "production_note": "实景拍摄,晨光效果",
      "reference_style": "传统仙侠场景",
      "difficulty_level": "简单"
    }
  },
  {
    "shot_id": "EP01-S002",
    "chapter_number": 1,
    "scene_number": 1,
    "duration": 6,
    "shot_type": "中景",
    "location": "青云宗外门弟子房",
    "time_of_day": "清晨",
    "composition": {
      "camera_position": "房间角落,面向床榻",
      "camera_movement": "固定镜头",
      "framing": "三分法",
      "focus_type": "主体清晰,背景略虚化"
    },
    "characters": [
      {
        "name": "顾玄",
        "position": "画面右侧,坐在床边",
        "action": "环顾四周,揉太阳穴,表情凝重",
        "expression": "困惑 → 思考",
        "costume": "粗布麻衣"
      }
    ],
    "visual_effects": {
      "environment": "简陋的木屋,陈设简单",
      "lighting": "昏暗自然光",
      "color_palette": "暖色调,偏暗",
      "special_effects": "无"
    },
    "audio": {
      "dialogue": "",
      "narration": "",
      "internal_monologue": "所以……我穿越了？而且是那种开局就是废材流的老套剧情？",
      "background_music": "轻柔带点幽默感",
      "sound_effects": [],
      "volume_level": "内心独白为主"
    },
    "editing": {
      "transition_to_next": "直接切",
      "pacing": "舒缓",
      "purpose": "展现主角的认知过程,带吐槽风格"
    },
    "notes": {
      "production_note": "实景拍摄",
      "reference_style": "现代修仙轻喜剧",
      "difficulty_level": "简单"
    }
  },
  {
    "shot_id": "EP01-S003",
    "chapter_number": 1,
    "scene_number": 1,
    "duration": 5,
    "shot_type": "特写",
    "location": "顾玄脑海/眼前",
    "time_of_day": "清晨",
    "composition": {
      "camera_position": "主观视角",
      "camera_movement": "界面浮入",
      "framing": "中心构图",
      "focus_type": "界面文字清晰,背景模糊"
    },
    "characters": [],
    "visual_effects": {
      "environment": "半透明蓝色界面浮现",
      "lighting": "界面自发光",
      "color_palette": "冷色调,蓝白色",
      "special_effects": "半透明界面,文字清晰显示:【天魔系统已激活】【正在绑定宿主……绑定完成】"
    },
    "audio": {
      "dialogue": "",
      "narration": "",
      "internal_monologue": "",
      "background_music": "科技感机械音背景",
      "sound_effects": ["系统机械音: '天魔系统已激活'"],
      "volume_level": "机械音突出"
    },
    "editing": {
      "transition_to_next": "直接切",
      "pacing": "中等",
      "purpose": "系统登场,关键设定"
    },
    "notes": {
      "production_note": "需要CG制作系统界面",
      "reference_style": "科技感+仙侠结合",
      "difficulty_level": "中等"
    }
  },
  {
    "shot_id": "EP01-S004",
    "chapter_number": 1,
    "scene_number": 1,
    "duration": 7,
    "shot_type": "近景",
    "location": "青云宗外门弟子房",
    "time_of_day": "清晨",
    "composition": {
      "camera_position": "正面拍摄",
      "camera_movement": "轻微推近",
      "framing": "中心构图",
      "focus_type": "主体清晰"
    },
    "characters": [
      {
        "name": "顾玄",
        "position": "画面中央",
        "action": "看着眼前界面,表情震惊",
        "expression": "震惊 → 疑惑",
        "costume": "粗布麻衣"
      }
    ],
    "visual_effects": {
      "environment": "木屋内景",
      "lighting": "昏暗自然光 + 界面蓝光",
      "color_palette": "冷暖对比",
      "special_effects": "系统界面浮现在眼前,显示详细信息"
    },
    "audio": {
      "dialogue": "等等,什么天魔系统？什么管理员？",
      "narration": "",
      "internal_monologue": "",
      "background_music": "轻快带悬疑",
      "sound_effects": ["系统机械音持续"],
      "volume_level": "对话为主"
    },
    "editing": {
      "transition_to_next": "直接切",
      "pacing": "中等",
      "purpose": "展示主角对系统的困惑"
    },
    "notes": {
      "production_note": "实景+CG界面",
      "reference_style": "现代修仙轻喜剧",
      "difficulty_level": "中等"
    }
  },
  {
    "shot_id": "EP01-S005",
    "chapter_number": 1,
    "scene_number": 1,
    "duration": 10,
    "shot_type": "特效特写",
    "location": "青云宗外门弟子房",
    "time_of_day": "清晨",
    "composition": {
      "camera_position": "环绕拍摄",
      "camera_movement": "快速环绕",
      "framing": "动态构图",
      "focus_type": "主体清晰,特效突出"
    },
    "characters": [
      {
        "name": "顾玄",
        "position": "画面中央",
        "action": "激活特效,周身金光大盛,被自己的特效吓一跳",
        "expression": "期待 → 震惊 → 慌乱",
        "costume": "粗布麻衣"
      }
    ],
    "visual_effects": {
      "environment": "木屋被金光照亮,如白昼",
      "lighting": "金色光芒璀璨夺目",
      "color_palette": "高对比度,金色为主",
      "special_effects": "周身金光大盛,雷电游走,视觉效果拉满,整个木屋被照得亮如白昼"
    },
    "audio": {
      "dialogue": "卧槽！",
      "narration": "",
      "internal_monologue": "这特效也太夸张了吧！跟不要钱似的！",
      "background_music": "恢弘震撼",
      "sound_effects": ["能量涌动声", "雷电噼啪声", "系统提示音"],
      "volume_level": "音效突出"
    },
    "editing": {
      "transition_to_next": "直接切",
      "pacing": "快速",
      "purpose": "展示系统特效的震撼,制造笑点"
    },
    "notes": {
      "production_note": "需要大量CG特效",
      "reference_style": "夸张特效风格",
      "difficulty_level": "复杂"
    }
  }
  //...后续根据章节内容补充
]
```

---

## 生成新章节分镜的步骤

### 第一步: 读取章节内容
- 完整阅读待生成分镜的章节
- 标记关键场景转折点
- 识别对话、动作、特效节点

### 第二步: 场景拆分
根据情节将章节拆分为多个场景,每个场景包含:
- 场景地点
- 时间段
- 人物数量和关系
- 是否有特效/战斗

### 第三步: 镜头设计
为每个场景设计镜头序列:
- 开场镜头(建立场景)
- 主要动作镜头
- 特写镜头(关键信息)
- 转场镜头

### 第四步: 细节填充
按照格式规范填充每个镜头的详细信息:
- 镜头类型和运动
- 人物动作和表情
- 特效描述
- 音效设计
- 剪辑节奏

### 第五步: 风格统一
确保:
- 视觉风格与整体设定一致
- 特效等级与积分消耗匹配
- 幽默元素适度穿插
- 节奏张弛有度

---

## 特殊场景处理指南

### 战斗场景
- 多使用快速切换
- 强调打击感
- 特效与动作配合
- 音效突出

### 系统界面
- 保持界面风格统一
- 文字清晰易读
- 半透明效果
- 浮现和消失自然

### 幽默场景
- 使用反差剪辑
- 突然静音或停顿
- 夸张表情特写
- 音效卡点

### 情感场景
- 缓慢推拉镜头
- 注重表情细节
- 柔和光线
- 抒情音乐

---

## 制作优先级

### 必须精做的场景
1. 所有特效场景
2. 重要转折点(如第14章真相发现)
3. 高潮战斗(如第18章、第26章)
4. 系统相关场景

### 标准制作场景
1. 日常对话
2. 人物互动
3. 场景转换

### 简化制作场景
1. 过渡镜头
2. 环境空镜
3. 背景人物

---

## 质量检查清单

生成完分镜后,检查以下要点:

- [ ] 镜头编号连续无重复
- [ ] 每个镜头都有明确目的
- [ ] 特效描述详细具体
- [ ] 音效与画面匹配
- [ ] 节奏张弛有度
- [ ] 人物性格体现
- [ ] 转场自然流畅
- [ ] 符合整体风格
- [ ] 制作难度标注准确
- [ ] 时长控制合理

---

## 输出格式示例

完整输出应该是这样的JSON数组:

```json
[
  {
    "shot_id": "EP01-S001",
    "chapter_number": 1,
    "scene_number": 1,
    // ... (完整字段)
  },
  {
    "shot_id": "EP01-S002",
    "chapter_number": 1,
    "scene_number": 1,
    // ... (完整字段)
  }
  // ... 更多镜头
]
```

每个章节独立生成一个JSON文件,命名规则: `storyboard-chapter-XX.json`

---

*版本: v1.0*
*创建日期: 2025-01-14*
*适用范围: 所有36章分镜生成*
