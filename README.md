# awesome-ppt-skill

> 精选的 AI Agent PPT / 幻灯片技能（Skills）清单。一句话 → 能交付的演示文稿，2026 年 agent 生态里最卷也最实用的赛道。
>
> A curated list of PPT / slide skills for AI coding agents — generation, image-to-editable revival, consulting-grade output, and the MCP route.

[![stars](https://img.shields.io/badge/entries-14-blue)](#) [![updated](https://img.shields.io/badge/updated-2026--11--13-green)](#) [![list](https://img.shields.io/badge/type-awesome_list-orange)](#)

**图例**：★ = GitHub stars（2026-11-13 快照）｜ ⏸ = 90 天以上未更新（谨慎依赖）｜ License 已逐项核实

---

## 端到端生成（当前最火的赛道）

一句话 → 直接产出可交付的 PPTX。这一类更新最快、竞争最激烈。

| 项目 | ★ | License | 活跃 | 一句话点评 |
|---|---|---|---|---|
| [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | 29.3k | MIT | 2026-11 | 话术设计 3.0：一句话产出网页 / App 原型 / **可编辑 PPTX** / 动画 / 信息图，花叔出品，社区口碑最好 |
| [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | 12.2k | Apache-2.0 | 2026-11 | 开源 AI Office 全家桶：Docs / Sheets / **Slides** / PDF / Markdown 一套搞定，适合要"不止 PPT"的场景 |
| [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | 10.6k | AGPL-3.0 | 2026-11 | 多来源素材 → 浏览器可编辑演示，注意 AGPL 传染性 |
| [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) | 4.1k | 自定义 | ⏸ 2026-06 | **17 套手工打磨的中文 PPTX 模板** + 无需渲染的构建流，中文模板质量是卖点 |
| [GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills) | 2.3k | 无 | ⏸ 2026-06 | 先用 GPT 生成图片版 PPT 再转**完全可编辑**的 PPTX，思路野；无 license 建议只参考 |

## 转换 / 复活类：把"死"的 PPT 变回可编辑

| 项目 | ★ | License | 活跃 | 一句话点评 |
|---|---|---|---|---|
| [ningzimu/image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill) | 3.3k | MIT | 2026-09 | Codex skill：幻灯片截图 / PDF / 图片型 PPTX → **可编辑 PPTX**，接手别人发来的"死"文件必备 |

## 咨询 / 专业风格

| 项目 | ★ | License | 活跃 | 一句话点评 |
|---|---|---|---|---|
| [crazyykhllc-bit/CyberPPT](https://github.com/crazyykhllc-bit/CyberPPT) | 1.9k | MIT | ⏸ 2026-07 | 高密度、咨询风格 PPT，内置 **SCR 叙事 + 风格确认 + PPTX 质量检查**，方法论完整 |
| [carnot-tech/jinba-consulting-pptx-skill](https://github.com/carnot-tech/jinba-consulting-pptx-skill) | 1.6k | MIT | 2026-11 | 咨询级 PPTX（日文社区），版本迭代勤 |

## 官方 / 生产级基座

| 项目 | ★ | License | 活跃 | 一句话点评 |
|---|---|---|---|---|
| [anthropics/skills → pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) | — | Apache-2.0 | 持续 | 驱动 Claude 文档能力的生产级 skill：pptxgenjs 坑位清单、OOXML 编辑、校验脚本。**机制层的事实标准**，上面所有 skill 都值得配合它读 |

## MCP 路线（不走 skill，走工具协议）

| 项目 | ★ | License | 活跃 | 一句话点评 |
|---|---|---|---|---|
| [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | 10.7k | MIT | 2026-11 | 自然语言 / Terraform / SQL / OpenAPI → draw.io 图，PPT 里的架构图缺口就靠它 |
| [yb2460/harness-anything](https://github.com/yb2460/harness-anything) | 3.1k | MIT | 2026-10 | Agent 控制枢纽：直接驱动 WPS / MS Office / Zotero / Photoshop 本体 |
| [GongRzhe/Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server) | 1.9k | MIT | ⏸ 2025-12 | python-pptx 封装的 pptx MCP 先驱，工具粒度细；一年未更新 |

## 内容与设计决策层（本仓库自研）

| 项目 | 说明 |
|---|---|
| [skills/ppt-design](./skills/ppt-design/SKILL.md) | **上面所有 skill 解决"怎么写 XML"，这个 skill 解决"写什么、怎么设计"**：故事线（SCQA/金字塔/断言式标题）、场景骨架（周报/路演/评审/答辩）、图表选型、设计系统、中文排版禁则、评审式 QA 清单。与任意 pptx 工具组合使用，附 WCAG 对比度检查脚本 |

## 通用大集合（不止 PPT）

- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — 最大的 Claude Skills 总目录
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — Claude Code 生态总资源

## 怎么选（30 秒决策树）

- 只想要**能交付的 PPT**，中文场景 → `huashu-design` 或 `GordenPPTSkill`（要模板）
- 别人给了你截图/PDF 要改 → `image-to-editable-ppt-skill`
- 要**咨询级叙事和逻辑** → `CyberPPT` / `jinba` + 本仓库 `ppt-design`
- 要在自己代码里**程序化生成** → anthropics pptx skill（机制）+ 本仓库 ppt-design（内容）
- 驱动本机**真实 Office/WPS** → `harness-anything` / PowerPoint-MCP-Server

## 入库标准

1. 真实可用（有可运行的 SKILL.md/脚本，不是 README 营销页）
2. License 明确（无 license 的会标注）
3. 最近一次提交时间如实标注，超 90 天标 ⏸
4. PR 提交新条目请附 stars 快照日期 + 一句"为什么值得收录"

## License

MIT — 见 [LICENSE](LICENSE)。清单快照日期 2026-11-13，由 [@Userrober](https://github.com/Userrober) 维护，调研与核证由自主编码 agent 在人类指导下完成。
