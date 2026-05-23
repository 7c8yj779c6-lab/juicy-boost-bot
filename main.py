import discord
import os

LIEN_SITE = "https://juicy-boost-site.vercel.app"

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

class FileBouton(discord.ui.View):
def __init__(self):
super().__init__(timeout=None)
self.add_item(discord.ui.Button(
label="🔴 Rejoindre la file d'attente",
url=LIEN_SITE,
style=discord.ButtonStyle.link
))

@bot.event
async def on_ready():
print(f"✅ Bot connecté : {bot.user}")

@bot.event
async def on_message(message):
if message.content == "!setup" and message.author.guild_permissions.administrator:
embed = discord.Embed(
title="🔥 Juicy's Boost — File d'attente",
description=(
"Tu veux te faire boost ?\n\n"
"Clique sur le bouton ci-dessous pour rejoindre la file d'attente !"
),
color=0xFF0000
)
embed.set_footer(text="Paiement PayPal uniquement • Juicy's Boost")
await message.channel.send(embed=embed, view=FileBouton())
await message.delete()

bot.run(os.environ["TOKEN"])

