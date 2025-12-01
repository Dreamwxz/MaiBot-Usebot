from typing import List, Tuple, Type, Optional
from src.plugin_system import (
    BasePlugin, register_plugin, BaseAction,
    ComponentInfo, ActionActivationType
)

# ===== Bot调用Action组件 =====

class BotTriggerAction(BaseAction):
    """Bot触发Action - 通过发送文本来激活其他Bot"""
    # 激活设置
    activation_type = ActionActivationType.ALWAYS  # 使用LLM判定
    parallel_action = False

    # 动作基本信息
    action_name = "bot_trigger"
    action_description = "发送特定文本来激活其他Bot的功能"

    # === 功能描述（必须填写）===
    action_parameters = {
        "trigger_text": "需要发送的触发文本"
        }
    action_require = [
        "当需要调用触发或者交互其他Bot时使用",
        "当用户请求需要你触发其他Bot时使用"
    ]
    associated_types = ["text", "command"]

    async def execute(self) -> Tuple[bool, Optional[str]]:
        """执行Bot触发动作 - 发送触发文本"""
        # 获取触发文本，如果没有提供则使用默认文本
        trigger_text = self.action_data.get("trigger_text", "")
        
        if not trigger_text:
            # 如果没有提供触发文本，使用一个通用的触发文本
            return False,"触发文本不能为空"
        
        # 发送触发文本
        await self.send_text(trigger_text)

        return True, f"发送了Bot触发文本: {trigger_text}"

# ===== 插件主类 =====

@register_plugin
class MaiBotUsebotPlugin(BasePlugin):
    """MaiBot-Usebot插件 - 让麦麦能更方便的在群聊中使用指令触发其他Bot"""

    # === 插件基本信息（必须填写）===
    plugin_name = "mai_bot_usebot"
    enable_plugin = True
    dependencies = []
    python_dependencies = []
    config_file_name = "config.toml"
    config_schema = {}

    def get_plugin_components(self) -> List[Tuple[ComponentInfo, Type]]:
        """返回插件包含的组件列表"""
        return [
            # 添加Bot触发Action组件
            (BotTriggerAction.get_action_info(), BotTriggerAction),
        ]
