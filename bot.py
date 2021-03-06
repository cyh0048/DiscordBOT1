import asyncio
from json import loads
import random
import os
import openpyxl
from datetime import datetime
import discord
from discord.ext import commands

client = discord.Client()
cclient = commands.Bot(command_prefix='!!')


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("000----------")

@client.event
async def on_message(message):
    sender = message.author.name
    nick = str(message.author.nick)

    if int(message.channel.id) == int('674410708544258048') and message.content.startswith("!출근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("관리자" + nick + "님이 출근 하셨습니다.　　" + now_time)
    if int(message.channel.id) == int('674410708544258048') and message.content.startswith("!퇴근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("관리자" + nick + "님이 퇴근 하셨습니다.　　" + now_time)

    if int(message.channel.id) == int('674075488100024339') and message.content.startswith("!출근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("👮경찰" + nick + "님이 출근 하셨습니다.　　" + now_time)
    if int(message.channel.id) == int('674075488100024339') and message.content.startswith("!퇴근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("👮경찰" + nick + "님이 퇴근 하셨습니다.　　" + now_time)

    if int(message.channel.id) == int('674083234115485696') and message.content.startswith("!출근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("EMS" +  nick + "님이 출근 하셨습니다.　　" + now_time)
    if int(message.channel.id) == int('674083234115485696') and message.content.startswith("!퇴근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("EMS" + nick + "님이 퇴근 하셨습니다.　　" + now_time)

    if int(message.channel.id) == int('674084356779933720') and message.content.startswith("!출근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("마피아" + nick + "님이 출근 하셨습니다.　　" + now_time)
    if int(message.channel.id) == int('674084356779933720') and message.content.startswith("!퇴근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("마피아" + nick + "님이 퇴근 하셨습니다.　　" + now_time)

    if int(message.channel.id) == int('674085239307632671') and message.content.startswith("!출근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("칠곡파" + nick + "님이 출근 하셨습니다.　　" + now_time)
    if int(message.channel.id) == int('674085239307632671') and message.content.startswith("!퇴근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("칠곡파" + nick + "님이 퇴근 하셨습니다.　　" + now_time)

    if int(message.channel.id) == int('674060336369893396') and message.content.startswith("!출근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("모터스" + nick + "님이 출근 하셨습니다.　　" + now_time)
    if int(message.channel.id) == int('674060336369893396') and message.content.startswith("!퇴근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("모터스" + nick + "님이 퇴근 하셨습니다.　　" + now_time)

    if int(message.channel.id) == int('674087295581945867') and message.content.startswith("!출근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("군인" + nick + "님이 출근 하셨습니다.　　" + now_time)
    if int(message.channel.id) == int('674087295581945867') and message.content.startswith("!퇴근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("군인" + nick + "님이 퇴근 하셨습니다.　　" + now_time)

    if int(message.channel.id) == int('674163348010565642') and message.content.startswith("!출근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("뉴비　" + nick + "님이 출근 하셨습니다.　　" + now_time)
    if int(message.channel.id) == int('674163348010565642') and message.content.startswith("!퇴근"):
        now = datetime.now()
        now_time = f'{now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
        await message.channel.send("뉴비　" + nick + "님이 퇴근 하셨습니다.　　" + now_time)

    if "씨발" in message.content or "개새끼" in message.content or "샹년" in message.content \
            or "좆" in message.content or "Tlqkf" in message.content or "병신" in message.content or "느금마" in message.content \
            or "애미" in message.content or "빡대가리" in message.content or "새끼" in message.content or "존나" in message.content or "존나" in message.content:
        author = message.guild.get_member(int(message.author.id))
        file = openpyxl.load_workbook("asdf.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.name):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("asdf.xlsx")
                if sheet["B" + str(i)].value == 2:
                    dogsae2 = discord.Embed(color=0xDF0101)
                    dogsae2.add_field(name="디스코드 이름", value=message.author.name, inline=False)
                    dogsae2.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=False)
                    dogsae2.add_field(name="사용언어", value=message.content, inline=False)
                    dogsae2.add_field(name="상태", value="투아웃", inline=False)
                    dogsae2.set_thumbnail(url=message.author.avatar_url)
                    # await client.get_channel(int(672143900940697600)).send(embed=dogsae2)
                    await message.channel.send(embed=dogsae2)
                    break
                elif sheet["B" + str(i)].value == 3:
                    dogsae3 = discord.Embed(color=0xDF0101)
                    dogsae3.add_field(name="디스코드 이름", value=message.author.name, inline=False)
                    dogsae3.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=False)
                    dogsae3.add_field(name="사용언어", value=message.content, inline=False)
                    dogsae3.add_field(name="상태", value="삼진아웃", inline=False)
                    dogsae3.set_thumbnail(url=message.author.avatar_url)
                    # await client.get_channel(int(672143900940697600)).send(embed=dogsae3)
                    await message.channel.send(embed=dogsae3)
                    await message.guild.ban(author)
                    break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.name)
                sheet["B" + str(i)].value = 1
                file.save("asdf.xlsx")
                dogsae = discord.Embed(color=0xDF0101)
                dogsae.add_field(name="디스코드 이름", value=message.author.name, inline=False)
                dogsae.add_field(name="디스코드 고유 아이디", value=message.author.id, inline=False)
                dogsae.add_field(name="사용언어", value=message.content, inline=False)
                dogsae.add_field(name="상태", value="원아웃", inline=False)
                dogsae.set_thumbnail(url=message.author.avatar_url)
                # await client.get_channel(int(672143900940697600)).send(embed=dogsae)
                await message.channel.send(embed=dogsae)
                break
            i += 1

    if message.content.startswith("~clear"):
        await message.channel.purge(limit=1000)

# client.run("NjczOTI1NjcwNjA2MzQwMTE5.XjjdRw.F3RYHU3leh9mBgZO8kSV2wHW8gI")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)