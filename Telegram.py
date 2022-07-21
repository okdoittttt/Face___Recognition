import telegram

class Sendtelegram:

    # Telegram API
    chat_token = "5412707226:AAH0GcrnT16aKknamkQW7j0ntXi76l9cREY"
    chat = telegram.Bot(token = chat_token)
    updates = chat.getUpdates()
    # for u in updates:
    #     print(u.message['chat']['id'])

    def sendMessege(self):
        bot = telegram.Bot(self.chat_token)
        text = '안녕하세요'
        bot.sendMessage(chat_id = "5526673347", text=text)

    # image = 'test_img.jpg'
    # bot.send_photo(chat_id = 'ID', photo=open(image, 'rb'))