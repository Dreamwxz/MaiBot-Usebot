# MaiBot-Usebot 插件

一个简单的MaiCore插件，让麦麦能更方便的在群聊中使用指令触发其他Bot。

## 功能说明

这个插件提供了一个Action组件，当LLM选择使用这个Action时，会发送一段文本来激活其他Bot的功能。

## 插件组件

### BotTriggerAction

- **Action名称**: `bot_trigger`
- **激活类型**: `ALWAYS` (始终激活)
- **功能**: 发送特定文本来激活其他Bot
- **使用场景**:
  - 当需要调用其他Bot协助处理任务时使用
  - 当需要触发其他Bot的特定功能时使用
  - 当需要与其他Bot进行交互时使用
  - 当用户请求需要其他Bot协助时使用

## 使用方法

1. 将插件放置在MaiCore的`plugins/`目录下
2. 启动MaiCore，插件会自动加载
3. 在群聊中，当LLM判断需要调用其他Bot时，会自动选择使用这个Action
4. Action会发送触发文本，激活其他Bot的功能

## 触发文本

默认情况下，Action会发送文本：`"@其他Bot 请协助处理这个请求"`

LLM也可以通过`action_parameters`提供自定义的触发文本。

## 技术细节

- **插件名称**: `mai_bot_usebot`
- **Action名称**: `bot_trigger`
- **激活类型**: `ALWAYS` - 始终在候选池中
- **关联类型**: `text` - 发送文本消息

## 文件结构

```
MaiBot-Usebot/
├── _manifest.json    # 插件清单文件
├── plugin.py         # 插件主文件
└── README.md         # 说明文档
```

## 开发信息

- **作者**: 小泽
- **版本**: 0.0.1Beta
- **许可证**: MIT
