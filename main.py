#   BIBLIOTECA
import discord 
from discord.ext import commands
import meuToken
from meuToken import meuToken

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

# MENSAGEM PARA CRIAÇÃO DE CANAIS
@gunter.event
async def on_guild_channel_create(canal:discord.abc.GuildChannel):
    await canal.send(f"novo canal criado :) ")

# MENSAGEM PARA NOVOS MEMBROS
@gunter.event
async def on_member_join(membro:discord.Member):
    canal = gunter.get_channel(1427064418356695150)
    await canal.send(f"{membro.display_name}, chegou no servidor!\nSeja bem vindo!")

# MENSAGEM PARA QUANDO MEMBRO SAIR
@gunter.event
async def on_member_remove(membro:discord.Member):
    canal = gunter.get_channel(1427064418356695150)
    await canal.send(f"{membro.display_name}, saiu do servidor... :(")


gunter.run(meuToken)