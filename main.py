#!/usr/bin/env -S pipenv run python
import sys

from pathlib import Path
from telegram import Bot, ParseMode
from telegram.utils.request import Request

from plugin import Plugin

chat_id = 108562525
plugins_ids = [7754, 10050, 11252]
token = Path(sys.path[0] + '/token.txt').read_text().strip()

if __name__ == '__main__':
    msg = Plugin.stringify(list(map(Plugin.load, plugins_ids)))
    print(msg)

    request = Request(
        proxy_url='socks5://phobos.public.opennetwork.cc:1090',
        urllib3_proxy_kwargs={'username': '108562525', 'password': 'oiqjv2ZD'})

    Bot(token, request=request) \
        .sendMessage(chat_id, '`{}`'.format(msg),
                     parse_mode=ParseMode.MARKDOWN, disable_notification=True)
