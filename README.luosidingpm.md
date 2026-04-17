# luosidingpm-skills

如果你在互联网公司做产品，你一定遇到过这些问题：

- 需求背景没判断清楚，评审时被追着问“为什么做”
- 模块描述太粗，开发实现时不断返工
- 漏了上下游和依赖，项目推进到一半才发现缺角色
- 每次写 PRD 都像从头来过，做完没有方法沉淀

luosidingpm 就是为了解决这些问题而设计的。

它不是一个“快速套模板写文档”的工具，而是一套用硬规则、深度追问和模块化 workflow 逼着 PM 把问题想清楚、把文档写透、把后续测试和实验衔接起来的技能仓库。

在这里，PRD 不是终点，测试用例、A/B 实验、系统图和评审也不是孤立动作。它们都被当作同一个产品问题在不同阶段的表达方式来处理。

## 仓库定位

本仓库适合互联网公司中的产品经理、增长产品经理、商家/运营产品经理、平台产品经理使用。

仓库中的 Skills 不是模板库，而是工作方法库。每个 Skill 都对应一类明确任务：

- `prd-deep-interview`：通过深度对话生成一份 PRD
- `pm-review-board`：站在多个角色视角 review 一份 PRD 或方案
- `test-case`：生成、补全、评审测试用例
- `ab-test-setup`：设计 A/B 实验
- `excalidraw-diagram-skill`：生成概念关系图、系统框架图等
- `playwright-interactive`：用于浏览器交互、调试和验证页面流程

## 适用平台

### Codex

将本仓库中的 Skill 目录放入 Codex 可扫描的 skills 目录中即可。  
若使用父子目录组织结构，需要根据本地环境决定是否额外创建一级目录入口或软链接。

### Claude

Claude 自定义 Skill 使用时，需要保证每个 Skill 目录中的 `SKILL.md` 可独立读取。  
如果平台要求 `Skill.md` 大小写格式，请在上传前按平台要求调整文件名。

### OpenClaw

将仓库挂载到 OpenClaw 可访问目录，并确保每个 Skill 的 `SKILL.md` 能被直接读取。  
如平台只扫描一级 Skill，则需要根据平台规则单独暴露入口。

## 基本使用方式

### 1. 主入口：先调用 `prd-deep-interview`

默认情况下，用户只需要先调用 `prd-deep-interview`。  
这是这套仓库的主入口，用于通过多轮深度对话生成一份 PRD。

在对话过程中，`prd-deep-interview` 不只是写文档，还会根据当前需求的类型和阶段，主动判断是否需要进入后续动作，并引导用户调用其他 skill。

也就是说，用户通常不需要一开始就手动唤起所有 skill，而是先通过 PRD 主流程把需求澄清清楚。

### 2. `pm-review-board`：独立评审入口

如果用户已经有一份 PRD，或者希望对现有方案进行多角色视角评审，可以单独调用 `pm-review-board`。

这个 skill 更适合：
- review 一份已有 PRD
- 站在不同角色视角挑战需求
- 帮用户找出逻辑缺口、范围问题和交付风险

### 3. `test-case`：在 PRD 产出后由主 skill 引导进入

当 `prd-deep-interview` 发现：
- 功能模块已经明确
- 状态、规则、异常和系统流程已经清楚

它会主动询问用户是否需要继续生成测试用例。  
如果用户确认需要，再路由到 `test-case`。

这里传递给 `test-case` 的不是整份 PRD，而是与测试直接相关的内容，例如：
- 功能模块与产品逻辑详细描述
- 数据交互与系统流程
- 状态、规则、异常、边界

所以用户通常不需要一开始手动调用 `test-case`，而是在 PRD 生成后，由主 skill 引导进入。

### 4. `ab-test-setup`：在 PRD 产出后由主 skill 引导进入

当 `prd-deep-interview` 判断当前需求存在：
- 方案对比
- 策略验证
- 转化优化
- 流量试点
- 体验实验

它会主动询问用户是否需要设计 A/B 实验。  
如果用户确认需要，再路由到 `ab-test-setup`。

传递给实验 skill 的内容主要来自 PRD 中与实验直接相关的章节，例如：
- 业务目标
- 用户价值目标
- 核心指标
- 约束指标
- 想验证的关键方案点

### 5. `playwright-interactive`：在竞品分析时由主 skill 引导进入

`playwright-interactive` 不是单独拿来做产品设计的主入口。  
它主要在竞品分析阶段发挥作用。

当 `prd-deep-interview` 判断当前需求需要做竞品调研时，会先询问用户是否要做竞品分析。  
如果用户确认需要，并且需要实际访问网页、点击页面、观察交互、截图收集证据，就会引导进入 `playwright-interactive`。

它的作用主要是：
- 打开竞品网页
- 观察页面结构
- 验证入口和交互路径
- 截图保存证据
- 帮助后续做页面级和功能级竞品拆解

也就是说，它服务的是竞品分析，不是独立于 PRD 外的主流程。

### 6. `excalidraw-diagram-skill`：在功能模块拆解阶段由主 skill 引导进入

当 `prd-deep-interview` 判断当前需求涉及：
- 多角色
- 多部门
- 多系统
- 多能力模块协同

它会主动提示用户：是否需要补一张概念关系图 / 系统框架图。  
如果用户确认需要，再路由到 `excalidraw-diagram-skill`。

它主要用于：
- 说明用户角色与系统之间的关系
- 说明需求模块之间的关系
- 说明上下游依赖和责任边界
- 补充 PRD 中不适合用时序图表达的结构关系

所以它不是用来替代系统交互图，而是用来辅助表达：
- 功能模块结构
- 角色与系统关系
- 部门与系统协同关系

### 7. 使用建议

如果你是第一次使用这套仓库，最简单的方式是：

1. 先调用 `prd-deep-interview`
2. 跟着它完成 PRD 深度对话
3. 在过程中根据主 skill 的提示，再进入：
   - `playwright-interactive`（竞品调研）
   - `excalidraw-diagram-skill`（关系图 / 框架图）
   - `test-case`（测试用例）
   - `ab-test-setup`（实验设计）

也就是说：
- `prd-deep-interview` 是主入口
- 其他 skill 是围绕 PRD 工作流逐步被引导出来的辅助能力

## 仓库结构

```text
luosidingpm/
├── README.md                          # 仓库说明文件
├── AGENTS.md                          # 共通工作原则与 PM 方法论约束
├── prd-deep-interview/
│   ├── SKILL.md                       # 核心 PRD Skill：深度对话生成 PRD
│   ├── references/                    # PRD 参考文档
│   │   ├── competitor-research-method.md   # 竞品分析方法
│   │   ├── prd-template.md                 # PRD 完整模板示例
│   │   ├── module-design-method.md         # 功能模块拆解与交互描述方法
│   │   ├── system-flow-method.md           # 数据交互、系统流程与 Mermaid 方法
│   │   └── 其他 reference                  # 其他补充参考文档
│   └── scripts/                       # PRD 相关辅助脚本
├── pm-review-board/
│   ├── SKILL.md                       # PRD / 内容评审 Skill
│   └── references/                    # 评审清单与参考文档
├── test-case/
│   ├── SKILL.md                       # 测试用例生成 / 补全 / 评审 Skill
│   ├── reference.md                   # 测试用例模板与书写规范
│   └── scripts/                       # 测试用例辅助脚本
├── ab-test-setup/
│   ├── SKILL.md                       # A/B 实验设计 Skill
│   └── references/                    # 样本量、实验模板等参考文档
├── excalidraw-diagram-skill/
│   ├── SKILL.md                       # 概念图 / 关系图 / 框架图 Skill
│   └── references/                    # 图示风格与参考说明
└── playwright-interactive/
    ├── SKILL.md                       # 浏览器交互与页面验证 Skill
    ├── agents/                        # 子代理配置文件
    └── assets/                        # 相关资源文件
```

## 这套仓库能做什么

这套仓库主要做两类事情：

### 一类：生成
- 生成 PRD
- 生成测试用例
- 生成实验方案
- 生成概念图、关系图、系统框架图

### 二类：评审
- 评审 PRD
- 评审测试用例
- 挑战需求逻辑和模块边界
- 帮助产品经理发现问题、补充缺口

## 设计原则

- 不是只写模板，而是沉淀 PM 方法论
- 不是只收集用户输入，而是主动判断、查漏补缺
- 不同 Skill 之间必须共享同一问题定义、目标和模块边界
- 文档输出必须服务后续设计、研发、测试、运营工作

## 当前状态

本仓库仍在持续迭代中。  
核心 PRD Skill 已经过多轮真实试跑，并在持续收敛：

- 背景澄清
- 角色与场景拆解
- 功能模块设计
- 数据交互与系统流程
- 数据追踪设计
- 后续动作联动（测试用例 / A/B 实验 / 图表）

后续会继续补齐更多 PM 实战工作流能力。
