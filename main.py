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
    imagemArquivo = discord.File("imagens\embedBeta.jpg", "beta.jpg")
    embed.set_image(url = "attachment://beta.jpg")

    await ctx.reply(file = imagemArquivo, embed = embed)

#   EMBED (TESTE3, COM THUMB, FOOTER E COLOR)
@gunter.command()
async def insta(ctx:commands.Context):
    embed = discord.Embed(title = "INSTA", description = "segue lá :)")

#   IMAGEM
    imagemInsta = discord.File("imagens\whatsappinsta.jpeg", "insta.jpeg")
    embed.set_image(url = "attachment://insta.jpeg")

#   THUMB
    thumb = discord.File("imagens\logoInsta.png", "logo.png")
    embed.set_thumbnail(url = "attachment://logo.png")

#   FOOTER
    embed.set_footer(text = "obrigada")

#   COLOR
    embed.color = discord.Color.gold()

    await ctx.reply(files = [imagemInsta, thumb], embed = embed)

# EMBED COM COMANDOS DO GUNTER
@gunter.command()
async def comandos(ctx:commands.Context):
    embed = discord.Embed(title = """Meus comandos :)""", description = 'SEMPRE USAR "!" ANTES\n- Gunter\n - nalu\n - beta\n- insta\n- surpresa\n- segredo\n- anna\n- farm\n- BOTOES')

#   imagem
    embed.set_image(url = "https://i.pinimg.com/736x/d4/0c/80/d40c80d32ad61f5be78b6650753e442c.jpg")

#   footer
    embed.set_footer(text = "imagens reais da nalu programando o gunter")

#   color
    embed.color = discord.Color.light_theme()

    await ctx.send(embed = embed)

#   TESTE DE BOTÃO
@gunter.command()
async def surpresa(ctx:commands.Context):
#   configuração da resposta do botão
    async def respostaBotao(interact:discord.Interaction):
        await interact.response.send_message("come aloong with mee")

#   configuração da aparência do botão
    view = discord.ui.View()
    botao = discord.ui.Button(label = 'clique aqui', style = discord.ButtonStyle.green) # função style: muda a aparência do botão

#   resposta do botão:
    botao.callback = respostaBotao

    view.add_item(botao)
    await ctx.reply(view = view)

#   BOTAO EPHEMERAL (Só quem apertou o botão vê a mensagem)
@gunter.command()
async def segredo(ctx:commands.Context):
    async def respostaBotao(interact:discord.Interaction):
        await interact.response.send_message("""beijos da nalu :)""", ephemeral= True)

    view = discord.ui.View()
    botao = discord.ui.Button(label = "clique aqui", style = discord.ButtonStyle.green)

    botao.callback = respostaBotao

    view.add_item(botao)
    await ctx.reply(view = view)


#   BOTÃO COM MAIS DE UMA RESPOSTA
@gunter.command()
async def anna(ctx:commands.Context):
    async def respostaBotao(interact:discord.Interaction):
        await interact.response.send_message("oque?")
        await interact.followup.send("você finaliza meus...")
        await interact.followup.send("SANDUÍCHES")
        await interact.followup.send('''era o que eu ia dizer''')

    view = discord.ui.View()
    botao = discord.ui.Button(label = "É MEIO DOIDO", style = discord.ButtonStyle.green)
    botao.callback = respostaBotao

    view.add_item(botao)
    await ctx.reply (view = view)

#   BOTÃO COM URL
@gunter.command()
async def farm(ctx:commands.Context):
    view = discord.ui.View()
    botao = discord.ui.Button(label = 'AURA MÁXIMA', style = discord.ButtonStyle.danger, url = "https://www.youtube.com/watch?v=7IFvoaH44Is")

    view.add_item(botao)
    await ctx.reply(view = view)

#   VIEW COM MAIS DE UM BOTÃO
@gunter.command()
async def BOTOES(ctx:commands.Context):

    view = discord.ui.View()
    botao1 = discord.ui.Button(label = "spotify", style = discord.ButtonStyle.green, url = "https://open.spotify.com/user/31mlgmrjumt75rhyfqoqxzidrqky?si=IxHS8BK-RaWqfC6P0MnVCA&utm_source=copy-link")
    botao2 = discord.ui.Button(label = "insta", style = discord.ButtonStyle.red, url = "https://www.instagram.com/nalucinante?igsh=MWhiZ2QwM3oxa21oZw==")
    botao3 = discord.ui.Button(label = "tiks", style = discord.ButtonStyle.grey, url = "https://www.tiktok.com/@nalucinante?_r=1&_t=ZS-989SCNOmVE1")

    view.add_item(botao1)
    view.add_item(botao2)
    view.add_item(botao3)
    await ctx.reply(view = view)

#   MENU DE SELEÇÃO
@gunter.command()
async def membros(ctx:commands.Context):
#   resposta do bot:
    async def selecaoResposta(interact:discord.Interaction):
        escolha = interact.data['values'][0]
        if escolha == "1":
            resposta = "Que ótima escolha, a nalu é realmente uma boa amiga"
        elif escolha == "2":
            resposta = "Bom saber, gunter fica feliz com essa resposta"
        elif escolha == "3":
            resposta = "Caramba! Gunter também gosta muito da nalu"
        
#       o ephemeral é para que apenas quem clicar na seleção veja a resposta
        await interact.response.send_message(resposta, ephemeral = True)

#   plaeceholder: o que está escrito em cima do menu
    menuSelecao = discord.ui.Select(placeholder = "Qual seu membro favorito?")
#   opções:
    opcoes = [
        discord.SelectOption(label = "Nalu", value = "1"),
        discord.SelectOption(label = "Nalu", value = "2"),
        discord.SelectOption(label = "Nalu", value = "3")
    ]
    menuSelecao.options = opcoes
    menuSelecao.callback = selecaoResposta
    view = discord.ui.View()
    view.add_item(menuSelecao)
    await ctx.send (view = view)

gunter.run(meuToken)