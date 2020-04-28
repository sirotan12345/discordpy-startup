# このファイルはgitignore指定されてます #

import os

# 実運用のHeroku上ではDISCORD_BOT_TOKENが定義されているため、それを使用する。
# ローカル動作確認時は別途確認用BOTのtokenを指定するが、token文字列はpush出来ないため空白にしてる。
try:
    DISCORD_BOT_TOKEN
    token = os.environ['DISCORD_BOT_TOKEN']
except NameError:
    # ここにtoken文字列を入れる。
    token = ""