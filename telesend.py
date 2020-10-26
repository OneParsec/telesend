from telethon import TelegramClient, sync
i = 0
api_id = 1903006
api_hash = 'c049a8f37835121fcd20b7e729ff8414'
client = TelegramClient('Telegram Spamer', api_id, api_hash)
client.start()
num_of_repeats = int(input('Сколько раз вы хотите отправить сообщение? : '))
message = input('Какое сообщение вы хотите отправить? : ')
name_of_client = input('Кому вы хотите отправить сообщение? : ')
while num_of_repeats != i:
	client.send_message(name_of_client, message)
	i = i + 1