#!/usr/bin/env -S pipenv run python
import sys

from logging import DEBUG, basicConfig
from pathlib import Path
from telegram import Bot, ParseMode
from telegram.utils.request import Request

from plugin import Plugin

my_plugin_id = 11252
plugins_ids = [7754, 10050, my_plugin_id]
plugins = {id: Plugin.load(id) for id in plugins_ids}

telegram_chat_id = 108562525
telegram_bot_token = Path(sys.path[0] + '/token.txt').read_text().strip()


def send_message(chat_id, msg, token):
    request = Request(
        proxy_url='socks5://phobos.public.opennetwork.cc:1090',
        urllib3_proxy_kwargs={'username': '108562525', 'password': 'oiqjv2ZD'})

    basicConfig(level=DEBUG, format='%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n')

    Bot(token, request=request) \
        .sendMessage(chat_id, msg, parse_mode=ParseMode.MARKDOWN, disable_notification=True)


def there_are_changes():
    store = Path(sys.path[0] + '/store.txt')
    content = store.read_text() if store.exists() else ''
    my_plugin = repr(plugins[my_plugin_id])

    if my_plugin.strip() != content.strip():
        store.write_text(my_plugin)
        return True


if __name__ == '__main__':
    if there_are_changes():
        msg = Plugin.stringify(plugins.values())
        print(msg, end='\n\n')

        send_message(telegram_chat_id, '`{}`'.format(msg), telegram_bot_token)
