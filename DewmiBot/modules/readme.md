## szrosebot Example plugin format
```python3
from DewmiBot.decorator import register
from .utils.disable import disableable_dec
from .utils.message import get_args_str

@register(cmds="rose")
@disableable_dec("rose")
async def _(message):
    j = "Hello there my name is rose"
    await message.reply(j)
    

__help__ = """
<b>Hi</b>
- /hi: Hello there my name is rose
"""
__mod_name__ = "rose"
```

<a href="https://t.me/slbotzone"><img src="https://img.shields.io/badge/support%20group-blue.svg?style=for-the-badge&logo=Telegram">
</a> <a href="https://t.me/SL_bot_zone"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
<a href="https://t.me/szrosebot"><img src="https://img.shields.io/badge/Foundbot%20on-blue.svg?style=for-the-badge&logo=Telegram">
