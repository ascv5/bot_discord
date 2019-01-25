import discord
import asyncio
import classe

client = discord.Client()

liste_interdite = []

@client.event

async def on_ready():
	print(client.user.name)
	print(client.user.id) 

@client.event
async def on_message(message):
	liste_interdite = []
	liste_interdite = classe.open_liste_interdite()
	msg = message.content

	if message.author == client.user:
		return

	else:
		try:
			index = liste_interdite.index(msg)
			if msg == liste_interdite[index]:
				await client.delete_message(message)
		except:
			pass
		print(liste_interdite)


client.run("NTM4Mzc5NTA0MTM4MDU5Nzg2.Dyy8gQ.TgwsK6_BySv3Py-OppZVMwlnEBg")
