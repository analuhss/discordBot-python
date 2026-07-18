#   BIBLIOTECA
import discord 
from discord.ext import commands
import token.py

#   PERMISSOES
permissoes = discord.Intentes.default()

#   PREFIXO PARA ATIVAR O GUNTER 
gunter = commands.Bot(commands_prefix = "!", intents = permissoes)

#   QUANDO O GUNTER LIGAR
@gunter.event
async def on_ready():
    print("Gunter funcionando")

gunter.run(token)