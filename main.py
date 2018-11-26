#!/usr/bin/env -S pipenv run python
import sys

import json
from logging import DEBUG, basicConfig
from pathlib import Path
from telegram import Bot, ParseMode
from telegram.utils.request import Request

from plugin import Plugin

my_plugin_id = 11252
plugins_ids = [7754, my_plugin_id]
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


def invalidate_cache_if_changed():
    store = Path(sys.path[0] + '/store.json')
    stored_data = json.loads((store.read_text() if store.exists() else '{}') or '{}')
    stored_plugins = {int(id): Plugin(data) for id, data in stored_data.items()}
    store.write_text(json.dumps({id: p.data for id, p in plugins.items()}))

    if my_plugin_id not in stored_plugins:
        return plugins  # no changes, the first message in history
    if plugins[my_plugin_id].data != stored_plugins[my_plugin_id].data:
        return stored_plugins


if __name__ == '__main__':
    stored_plugins = invalidate_cache_if_changed()

    if stored_plugins:
        msg = Plugin.stringify(plugins, stored_plugins)
        print(msg, end='\n\n')

        send_message(telegram_chat_id, '`{}`'.format(msg), telegram_bot_token)
