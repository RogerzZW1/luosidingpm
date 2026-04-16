# luosidingpm-skills


<img width="1024" height="572" alt="image" src="https://github.com/user-attachments/assets/9b38f5d7-452a-42ca-a908-54fe1f0e10ea" />

---

# 在做PM的时候是否遇到过以下痛点
- 需求背景没判断清楚，评审时被追着问“为什么做”，被团队内认为业务思考不足
- 模块描述太粗，开发实现时不断返工，被研发投诉不专业
- 漏了上下游和依赖，项目推进到一半才发现缺角色，被质疑项目管理
- 每次新写 PRD 都像从头来过，做完没有方法论SOP，被老板喷没有沉淀

luosidingpm 就是为了解决这些问题而设计的。

它不是一个“快速套模板写文档”的工具，而是一套用硬规则、深度追问和模块化 workflow 逼着 PM 把问题想清楚、把文档写透、把后续测试和实验衔接起来的技能仓库。

在这里，PRD 不是终点，测试用例、A/B 实验、系统图和评审也不是孤立动作。它们都被当作同一个产品问题在不同阶段的表达方式来处理。

---

## 仓库定位

本仓库适合互联网公司中的产品经理、增长产品经理、商家/运营产品经理、平台产品经理使用。

仓库中的 Skills 不是模板库，而是工作方法库。每个 Skill 都对应一类明确任务：

- `prd-deep-interview`：通过深度对话生成一份 PRD
- `pm-review-board`：站在多个角色视角 review 一份 PRD 或方案
- `test-case`：生成、补全、评审测试用例
- `ab-test-setup`：设计 A/B 实验
- `excalidraw-diagram-skill`：生成概念关系图、系统框架图等
- `playwright-interactive`：用于浏览器交互、调试和验证页面流程，做竞品分析的

---

## 输出prd参考
交互形式：深度对话➕模块追问
<img width="923" height="542" alt="image" src="https://github.com/user-attachments/assets/bfce4eca-c5b4-40df-92d2-55a7eb194da9" />
<img width="923" height="990" alt="image" src="https://github.com/user-attachments/assets/11a9a97a-26fc-4063-97ca-58d2460bdd3a" />
<img width="923" height="984" alt="image" src="https://github.com/user-attachments/assets/54b81bac-db7d-4e93-b625-c02451b000ce" />
<img width="923" height="620" alt="image" src="https://github.com/user-attachments/assets/64191b68-65bc-4733-aa6f-b76e9188b3a3" />
<img width="923" height="669" alt="image" src="https://github.com/user-attachments/assets/f94e514b-f337-4c11-a6a1-b4965bbfe8bc" />

---

## 市面上的 PRD Skills 常见问题

我对比过至少 5 份 PRD Skills，包括海外的 `Write-a-prd`、`prd-development`，以及一些国内博主发布的 PRD Skills，主要发现以下问题：

### 1. 缺乏判断
很多 PRD Skills 在功能描述部分，只会把“用户说了什么”直接填进对应框架里。  
它们不教 AI 如何判断：
- 需求模块拆解是否合理
- 用户输入内容是否足够具体
- 当前描述是否能直接进入 PRD
- 内容质量是高还是低

结果就是：看起来像 PRD，实际上只是“用户原话整理版”。

### 2. 缺乏细节
许多 PRD Skills 对需求描述粒度要求太粗。  
它们会要求写“页面交互”“状态流转”，但不会进一步定义：

- 页面和状态的层级
- 条件分支
- UI 交互的详细结构
- 文案、字段、格式、失败提示的表达方式
- 开发和测试真正需要的细节粒度

最后生成的内容往往停留在“有标题、有模块”，但远远不够落地。

### 3. 缺乏沉淀（非常重要）
很多 Skills 是一次性使用逻辑：
- PM 调一次
- 发现问题
- 手工改掉
- 下次再调
- 同样的问题继续出现

也就是说，Skill 没有真正帮助 PM 积累结构化经验，缺少持续迭代和学习机制。

### 4. 缺乏业务思考
很多 Skills 在业务背景部分，只会通过几轮问询确认“这似乎是个问题”，但不会帮助 PM 继续思考：

- 这是不是当前最重要的问题
- 为什么现在做
- 不做会怎样
- 当前方案是不是唯一方案
- 有没有替代方案
- 业务价值和优先级是否成立

也就是说，它们会问，但不会真正“拷打”。

### 5. 缺乏关联性
很多 Skills 把章节写得彼此独立：
- 背景写背景
- 模块写模块
- 埋点写埋点

但不会继续判断：
- 写出来的功能模块是否真的在解决业务问题
- 设计的埋点和指标是否真能反映业务目标
- 用户角色和模块是否一一承接
- 测试用例、实验设计是否能与 PRD 对齐

这种“章节齐全但不关联”的文档，对产品落地帮助非常有限。

---

## 我的 Skills 如何解决 PM 的痛点

<img width="1024" height="572" alt="image" src="https://github.com/user-attachments/assets/9cc731eb-dc8e-4112-877a-cba360690d34" />

### 1. 反复鞭打业务思考
在 `prd-deep-interview` 中，业务背景不是简单收集，而是会通过：

- 多维度业务追问
- 反方检验
- 优先级判断
- 方案必要性判断

去逼 PM 想清楚：
- 当前问题是否成立
- 当前方案是否只是“想法”
- 为什么是现在做
- 为什么不是别的方案

也就是说，它不是让你顺着写，而是逼你先把问题想透。

### 2. 为模块描述配上硬规则
在功能模块与产品逻辑详细描述部分，我给了非常明确的结构和方法，不再是简单要求“写页面和交互”。

例如：
- 需求列表
- 大模块 / 小模块拆解
- 页面描述
- 用户交互详细描述
- 通过 `EP / BVA / ST / EG` 反推交互分支、状态和失败场景

这样做的目的，是确保需求模块不只是“看起来完整”，而是能真正覆盖开发和测试所需要的内容。

### 3. 配上通过与否的标准
这套 Skill 不是只教你“怎么写”，还会判断：
- 当前模块输入是否够支撑输出
- 当前输入是否属于这一章节
- 当前内容和前文是否一致
- 当前模块是否已经达到可交付粒度

也就是说，每个模块不是“写出来就算完成”，而是会判断“是不是写得好、是不是写透了”。

### 4. 在上下游管理上扩充角色视角
不是只看：
- 前端
- 后端
- 测试
- 设计

而是把这些角色都纳入依赖项评估：
- 法务
- 用户风控
- 文案
- 用户端
- 运营端
- 商家端
- 外部 API
- 算法
- 数仓
- 中台

这样做的目的是让 PM 在写需求时，更接近真实项目管理，而不是只站在页面视角写文档。

### 5. 在沉淀 SOP 上预留 learning loop
这一部分还没有完全实现，但方向已经明确：
- 记录每次真实试跑中暴露的 bug
- 记录自己对输出风格和结构的 feedback
- 把这些问题回写进 skill
- 形成一个不断迭代的 learning loop

也就是让 Skill 不断学习，而不是永远犯同样的错。

### 6. 集成大量辅助工具
这套仓库并不只生成 PRD，而是把 PM 真实工作中常见的下游动作也纳入了：

- `test-case`：测试用例生成 / 评审
- `ab-test-setup`：A/B 实验设计
- `playwright-interactive`：浏览器交互与网页验证
- `excalidraw-diagram-skill`：概念图、关系图、系统框架图

这些工具不是孤立的，而是围绕 PM 的完整工作流服务。

---

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

---

## 基本使用方式

如果你是第一次使用这套仓库，最简单的方式是：

1. 对你的agent说：“我想写一份prd，请使用luosidingpm skill中的`prd-deep-interview“
2. 在过程中根据主 skill 的提示，再进入：
   - `playwright-interactive`（竞品调研）
   - `excalidraw-diagram-skill`（关系图 / 框架图）
   - `test-case`（测试用例）
   - `ab-test-setup`（实验设计）

也就是说：
- `prd-deep-interview` 是主入口
- 其他 skill 是围绕 PRD 工作流逐步被引导出来的辅助能力

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

---

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
