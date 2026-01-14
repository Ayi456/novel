#!/usr/bin/env python3
"""
批量优化剩余章节的分镜文件
根据实际章节内容生成高质量分镜
"""
import json
import os
import re

def read_chapter_content(chapter_num):
    """读取章节内容"""
    chapter_file = f"/Users/null/Desktop/Code/github/novel/novels/novel-001/chapters/chapter-{chapter_num:03d}.md"
    try:
        with open(chapter_file, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"警告: 找不到章节文件 {chapter_file}")
        return None

def generate_storyboard_from_content(chapter_num, content):
    """根据章节内容生成分镜"""
    # 分割章节为段落
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip() and not p.strip().startswith('#')]
    
    # 移除标题行
    paragraphs = [p for p in paragraphs if not p.startswith('#')]
    
    # 生成分镜
    shots = []
    scene_num = 1
    shot_id = 1
    
    for para in paragraphs[:20]:  # 限制段落数量以控制分镜数量
        if len(para) < 20:  # 跳过太短的段落
            continue
            
        # 根据段落内容决定镜头类型
        if '战斗' in para or '攻击' in para or '剑' in para or '法术' in para:
            shot_type = "中景"
            movement = "快速跟随"
            pacing = "激烈"
        elif '震惊' in para or '惊讶' in para or '瞪' in para:
            shot_type = "特写"
            movement = "推镜"
            pacing = "震撼"
        elif '说' in para or '道' in para or '问' in para or '答' in para:
            shot_type = "近景"
            movement = "轻微推镜"
            pacing = "对话"
        elif '看' in para or '望' in para or '观' in para:
            shot_type = "远景"
            movement = "缓慢拉远"
            pacing = "舒缓"
        else:
            shot_type = "中景"
            movement = "固定镜头"
            pacing = "中等"
        
        # 创建镜头
        shot = {
            "shot_id": f"EP{chapter_num:02d}-S{shot_id:03d}",
            "chapter_number": chapter_num,
            "scene_number": scene_num,
            "duration": 6,
            "shot_type": shot_type,
            "location": f"场景{scene_num}",
            "time_of_day": "白天",
            "composition": {
                "camera_position": "正面拍摄",
                "camera_movement": movement,
                "framing": "标准构图",
                "focus_type": "主体清晰"
            },
            "characters": [
                {
                    "name": "主要角色",
                    "position": "画面中央",
                    "action": "推进剧情",
                    "expression": "根据情境",
                    "costume": "修仙服饰"
                }
            ],
            "visual_effects": {
                "environment": "根据场景",
                "lighting": "自然光",
                "color_palette": "自然色调",
                "special_effects": "根据需要添加特效"
            },
            "audio": {
                "dialogue": para[:100] if len(para) > 100 else para,
                "narration": "",
                "internal_monologue": "",
                "background_music": pacing,
                "sound_effects": [],
                "volume_level": "正常"
            },
            "editing": {
                "transition_to_next": "直接切",
                "pacing": pacing,
                "purpose": "推进剧情"
            },
            "notes": {
                "production_note": "根据实际内容调整",
                "reference_style": "仙侠风格",
                "difficulty_level": "中等"
            }
        }
        
        shots.append(shot)
        shot_id += 1
        scene_num += 1
        
        if shot_id > 18:  # 限制最大镜头数
            break
    
    return shots

def main():
    """主函数"""
    chapters_to_optimize = [8, 9, 16, 18, 19, 22, 24, 25]
    
    for chapter_num in chapters_to_optimize:
        print(f"\n正在处理第 {chapter_num} 章...")
        
        # 读取章节内容
        content = read_chapter_content(chapter_num)
        if content is None:
            continue
        
        # 生成分镜
        shots = generate_storyboard_from_content(chapter_num, content)
        
        # 保存分镜文件
        storyboard_file = f"/Users/null/Desktop/Code/github/novel/novels/novel-001/storyboards/storyboard-chapter-{chapter_num:02d}.json"
        
        with open(storyboard_file, 'w', encoding='utf-8') as f:
            json.dump(shots, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 第 {chapter_num} 章分镜已生成: {len(shots)} 个镜头")

if __name__ == "__main__":
    main()
