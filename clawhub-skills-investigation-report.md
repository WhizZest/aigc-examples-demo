# ClawHub相关Skill调查研究报告

**报告生成时间**: 2026-03-15T14:30:00+08:00
**调查人**: AI Agent
**版本**: 1.0

---

## 调查概述

本报告对本地安装的5个ClawHub相关skill进行了深入比较和分析，包括功能、特点、适用场景等维度的综合评估。

## 调查对象

本次调查的5个skill：

1. **clawhub** (steipete/clawdis@clawhub)
2. **clawhub-cli** (ClawHub安装)
3. **find-skills** (vercel-labs/skills@find-skills)
4. **vassili-clawhub-cli** (vince-winkintel/clawhub-cli-skill)
5. **clawhub-cli-skill** (vince-winkintel/clawhub-cli-skill)

---

## 详细对比分析

### 1. clawhub (steipete/clawdis@clawhub)

**基本信息**
- **来源**: steipete/clawdis@clawhub
- **注册表**: clawhub.com
- **行数**: 77行
- **核心定位**: ClawHub CLI基础使用指导

**功能覆盖**
- ✅ 安装: `npm i -g clawhub`
- ✅ 认证: `clawhub login`, `clawhub whoami`
- ✅ 搜索: `clawhub search "postgres backups"`
- ✅ 安装: `clawhub install my-skill --version 1.2.3`
- ✅ 更新: `clawhub update --all`, `clawhub update --force`
- ✅ 列表: `clawhub list`
- ✅ 发布: `clawhub publish ./my-skill --slug my-skill`

**特点分析**
- 简洁明了，77行
- 包含基本命令示例
- 注明默认注册表和工作目录
- 基于hash的更新机制
- 适合快速查阅

**适用场景**
- 需要快速查阅ClawHub CLI基本命令
- 新手入门学习

---

### 2. clawhub-cli (ClawHub安装)

**基本信息**
- **来源**: ClawHub安装
- **注册表**: clawhub.ai
- **行数**: 140行
- **核心定位**: ClawHub CLI Helper - 详细指导

**功能覆盖**
- ✅ 搜索技能: `clawhub search "your query"`
- ✅ 安装技能: `clawhub install <skill-slug> --version <semver>`
- ✅ 列出已安装: `clawhub list`
- ✅ 更新技能: `clawhub update --all`, `clawhub update <skill-slug>`
- ✅ 发布单个技能: `clawhub publish ./skills/my-skill --slug my-skill --version 0.1.0 --tags latest`
- ✅ 批量同步: `clawhub sync --all`

**特点分析**
- 140行，内容详细
- 包含Requirements部分
- Common Workflows分类清晰
- Verification and Troubleshooting指导
- 支持更多发布选项（tags, changelog, bump, dry-run）

**适用场景**
- 需要详细指导使用ClawHub CLI
- 日常开发和维护工作

---

### 3. find-skills (vercel-labs/skills@find-skills)

**基本信息**
- **来源**: vercel-labs/skills@find-skills
- **注册表**: skills.sh
- **行数**: 142行
- **安装量**: 548.7K
- **核心定位**: skills.sh生态发现工具

**功能覆盖**
- ✅ 搜索技能: `npx skills find [query]`
- ✅ 安装技能: `npx skills add <package> -g -y`
- ✅ 检查更新: `npx skills check`
- ✅ 更新技能: `npx skills update`

**特点分析**
- 142行，内容全面
- 548.7K安装量，最流行
- 6步完整工作流程
- 质量验证机制（安装量、来源声誉、GitHub stars）
- 分类搜索指导
- 通用skill分类表

**适用场景**
- 发现和安装skills.sh生态中的技能
- 需要质量保证的技能选择

**与其他skill的区别**
- **不同生态系统**: skills.sh vs clawhub.com/clawhub.ai
- **不同工具**: `npx skills` vs `clawhub`
- **不同目标**: 发现通用技能 vs 管理ClawHub技能

---

### 4. vassili-clawhub-cli (vince-winkintel/clawhub-cli-skill)

**基本信息**
- **来源**: https://github.com/vince-winkintel/clawhub-cli-skill
- **注册表**: clawhub.ai
- **行数**: 77行
- **核心定位**: ClawHub CLI Helper - 简洁版本

**功能覆盖**
- ✅ 搜索技能: `clawhub search "your query"`
- ✅ 安装技能: `clawhub install <skill-slug>`
- ✅ 列出已安装: `clawhub list`
- ✅ 更新技能: `clawhub update --all`, `clawhub update <skill-slug>`
- ✅ 发布单个技能: `clawhub publish ./skills/my-skill --slug my-skill --version 0.1.0 --tags latest`
- ✅ 批量同步: `clawhub sync --all`

**特点分析**
- 77行，简洁版本
- 与clawhub-cli功能相同
- 内容更精简

**适用场景**
- 需要简洁的ClawHub CLI指导

**与clawhub-cli的对比**
- **功能相同**: 两者功能完全一致
- **内容长度**: clawhub-cli (140行) vs vassili-clawhub-cli (77行)
- **推荐**: clawhub-cli更详细

---

### 5. clawhub-cli-skill (vince-winkintel/clawhub-cli-skill)

**基本信息**
- **来源**: https://github.com/vince-winkintel/clawhub-cli-skill
- **注册表**: clawhub.ai
- **行数**: 324行
- **核心定位**: 完整ClawHub CLI参考文档

**功能覆盖**
- ✅ **全局标志**: `--workdir`, `--dir`, `--site`, `--registry`, `--no-input`
- ✅ **HTTP代理支持**: 代理配置、环境变量
- ✅ **配置文件**: 存储位置、覆盖选项
- ✅ **认证**: `clawhub login`, `clawhub whoami`, `clawhub logout`
- ✅ **搜索和发现**: `clawhub search`, `clawhub explore`
- ✅ **检查**: `clawhub inspect` (支持版本、文件、JSON输出)
- ✅ **安装和卸载**: `clawhub install`, `clawhub uninstall`
- ✅ **更新**: `clawhub update`, 基于fingerprinting
- ✅ **列表**: `clawhub list`
- ✅ **发布**: `clawhub publish`, MIT-0许可
- ✅ **同步**: `clawhub sync`, 批量发布、版本控制
- ✅ **Star/Unstar**: `clawhub star`, `clawhub unstar`
- ✅ **删除/恢复**: `clawhub delete`, `clawhub undelete`
- ✅ **所有权转移**: `clawhub transfer`
- ✅ **管理员命令**: `clawhub ban-user`, `clawhub set-role`

**特点分析**
- 324行，最全面
- 包含所有ClawHub CLI命令
- 详细的故障排除指导
- Known Gotchas部分
- Lockfile格式说明
- 遥测控制选项

**适用场景**
- 需要完整的ClawHub CLI参考文档
- 高级用户和开发者

**与其他skill的对比**
- **最全面**: 包含所有命令和高级功能
- **最详细**: 324行，涵盖所有方面
- **最权威**: 官方CLI文档的完整参考

---

## 功能对比矩阵

| 功能 | clawhub | clawhub-cli | find-skills | vassili-clawhub-cli | clawhub-cli-skill |
|------|----------|-------------|--------------|---------------------|------------------|
| 基本命令 | ✅ | ✅ | ❌ | ✅ | ✅ |
| 详细工作流程 | ❌ | ✅ | ✅ | ❌ | ✅ |
| 质量验证 | ❌ | ❌ | ✅ | ❌ | ❌ |
| 生态系统 | ClawHub | ClawHub | skills.sh | ClawHub | ClawHub |
| 全局标志 | ❌ | ❌ | ❌ | ❌ | ✅ |
| 代理支持 | ❌ | ❌ | ❌ | ❌ | ✅ |
| 配置文件 | ❌ | ❌ | ❌ | ❌ | ✅ |
| Inspect命令 | ❌ | ❌ | ❌ | ❌ | ✅ |
| Explore命令 | ❌ | ❌ | ❌ | ❌ | ✅ |
| Sync命令 | ✅ | ✅ | ❌ | ✅ | ✅ |
| Star/Unstar | ❌ | ❌ | ❌ | ❌ | ✅ |
| 所有权转移 | ❌ | ❌ | ❌ | ❌ | ✅ |
| 管理员命令 | ❌ | ❌ | ❌ | ❌ | ✅ |
| 故障排除 | ❌ | ✅ | ❌ | ❌ | ✅ |
| Known Gotchas | ❌ | ❌ | ❌ | ❌ | ✅ |
| 行数 | 77 | 140 | 142 | 77 | 324 |

---

## 综合评估

### 按功能完整性排名

1. **clawhub-cli-skill** ⭐⭐⭐⭐⭐ (324行，最全面)
2. **clawhub-cli** ⭐⭐⭐⭐ (140行，详细)
3. **find-skills** ⭐⭐⭐⭐ (142行，完整工作流程)
4. **clawhub** ⭐⭐⭐ (77行，简洁)
5. **vassili-clawhub-cli** ⭐⭐⭐ (77行，简洁)

### 按实用性排名

1. **find-skills** ⭐⭐⭐⭐⭐ (548.7K安装量，最流行)
2. **clawhub-cli-skill** ⭐⭐⭐⭐⭐ (最全面)
3. **clawhub-cli** ⭐⭐⭐⭐ (详细)
4. **clawhub** ⭐⭐⭐ (简洁)
5. **vassili-clawhub-cli** ⭐⭐⭐ (简洁)

### 按生态系统排名

1. **find-skills** (skills.sh生态，548.7K安装量)
2. **clawhub-cli-skill** (ClawHub生态，最全面)
3. **clawhub-cli** (ClawHub生态，详细)
4. **clawhub** (ClawHub生态，简洁)
5. **vassili-clawhub-cli** (ClawHub生态，简洁)

---

## 推荐使用场景

### 1. 快速查阅基本命令

**推荐**: **clawhub** 或 **vassili-clawhub-cli**

**理由**:
- 简洁明了，77行
- 包含基本命令示例
- 适合快速查阅

**使用示例**:
```bash
# 快速查看安装命令
clawhub install my-skill

# 快速查看更新命令
clawhub update --all
```

---

### 2. 详细指导使用ClawHub CLI

**推荐**: **clawhub-cli**

**理由**:
- 详细的工作流程
- Verification and Troubleshooting指导
- 适合日常使用

**使用示例**:
```bash
# 按照详细工作流程发布技能
clawhub publish ./skills/my-skill \
  --slug my-skill \
  --name "My Skill" \
  --version 0.1.0 \
  --tags latest
```

---

### 3. 发现skills.sh生态中的技能

**推荐**: **find-skills**

**理由**:
- 548.7K安装量，最流行
- 质量验证机制
- 6步完整工作流程

**使用示例**:
```bash
# 搜索技能
npx skills find react

# 安装技能
npx skills add vercel-labs/agent-skills@react-best-practices -y
```

---

### 4. 完整ClawHub CLI参考

**推荐**: **clawhub-cli-skill**

**理由**:
- 324行，最全面
- 包含所有命令和高级功能
- 详细的故障排除指导

**使用示例**:
```bash
# 使用高级功能
clawhub inspect my-skill --versions --limit 50
clawhub explore --sort trending --limit 50
clawhub sync --all --no-input --changelog "Automated sync"
```

---

## 最佳实践建议

### 日常使用组合

**推荐组合**: `clawhub-cli-skill` (完整参考) + `find-skills` (技能发现)

**理由**:
- 覆盖两个主要生态系统
- 提供完整的CLI参考
- 支持技能发现和安装

**工作流程**:
1. 使用`find-skills`发现需要的技能
2. 使用`clawhub-cli-skill`管理ClawHub技能
3. 根据需要查阅详细文档

---

### 快速查阅组合

**推荐组合**: `clawhub` 或 `vassili-clawhub-cli` (简洁)

**理由**:
- 快速查阅基本命令
- 适合新手入门

**工作流程**:
1. 快速查看基本命令
2. 按照示例执行操作
3. 遇到问题时查看详细文档

---

### 详细指导组合

**推荐组合**: `clawhub-cli` (详细)

**理由**:
- 详细的工作流程
- Verification and Troubleshooting指导

**工作流程**:
1. 按照详细工作流程操作
2. 遇到问题时查看故障排除部分
3. 使用验证命令检查结果

---

## 关键发现

### 1. 生态系统差异

**发现**: 这些skill属于不同的生态系统

- **ClawHub生态**: clawhub.com, clawhub.ai
- **skills.sh生态**: skills.sh

**影响**: 需要根据使用的生态系统选择相应的skill

---

### 2. 功能重叠

**发现**: clawhub-cli和vassili-clawhub-cli功能完全相同

**影响**: 选择更详细的clawhub-cli更合适

---

### 3. 内容完整性

**发现**: clawhub-cli-skill是最全面的参考文档

**影响**: 作为主要参考文档使用

---

### 4. 质量保证

**发现**: find-skills包含质量验证机制

**影响**: 在选择技能时提供质量保证

---

### 5. 来源纠正

**发现**: vassili-clawhub-cli的正确来源是 https://github.com/vince-winkintel/clawhub-cli-skill

**影响**: 确保引用正确的来源

---

## 结论

本次调查分析了5个ClawHub相关skill，它们各有特色：

1. **clawhub-cli-skill**: 最全面，适合作为主要参考文档
2. **find-skills**: 最流行，适合发现skills.sh生态中的技能
3. **clawhub-cli**: 详细，适合日常使用
4. **clawhub**: 简洁，适合快速查阅
5. **vassili-clawhub-cli**: 简洁，与clawhub-cli功能相同

**推荐策略**:
- 日常使用: `clawhub-cli-skill` + `find-skills`
- 快速查阅: `clawhub` 或 `vassili-clawhub-cli`
- 详细指导: `clawhub-cli`

这些skill可以根据具体需求灵活组合使用，为不同的使用场景提供最佳支持。

---

## 附录

### A. 安装命令汇总

```bash
# ClawHub CLI
npm i -g clawhub

# Skills CLI
npx skills find [query]
npx skills add <owner/repo@skill> -y
```

### B. 常用命令速查

```bash
# ClawHub CLI
clawhub search "query"
clawhub install <skill>
clawhub update --all
clawhub list

# Skills CLI
npx skills find [query]
npx skills add <package> -y
npx skills check
npx skills update
```

### C. 相关链接

- ClawHub: https://clawhub.com
- ClawHub AI: https://clawhub.ai
- Skills.sh: https://skills.sh/
- vince-winkintel/clawhub-cli-skill: https://github.com/vince-winkintel/clawhub-cli-skill