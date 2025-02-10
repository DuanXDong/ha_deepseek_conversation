# 🚀 DeepSeek智能家居对话助手

![Home Assistant版本要求](https://img.shields.io/badge/homeassistant-2024.3%2B-blue)
![授权协议](https://img.shields.io/badge/license-Apache%202.0-green)

让您的HomeAssistant通过DeepSeek大模型获得自然对话能力，像管家一样控制智能家居设备！

## 🌟 核心功能
| 功能类别       | 具体能力                  | 使用场景示例               |
|----------------|--------------------------|--------------------------|
| **基础对话**    | 自然语言交互              | "打开客厅的灯"           |
| **设备控制**    | 通过对话操作智能设备       | "把空调调到26度"         |
| **状态查询**    | 查询设备状态              | "现在室内温度是多少？"    |
| **情景模式**    | 执行复杂场景              | "我要看电影模式"          |


## 安装方法

### 通过HACS安装（推荐）
1. 打开HACS -> 集成
2. 点击右上角三个点菜单 -> 自定义仓库
3. 输入仓库URL：`https://github.com/DuanXDong/ha_deepseek_conversation`
4. 选择类别为"Integration"
5. 点击添加，然后在集成列表中找到并安装

### 手动安装
1. 下载最新发布版ZIP文件
2. 解压到 `custom_components/deepseek_conversation` 目录
3. 重启HomeAssistant

## 配置步骤

1. 进入 **配置** -> **设备与服务** -> **添加集成**
2. 搜索选择 **DeepSeek Conversation**
3. 输入您的[DeepSeek API密钥](https://platform.deepseek.com/api-keys)
4. （可选）调整高级设置：
   - **对话模型**：默认deepseek-chat
   - **最大令牌数**：控制响应长度（默认4096）
   - **温度值**：调整生成随机性（0-2，默认0.7）
   - **系统提示**：自定义AI行为指令

## 📖 使用说明

### 🔧 服务调用
集成提供以下服务：

#### `deepseek_conversation.chat`
- **功能**：与DeepSeek大模型进行自然语言对话
- **参数**：
  - `prompt`: 输入提示（必填）
  - `model`: 选择模型版本（默认"deepseek-chat"）
  - `temperature`: 生成多样性控制（0-2，默认0.7）
  - `max_tokens`: 最大输出长度（默认2048）

## 🛠️ 配置参数
| 参数        | 必填 | 说明                          |
|-------------|------|-----------------------------|
| api_key     | 是   | DeepSeek平台获取的API密钥       |
| model       | 否   | 默认使用最新对话模型             |
| temperature | 否   | 值越高回答越随机(0.0-2.0)       |
| max_history | 否   | 保留的对话历史条数(默认5条)      |

## 📚 最佳实践
### 温度值设置建议
| 场景         | 推荐值 | 效果说明               |
|--------------|--------|------------------------|
| 设备控制     | 0.3-0.5| 高准确性，低随机性     |
| 日常对话     | 0.6-0.8| 平衡创意与准确性       |
| 创意生成     | 1.0-1.5| 高创意性，多样化响应   |

## 使用方法

### 基础对话
1. 在HomeAssistant侧边栏打开对话功能
2. 直接与"DeepSeek"代理对话


### 高级参数配置
在集成选项中可以：
- 切换推荐配置/自定义配置
- 连接HomeAssistant本地LLM
- 调整生成参数

## ❓ 常见问题

### Q1: 如何获取API密钥？
A: 访问[DeepSeek开发者平台](https://platform.deepseek.com)，注册账号后可在控制台生成API密钥

### Q2: 为什么对话响应速度慢？
A: 可能原因：
1. 网络延迟较高（尝试ping api.deepseek.com）
2. 提示语过长（精简prompt内容）
3. 模型负载较高（重试或降低temperature值）

### Q3: 最大历史记录数设置多少合适？
A: 建议值5-10条，过多会导致：
1. 消耗更多API tokens
2. 模型可能遗忘早期对话重点
3. 增加响应延迟


## 🤝 参与贡献
欢迎通过以下方式参与改进：
1. 提交Issue报告问题
2. 发起Pull Request贡献代码
3. 完善[中文文档](docs/README_ZH.md)
4. 分享你的使用案例