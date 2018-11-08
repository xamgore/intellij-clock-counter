## intellij-clock downloads tracker

<img align="right" width="80" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/768px-Telegram_logo.svg.png">

This project is used to automatically take information about downloads of the [intellij-clock](https://github.com/xamgore/intellij-clock) plugin (with its rivals) and send it to my personal Telegram's chat room.

```yaml
Clock:         ⇊2398  ✩3.0  ꆜ4
Time:          ⇊86    ✩1.0  ꆜ1
Clock Widget:  ⇊80    ✩5.0  ꆜ2
```


### Development & usage

##### How to get _bot's token_

Ask [@BotFather](https://t.me/BotFather) for it: send `/newbot`, pick up a name and nickname.

##### How to get _chat_id_

Open the chat with bot, press `/start`, find id on the page `https://api.telegram.org/bot<token>/getUpdates`

##### How to run

```
$ pipenv install
$ echo 'bot-token' > token.txt
$ pipenv run python main.py
```

##### Add [a task](https://crontab.guru/#0_19_*_*_*) to cron

```
$ crontab -e

SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# m h  dom mon dow   command
0 19 * * *   cd $HOME/intellij-clock-tracker && pipenv run python main.py > log.out 2>&1
```
