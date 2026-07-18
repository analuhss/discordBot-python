#   BIBLIOTECA
import discord 
from discord.ext import commands
import meuToken.py
from meuToken.py import meuToken

#   PERMISSOES
permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True

#   PREFIXO PARA ATIVAR O GUNTER 
gunter = commands.Bot(command_prefix = "!", intents = permissoes)

#   QUANDO O GUNTER LIGAR
@gunter.event
async def on_ready():
    print("Gunter funcionando")

#   COMANDO BÁSICO DE RESPOSTA
@gunter.command()
async def Gunter(ctx:commands.Context):
    nomeUsuario = ctx.author.display_name
    await ctx.reply(f"to aqui {nomeUsuario} :) ")

gunter.run(meuToken)