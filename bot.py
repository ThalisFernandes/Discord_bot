import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.responses_handler(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)





def run_discord_bot():
    TOKEN = 'MTA5MzYzMzcwMjA2NTYwNjY4Ng.G1grMv.xkOlO_gstLVf765DfMnbu3C7ov40zI6u0Nb8vk'
    intent = discord.Intents().all()
    client = discord.Client(intents=intent)

    @client.event
    async def on_ready():
        print(f'{client.user} está na ativa!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said:'{user_message}'({channel})")
        if user_message[0] == '.':
            await send_message(message, user_message, is_private=False)
            

    client.run(TOKEN)