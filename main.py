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

#   EMBED (TESTEKK, COM IMAGEM URL)
@gunter.command()
async def nalu(ctx:commands.Context):
    embed = discord.Embed(title = "Quem é nalu?", description = "Bom...\nA nalu é a criadora de todos os multiversos presentes na terra. Ela não apenas dita as regras do espaço-tempo, como cada decisão exala +100.000.00aura.\nEnquanto meros mortais tentam entender a física quântica, a NALU molda realidades paralelas antes de abrir os olhos.")

#   imagem da internet
    embed.set_image(url = "https://i.pinimg.com/736x/3c/a5/eb/3ca5ebdcc3a159df3bb1378eac2471a3.jpg")

    await ctx.reply(embed = embed)

#   EMBED (TESTE 2, COM IMAGEM DOS ARQUIVOS)
@gunter.command()
async def beta(ctx:commands.Context):
    embed = discord.Embed(title = "Beta?", description = "beta é quem me chama, cala boca e não reclama.")
    
#   imagem do computador
    imagemArquivo = discord.File("embedBeta.jpg", "beta.jpg")
    embed.set_image(url = "attachment://beta.jpg")

    await ctx.reply(file = imagemArquivo, embed = embed)

#   EMBED (TESTE3, COM THUMB, FOOTER E COLOR)
@gunter.command()
async def insta(ctx:commands.Context):
    embed = discord.Embed(title = "INSTA", description = "segue lá :)")

#   IMAGEM
    imagemInsta = discord.file("whatsappinsta.jpg", "insta.jpg")
    embed.set_image(url = "attachment://insta.jpg")

#   THUMB
    thumb = discord.File("logoInsta.png", "logo.png")
    embed.set_thumbnail(url = "attachment://logo.png")

#   FOOTER
    embed.set_footer(text = "obrigada")

#   COLOR
    embed.color = discord.Color.gold()

    await ctx.reply(files = [imagemInsta, thumb], embed = embed)

# EMBED COM COMANDOS DO GUNTER
@gunter.command()
async def comandos(ctx:commands.Context):
    embed = discord.Embed(title = """"Meus comandos :)", description = "SEMPRE USAR "!" ANTES\n- Gunter\n - nalu\n - beta\n- insta""")

#   imagem
    embed.set_image(url = "https://i.pinimg.com/736x/d4/0c/80/d40c80d32ad61f5be78b6650753e442c.jpg")

#   footer
    embed.set_footer(text = "imagens reais da nalu programando o gunter")

#   color
    embed.color = discord.Color.white()

    await ctx.reply(embed = embed)

gunter.run(meuToken)