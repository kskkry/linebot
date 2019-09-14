from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

ch_token = "EehKZVJEnoMsmRZLHZDbaZHOfUvWsBn8eIEY9FnNIe+hoq1gdCWnFI3aYaLRS2DVvCT3EAfyt7yqW0ujDW/248Jk/KT/yaxmk800m5HudLrPGdqlhoOvV6MvSgaiDtvjCOh0UHqplS32TCVDXMJqngdB04t89/1O/w1cDnyilFU="
ch_secret = "8d72b53329c11a0f75ef870ee8f040f5"

lba = LineBotApi(ch_token)
handler = WebhookHandler(ch_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



