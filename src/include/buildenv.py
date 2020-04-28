import os

# 実運用のHeroku上はDISCORD_BOT_TOKENが定義されている。
# ローカル動作確認時はDISCORD_BOT_TOKENが未定義なので、確認用BOTのtokenを指定する。
try:
    DISCORD_BOT_TOKEN
    token = os.environ['DISCORD_BOT_TOKEN']
except NameError:
    token = "NzA0NzEyMDcxNjE4NDk0NjQ0.XqhK8Q.0kY9QT7MIlmh0XMqIGDbk3X2zUY"