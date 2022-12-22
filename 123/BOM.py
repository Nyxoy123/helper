import discord
import discord
from discord.ext import commands
from config import settings
import asyncpraw
import asyncio
import os
import config
import requests as rq, time
from discord.ext import tasks
import requests
import json
from pprint import pprint
from discord import member

bot = commands.Bot(intents=intents, command_prefix = lambda b, m: ["m.", "M.", "м.", "М."])

@bot.event
async def on_ready():
    test1_task.start() # Monika 
    test2_task.start() # Yuri 
    test3_task.start() # Natsuki 
    test4_task.start() # Sayori 
    test5_task.start() # ddlc
    test6_task.start() # doki
    test7_task.start() # xen
    test8_task.start() # art
    test9_task.start() # min
    test10_task.start() # vagina 
    test11_task.start() # lesbi
    test12_task.start() # dota2
    test13_task.start() # anime
    test23_task.start() # shinobi

    await bot.change_presence(status=discord.Status.online, activity=discord.Game("#HENTAI CLUB#"))
    print("STARTED")

@tasks.loop(minutes=30) # Л клуб monika
async def test1_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=monika_(doki_doki_literature_club)+")

    list_porn = resp.json()

    with open("urls.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("urls.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("urls.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(988407397846487090)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # Л клуб yuri
async def test2_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=yuri_(doki_doki_literature_club)+")

    list_porn = resp.json()

    with open("urls2.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("urls2.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("urls2.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(881958907340271667)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # Л клуб natsuki
async def test3_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=natsuki_(doki_doki_literature_club)+")

    list_porn = resp.json()

    with open("urls3.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("urls3.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("urls3.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(881958907340271667)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # Л клуб Sayori
async def test4_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=sayori_(doki_doki_literature_club)+")

    list_porn = resp.json()

    with open("urls4.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("urls4.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("urls4.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(881958907340271667)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # Л клуб  ddlc
async def test5_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=ddlc")

    list_porn = resp.json()

    with open("urls5.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("urls5.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("urls5.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(881958907340271667)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # Л клуб
async def test6_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=doki_doki_literature_club")

    list_porn = resp.json()

    with open("urls6.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("urls6.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("urls6.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(881958907340271667)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # хен
async def test7_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&")

    list_porn = resp.json()

    with open("urls7.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("urls7.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("urls7.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(1055127134823272469)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # art
async def test8_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=art")

    list_porn = resp.json()

    with open("urls8.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("urls8.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("urls8.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(988428068840419361)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # Minecraft
async def test9_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=minecraft")

    list_porn = resp.json()

    with open("min.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("min", "r") as fr:
            if (fr.read() != preview_url):
                with open("min.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(994976604470124554)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # Vagina
async def test10_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=vagina")

    list_porn = resp.json()

    with open("vagina.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("vagina.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("vagina.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(994977058964897902)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # lesbian
async def test11_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=lesbian")

    list_porn = resp.json()

    with open("lesbi.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("lesbi.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("lesbi.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(994977319095648276)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # dota2
async def test12_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=dota2")

    list_porn = resp.json()

    with open("dota2.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("dota2.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("dota2.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(994978051786031207)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # anime
async def test13_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=anime")

    list_porn = resp.json()

    with open("anime.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("anime.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("anime.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(994978610031116428)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

@tasks.loop(minutes=30) # Л клуб shinobi
async def test23_task():
    resp = requests.get("https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&tags=shinobi")

    list_porn = resp.json()

    with open("shinobi.txt", "r") as fr:
      last_porn = fr.read()

    new_porn = []
    for porn in list_porn:
      if porn['preview_url'] == last_porn:
        break
      else:
        new_porn.append(porn['preview_url'])
        
    for preview_url in new_porn:
        print("Обнаружен новый пост! Ссылка: " + preview_url)
            
        with open("shinobi.txt", "r") as fr:
            if (fr.read() != preview_url):
                with open("shinobi.txt", "w") as fw:
                    fw.write(preview_url)
                    await (bot.get_channel(988407397846487090)).send(preview_url)

    else: print("Нового поста не обнаружено")
    time.sleep(3)

bot.run (config.settings["DISCORD_TOKEN"])