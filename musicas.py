#antes de rodar: pip install -U discord.py[voice] yt-dlp PyNaCl
# e o FFmpeg precisa estar isntalado no sistema(não é pacote pip, é acessível no PATH -> Windows: winget install ffmpeg)

import discord
from discord import app_commands
import yt_dlp as youtube_dl

ydlOptions = {
    "format": "bestaudio/best", #pega a melhor qualidade disponível
    "noplaylist": True, # se o link for de uma playlist, pega só a primeira música
    "quiet" : True, # Não fica printando logs no terminal
    "default_searach": "ytsearach" #se o usuário digitar um nome em vez de um link, o yt-dlp faz uma busca no Youtube
    "source_address": "0.0.0.0", #Ajuste de rede que evita alguns erros de conexão IPv6, comuns com esse tipo de extração
}

ffmepegOptions = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    # flags de reconexão automática, importantws porque streams de audio podem cair no meio
    "options": "-vn",
    # No vídeo, descarta qualquer faixa de vídeo, já que só queremos o áudio
}

# FILA DE MÚSICAS POR SERVIDOR (id_guild -> lista de url_audio, titulo)
filas: dict[int, list[tuple[str]]] = {}

def registrarComandosMusica(gunter: discord.Client):
    # registra os comandos de música na árvore de comandos

def getFila(guild_id: int) -> list: #se o servidor nao tem uma lista ele cria uma
    if guild_id not in filas:
        filas[guild_id] = []
    return filas[guild_id]

def tocarProxima(guild: discord.Guild):
    fila = getFila(guild.id)
    vc = guild.voice_client

    if not fila or vc is None:
        return
    
    fonte = discord.FFmpegPCMAudio(url_audio,**ffmepegOptions)
    vc.play(fonte, after=lambda erro: tocarProxima(guild))

    # ENTRAR NO CANAL DE VOZ


