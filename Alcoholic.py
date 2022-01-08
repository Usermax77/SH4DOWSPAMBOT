import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest


from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest


from Config import STRING, SUDO, BIO_MESSAGE, ALIVE_NAME, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 , STRING26 , STRING27 , STRING28 , STRING29 , STRING30
import asyncio
import telethon.utils
from telethon.import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH 
String_Session01 = STRING
String_Session02 = STRING2
String_Session03 = STRING3
String_Session04 = STRING4
String_Session05 = STRING5
String_Session06 = STRING6
String_Session07 = STRING7
String_Session08 = STRING8
String_Session09 = STRING9
String_Session10 = STRING10
String_Session11 = STRING11
String_Session12 = STRING12
String_Session13 = STRING13
String_Session14 = STRING14
String_Session15 = STRING15
String_Session16 = STRING16
String_Session17 = STRING17
String_Session18 = STRING18
String_Session19 = STRING19
String_Session20 = STRING20
String_Session21 = STRING21
String_Session22 = STRING22
String_Session23 = STRING23
String_Session24 = STRING24
String_Session25 = STRING25
String_Session26 = STRING26
String_Session27 = STRING27
String_Session28 = STRING28
String_Session29 = STRING29
String_Session30 = STRING30
String_Session31 = STRING31
String_Session32 = STRING32
String_Session33 = STRING33
String_Session34 = STRING34
String_Session35 = STRING35
String_Session36 = STRING36
String_Session37 = STRING37
String_Session38 = STRING38
String_Session39 = STRING39
String_Session40 = STRING40
String_Session41 = STRING41
String_Session42 = STRING42
String_Session43 = STRING43
String_Session44 = STRING44
String_Session45 = STRING45
String_Session46 = STRING46
String_Session47 = STRING47
String_Session48 = STRING48
String_Session49 = STRING49
String_Session50 = STRING50

Bot1 = ''
Bot2 = ''
Bot3 = ''
Bot4 = ''
Bot5 = ''
Bot6 = ''
Bot7 = ''
Bot8 = ''
Bot9 = ''
Bot10 = ''
Bot11 = ''
Bot12 = ''
Bot13 = ''
Bot14 = ''
Bot15 = ''
Bot16 = ''
Bot17 = ''
Bot18 = ''
Bot19 = ''
Bot20 = ''
Bot21 = ''
Bot22 = ''
Bot23 = ''
Bot24 = ''
Bot25 = ''
Bot26 = ''
Bot27 = ''
Bot28 = ''
Bot29 = ''
Bot30 = ''
Bot31 = ''
Bot32 = ''
Bot33 = ''
Bot34 = ''
Bot35 = ''
Bot36 = ''
Bot37 = ''
Bot38 = ''
Bot39 = ''
Bot40 = ''
Bot41 = ''
Bot42 = ''
Bot43 = ''
Bot44 = ''
Bot45 = ''
Bot46 = ''
Bot47 = ''
Bot48 = ''
Bot49 = ''
Bot50 = ''


que = {}

SMEX_USERS = []
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_yukki():
    global Bot1
    global Bot2
    global Bot3
    global Bot4
    global Bot5
    global Bot6
    global Bot7
    global Bot8
    global Bot9
    global Bot10
    global Bot11
    global Bot12
    global Bot13
    global Bot14
    global Bot15
    global Bot16
    global Bot17
    global Bot18
    global Bot19
    global Bot20
    global Bot21
    global Bot22
    global Bot23
    global Bot24
    global Bot25
    global Bot26
    global Bot27
    global Bot28
    global Bot29
    global Bot30
    global Bot31
    global Bot32
    global Bot33
    global Bot34
    global Bot35
    global Bot36
    global Bot37
    global Bot38
    global Bot39
    global Bot40
    global Bot41
    global Bot42
    global Bot43
    global Bot44
    global Bot45
    global Bot46
    global Bot47
    global Bot48
    global Bot49
    global Bot50

   if String_Session01:
        session_name = str(String_Session01)
        print("String 1 Found")
        Bot1 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await Bot1.start()
            botme = await Bot1.get_me()
            await Bot1(functions.channels.JoinChannelRequest(channel=""))
            await Bot1(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot1(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot1(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot1(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        Bot1 = TelegramClient(session_name, a, b)
        try:
            await Bot1.start()
        except Exception as e:
            pass

    if String_Session02:
        session_name = str(String_Session02)
        print("String 2 Found")
        Bot2 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await Bot2.start()
            botme = await Bot2.get_me()
            await Bot2(functions.channels.JoinChannelRequest(channel=""))
            await Bot2(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot2(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot2(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot2(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        session_name = "startup"
        Bot2 = TelegramClient(session_name, a, b)
        try:
            await Bot2.start()
        except Exception as e:
            pass
       
      if String_Session03:
        session_name = str(String_Session03)
        print("String 3 Found")
        Bot3 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await Bot3.start()
            botme = await Bot3.get_me()
            await Bot3(functions.channels.JoinChannelRequest(channel=""))
            await Bot3(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot3(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot3(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot3(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        session_name = "startup"
        Bot3 = TelegramClient(session_name, a, b)
        try:
            await Bot3.start()
        except Exception as e:
            pass

       if String_Session04:
        session_name = str(String_Session04)
        print("String 4 Found")
        Bot4 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await Bot4.start()
            botme = await Bot4.get_me()
            await Bot4(functions.channels.JoinChannelRequest(channel=""))
            await Bot4(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot4(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot4(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot4(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        session_name = "startup"
        Bot4 = TelegramClient(session_name, a, b)
        try:
            await Bot4.start()
        except Exception as e:
            pass

       if String_Session05:
        session_name = str(String_Session05)
        print("String 5 Found")
        Bot5 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await Bot5.start()
            botme = await Bot5.get_me()
            await Bot5(functions.channels.JoinChannelRequest(channel=""))
            await Bot5(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot5(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot5(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot5(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        session_name = "startup"
        Bot5 = TelegramClient(session_name, a, b)
        try:
            await Bot5.start()
        except Exception as e:
            pass

       if String_Session06:
        session_name = str(String_Session06)
        print("String 6 Found")
        Bot6 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await Bot6.start()
            botme = await Bot6.get_me()
            await Bot6(functions.channels.JoinChannelRequest(channel=""))
            await Bot6(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot6(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot6(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot6(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        session_name = "startup"
        Bot6 = TelegramClient(session_name, a, b)
        try:
            await Bot6.start()
        except Exception as e:
            pass

       if String_Session07:
        session_name = str(String_Session07)
        print("String 7 Found")
        Bot7 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await Bot7.start()
            botme = await Bot7.get_me()
            await Bot7(functions.channels.JoinChannelRequest(channel=""))
            await Bot7(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot7(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot7(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot7(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        session_name = "startup"
        Bot7 = TelegramClient(session_name, a, b)
        try:
            await Bot7.start()
        except Exception as e:
            pass

       if String_Session08:
        session_name = str(String_Session08)
        print("String 8 Found")
        Bot8 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await Bot8.start()
            botme = await Bot8.get_me()
            await Bot8(functions.channels.JoinChannelRequest(channel=""))
            await Bot8(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot8(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot8(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot8(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        session_name = "startup"
        Bot8 = TelegramClient(session_name, a, b)
        try:
            await Bot8.start()
        except Exception as e:
            pass

       if String_Session09:
        session_name = str(String_Session09)
        print("String 9 Found")
        Bot9 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await Bot9.start()
            botme = await Bot9.get_me()
            await Bot9(functions.channels.JoinChannelRequest(channel=""))
            await Bot9(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot9(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot9(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot9(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        session_name = "startup"
        Bot9 = TelegramClient(session_name, a, b)
        try:
            await Bot9.start()
        except Exception as e:
            pass

       if String_Session10:
        session_name = str(String_Session10)
        print("String 10 Found")
        Bot10 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await Bot10.start()
            botme = await Bot10.get_me()
            await Bot10(functions.channels.JoinChannelRequest(channel=""))
            await Bot10(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot10(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot10(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot10(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        session_name = "startup"
        Bot10 = TelegramClient(session_name, a, b)
        try:
            await Bot10.start()
        except Exception as e:
            pass

       if String_Session11:
        session_name = str(String_Session11)
        print("String 11 Found")
        Bot11 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await Bot11.start()
            botme = await Bot11.get_me()
            await Bot11(functions.channels.JoinChannelRequest(channel=""))
            await Bot11(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot11(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot11(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot11(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        session_name = "startup"
        Bot11 = TelegramClient(session_name, a, b)
        try:
            await Bot11.start()
        except Exception as e:
            pass

       if String_Session12:
        session_name = str(String_Session12)
        print("String 12 Found")
        Bot12 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await Bot12.start()
            botme = await Bot12.get_me()
            await Bot12(functions.channels.JoinChannelRequest(channel=""))
            await Bot12(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot12(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot12(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot12(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        session_name = "startup"
        Bot12 = TelegramClient(session_name, a, b)
        try:
            await Bot12.start()
        except Exception as e:
            pass

       if String_Session13:
        session_name = str(String_Session13)
        print("String 13 Found")
        Bot13 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await Bot13.start()
            botme = await Bot13.get_me()
            await Bot13(functions.channels.JoinChannelRequest(channel=""))
            await Bot13(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot13(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot13(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot13(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        session_name = "startup"
        Bot13 = TelegramClient(session_name, a, b)
        try:
            await Bot13.start()
        except Exception as e:
            pass

       if String_Session14:
        session_name = str(String_Session14)
        print("String 14 Found")
        Bot14 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await Bot14.start()
            botme = await Bot14.get_me()
            await Bot14(functions.channels.JoinChannelRequest(channel=""))
            await Bot14(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot14(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot14(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot14(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        session_name = "startup"
        Bot14 = TelegramClient(session_name, a, b)
        try:
            await Bot14.start()
        except Exception as e:
            pass

       if String_Session15:
        session_name = str(String_Session15)
        print("String 15 Found")
        Bot15 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await Bot15.start()
            botme = await Bot15.get_me()
            await Bot15(functions.channels.JoinChannelRequest(channel=""))
            await Bot15(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot15(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot15(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot15(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        session_name = "startup"
        Bot15 = TelegramClient(session_name, a, b)
        try:
            await Bot15.start()
        except Exception as e:
            pass

       if String_Session16:
        session_name = str(String_Session16)
        print("String 16 Found")
        Bot16 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await Bot16.start()
            botme = await Bot16.get_me()
            await Bot16(functions.channels.JoinChannelRequest(channel=""))
            await Bot16(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot16(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot16(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot16(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        Bot16 = TelegramClient(session_name, a, b)
        try:
            await Bot16.start()
        except Exception as e:
            pass

       if String_Session17:
        session_name = str(String_Session17)
        print("String 17 Found")
        Bot17 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await Bot17.start()
            botme = await Bot17.get_me()
            await Bot17(functions.channels.JoinChannelRequest(channel=""))
            await Bot17(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot17(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot17(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot17(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        Bot17 = TelegramClient(session_name, a, b)
        try:
            await Bot17.start()
        except Exception as e:
            pass

       if String_Session18:
        session_name = str(String_Session18)
        print("String 18 Found")
        Bot18 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await Bot18.start()
            botme = await Bot18.get_me()
            await Bot18(functions.channels.JoinChannelRequest(channel=""))
            await Bot18(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot18(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot18(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot18(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        Bot18 = TelegramClient(session_name, a, b)
        try:
            await Bot18.start()
        except Exception as e:
            pass

       if String_Session19:
        session_name = str(String_Session19)
        print("String 19 Found")
        Bot19 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await Bot19.start()
            botme = await Bot19.get_me()
            await Bot19(functions.channels.JoinChannelRequest(channel=""))
            await Bot19(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot19(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot19(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot19(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        Bot19 = TelegramClient(session_name, a, b)
        try:
            await Bot19.start()
        except Exception as e:
            pass

       if String_Session20:
        session_name = str(String_Session20)
        print("String 20 Found")
        Bot20 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await Bot20.start()
            botme = await Bot20.get_me()
            await Bot20(functions.channels.JoinChannelRequest(channel=""))
            await Bot20(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot20(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot20(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot20(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        Bot20 = TelegramClient(session_name, a, b)
        try:
            await Bot20.start()
        except Exception as e:
            pass

       if String_Session21:
        session_name = str(String_Session21)
        print("String 21 Found")
        Bot21 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await Bot21.start()
            botme = await Bot21.get_me()
            await Bot21(functions.channels.JoinChannelRequest(channel=""))
            await Bot21(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot21(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot21(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot21(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        Bot21 = TelegramClient(session_name, a, b)
        try:
            await Bot21.start()
        except Exception as e:
            pass

       if String_Session22:
        session_name = str(String_Session22)
        print("String 22 Found")
        Bot22 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await Bot22.start()
            botme = await Bot22.get_me()
            await Bot22(functions.channels.JoinChannelRequest(channel=""))
            await Bot22(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot22(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot22(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot22(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        Bot22 = TelegramClient(session_name, a, b)
        try:
            await Bot22.start()
        except Exception as e:
            pass

       if String_Session23:
        session_name = str(String_Session23)
        print("String 23 Found")
        Bot23 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await Bot23.start()
            botme = await Bot23.get_me()
            await Bot23(functions.channels.JoinChannelRequest(channel=""))
            await Bot23(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot23(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot23(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot23(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        Bot23 = TelegramClient(session_name, a, b)
        try:
            await Bot23.start()
        except Exception as e:
            pass

       if String_Session24:
        session_name = str(String_Session24)
        print("String 24 Found")
        Bot24 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await Bot24.start()
            botme = await Bot24.get_me()
            await Bot24(functions.channels.JoinChannelRequest(channel=""))
            await Bot24(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot24(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot24(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot24(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        Bot24 = TelegramClient(session_name, a, b)
        try:
            await Bot24.start()
        except Exception as e:
            pass

       if String_Session25:
        session_name = str(String_Session25)
        print("String 25 Found")
        Bot25 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await Bot25.start()
            botme = await Bot25.get_me()
            await Bot25(functions.channels.JoinChannelRequest(channel=""))
            await Bot25(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot25(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot25(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot25(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        Bot25 = TelegramClient(session_name, a, b)
        try:
            await Bot25.start()
        except Exception as e:
            pass

       if String_Session26:
        session_name = str(String_Session26)
        print("String 26 Found")
        Bot26 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await Bot26.start()
            botme = await Bot26.get_me()
            await Bot26(functions.channels.JoinChannelRequest(channel=""))
            await Bot26(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot26(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot26(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot26(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        Bot26 = TelegramClient(session_name, a, b)
        try:
            await Bot26.start()
        except Exception as e:
            pass

       if String_Session27:
        session_name = str(String_Session27)
        print("String 27 Found")
        Bot27 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await Bot27.start()
            botme = await Bot27.get_me()
            await Bot27(functions.channels.JoinChannelRequest(channel=""))
            await Bot27(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot27(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot27(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot27(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        session_name = "startup"
        Bot27 = TelegramClient(session_name, a, b)
        try:
            await Bot27.start()
        except Exception as e:
            pass

       if String_Session28:
        session_name = str(String_Session28)
        print("String 28 Found")
        Bot28 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await Bot28.start()
            botme = await Bot28.get_me()
            await Bot28(functions.channels.JoinChannelRequest(channel=""))
            await Bot28(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot28(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot28(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot28(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        session_name = "startup"
        Bot28 = TelegramClient(session_name, a, b)
        try:
            await Bot28.start()
        except Exception as e:
            pass

       if String_Session29:
        session_name = str(String_Session29)
        print("String 29 Found")
        Bot29 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await Bot29.start()
            botme = await Bot29.get_me()
            await Bot29(functions.channels.JoinChannelRequest(channel=""))
            await Bot29(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot29(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot29(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot29(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        session_name = "startup"
        Bot29 = TelegramClient(session_name, a, b)
        try:
            await Bot29.start()
        except Exception as e:
            pass

       if String_Session30:
        session_name = str(String_Session30)
        print("String 30 Found")
        Bot30 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await Bot30.start()
            botme = await Bot30.get_me()
            await Bot30(functions.channels.JoinChannelRequest(channel=""))
            await Bot30(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot30(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot30(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot30(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        session_name = "startup"
        Bot30 = TelegramClient(session_name, a, b)
        try:
            await Bot30.start()
        except Exception as e:
            pass

       if String_Session31:
        session_name = str(String_Session31)
        print("String 31 Found")
        Bot31 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 31")
            await Bot31.start()
            botme = await Bot31.get_me()
            await Bot31(functions.channels.JoinChannelRequest(channel=""))
            await Bot31(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot31(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot31(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot31(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "startup"
        Bot31 = TelegramClient(session_name, a, b)
        try:
            await Bot31.start()
        except Exception as e:
            pass

       if String_Session32:
        session_name = str(String_Session32)
        print("String 32 Found")
        Bot32 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 32")
            await Bot32.start()
            botme = await Bot32.get_me()
            await Bot32(functions.channels.JoinChannelRequest(channel=""))
            await Bot32(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot32(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot32(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot32(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        session_name = "startup"
        Bot32 = TelegramClient(session_name, a, b)
        try:
            await Bot32.start()
        except Exception as e:
            pass

       if String_Session33:
        session_name = str(String_Session33)
        print("String 33 Found")
        Bot33 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 33")
            await Bot33.start()
            botme = await Bot33.get_me()
            await Bot33(functions.channels.JoinChannelRequest(channel=""))
            await Bot33(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot33(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot33(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot33(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        session_name = "startup"
        Bot33 = TelegramClient(session_name, a, b)
        try:
            await Bot33.start()
        except Exception as e:
            pass

       if String_Session34:
        session_name = str(String_Session34)
        print("String 34 Found")
        Bot34 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 34")
            await Bot34.start()
            botme = await Bot34.get_me()
            await Bot34(functions.channels.JoinChannelRequest(channel=""))
            await Bot34(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot34(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot34(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot34(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        session_name = "startup"
        Bot34 = TelegramClient(session_name, a, b)
        try:
            await Bot34.start()
        except Exception as e:
            pass

       if String_Session35:
        session_name = str(String_Session35)
        print("String 35 Found")
        Bot35 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 35")
            await Bot35.start()
            botme = await Bot35.get_me()
            await Bot35(functions.channels.JoinChannelRequest(channel=""))
            await Bot35(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot35(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot35(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot35(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        session_name = "startup"
        Bot35 = TelegramClient(session_name, a, b)
        try:
            await Bot35.start()
        except Exception as e:
            pass

       if String_Session36:
        session_name = str(String_Session36)
        print("String 36 Found")
        Bot36 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 36")
            await Bot36.start()
            botme = await Bot36.get_me()
            await Bot36(functions.channels.JoinChannelRequest(channel=""))
            await Bot36(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot36(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot36(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot36(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "startup"
        Bot36 = TelegramClient(session_name, a, b)
        try:
            await Bot36.start()
        except Exception as e:
            pass

       if String_Session37:
        session_name = str(String_Session37)
        print("String 37 Found")
        Bot37 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 37")
            await Bot37.start()
            botme = await Bot37.get_me()
            await Bot37(functions.channels.JoinChannelRequest(channel=""))
            await Bot37(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot37(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot37(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot37(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "startup"
        Bot37 = TelegramClient(session_name, a, b)
        try:
            await Bot37.start()
        except Exception as e:
            pass

       if String_Session38:
        session_name = str(String_Session38)
        print("String 38 Found")
        Bot38 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 38")
            await Bot38.start()
            botme = await Bot38.get_me()
            await Bot38(functions.channels.JoinChannelRequest(channel=""))
            await Bot38(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot38(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot38(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot38(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "startup"
        Bot38 = TelegramClient(session_name, a, b)
        try:
            await Bot38.start()
        except Exception as e:
            pass

       if String_Session39:
        session_name = str(String_Session39)
        print("String 39 Found")
        Bot39 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 39")
            await Bot39.start()
            botme = await Bot39.get_me()
            await Bot39(functions.channels.JoinChannelRequest(channel=""))
            await Bot39(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot39(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot39(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot39(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "startup"
        Bot39 = TelegramClient(session_name, a, b)
        try:
            await Bot39.start()
        except Exception as e:
            pass

       if String_Session40:
        session_name = str(String_Session40)
        print("String 40 Found")
        Bot40 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 40")
            await Bot40.start()
            botme = await Bot40.get_me()
            await Bot40(functions.channels.JoinChannelRequest(channel=""))
            await Bot40(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot40(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot40(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot40(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "startup"
        Bot40 = TelegramClient(session_name, a, b)
        try:
            await Bot40.start()
        except Exception as e:
            pass

       if String_Session41:
        session_name = str(String_Session41)
        print("String 41 Found")
        Bot41 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 41")
            await Bot41.start()
            botme = await Bot41.get_me()
            await Bot41(functions.channels.JoinChannelRequest(channel=""))
            await Bot41(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot41(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot41(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot41(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 41 not Found")
        session_name = "startup"
        Bot41 = TelegramClient(session_name, a, b)
        try:
            await Bot41.start()
        except Exception as e:
            pass

       if String_Session42:
        session_name = str(String_Session42)
        print("String 42 Found")
        Bot42 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 42")
            await Bot42.start()
            botme = await Bot42.get_me()
            await Bot42(functions.channels.JoinChannelRequest(channel=""))
            await Bot42(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot42(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot42(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot42(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 42 not Found")
        session_name = "startup"
        Bot42 = TelegramClient(session_name, a, b)
        try:
            await Bot42.start()
        except Exception as e:
            pass

       if String_Session43:
        session_name = str(String_Session43)
        print("String 43 Found")
        Bot43 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 43")
            await Bot43.start()
            botme = await Bot43.get_me()
            await Bot43(functions.channels.JoinChannelRequest(channel=""))
            await Bot43(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot43(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot43(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot43(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 43 not Found")
        session_name = "startup"
        Bot43 = TelegramClient(session_name, a, b)
        try:
            await Bot43.start()
        except Exception as e:
            pass

       if String_Session44:
        session_name = str(String_Session44)
        print("String 44 Found")
        Bot44 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 44")
            await Bot44.start()
            botme = await Bot44.get_me()
            await Bot44(functions.channels.JoinChannelRequest(channel=""))
            await Bot44(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot44(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot44(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot44(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 44 not Found")
        session_name = "startup"
        Bot44 = TelegramClient(session_name, a, b)
        try:
            await Bot44.start()
        except Exception as e:
            pass

       if String_Session45:
        session_name = str(String_Session45)
        print("String 45 Found")
        Bot45 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 45")
            await Bot45.start()
            botme = await Bot45.get_me()
            await Bot45(functions.channels.JoinChannelRequest(channel=""))
            await Bot45(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot45(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot45(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot45(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 45 not Found")
        session_name = "startup"
        Bot45 = TelegramClient(session_name, a, b)
        try:
            await Bot45.start()
        except Exception as e:
            pass

       if String_Session46:
        session_name = str(String_Session46)
        print("String 46 Found")
        Bot46 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 46")
            await Bot46.start()
            botme = await Bot46.get_me()
            await Bot46(functions.channels.JoinChannelRequest(channel=""))
            await Bot46(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot46(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot46(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot46(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 46 not Found")
        session_name = "startup"
        Bot46 = TelegramClient(session_name, a, b)
        try:
            await Bot46.start()
        except Exception as e:
            pass

       if String_Session47:
        session_name = str(String_Session47)
        print("String 47 Found")
        Bot47 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 47")
            await Bot47.start()
            botme = await Bot47.get_me()
            await Bot47(functions.channels.JoinChannelRequest(channel=""))
            await Bot47(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot47(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot47(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot47(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 47 not Found")
        session_name = "startup"
        Bot47 = TelegramClient(session_name, a, b)
        try:
            await Bot47.start()
        except Exception as e:
            pass

       if String_Session48:
        session_name = str(String_Session48)
        print("String 48 Found")
        Bot48 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 48")
            await Bot48.start()
            botme = await Bot48.get_me()
            await Bot48(functions.channels.JoinChannelRequest(channel=""))
            await Bot48(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot48(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot48(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot48(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 48 not Found")
        session_name = "startup"
        Bot48 = TelegramClient(session_name, a, b)
        try:
            await Bot48.start()
        except Exception as e:
            pass

       if String_Session49:
        session_name = str(String_Session49)
        print("String 49 Found")
        Bot49 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 49")
            await Bot49.start()
            botme = await Bot49.get_me()
            await Bot49(functions.channels.JoinChannelRequest(channel=""))
            await Bot49(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot49(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot49(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot49(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 49 not Found")
        session_name = "startup"
        Bot49 = TelegramClient(session_name, a, b)
        try:
            await Bot49.start()
        except Exception as e:
            pass

       if String_Session50:
        session_name = str(String_Session50)
        print("String 50 Found")
        Bot50 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 50")
            await Bot50.start()
            botme = await Bot50.get_me()
            await Bot50(functions.channels.JoinChannelRequest(channel=""))
            await Bot50(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT_SUPPORT"))
            await Bot50(functions.channels.JoinChannelRequest(channel="@SH4DOW_SPAMBOT"))
            await Bot50(functions.channels.JoinChannelRequest(channel="@SH4DOW_BOT_PROJECT"))
            await Bot50(functions.channels.JoinChannelRequest(channel="@SH4DOW_COMMUNITY"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 50 not Found")
        session_name = "startup"
        Bot50 = TelegramClient(session_name, a, b)
        try:
            await Bot50.start()
        except Exception as e:
            pass
                  
   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@Bot01.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot02.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot03.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot04.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot05.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot06.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot07.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot08.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot09.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\.bio"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(yukki[0])
            text = "Changing Bio"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio By MULTI SPAMBOT")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@Bot01.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot02.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot03.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot04.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot05.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot06.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot07.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot08.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot09.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\.join"))


async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@Bot01.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot02.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot03.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot04.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot05.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot06.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot07.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot08.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot09.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))



async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
         
@Bot1.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot02.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot03.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot04.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot05.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot06.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot07.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot08.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot09.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot10.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot11.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot12.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot13.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot14.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot15.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot16.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot17.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot18.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot19.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot20.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot21.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot22.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot23.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot24.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot25.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot26.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot27.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot28.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot29.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot30.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot31.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot32.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot33.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot34.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot35.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot36.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot37.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot38.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot39.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot40.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot41.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot42.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot43.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot44.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot45.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot46.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot47.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot48.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot49.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@Bot50.on(events.NewMessage(incoming=True, pattern=r"\.leave"))


async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".leave(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            bc = int(bc)
            text = "𝐎𝐊 𝐅𝐈𝐍𝐄 𝐌𝐀𝐍 𝐀𝐑𝐊𝐇𝐀𝐌𝐱𝐆𝐎𝐃 𝐁𝐎𝐓 𝐋𝐄𝐀𝐕𝐈𝐍𝐆....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                

@idk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\*delayspam"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\*bigspam"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\*raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@idk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@put.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\*repo"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 =     eagle\n\nCommand:\n\n.eagle <count> <Username of User>\n\n.eagle <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(EAGLE)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.2)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(EAGLE)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.2)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )




@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@adk.on(events.NewMessage(incoming=True))
@bdk.on(events.NewMessage(incoming=True))
@cdk.on(events.NewMessage(incoming=True))
@edk.on(events.NewMessage(incoming=True))
@ddk.on(events.NewMessage(incoming=True))
@vkk.on(events.NewMessage(incoming=True))
@kkk.on(events.NewMessage(incoming=True))
@lkk.on(events.NewMessage(incoming=True))
@mkk.on(events.NewMessage(incoming=True))
@sid.on(events.NewMessage(incoming=True))
@shy.on(events.NewMessage(incoming=True))
@aan.on(events.NewMessage(incoming=True))
@ake.on(events.NewMessage(incoming=True))
@eel.on(events.NewMessage(incoming=True))
@khu.on(events.NewMessage(incoming=True))
@shi.on(events.NewMessage(incoming=True))
@yaa.on(events.NewMessage(incoming=True))
@dav.on(events.NewMessage(incoming=True))
@raj.on(events.NewMessage(incoming=True))
@put.on(events.NewMessage(incoming=True))
@eag.on(events.NewMessage(incoming=True))
@gle.on(events.NewMessage(incoming=True))
@wal.on(events.NewMessage(incoming=True))
@aaa.on(events.NewMessage(incoming=True))
@boy.on(events.NewMessage(incoming=True))


async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\*replyraid"))



async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "OK SIR WE WILL FUCK THIS BITCH YOU ENJOY THE SHOW..."
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "OK SIR WE WILL FUCK THIS BITCH YOU ENJOY THE SHOW..."
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\*dreplyraid"))


async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "OK MAN WE WILL STOP NOW KALP GAYA HAI BECHARA..."
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "OK MAN WE WILL STOP NOW KALP GAYA HAI BECHARA..."
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    







async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


@idk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@put.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\*add"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\*add"))


async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        mafia = await event.edit(f"`processing...`")
    else:
        h1m4n5hu0p = await get_chatinfo(event)
        chat = await event.get_chat()
        
    if event.is_private:
        return await event.edit("`Sorry, Cant add users here`")
    s = 0
    f = 0
    error = "None"

    await event.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(h1m4n5hu0p.full_chat.id):
        try:
            if error.startswith("Too"):
                return await event.edit(
                    f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await event.edit(
                f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await event.edit(
        f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people"
    )









@idk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@put.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\*ping"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\*ping"))

async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "𝐀𝐑𝐊𝐇𝐀𝐌𝐱𝐆𝐎𝐃 𝐒𝐏𝐀𝐌𝐁𝐎𝐓 𝐎𝐏!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"𝐀𝐑𝐊𝐇𝐀𝐌𝐱𝐆𝐎𝐃 𝐎𝐏 🥵🔥!\n`{ms}` ms{ALIVE_NAME} ")



        
        

@idk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\*restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "2𝐌𝐈𝐍 𝐖𝐀𝐈𝐓 𝐏𝐑𝐎 𝐁𝐎𝐓 𝐑𝐄𝐁𝐎𝐎𝐓𝐈𝐍𝐆...\n\nNow Wait Till Piro Bot Is Rebooting..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        try:
            await vkk.disconnect()
        except Exception as e:
            pass
        try:
            await kkk.disconnect()
        except Exception as e:
            pass
        try:
            await lkk.disconnect()
        except Exception as e:
            pass
        try:
            await mkk.disconnect()
        except Exception as e:
            pass
        try:
            await sid.disconnect()
        except Exception as e:
            pass
        try:
            await shy.disconnect()
        except Exception as e:
            pass
        try:
            await aan.disconnect()
        except Exception as e:
            pass
        try:
            await ake.disconnect()
        except Exception as e:
            pass
        try:
            await eel.disconnect()
        except Exception as e:
            pass
        try:
            await khu.disconnect()
        except Exception as e:
            pass
        try:
            await shi.disconnect()
        except Exception as e:
            pass
        try:
            await yaa.disconnect()
        except Exception as e:
            pass
        try:
            await dav.disconnect()
        except Exception as e:
            pass
        try:
            await raj.disconnect()
        except Exception as e:
            pass
        try:
            await put.disconnect()
        except Exception as e:
            pass
        try:
            await eag.disconnect()
        except Exception as e:
            pass
        try:
            await gle.disconnect()
        except Exception as e:
            pass
        try:
            await wal.disconnect()
        except Exception as e:
            pass
        try:
            await aaa.disconnect()
        except Exception as e:
            pass
        try:
            await boy.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@put.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\*help"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\*help"))

async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "⛓𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀⛓\n\n⚜𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙⚜:\n*ping\n*restart\n\n🔰𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙🔰:\n*bio\n*join\n*pjoin\n*leave\n\n🛡𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙🛡:\n*delayspam\n*bigspam\n*raid\n*replyraid\n*dreplyraid\n\n\nIf You Dont Understand How To Use This Bot Then Dont Use Your Noob Mind Just Contact @YashOP_XD"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """

💥💥 𝘼𝙍𝙆𝙃𝘼𝙈𝙭𝙂𝙊𝘿 𝙎𝙋𝘼𝙈 𝘽𝙊𝙏 💥💥💥
💥 𝐁𝐎𝐓 𝐁𝐘 𝐘𝐀𝐒𝐇 𝐀𝐍𝐃 𝐋𝐔𝐂𝐈𝐅𝐄𝐑 💥"""

print(text)
print("")
print("𝗔𝗥𝗞𝗛𝗔𝗠𝘅𝗚𝗢𝗗 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧 𝗥𝗘𝗔𝗗𝗬 𝗙𝗢𝗥 𝗨𝗦𝗘 𝗖𝗛𝗘𝗖𝗞 𝗕𝗬 𝗗𝗢𝗜𝗡𝗚 *ping")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        khu.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        yaa.disconnect()
    except Exception as e:
        pass
    try:
        dav.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
    try:
        eag.disconnect()
    except Exception as e:
        pass
    try:
        gle.disconnect()
    except Exception as e:
        pass
    try:
        wal.disconnect()
    except Exception as e:
        pass
    try:
        aaa.disconnect()
    except Exception as e:
        pass
    try:
        boy.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        khu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        dav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eag.run_until_disconnected()
    except Exception as e:
        pass
    try:
        gle.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wal.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        boy.run_until_disconnected()
    except Exception as e:
        pass


