from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback
from gtts import gTTS
from googletrans import Translator
import logging
from threading import Thread
botStart = time.time()
#================
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
images = json.load(imagesOpen)
stickers = json.load(stickersOpen)
#===========
print ("Memuat Akun Anda")
#k1 = LINE() #Login Via QR
k1 = LINE("Ezlr0pxTvvtHkEkamjHf.9ocyg1talQ+9eEucqY0ihW.jbh6JwmzJt4VusNhYuaecGk1/V1SV1emyOqy45+0Krc=")
k1.log("\nToken Anda => " + str(k1.authToken))
print ("Sukses Login Akun BOT 1")
#===========
print ("Memuat Akun Assist 1")
#k2 = LINE() #Login Via QR
k2 = LINE("EzbOBKT0Obs4KwMyyd25.H3QVRcxrf43MfR2E0Grvrq.JhqyASmKbj80cCm47A879AiaejWK4y9+xWzsQ4ebIXw=")
k2.log("\nToken Assist 1 => " + str(k2.authToken))
print ("Sukses Login Akun Assist 1")
#================
print ("Memuat Akun Assist 2")
#k3 = LINE() #Login Via QR
k3 = LINE("EzOJOFT6eXVONwl8B3xc.Ab1BijZe40SubzicZIooJa.Qv7tzgN1C5qPvhCZtMT6GpZ8ENLqL3RjQUWwA1Bwe+k=")
k3.log("\nToken Assist 2 => " + str(k3.authToken))
print ("Sukses Login Akun Assist 2")
#===========
print ("Sukses Menjalankan Semua BOT !!!")
print ("╔════════════════════════")
print ("║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓")
print ("║   ★‡Bot Siap Digunakan★")
print ("║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓")
print ("║ ⭐FI__FAMZ__BOTZ⭐")
print ("╚════════════════════════")

MMenu ="""╔═════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║      ✰Bot Menu✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║╔════════════
║╠[✰]Setting menu
║╠[✰]Set
║╠[✰]Bot:in
║╠[✰]Bot:out
║╠[✰]bye*bot
║╠[✰]Respon
║╠[✰]Tagall
║╠[✰]Sider on/off
║╠[✰]Me
║╠[✰]Gn <Nama Group>
║╠[✰]Speed
║╠[✰]Ginfo
║╠[✰]Memberlist
║╠[✰]Getpict @tag
║╠[✰]Getvideo @tag
║╠[✰]Getname @Tag
║╠[✰]Getstatus @Tag
║╠[✰]Getcontact @Tag
║╠[✰]Getmid @Tag
║╠[✰]Add @Tag
║╠[✰]Admin add:<Spasi>MID
║╠[✰]Admin del:<Spasi>MID
║╠[✰]Adminlist
║╠[✰]Kick @Tag
║╠[✰]Ban @Tag
║╠[✰]Unban @Tag
║╠[✰]Blacklist <send Contact>
║╠[✰]Unblacklist <send Contact>
║╠[✰]Banall
║╠[✰]Unbanall
║╠[✰]Clearban
║╠[✰]Banlist
║╠[✰]Abouts
║╠[✰]@restart
║╠[✰]Runtime
║╠[✰]Mymid
║╠[✰]Botmid
║╠[✰]Allname <Nama>
║╠[✰]Gid
║╠[✰]Gurl
║╠[✰]Gruplist
║╠[✰]Gpict
║╠[✰]Gname
║╠[✰]Buka/Tutup qr
║╠[✰]Link group
║╚════════════
║♥Ytmp4 <txt>
║♥Smule <id>
║♥Smuledown <link oc>
╠═════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║FI___FAMZ____BOTZ
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║https://line.me/ti/p/XBrmvKXrkF
╚═════════════"""

MSetting ="""╔══════════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║       ✰Setting Menu✰
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║╔═════════════════
║╠[✰]Protectkick on|off
║╠[✰]Protectqr on|off
║╠[✰]Protectname on|off
║╠[✰]Protectcancel on|off
║╠[✰]Sambutan:on|off
║╠[✰]Contact:on|off
║╚═════════════════
╠══════════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║       FI___FAMZ____BOTZ
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
╚══════════════════"""
#================ 
oepoll = OEPoll(k1)
k1Profile = k1.getProfile()
k1Settings = k1.getSettings()
k1MID = k1.getProfile().mid
k2MID = k2.getProfile().mid
k3MID = k3.getProfile().mid
#================
KAC = [k2,k3]
Bots = [k1MID,k2MID,k3MID]

admin=["uf4e0981b54c02eaffd11e502432d081f"], #Ganti Dengan MID Kalian
#================
msg_dict = {}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

wait={
    "lang":"JP",
    "Sambutan":True,
    "contact":False,
    "AddFriend":False,
    "autoAdd":True,
    "autoJoin":True,
    "Protectkick":True,
    "pname":{},
    "pro_name":{},
    "ProtectInvite":True,
    "ProtectQR":True,
    "Protectcancel":True,
    "checkContact": False,
    "myProfile": {
        "displayName": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "addadmin":False,
    "delladmin":False,
    "banAdd":False,
    "banDel":False,
    "Sider":{},
    "blacklist":{}
}
wait["myProfile"]["displayName"] = k1Profile.displayName
wait["myProfile"]["statusMessage"] = k1Profile.statusMessage
wait["myProfile"]["pictureStatus"] = k1Profile.pictureStatus

def mention(self, to, nama):
        aa = ""
        bb = ""
        strt = int(0)
        akh = int(0)
        nm = nama
        myid = self.talk.getProfile().mid
        if myid in nm:    
            nm.remove(myid)
        for mm in nm:
          akh = akh + 6
          aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
          strt = strt + 7
          akh = akh + 1
          bb += "@nrik \n"
        aa = (aa[:int(len(aa)-1)])
        text = bb
        try:
            msg = Message()
            msg.to = to
            msg.text = text
            msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}'}
            msg.contentType = 0
            self.talk.sendMessage(0, msg)
        except Exception as error:
           print(error, 'def Mention')
           
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
        k1.sendMessage(msg)
    except Exception as error:
        print (error)

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
            
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    k1.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
def translate(to_translate, to_language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':random.choice(settings["userAgent"])}
    cari_hasil = 'class="t0">'
    request = urllib.parse.Request(url, headers=agent)
    page = urllib.parse.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result
    
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k1.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        k1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Tag User「{}」\n\n  [ Tag ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(k1.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        k1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        k1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    k1.sendMessage(to, '', contentMetadata, 7)
    
def sendImage(to, path, name="image"):
    try:
        k1.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def sendMessageWithFooter(to, text):
	ticket = settings["idline"]
	h = k1.getContact(k1MID)
	pict = "http://dl.profile.line-cdn.net/" + h.pictureStatus
	mecin = k1Profile.displayName
	garam = {"AGENT_ICON": pict,
	    "AGENT_NAME": mecin,
	    "AGENT_LINK": ticket
	}
	k1.sendMessage(to, text, contentMetadata=garam)
def sendMentionFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Meka Finee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    k1.sendMessage(to, textx, {'AGENT_NAME': k1Profile.displayName, 'AGENT_LINK': settings["idline"],'AGENT_ICON': "http://dl.profile.line-cdn.net/0h6wkn-ZTOaVhWF0QWcOQWD2pSZzUhOW8QLiMubCQQNG8vdCcObiEgPyYTPzpycygOPXlxayMSPm54", 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 1*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        k1.sendMessage(tmp, "Bot active again.!")
                    except Exception as error:
                        logError(error)
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            koplaxs = pesan.replace(settings["keyCommand"],"")
        else:
            koplaxs = "Undefined command"
    else:
        koplaxs = text.lower()
    return koplaxs
    
def bot(op):
    try:
        if op.type == 0:
            return

        if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                to = msg.to
                if msg.contentType == 13:
                  if wait["contact"] == True:
                    msg.contentType = 0
                    k1.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                      contact = k1.getContact(msg.contentMetadata["mid"])
                      try:
                        cu = k1.channel.getCover(msg.contentMetadata["mid"])
                      except:
                        pass
                    else:
                      contact = k1.getContact(msg.contentMetadata["mid"])
                      try:
                        cu = k1.channel.getCover(msg.contentMetadata["mid"])
                      except:
                        pass
                        
                  elif wait["AddFriend"] == True:
                  ##if msg._from in OWNER:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = k1.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                      if _name in s.displayName:
                        k1.sendMessage(msg.to,"-> " + _name + " was here")
                        break
                      elif invite in wait["blacklist"]:
                        k1.sendMessage(msg.to,"Sorry, " + _name + " On Blacklist")
                        k1.sendMessage(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                        break
                      else:
                        targets.append(invite)
                    if targets == []:
                      pass
                    else:
                      for target in targets:
                        try:
                          k1.findAndAddContactsByMid(target)
                          #k1.inviteIntoGroup(msg.to,[target])
                          k1.sendMessage(msg.to,"Already Invited Boss 💋: \n➡" + _name)
                          wait["AddFriend"] = False
                          break
                        except:
                          try:
                            k1.findAndAddContactsByMid(invite)
                            #k1.inviteIntoGroup(op.param1,[invite])
                            wait["AddFriend"] = False
                          except:
                            try:
                              k1.findAndAddContactsByMid(invite)
                              #k1.inviteIntoGroup(op.param1,[invite])
                              wait["AddFriend"] = False
                              k1.sendMessage(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                              break
                            except:
                              try:
                                k1.findAndAddContactsByMid(invite)
                                #k1.inviteIntoGroup(op.param1,[invite])
                                wait["AddFriend"] = False
                                k1.sendMessage(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                                break
                              except:
                                k1.sendMessage(msg.to,"Negative, Error detected")
                                wait["AddFriend"] = False
                                break
                                
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        koplaxs = command(text)
                        if msg.text in ["Absen","Absen bot","Absen dulu","Respon"]:
                          k2.sendMessage(msg.to,"𖤓Hadir Boss𖤓")
                          k3.sendMessage(msg.to,"𖤓Hadir Boss𖤓")
                          k2.sendMessage(msg.to,"Semua Sudah Hadir Boss\nSiap Protect Group")
                  
                        if koplaxs == "help":
                            if wait["lang"] == "JP":
                              k1.sendMessage(msg.to,MMenu)
                            else:
                              k1.sendMessage(msg.to,MMenu)
                              
                        elif msg.text in ["Setting menu","Setting menu"]:
                         ##if msg._from in OWNER:
                           if wait["lang"] == "JP":
                              k1.sendMessage(msg.to,MSetting)
                           else:
                              k1.sendMessage(msg.to,MSetting)
                  
                        elif koplaxs.startswith("tagme "):
                          ##if sender in OWNER:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            settings["tag"] = str(key).lower()
                            k1.sendMessage(to, "Berhasil mengganti Auto Respon")
                            
                        elif koplaxs == "spamcall":
                          #if sender in OWNER:
                            if msg.toType == 2:
                                group = k1.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                k1.acquireGroupCallRoute(to)
                                k1.inviteIntoGroupCall(to, contactIds=members)
                                k1.acquireGroupCallRoute(to)
                                k1.inviteIntoGroupCall(to, contactIds=members)
                                k1.acquireGroupCallRoute(to)
                                k1.inviteIntoGroupCall(to, contactIds=members)
                                k1.acquireGroupCallRoute(to)
                                k1.inviteIntoGroupCall(to, contactIds=members)
                                k1.acquireGroupCallRoute(to)
                                k1.inviteIntoGroupCall(to, contactIds=members)
                                k1.sendMessage(to, "Berhasil")
                        elif koplaxs.startswith("smuledown "): 
                          ##if sender in OWNER:
                            separate = text.split(" ")
                            linknya = text.replace(separate[0] + " ","")
                            k1.sendMessage(to, "https://sing.salon/smule-downloader/?url="+linknya)
                        elif koplaxs == "abouts":
                          ##if sender in admin:
                            k1.sendMessage(to,"Waiting..")
                            h = k1.getContact(sender)
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            start = time.time()
                            elapsed_time = time.time() - start
                            owner = "ued156c86ffa56024c0acba16f7889e6d"
                            creator = k1.getContact(owner)
                            grouplist = k1.getGroupIdsJoined()
                            contactlist = k1.getAllContactIds()
                            blockedlist = k1.getBlockedContactIds()
                            CVU = ["0.9℃","1.1℃","1.0℃","1.2℃","1.3℃","1.4℃","1.5℃","1.6℃","0.8℃"]
                            resultCvu = random.choice(CVU)
                            aboter = "╔╦━━━[ABOUT BOTS]━━━╦━━╮"
                            aboter += "\n║╠ Nama BOT: FI___FAMZ____BOTZ"
                            aboter += "\n║╠ Bot active: {}".format(str(runtime))
                            aboter += "\n║╠ Bot version: *Python3"
                            aboter += "\n║╠ Thrift version: 0.11.0"
                            aboter += "\n║╠ Runner cvu: "+resultCvu
                            aboter += "\n║╠ Version bots: Versi 2.4"
                            #aboter += "\n║╠ Expt Bots: "+settings["EXPT"]
                            aboter += "\n║╠ SpeedBots: {}".format(str(elapsed_time))
                            aboter += "\n║╠══════════════════"
                            aboter += "\n║╠ Creator name : {}".format(creator.displayName)
                            aboter += "\n║╠ Creator id :  https://line.me/ti/p/XBrmvKXrkF"
                            aboter += "\n╚╩━━[Succes]━━╩━╯"
                            #cover = "http://oi65.tinypic.com/vrwugj.jpg"
                            #k1.sendImageWithURL(to, "http://oi65.tinypic.com/vrwugj.jpg")
                            k1.sendMessage(to, aboter)
#======================================
                        elif koplaxs == "bot:out":
                          ##if sender in OWNER:
                            k2.leaveGroup(msg.to)
                            k3.leaveGroup(msg.to)
                            
                        elif msg.text in ["Bot out"]:
                          ##if sender in OWNER:
                            gid = k2.getGroupIdsJoined()
                            gid = k3.getGroupIdsJoined()
                            for i in gid:
                              k1.sendMessage(i, "BOT Dipaksa Keluar Oleh Owner\nBye !!!")
                              k3.leaveGroup(i)
                              k2.leaveGroup(i)

                        elif koplaxs == "1in":
                          ##if sender in OWNER:
                            G = k1.getGroup(msg.to)
                            ginfo = k1.getGroup(msg.to)
                            G.preventedJoinByTicket = False
                            k1.updateGroup(G)
                            invsend = 0
                            Ticket = k1.reissueGroupTicket(msg.to)
                            k2.acceptGroupInvitationByTicket(to,Ticket)
                            G = k1.getGroup(msg.to)
                            G.preventedJoinByTicket = True
                            k2.updateGroup(G)
                            G.preventedJoinByTicket(G)
                            k2.updateGroup(G)
                        elif koplaxs == "2in":
                          ##if sender in OWNER:
                            G = k1.getGroup(msg.to)
                            ginfo = k1.getGroup(msg.to)
                            G.preventedJoinByTicket = False
                            k1.updateGroup(G)
                            invsend = 0
                            Ticket = k1.reissueGroupTicket(msg.to)
                            k3.acceptGroupInvitationByTicket(to,Ticket)
                            G = k1.getGroup(msg.to)
                            G.preventedJoinByTicket = True
                            k3.updateGroup(G)
                            G.preventedJoinByTicket(G)
                            k3.updateGroup(G)
                        elif koplaxs == "bot:in":
                         ##if sender in OWNER:
                            G = k1.getGroup(msg.to)
                            ginfo = k1.getGroup(msg.to)
                            G.preventedJoinByTicket = False
                            k1.updateGroup(G)
                            invsend = 0
                            Ticket = k1.reissueGroupTicket(msg.to)
                            k2.acceptGroupInvitationByTicket(to,Ticket)
                            k3.acceptGroupInvitationByTicket(to,Ticket)
                            G = k1.getGroup(msg.to)
                            G.preventedJoinByTicket = True
                            random.choice(KAC).updateGroup(G)
                            G.preventedJoinByTicket(G)
                            random.choice(KAC).updateGroup(G)
                        elif koplaxs == "inviteall":
                          #if sender in OWNER:
                            anggota = [k2MID,k3MID]
                            k1.inviteIntoGroup(msg.to, anggota)
                            k2.acceptGroupInvitation(msg.to)
                            k3.acceptGroupInvitation(msg.to)
                            
                        elif koplaxs == "fuckban":
                          #if sender in OWNER:
                            group = k1.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in settings["blacklist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                random.choice(KAC).sendMessage(to,"Noting blacklist in group..")
                                return
                            for jj in matched_list:
                                try:
                                    klist=[k2,k3]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(to,[jj])
                                    print((to,[jj]))
                                except:
                                    pass
#======================================
                        elif koplaxs == "@restart":
                          #if sender in OWNER:
                            k1.sendMessage(to, "Sebentar...")
                            k1.sendMessage(to, "Selesai.!!\n\nSilahkan command 1x ktik me\ntunggu beberapa saat skitar 1-2 mnt\njika respon command me lagi 1x\ntunggu respon (DONE NORMAL)")
                            settings["restartPoint"] = to
                            restartBot()
                        elif koplaxs == "runtime":
                          #if sender in OWNER:
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            k1.sendMessage(to, "┣━━━RUNTIME BOTS━━━╣\n ┣━{}━╣".format(str(runtime)))
                        elif koplaxs == "unsend":
                          #if sender in OWNER:
                            k1.unsendMessage(msg_id)
                        elif koplaxs == "speed":
                          #if sender in admin:
                            start = time.time()
                            k1.sendMessage(to, "Menghitung Duit...")
                            elapsed_time = time.time() - start
                            k1.sendMessage(to,format(str(elapsed_time)))
                            #k1.sendMessage(to,format(str(elapsed_time)))
                            k2.sendMessage(to,format(str(elapsed_time)))
                            k3.sendMessage(to,format(str(elapsed_time)))
                            #k4.sendMessage(to,format(str(elapsed_time)))
                            #k5.sendMessage(to,format(str(elapsed_time)))
                            #k6.sendMessage(to,format(str(elapsed_time)))
                            #k7.sendMessage(to,format(str(elapsed_time)))
                            #k8.sendMessage(to,format(str(elapsed_time)))
                            #k9.sendMessage(to,format(str(elapsed_time)))
                            #k10.sendMessage(to,format(str(elapsed_time)))
#==============================================================================#
#==============================================================================#
                        elif koplaxs.startswith("b1name "):
                          #if sender in OWNER:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 20:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendMessage(to,"┣━━━╦NAMA PROFILE DIUBAH MENJADI╦━━━╣\n{}".format(str(string)))
                        elif koplaxs.startswith("b2name "):
                          #if sender in OWNER:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 20:
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(to,"┣━━━╦NAMA PROFILE DIUBAH MENJADI╦━━━╣\n{}".format(str(string)))
                        elif koplaxs.startswith("allname "):
                          #if sender in OWNER:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 20:
                                profile = k2.getProfile()
                                profile.displayName = string
                                k2.updateProfile(profile)
                                k2.sendMessage(to,"{}".format(str(string)))
                            if len(string) <= 20:
                                profile = k3.getProfile()
                                profile.displayName = string
                                k3.updateProfile(profile)
                                k3.sendMessage(to,"{}".format(str(string)))
                            
                        elif koplaxs.startswith("botstatus "):
                          #if sender in OWNER:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = k2.getProfile()
                                profile.statusMessage = string
                                k2.updateProfile(profile)
                                k2.sendMessage(to,"┣━━━╦STATUS PROFILE DIUBAH MENJADI╦━━━╣\n {}".format(str(string)))
                            if len(string) <= 500:
                                profile = k3.getProfile()
                                profile.statusMessage = string
                                k3.updateProfile(profile)
                                k3.sendMessage(to,"┣━━━╦STATUS PROFILE DIUBAH MENJADI╦━━━╣\n {}".format(str(string)))
                            
                        elif koplaxs == "me":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            k1.sendMessage(to,"┣━━╦KONTAK PROFILE╦━━╣\n " + readTime)
                            sendMentionFooter(to, "@!", [sender])
                            k1.sendContact(to, sender)
                        elif koplaxs == "mybots":
                          #if sender in OWNER:
                            k1.sendMessage(to,"┣━━╦━━━━━━━━━━━╦━━╣")
                            k1.sendContact(to, k2MID)
                            k1.sendContact(to, k3MID)
                            k1.sendMessage(to,"┣━━╦━━━KONTAK BOTS━━━╦━━╣")
                        elif koplaxs == "mymid":
                            h = k1.getContact(sender)
                            k1.sendMessage(to,h.mid)
                        elif koplaxs == "botmid":
                          #if sender in OWNER:
                            h = k1.getContact(k1MID)
                            k1.sendMessage(to,h.mid)
                            h = k2.getContact(k2MID)
                            k2.sendMessage(to,h.mid)
                            h = k3.getContact(k3MID)
                            k3.sendMessage(to,h.mid)
                            
                        elif koplaxs == "myinfo":
                          #if sender in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            h = k1.getContact(sender)
                            k1.sendMessage(to,"┣━━╦━━INFO KONTAK━━╦━━╣")
                            k1.sendContact(to, sender)
                            k1.sendMessage(to,"┣━━╦━━━INFO MID━━━╦━━╣\n" + h.mid)
                            k1.sendMessage(to,"┣━━╦━━INFO NAMA━━╦━━╣\n" + h.displayName)
                            k1.sendMessage(to,"┣━━╦━━INFO STATUS━━╦━━╣\n" + h.statusMessage)
                            k1.sendMessage(to,"┣━━╦━━FOTO PROFILE━━╦━━╣")
                            k1.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            k1.sendMessage(to,"Success..\n" + readTime)
                        elif koplaxs == "myvideo":
                          #if sender in admin:
                            h = k1.getContact(sender)
                            k1.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                        elif koplaxs.startswith("getmid "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = ""
                                for ls in lists:
                                    ret_ += "{}".format(str(ls))
                                k1.sendMessage(to, str(ret_))
                        elif koplaxs.startswith("getpict "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.line.naver.jp/" + k1.getContact(ls).pictureStatus
                                    k1.sendImageWithURL(to, str(path))
                        elif koplaxs.startswith("getvideo "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.line.naver.jp/" + k1.getContact(ls).pictureStatus
                                    k1.sendVideoWithURL(to, str(path))
                        elif koplaxs.startswith("getname "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = k1.getContact(ls)
                                    k1.sendMessage(to, "┣━━NAMA DI TAMPILKAN━━╣\n{}".format(str(contact.displayName)))
                        elif koplaxs.startswith("getstatus "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = k1.getContact(ls)
                                    k1.sendMessage(to, "┣━━╦━━STATUS DI TAMPILKAN━━╦━━╣\n{}".format(str(contact.statusMessage)))
                        elif koplaxs.startswith("getcontact "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = k1.getContact(ls)
                                    mi_d = contact.mid
                                    k1.sendContact(to, mi_d)
                        elif koplaxs.startswith("copy "):
                          #if sender in OWNER:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        contact = mention["M"]
                                        break
                                    try:
                                        k1.cloneContactProfile(contact)
                                        k1.sendMessage(msg.to, "Success.!!")
                                    except:
                                        k1.sendMessage(to, "Gagal..")
                        elif koplaxs == "recopy":
                          #if sender in OWNER:
                            try:
                                k1Profile = k1.getProfile()
                                k1Profile.displayName = str(settings["myProfile"]["displayName"])
                                k1Profile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                k1Profile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                coverId = str(settings["myProfile"]["coverId"])
                                k1.updateProfileAttribute(8, k1Profile.pictureStatus)
                                k1.updateProfileCoverById(coverId)
                                k1.updateProfile(k1Profile)
                                k1.sendContact(to, sender)
                                k1.sendMessage(to, "Success.!!")
                            except Exception as e:
                                k1.sendMessage(to, "Tidak ada backupan kontak profile\nlain di backup dulu..")
                                k1.sendMessage(to, str(e))
                        elif koplaxs == "mybackup":
                          #if sender in OWNER:
                            try:
                                profile = k1.getProfile()
                                settings["myProfile"]["displayName"] = str(profile.displayName)
                                settings["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                settings["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                coverId = k1.getProfileDetail()["result"]["objectId"]
                                settings["myProfile"]["coverId"] = str(coverId)
                                k1.sendMessage(to, "Berhasil backup profile")
                            except Exception as e:
                                k1.sendMessage(to, "Gagal backup profile")
                                k1.sendMessage(to, str(e))
#======================================================
                        elif koplaxs.startswith("music "):
                          #if sender in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split(" no ")
                            search = str(cond[0])
                            result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            if len(cond) == 1:
                                num = 0
                                ret_ = "╭━━━━══[Daftar lagu]"
                                for music in data["result"]:
                                    num += 1
                                    ret_ += "\n┣═ {}. {}".format(str(num), str(music["single"]))
                                ret_ += "\n╰━━━━━═[ Total {} Lagu]".format(str(len(data["result"])))
                                ret_ += "\n[Info]\nGunakan Kata kunci di bawah ini coy\n{} no「number」".format(str(msg.text),str(search))
                                k1.sendMessage(to, str(ret_))
                            elif len(cond) == 2:
                                num = int(cond[1])
                                if num <= len(data["result"]):
                                    music = data["result"][num - 1]
                                    result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                    data = result.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        ret_ = "╭━━━━══[Ditampilkan]"
                                        ret_ += "\n┣═ Title : {}".format(str(data["result"]["song"]))
                                        ret_ += "\n┣═ Album : {}".format(str(data["result"]["album"]))
                                        #ret_ += "\n┣═ Size : {}".format(str(data["result"]["size"]))
                                        #ret_ += "\n┣═ Link : {}".format(str(data["result"]["mp3"][0]))
                                        ret_ += "\n╰━━━━━═[Selesai]"
                                        k1.sendImageWithURL(to, str(data["result"]["img"]))
                                        k1.sendMessage(to, str(ret_))
                                        k1.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                                        k1.sendMessage(to, "Selamat Mendengarkan Kak...")
                                        k1.sendImageWithURL(to, "http://oi65.tinypic.com/3088ih2.jpg")
                        elif koplaxs.startswith("liryc "):
                          #if sender in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split(" no ")
                            search = cond[0]
                            api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                            data = api.text
                            data = json.loads(data)
                            if len(cond) == 1:
                                num = 0
                                ret_ = "╭━━━══[Ditampilkan]"
                                for lyric in data["results"]:
                                    num += 1
                                    ret_ += "\n┣═ {}. {}".format(str(num), str(lyric["single"]))
                                ret_ += "\n╰━━━━═[ Total {} Di tampilkan]".format(str(len(data["results"])))
                                ret_ += "\n[Info]\nGunakan Kata kunci di bawah ini\n{}Liricalbum {} no「number」".format(settings["keyCommand"],str(search))
                                k1.sendMessage(to, str(ret_))
                            elif len(cond) == 2:
                                num = int(cond[1])
                                if num <= len(data["results"]):
                                    lyric = data["results"][num - 1]
                                    api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                    data = api.text
                                    data = json.loads(data)
                                    lyrics = data["results"]["lyric"]
                                    lyric = lyrics.replace('ti:','Title - ')
                                    lyric = lyric.replace('ar:','Artist - ')
                                    lyric = lyric.replace('al:','Album - ')
                                    removeString = "[1234567890.:]"
                                    for char in removeString:
                                        lyric = lyric.replace(char,'')
                                    k1.sendMessage(to, str(lyric))
#========================#
                        elif koplaxs.startswith("ytlink "):
                          #if sender in admin:
                            k1.sendMessage(to, "Waiting...")
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ Youtube link di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} link]━━━━━".format(len(datas))
                                k1.sendMessage(to, str(ret_))
                        elif koplaxs.startswith("ytmp3 "):
                          #if sender in admin:
                            try:
                                k1.sendMessage(to,"Waitting...\nJangan command apapun sampai muncul\nProsess ini membutuhkan waktu yang lama\nJadi haraf sabar..")
                                textToSearch = (msg.text).replace("ytmp3 ", "").strip()
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl = 'https://www.youtube.com' + results['href']
                                vid = pafy.new(dl)
                                stream = vid.audiostreams
                                for s in stream:
                                    start = timeit.timeit()
                                    vin = s.url
                                    img = vid.bigthumbhd
                                    hasil = vid.title
                                    hasil += '\n\nPenulis : ' +str(vid.author)
                                    hasil += '\nDurasi   : ' +str(vid.duration)+ ' (' +s.quality+ ') '
                                    hasil += '\nRating   : ' +str(vid.rating)
                                    hasil += '\nDitonton    : ' +str(vid.viewcount)+ 'x '
                                    hasil += '\nDiterbitkan : ' +vid.published
                                    hasil += '\n\nTime taken : %s' % (start)
                                    hasil += '\n\n Tunggu encoding selesai...'
                                k1.sendAudioWithURL(to,vin)
                                k1.sendImageWithURL(to,img)
                                k1.sendMessage(to,hasil)
                            except:
                                k1.sendMessage(to,"Gagal Mencari...")

                        elif koplaxs.startswith("ytmp4 "):
                          #if sender in admin:
                            try:
                                k1.sendMessage(to,"Waitting...\nJangan command apapun sampai muncul\nProsess ini membutuhkan waktu yang lama\nJadi haraf sabar..")
                                textToSearch = (msg.text).replace("ytmp4 ", "").strip()
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl = 'https://www.youtube.com' + results['href']
                                vid = pafy.new(dl)
                                stream = vid.streams
                                for s in stream:
                                    vin = s.url
                                    hasil = 'Informasi\n\n'
                                    hasil += 'Judul:\n ' + vid.title
                                    hasil += '\n Tunggu encoding selesai...'
                                k1.sendVideoWithURL(to,vin)
                                k1.sendMessage(to,hasil)
                            except:
                                k1.sendMessage(to,"Gagal Mencari...")
                        elif koplaxs.startswith("images "):
                          #if sender in OWNER:
                            separate = msg.text.split(" ")
                            search = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    items = data["result"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    k1.sendImageWithURL(to, str(path))
                        elif koplaxs.startswith("imagetxt "):
                          #if sender in OWNER:
                            sep = msg.text.split(" ")
                            textnya = msg.text.replace(sep[0] + " ","")
                            urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                            k1.sendImageWithURL(msg.to, urlnya)
                        elif koplaxs.startswith("screenshoot "):
                          #if sender in OWNER:
                            k1.sendMessage(to, "Waitting...")
                            sep = text.split(" ")
                            query = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                data = r.text
                                data = json.loads(data)
                                k1.sendImageWithURL(to, data["result"])

                        elif koplaxs.startswith("ttl "):
                          #if sender in admin:
                            try:
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ","")
                                r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                ret_ = "╭━━━━════[Tanggal,Lahir]"
                                ret_ += "\n┣═Tanggal lahir : {}".format(str(data["data"]["lahir"]))
                                ret_ += "\n┣═Umur : {}".format(str(data["data"]["usia"]))
                                ret_ += "\n┣═Tanggal ultah : {}".format(str(data["data"]["ultah"]))
                                ret_ += "\n┣═Zodiak : {}".format(str(data["data"]["zodiak"]))
                                ret_ += "\n╰━━═════[HANYA PREDIKSI]"
                                k1.sendMessage(to, str(ret_))
                            except Exception as error:
                                logError(error)
                        elif koplaxs.startswith("info-ig "):
                          #if sender in OWNER:
                            sep = text.split(" ")
                            instagram = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                html = web.get("https://www.instagram.com/" + instagram + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://instagram.com/" + instagram
                                k1.sendImageWithURL(msg.to, text1[0])
                                k1.sendMessage(to, user + user1 + followers + following + post + link)
                                print("[Notif] Search Instagram Sucess")
                        elif koplaxs.startswith("info-fb "):
                          #if sender in OWNER:
                            sep = text.split(" ")
                            facebook = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                html = web.get("https://www.facebook.com/" + facebook + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://facebook.com/" + facebook
                                k1.sendImageWithURL(msg.to, text1[0])
                                k1.sendMessage(to, user + user1 + followers + following + post + link)
                        elif koplaxs.startswith("smule "):
                          #if sender in admin:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            smule = "https://www.smule.com/"+ key
                            k1.sendMessage(to, "ini id smulenya kak\n" + smule)
                        elif koplaxs.startswith("searchsmule "):
                          #if sender in admin:
                            k1.sendMessage(to, "Waiting...")
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://www.smule.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ list smule di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.smule.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} id]━━━━━".format(len(datas))
                                k1.sendMessage(to, str(ret_))
                        elif koplaxs.startswith("twitter "):
                          #if sender in OWNER:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            twitter = "https://www.twitter.com/"+ key
                            k1.sendMessage(to, "pencarian untuk user id " + sep + "ini twitternya kak\n" + twitter)
                        elif koplaxs.startswith("shalat "):
                          #if sender in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isya : ":
                                    ret_ = "╭━━══[ Jadwal Sholat Sekitar " + data[0] + " ]"
                                    ret_ += "\n┣═Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n┣═Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n┣═" + data[1]
                                    ret_ += "\n┣═" + data[2]
                                    ret_ += "\n┣═" + data[3]
                                    ret_ += "\n┣═" + data[4]
                                    ret_ += "\n┣═" + data[5]
                                    ret_ += "\n╰━━══[ Success ]"
                                else:
                                    ret_ = "Error : lokasi tidak dintemukan" 
                                k1.sendMessage(to, str(ret_))
                        elif koplaxs.startswith("imsak "):
                          #if sender in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "Imsak 🌃 : ":
                                    ret_ = "╭━━══[ Jadwal Imsak di " + data[0] + " ]"
                                    ret_ += "\n┣═Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n┣═Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n┣═" + data[1]
                                    ret_ += "\n╰━━══[ Jangan lupa doa niat puasa nya ]"
                                else:
                                    ret_ = "Error : lokasi tidak dintemukan" 
                                k1.sendMessage(to, str(ret_))
                        elif koplaxs.startswith("maghrib "):
                          #if sender in OWNER:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if data[4] != "Maghrib 🌇: ":
                                    ret_ = "╭━━══[ Jadwal Buka puasa di " + data[0] + " ]"
                                    ret_ += "\n┣═Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n┣═Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n┣═" + data[4]
                                    ret_ += "\n╰━━══[ Jangan lupa doa buka puasanya ]"
                                else:
                                    ret_ = "Error : lokasi tidak dintemukan" 
                                k1.sendMessage(to, str(ret_))
                        elif koplaxs.startswith("cuaca "):
                          #if sender in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                  ret_ = "╭━━════[ Weather Status ]"
                                  ret_ += "\n┣═Location : " + data[0].replace("Temperatur di kota ","")
                                  ret_ += "\n┣═Suhu : " + data[1].replace("Suhu : ","") + "°C"
                                  ret_ += "\n┣═Kelembaban : " + data[2].replace("Kelembaban : ","") + "%"
                                  ret_ += "\n┣═Tekanan udara : " + data[3].replace("Tekanan udara : ","") + "HPa"
                                  ret_ += "\n┣═Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + "m/s"
                                  ret_ += "\n┣═══[ Time Status ]"
                                  ret_ += "\n┣═Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                  ret_ += "\n┣═Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                  ret_ += "\n╰━━═════[ Success ]"
                                else:
                                  ret_ = "[Weather Status] Error : Location not found"
                                k1.sendMessage(to, str(ret_))
                                
                        elif koplaxs.startswith("lokasi "):
                          #if sender in OWNER:
                            try:
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                                    r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╭━━════[ Location Status ]"
                                        ret_ += "\n┣═Location : " + data[0]
                                        ret_ += "\n┣═Google Maps : " + link
                                        ret_ += "\n╰━━━═════[ Success ]"
                                    else:
                                        ret_ = "[Details Location] Error : Location not found"
                                    k1.sendMessage(to,str(ret_))
                            except Exception as error:
                                logError(error)
            #           T E X T     T O     S P E E C H             #
            
                        elif koplaxs.startswith("sayi "):
                          #if sender in admin:
                            sep = text.split(" ")
                            say = text.replace(sep[0] + " ","")
                            lang = 'en'
                            tts = gTTS(text=say, lang=lang)
                            tts.save("inggris.mp3")
                            k1.sendAudio(to,"inggris.mp3")
                            
                        elif koplaxs.startswith("say "):
                          #if sender in admin:
                            sep = text.split(" ")
                            say = text.replace(sep[0] + " ","")
                            lang = 'id'
                            tts = gTTS(text=say, lang=lang)
                            tts.save("indo.mp3")
                            k1.sendAudio(to,"indo.mp3")
#===========================
#===========================#
                        elif koplaxs == "tagall":
                          #if sender in admin:
                               group = k1.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
 #============== TEST CCTV DAN SIDER =========================
                        elif koplaxs == "cctv2":
                            #if sender in admin:
                              k1.sendMessage(to, "Mencari CCTV...")
                              try:
                               del wait2['readPoint'][to]
                               del wait2['readMember'][to]
                              except:
                                pass
                              now2 = datetime.now()
                              wait2['readPoint'][to] = msg.id
                              wait2['readMember'][to] = ""
                              wait2['setTime'][to] = datetime.strftime(now2,"%H:%M")
                              wait2['ROM'][to] = {}
                            
                        elif koplaxs == "ciduk2":
                            #if sender in admin:
                              if msg.to in wait2['readPoint']:
                                if wait2["ROM"][msg.to].items() == []:
                                  chiya = ""
                                else:
                                  chiya = ""
                                  for rom in wait2["ROM"][msg.to].items():
                                  #print rom
                                    chiya += rom[1] + "\n"
                                k1.sendMessage(msg.to, "||Dilihat Oleh||%s\n\n||By : Ｏｎｅ ｐｉｅｃｅ Ｔｅａｍ||\n\n>Pelaku CCTV<\n%sAwas Yang CCTV Bintitan\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                              else:
                               k1.sendMessage(msg.to, "Ketik Cctv Dulu Njir\nBaru Ketik Ciduk\nDasar Pikun ♪")
                               
                        elif koplaxs == "sider:on":
                          #if sender in admin:
                            try:
                              del cctv['point'][msg.to]
                              del cctv['sidermem'][msg.to]
                              del cctv['cyduk'][msg.to]
                            except:
                              pass
                            cctv['point'][msg.to] = msg.id
                            cctv['sidermem'][msg.to] = ""
                            cctv['cyduk'][msg.to]=True
                            wait["Sider"] = True
                            k1.sendMessage(msg.to,"Siap Boskuhh...!!")
                            
                        elif koplaxs == "sider:off":
                          #if sender in admin:
                            if msg.to in cctv['point']:
                              cctv['cyduk'][msg.to]=False
                              wait["Sider"] = False
                              k1.sendMessage(msg.to, "Cek Sider Off")
                            else:
                              k1.sendMessage(msg.to, "Woyyy\nBelom Di Set")
                    
#============== SELESAI ===================
                                    
                        elif koplaxs == "cctv:on":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if receiver in read['readPoint']:
                                try:
                                    del read['readPoint'][receiver]
                                    del read['readMember'][receiver]
                                    del read['readTime'][receiver]
                                except:
                                    pass
                                read['readPoint'][receiver] = msg_id
                                read['readMember'][receiver] = ""
                                read['readTime'][receiver] = readTime
                                read['ROM'][receiver] = {}
                                k1.sendMessage(receiver,"Mencari Cicitipi ...")
                            else:
                                try:
                                    del read['readPoint'][receiver]
                                    del read['readMember'][receiver]
                                    del read['readTime'][receiver]
                                except:
                                    pass
                                read['readPoint'][receiver] = msg_id
                                read['readMember'][receiver] = ""
                                read['readTime'][receiver] = readTime
                                read['ROM'][receiver] = {}
                                k1.sendMessage(receiver,"Set reading point : \n" + readTime)
                        elif koplaxs == "cctv:off":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if receiver not in read['readPoint']:
                                k1.sendMessage(receiver,"Cicitipi off")
                            else:
                                try:
                                    del read['readPoint'][receiver]
                                    del read['readMember'][receiver]
                                    del read['readTime'][receiver]
                                except:
                                    pass
                                k1.sendMessage(receiver,"Delete reading point : \n" + readTime)
    
                        elif koplaxs == "cctv:rest":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if msg.to in read["readPoint"]:
                                try:
                                    del read["readPoint"][msg.to]
                                    del read["readMember"][msg.to]
                                    del read["readTime"][msg.to]
                                    del read["ROM"][msg.to]
                                except:
                                    pass
                                k1.sendMessage(to, "Reset reading point : \n" + readTime)
                            else:
                                k1.sendMessage(to, "Belum aktif. Silahkan aktifkan terlebih dahulu")
                                
                        elif koplaxs == "ciduk":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if receiver in read['readPoint']:
                                if read["ROM"][receiver].items() == []:
                                    k1.sendMessage(receiver,"Tidak Ada Sider")
                                else:
                                    chiya = []
                                    for rom in read["ROM"][receiver].items():
                                        chiya.append(rom[1])
                                    cmem = k1.getContacts(chiya) 
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '╭━━╦Daftar yang terbaca╦━━╮\n'
                                for x in range(len(cmem)):
                                    xname = str(cmem[x].displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@c\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                text = xpesan+ zxc + "\n" + readTime
                                try:
                                    k1.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except Exception as error:
                                    print (error)
                                pass
                            else:
                                k1.sendMessage(receiver,"Lurking has not been set.")
#======================================
#====================#
                        elif koplaxs.startswith("addimage "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                settings["addImage"]["status"] = True
                                settings["addImage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Silahkan kirim gambar yang ingin anda tambahkan")
                            else:
                                k1.sendMessage(to, "Gambar sudah ada dalam list")
                        elif koplaxs.startswith("delimage "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                k1.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Berhasil menghapus gambar {}".format(str(name.lower())))
                            else:
                                k1.sendMessage(to, "Gambar tidak ada dalam list")
                        elif koplaxs.startswith("setimage "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                settings["addImage"]["status"] = True
                                settings["addImage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Silahkan kirim gambar yang ingin anda ubah")
                            else:
                                k1.sendMessage(to, "Gambar tidak ada dalam list")
                        elif koplaxs == "imagelist":
                            load()
                            ret_ = "╔══[ List Images ]"
                            for image in images:
                                ret_ += "\n╠ " + image.title()
                            ret_ += "\n╚══[ Total {} Images ]".format(str(len(images)))
                            k1.sendMessage(to, ret_)
                        elif koplaxs.startswith("spamimage "):
                            load()
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ","")
                            cond = text.split(" ")
                            jml = int(cond[0])
                            imagename = text.replace(cond[0] + " ","").lower()
                            if imagename in images:
                                imgURL = images[imagename]
                            else:
                                k1.sendMessage(to, "Gambar tidak ditemukan")
                                return
                            for x in range(jml):
                                k1.sendImage(to, imgURL)
                        elif koplaxs.startswith("addsticker "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                settings["addSticker"]["status"] = True
                                settings["addSticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = {}
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Silahkan kirim stiker yang ingin anda tambahkan")
                            else:
                                k1.sendMessage(to, "Nama stiker sudah ada dalam list")
                        elif koplaxs.startswith("delsticker "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Berhasil menghapus stiker {}".format(str(name.lower())))
                            else:
                                k1.sendMessage(to, "Stiker tidak ada dalam list")
                        elif koplaxs.startswith("setsticker "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                settings["addSticker"]["status"] = True
                                settings["addSticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Silahkan kirim stiker yang ingin anda ubah")
                            else:
                                k1.sendMessage(to, "Stiker tidak ada dalam list")
                        elif koplaxs == "stickerlist":
                            load()
                            ret_ = "╔══[ List Sticker ]"
                            for sticker in stickers:
                                ret_ += "\n╠ " + sticker.title()
                            ret_ += "\n╚══[ Total {} Stickers ]".format(str(len(stickers)))
                            k1.sendMessage(to, ret_)
                        elif koplaxs.startswith("spamsticker "):
                            load()
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ","")
                            cond = text.split(" ")
                            jml = int(cond[0])
                            stickername = text.replace(cond[0] + " ","").lower()
                            if stickername in stickers:
                                sid = stickers[stickername]["STKID"]
                                spkg = stickers[stickername]["STKPKGID"]
                                sver = stickers[stickername]["STKVER"]
                            else:
                                return
                            for x in range(jml):
                                sendSticker(to, sver, spkg, sid)
#=====================================
                        elif koplaxs.startswith("kick "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        wait["blacklist"][ls] = True
                                        berak = [k2,k3]
                                        berakin = random.choice(berak)
                                        berakin.kickoutFromGroup(to,[ls])
                                        print (to,[ls])
                                    except:
                                        try:
                                            wait["blacklist"][ls] = True
                                            berak = [k2,k3]
                                            berakin = random.choice(berak)
                                            berakin.kickoutFromGroup(to,[ls])
                                            print (to,[ls])
                                        except:
                                            pass
#=====================================#
                        elif "Admin add: " in msg.text:
                         #if msg._from in OWNER:
                          gid = msg.text.replace("Admin add: ","")
                          if gid == "":
                           k1.sendMessage(msg.to,"Invalid Mid")
                          else:
                           if gid in admin:
                            k1.sendMessage(msg.to,"Makhluk Ini Sudah Jadi Admin Boss")
                            #pass
                           else:
                            admin.append(gid)
                            k1.sendMessage(msg.to,"Added to Admin List")
                          
                        elif "Admin del: " in msg.text:
                          #if msg._from in OWNER:
                            gid = msg.text.replace("Admin del: ","")
                            if gid == "":
                              k1.sendMessage(msg.to,"Invalid Mid")
                            else:
                              if gid in admin:
                                admin.remove(gid)
                                k1.sendMessage(msg.to,"Deleted From Admin List")
                              else:
                                k1.sendMessage(msg.to,"This Person Not in Admin List Boss")
                                #pass
                                
                        elif koplaxs.startswith("friend "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        k1.sendMessage(to,"Mencoba Menambakan Teman")
                                        k1.findAndAddContactsByMid(ls)
                                        k2.findAndAddContactsByMid(ls)
                                        k3.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.sendMessage(to,"Sukses")
                                    except:
                                        k1.sendMessage(to,"ERROR")
                                
                        elif koplaxs.startswith("unban "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del wait["blacklist"][ls]
                                        k1.sendMessage(to,"Blacklist berhasil dihapus")
                                        print("[Notif] Delete blacklist Success")
                                    except:
                                        k1.sendMessage(to,"Tidak ada dalam daftar blacklist")
                        elif koplaxs.startswith("ban "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        wait["blacklist"][ls] = True
                                        k1.sendMessage(to,"Succes.!!")
                                        print("[Notif] menambahkan blacklist Success")
                                    except:
                                        k1.sendMessage(to,"Sudah ada dalam daftar blacklist")
                        elif koplaxs.startswith("unblock "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del settings["bancet"][ls]
                                        k1.sendMessage(to,"Block berhasil dihapus")
                                        k1.findAndAddContactsByMid(ls)
                                        print("[Notif] Delete blockchat Success")
                                    except:
                                        k1.sendMessage(to,"Tidak ada dalam daftar block")
                        elif koplaxs.startswith("block "):
                          #if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        settings["bancet"][ls] = True
                                        k1.sendMessage(to,"Succes.!!")
                                        k1.findBlockedContactsByMid(ls)
                                        print("[Notif] menambahkan block Success")
                                    except:
                                        k1.sendMessage(to,"Sudah ada dalam daftar block")
                        elif koplaxs == "banall":
                          #if sender in OWNER:
                            if msg.toType == 2:
                                gs = k1.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    k1.sendMessage(to,"Noting member")
                                else:
                                    for target in targets:
                                         if target not in wait["blacklist"] or target not in Bots:
                                            try:
                                                waiy["blacklist"][target] = True
                                                k1.sendMessage(to,"Succes.!!")
                                            except:
                                                pass
                        elif koplaxs == "adminall":
                          #if sender in OWNER:
                            if msg.toType == 2:
                                gs = k1.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    k1.sendMessage(to,"Noting member")
                                else:
                                    for target in targets:
                                         if target not in admin or target not in Bots:
                                            try:
                                                admin[target] = True
                                                k1.sendMessage(to,"Succes.!!")
                                            except:
                                                pass
                        elif koplaxs == "unbanall":
                            if msg.toType == 2:
                                gs = k1.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    k1.sendMessage(to,"Tidak ada member terblacklist di grup ini")
                                else:
                                    for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                k1.sendMessage(to,"Succes.!!")
                                            except:
                                                pass
                        elif koplaxs == "blockall":
                            if msg.toType == 2:
                                gs = k1.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    k1.sendMessage(to,"Noting member")
                                else:
                                    for target in targets:
                                         if target not in settings["bancet"] or target not in Bots:
                                            try:
                                                settings["bancet"][target] = True
                                                k1.sendMessage(to,"Succes.!!Blocked")
                                            except:
                                                pass
                        elif koplaxs == "unblockall":
                            if msg.toType == 2:
                                gs = k1.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    k1.sendMessage(to,"Tidak ada member block di grup ini")
                                else:
                                    for target in targets:
                                            try:
                                                del settings["bancet"][target]
                                                k1.sendMessage(to,"Succes.!!Unblocked")
                                            except:
                                                pass
                        elif koplaxs == "blacklist":
                            wait["blacklist"] = True
                            k1.sendMessage(to, "Silahkan kirim kontak")
                        elif koplaxs == "unblacklist":
                            wait["banDel"] = True
                            k1.sendMessage(to, "Silahkan kirim kontak")
                        elif koplaxs == "banlist":
                                if wait["blacklist"] == {}:
                                    k1.sendMessage(to,"Tidak Ada kontak blacklist")
                                else:
                                    k1.sendMessage(to,"═══════List blacklist═══════")
                                    h = ""
                                    for i in wait["blacklist"]:
                                        h = k1.getContact(i)
                                        k1.sendContact(to,i)
                                        
                        elif msg.text in ["Adminlist","adminlist"]:
                          if admin == []:
                            k1.sendMessage(msg.to,"The Adminlist is empty")
                          else:
                            k1.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════════\n║👑 Admin One Piece Bot 👑\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                            for mi_d in admin:
                              mc += "║[★]" + k1.getContact(mi_d).displayName + "\n"
                            k1.sendMessage(msg.to,mc)
                            
                        elif koplaxs == "adminlist2":
                          #if sender in admin:
                                if admin == {}:
                                    k1.sendMessage(to,"NOTING ADMIN..")
                                else:
                                    k1.sendMessage(to,"═══════List Admin═══════")
                                    h = ""
                                    for i in admin:
                                        h = k1.getContact(i)
                                        k1.sendContact(to,i)
                        elif koplaxs == "blocklist":
                                if settings["bancet"] == {}:
                                    k1.sendMessage(to,"Tidak Ada kontak blocklist")
                                else:
                                    k1.sendMessage(to,"═══════List blockchat═══════")
                                    h = ""
                                    for i in settings["bancet"]:
                                        h = k1.getContact(i)
                                        k1.sendContact(to,i)
                        elif koplaxs == "clearban":
                          #if sender in OWNER:
                            wait["blacklist"] = {}
                            k1.sendMessage(to,"done all deleted blacklist")
                            k1.sendMessage(to,"succes.!!")
                            k2.sendMessage(to,"succes.!!")
                            k3.sendMessage(to,"succes.!!")
                            
                        elif koplaxs == "clearadmin":
                          #if sender in OWNER:
                            settings["admin"] = {}
                            k1.sendMessage(to,"done all deleted admin")
                        elif koplaxs == "clearblock":
                          #if sender in OWNER:
                            settings["bancet"] = {}
                            k1.sendMessage(to,"done all deleted blocked")
                        elif koplaxs == "clearchat":
                          #if sender in OWNER:
                            k1.removeAllMessages(op.param2)
                            k1.removeAllMessages(op.param2)
                            k2.removeAllMessages(op.param2)
                            k3.removeAllMessages(op.param2)
                            k1.sendMessage(to, "Berhasil hapus semua chat")
                            
                        elif koplaxs.startswith("sendgrup "):
                          #if sender in OWNER:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = k1.groups
                            for group in groups:
                                sendMessageWithFooter(group, "╭━━━━━╦BroadCast by ONE PIECE TEAM╦━━━━━╮\n{}".format(str(txt)))
                            k1.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                                
                        elif koplaxs.startswith("Broadcast "):
                          #if sender in OWNER:
                            sep = text.split(" ")
                            pesan = text.replace(sep[0] + " ","")
                            saya = k1.getGroupIdsJoined()
                            for group in saya:
                                k1.sendMessage(group,"[ Broadcast ]\n" + str(pesan))
                                
                        elif koplaxs.startswith("gname "):
                          #if sender in OWNER:
                            if msg.toType == 2:
                                X = k1.getGroup(to)
                                sep = msg.text.split(" ")
                                X.name = msg.text.replace(sep[0] + " ","")
                                k1.updateGroup(X)
                                
                        elif koplaxs == "gruplist":
                            groups = k1.groups
                            ret_ = "╭━━━━━══[ Group List ]══━━━━━╮"
                            no = 0 + 1
                            for gid in groups:
                                group = k1.getGroup(gid)
                                ret_ += "\n┣═ {}. {} ┣═Member: {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╰━━━━━══[ Total {} Groups ]════━━━━━".format(str(len(groups)))
                            k1.sendMessage(to, str(ret_))
                        elif koplaxs == "friendlist":
                            contactlist = k1.getAllContactIds()
                            kontak = k1.getContacts(contactlist)
                            num=1
                            msgs="╭━━━━━══[ Friend List ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Friend Result ]══━━━━━\nTotal : %i" % len(kontak)
                            k1.sendMessage(to, msgs)
                                
                        elif koplaxs == "friendblocklist":
                            blockedlist = k1.getBlockedContactIds()
                            kontak = k1.getContacts(blockedlist)
                            num=1
                            msgs="╭━━━━━══[ Friend Block ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Block Result ]══━━━━━\nBlock Total : %i" % len(kontak)
                            k1.sendMessage(to, msgs)
                        elif koplaxs == "gcreator":
                            k1.sendMessage(to, "━━━━══[Pembuat Grup]══━━━━")
                            group = k1.getGroup(to)
                            GS = group.creator.mid
                            k1.sendContact(to, GS)
                            k1.sendMessage(to, "━━━━══━━╩━━══━━━━")
                        elif koplaxs == "memberlist":
                          #if sender in admin:
                            if msg.toType == 2:
                                    group = k1.getGroup(to)
                                    ret_ = "╭━━━══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n┣═ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                                    k1.sendMessage(to, str(ret_))
                                
                        elif koplaxs == "pendinglist":
                            #if sender in OWNER:
                                if msg.toType == 2:
                                    group = k1.getGroup(to)
                                    ret_ = "╭━━━══[ Pending List ]"
                                    no = 0 + 1
                                    if group.invitee is None or group.invitee == []:
                                        k1.sendMessage(to, "Tidak ada pendingan")
                                        return
                                    else:
                                        for pen in group.invitee:
                                            ret_ += "\n┣═ {}. {}".format(str(no), str(pen.displayName))
                                            no += 1
                                        ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                        k1.sendMessage(to, str(ret_))
                        
                        elif koplaxs == "ginfo":
                            #if sender in admin:
                                group = k1.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Qr tidak tersedia karna di tutup"
                                else:
                                    gQr = "Open"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(k1.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭━━━━══[ Group Info ]"
                                ret_ += "\n┣═Nama Group : {}".format(str(group.name))
                                ret_ += "\n┣═ID Group : {}".format(group.id)
                                ret_ += "\n┣═Pembuat : {}".format(str(gCreator))
                                ret_ += "\n┣═Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n┣═Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣═━━━Kode Qr/Link━━━═"
                                ret_ += "\n┣═Group Ticket : {}".format(gTicket)
                                ret_ += "\n┣═Group Qr : {}".format(gQr)
                                ret_ += "\n╰━━━━══[ CREATOR ONE PIECE TEAM]"
                                k1.sendMessage(to, str(ret_))
                            
                        elif koplaxs == "gpict":
                          #if sender in admin:
                            group = k1.getGroup(to)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            k1.sendImageWithURL(to, path)
                        elif koplaxs == "gname":
                          #if sender in admin:
                            gid = k1.getGroup(to)
                            k1.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                        elif koplaxs == "gid":
                          #if sender in admin:
                            gid = k1.getGroup(to)
                            k1.sendMessage(to,gid.id)
                        elif koplaxs == "gurl":
                          #if sender in admin:
                            if msg.toType == 2:
                                group = k1.getGroup(to)
                                if group.preventedJoinByTicket == False:
                                    ticket = k1.reissueGroupTicket(to)
                                    k1.sendMessage(to, "https://line.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    group.preventedJoinByTicket = False
                                    k1.updateGroup(group)
                                    k1.sendMessage(to, "https://line.me/R/ti/g/{}".format(str(ticket)))
                        elif msg.text in ["Buka qr","buka qr"]:
                         if msg._from in admin:
                            if msg.toType == 2:
                                group = k1.getGroup(to)
                                if group.preventedJoinByTicket == False:
                                    k1.sendMessage(to, "Sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    k1.updateGroup(group)
                                    k1.sendMessage(to, "Berhasil membuka Qr")
                        elif msg.text in ["Tutup qr","tutup qr"]:
                         if msg._from in admin:
                            if msg.toType == 2:
                                group = k1.getGroup(to)
                                if group.preventedJoinByTicket == True:
                                    k1.sendMessage(to, "Sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    k1.updateGroup(group)
                                    k1.sendMessage(to, "Berhasil menutup Qr")
#==============================================================================#
                        elif koplaxs == "set":
                          #if sender in admin:
                            try:
                                ret_ = "╭━━╦̰̰̈́Ｏｎｅ ｐｉｅｃｅ Ｔｅａｍ╦━━╮\n┣━━━━Status Proteksi━━━━"
                                if wait["Protectkick"] == True: ret_ += "\n┣━╣ Protect Kick Enable✔"
                                else: ret_ += "\n┣━╣ Protect Kick Disable❌"
                                if wait["ProtectInvite"] == True: ret_ += "\n┣━╣ Protect Invite Enable✔"
                                else: ret_ += "\n┣━╣ Protect Invite Disable❌"
                                if wait["ProtectQR"] == True: ret_ += "\n┣━╣ Protect QR Enable✔"
                                else: ret_ += "\n┣━╣ Protect QR Disable❌"
                                if wait["Protectcancel"] == True: ret_ += "\n┣━╣ Protect Cancel Enable✔"
                                else: ret_ += "\n┣━╣ Protect Cancel Disable❌"
                                if wait["autoAdd"] == True: ret_ += "\n┣━╣ AutoAdd Enable✔"
                                else: ret_ += "\n┣━╣ AutoAdd Disable❌"
                                if wait["contact"] == True: ret_ += "\n┣━╣ Contact  Enable✔"
                                else: ret_ += "\n┣━╣ Contact  Disable❌"
                                if wait["AddFriend"] == True: ret_ += "\n┣━╣ Add Friend  Enable✔"
                                else: ret_ += "\n┣━╣ Add Friend  Disable❌"
                                ret_ += "\n┣━━━━━━━━━━━━━━━━━\n╰━╩𖤓Ｏｎｅ ｐｉｅｃｅ Ｔｅａｍ𖤓╩━╯"
                                k1.sendMessage(to, str(ret_))
                            except Exception as e:
                                k1.sendMessage(to, str(e))
                                
                        elif msg.text in ["Protectkick:on","protectkick:on"]:
                          #if msg._from in OWNER:
                            if wait["Protectkick"] == True:
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Protect Kickers On")
                              else:
                                k1.sendMessage(msg.to,"Done")
                            else:
                              wait["Protectkick"] = True
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Udah On Njir\nPikun Lu")
                              else:
                                k1.sendMessage(msg.to,"done")
                                
                        elif msg.text in ["Protectkick:off","protectkick:off"]:
                          #if msg._from in OWNER:
                            if wait["Protectkick"] == False:
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Protect Kickers Off")
                              else:
                                k1.sendMessage(msg.to,"Done")
                            else:
                              wait["Protectkick"] = False
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Udah Off Njir\nPikun Lu")
                              else:
                                k1.sendMessage(msg.to,"done")
                                
                        elif msg.text in ["Protectinvite:on","protectinvite:on"]:
                          #if msg._from in OWNER:
                            if wait["ProtectInvite"] == True:
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Protect Invite On")
                              else:
                                k1.sendMessage(msg.to,"Done")
                            else:
                              wait["ProtectInvite"] = True
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Udah On Njir\nPikun Lu")
                              else:
                                k1.sendMessage(msg.to,"done")
                                
                        elif msg.text in ["Protectinvite:off","protectinvite:off"]:
                          #if msg._from in OWNER:
                            if wait["ProtectInvite"] == False:
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Protect Invite Off")
                              else:
                                k1.sendMessage(msg.to,"Done")
                            else:
                              wait["ProtectInvite"] = False
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Udah Off Njir\nPikun Lu")
                              else:
                                k1.sendMessage(msg.to,"done")
                                
                        elif msg.text in ["Protectqr:on","protectqr:on"]:
                          #if msg._from in OWNER:
                            if wait["ProtectQR"] == True:
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Protect QR On")
                              else:
                                k1.sendMessage(msg.to,"Done")
                            else:
                              wait["ProtectQR"] = True
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Udah On Njir\nPikun Lu")
                              else:
                                k1.sendMessage(msg.to,"done")
                                
                        elif msg.text in ["Protectqr:off","protectqr:off"]:
                          #if msg._from in OWNER:
                            if wait["ProtectQR"] == False:
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Protect QR Off")
                              else:
                                k1.sendMessage(msg.to,"Done")
                            else:
                              wait["ProtectQR"] = False
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Udah Off Njir\nPikun Lu")
                              else:
                                k1.sendMessage(msg.to,"done")
                                
                        elif msg.text in ["Protectcancel:on","protectcancel:on"]:
                          #if msg._from in OWNER:
                            if wait["Protectcancel"] == True:
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Protect Cancel On")
                              else:
                                k1.sendMessage(msg.to,"Done")
                            else:
                              wait["Protectcancel"] = True
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Udah On Njir\nPikun Lu")
                              else:
                                k1.sendMessage(msg.to,"done")
                                
                        elif msg.text in ["Protectcancel:off","protectcancel:off"]:
                          #if msg._from in OWNER:
                            if wait["Protectcancel"] == False:
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Protect Cancel Off")
                              else:
                                k1.sendMessage(msg.to,"Done")
                            else:
                              wait["Protectcancel"] = False
                              if wait["lang"] == "JP":
                                k1.sendMessage(msg.to,"Udah Off Njir\nPikun Lu")
                              else:
                                k1.sendMessage(msg.to,"done")
                                
                        elif koplaxs == "friend:on":
                          #if sender in OWNER:
                            wait["AddFriend"] = True
                            k1.sendMessage(to, "Kirim Kontaknya Boss")
                            
                        elif koplaxs == "friend:on":
                          #if sender in OWNER:
                            wait["AddFriend"] = False
                            k1.sendMessage(to, "Kirim Kontaknya Boss")
                                
                        elif koplaxs == "autoadd:on":
                          #if sender in OWNER:
                            settings["autoAdd"] = True
                            k1.sendMessage(to, "Already on")
                        elif koplaxs == "autoadd:off":
                            settings["autoAdd"] = False
                            k1.sendMessage(to, "Already off")
                        elif koplaxs == "autojoin:on":
                            wait["autoJoin"] = True
                            k1.sendMessage(to, "Already on")
                        elif koplaxs == "autojoin:off":
                            wait["autoJoin"] = False
                            k1.sendMessage(to, "Already off")
                        elif koplaxs == "sambutan:on":
                            if msg.to in settings["SAMBUT"]:
                                k1.sendMessage(to, "Already on")
                            else:
                                k1.sendMessage(to, "Sudah on")
                                settings["SAMBUT"][msg.to] = True
                        elif koplaxs == "sambutan:off":
                            if msg.to in settings["SAMBUT"]:
                                k1.sendMessage(to, "Already off")
                                del settings["SAMBUT"][msg.to]
                            else:
                                k1.sendMessage(to, "Sudah off")
                        elif koplaxs == "respon:on":
                            settings["detectMention"] = True
                            k1.sendMessage(to, "Already on")
                        elif koplaxs == "respon:off":
                            settings["detectMention"] = False
                            k1.sendMessage(to, "Already off")
                        elif koplaxs == "jointicket:on":
                            settings["autoJoinTicket"] = True
                            k1.sendMessage(to, "Already on")
                        elif koplaxs == "jointicket:off":
                            settings["autoJoinTicket"] = False
                            k1.sendMessage(to, "Already off")
                            
                        elif msg.text in ["Contact On","Contact on","contact on"]:
                         #if msg._from in OWNER:
                          if wait["contact"] == True:
                           if wait["lang"] == "JP":
                            k1.sendMessage(msg.to,"Cek Mid Lewat Share Kontak On")
                           else:
                            k1.sendMessage(msg.to,"done")
                          else:
                           wait["contact"] = True
                           if wait["lang"] == "JP":
                            k1.sendMessage(msg.to,"Cek Mid Lewat Share Kontak On")
                           else:
                            k1.sendMessage(msg.to,"done")
                            
                        elif msg.text in ["Contact Off","Contact off","contact off"]:
                         #if msg._from in OWNER:
                          if wait["contact"] == False:
                           if wait["lang"] == "JP":
                            k1.sendMessage(msg.to,"Cek Mid Lewat Share Kontak Off")
                           else:
                            k1.sendMessage(msg.to,"done")
                          else:
                           wait["contact"] = False
                           if wait["lang"] == "JP":
                            k1.sendMessage(msg.to,"Cek Mid Lewat Share Kontak Off")
                           else:
                            k1.sendMessage(msg.to,"done")
                            
                        elif koplaxs == "contact:on":
                            settings["checkContact"] = True
                            k1.sendMessage(to, "Already on")
                        elif koplaxs == "contact:off":
                            settings["checkContact"] = False
                            k1.sendMessage(to, "Already off")
                        elif koplaxs == "share:on":
                            settings["checkPost"] = True
                            k1.sendMessage(to, "Already on")
                        elif koplaxs == "share:off":
                            settings["checkPost"] = False
                            k1.sendMessage(to, "Already off")
                        elif koplaxs == "autoread:on":
                            settings["autoRead"] = True
                            k1.sendMessage(to, "Already on")
                        elif koplaxs == "autoread:off":
                            settings["autoRead"] = False
                            k1.sendMessage(to, "Already off")
                        elif koplaxs == "unsend:on":
                            settings["unsendMessage"] = True
                            k1.sendMessage(to, "Already on")
                        elif koplaxs == "unsend:off":
                            settings["unsendMessage"] = False
                            k1.sendMessage(to, "Already off")
#===============================================================
                        elif koplaxs == "list protect":
                                pli = ""
                                pme = ""
                                pna = ""
                                pin = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = Prolink
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    pli += str(a) + ". " +k1.getGroup(group).name + "\n"
                                gid = PROTECT
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    pme += str(b) + ". " +k1.getGroup(group).name + "\n"
                                gid = Proname
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    pna += str(d) + ". " +k1.getGroup(group).name + "\n"
                                gid = Proinvite
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    pin += str(c) + ". " +k1.getGroup(group).name + "\n"
                                k1.sendMessage(msg.to,"╭━━╦̰̰̈́𖤓Ｏｎｅ ｐｉｅｃｅ Ｔｅａｍ𖤓╦━━╮\n┣━╣PROTECT LINK:: "+pli+"\n┣━╣PROTECTION:: "+pme+"\n┣━╣PROTECT NAME:: "+pna+"\n┣━╣PROTECT INVITE:: "+pin+"\n╰━╩TOTAL %s PRO GROUPS╩━╯" %(str(len(Prolink)+len(PROTECT)+len(Proname)+len(Proinvite))))
                        elif koplaxs == "Namelock:on":
                          #if sender in admin:
                            if msg.to in wait['pname']:
                              k1.sendMessage(msg.to,"Protect Name On.")
                            else:
                              k1.sendMessage(msg.to,"Protect Name ON")
                              wait['pname'][msg.to] = True
                              wait['pro_name'][msg.to] = k1.getGroup(msg.to).name
                              
                        elif koplaxs == "Namelock:off":
                          #if sender in admin:
                            if msg.to in wait['pname']:
                              k1.sendMessage(msg.to,"ƬƲƦƝ ƠƑƑ.")
                              del wait['pname'][msg.to]
                            else:
                              k1.sendMessage(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
                            
                        elif "Getline " in msg.text:
                          #if sender in admin:
                            msgg = msg.text.replace("Getline ",'')
                            conn = k1.findContactsByUserid(msgg)
                            if True:
                              k1.sendContact(to, conn.mid)
                              k1.sendMessage(to,"http://k1.me/ti/p/~" + msgg)
                        elif "Cekmid " in msg.text:
                          #if sender in admin:
                            mmid = msg.text.replace("Cekmid ","")
                            h = k1.getContact(mmid)
                            k1.sendMessage(to, h.displayName)
                            k1.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            k1.sendContact(to, mmid)
                            
                        elif "Getcontact " in msg.text:
                          #if msg._from in OWNER:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = k1.getContact(key1)
                            k1.sendContact(msg.to,key1)
                        elif "Getname " in msg.text:
                          #if msg._from in OWNER:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = k1.getContact(key1)
                            try:
                              k1.sendMessage(msg.to, "══════❴CONTACT NAME❵══════\n" + contact.displayName)
                            except:
                              k1.sendMessage(msg.to, "══════❴CONTACT NAME❵══════\n" + contact.displayName)
                        elif msg.text in ["Myname"]:
                          h = k1.getContact(msg._from)
                          k1.sendMessage(msg.to, "══════❴YOUR.NAME❵══════\n" + h.displayName)
                        elif msg.text in ["Mybio"]:
                          if msg._from in admin:
                            h = k1.getContact(msg._from)
                            k1.sendMessage(msg.to, "══════❴YOUR.STATUS❵══════\n" + h.statusMessage)
                        elif msg.text in ["Mypict"]:
                          if msg._from in admin:
                            h = k1.getContact(msg._from)
                            k1.sendMessage(msg.to, "══════❴YOUR.PICTURES❵══════")
                            k1.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                        elif msg.text in ["Myvid"]:
                          if msg._from in admin:
                            h = k1.getContact(msg._from)
                            k1.sendMessage(msg.to, "══════❴YOUR.VIDEO PICTURES❵══════")
                            k1.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                        elif msg.text in ["Urlpict"]:
                          if msg._from in admin:
                            h = k1.getContact(msg._from)
                            k1.sendMessage(msg.to, "══════❴YOUR.URL.PICTURES❵══════")
                            k1.sendMessage(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                        elif "Getmid @" in msg.text:
                          if msg._from in admin:
                            _name = msg.text.replace("Getmid @","")
                            _nametarget = _name.rstrip(' ')
                            gs = k1.getGroup(msg.to)
                            for g in gs.members:
                              if _nametarget == g.displayName:
                                k1.sendMessage(msg.to, g.mid)
                          else:
                            pass
                        elif "Getinfo" in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = k1.getContact(key1)
                            try:
                              k1.sendMessage(msg.to,"🎀═displayName═🎀\n✤[" + contact.displayName + "]✤\n🎀═MIDs═🎀\n✤[" + contact.mid + "]✤\n🎀═StatusContact═🎀\n✤" + contact.statusMessage + "✤")
                            except:
                              k1.sendMessage(msg.to,"??═displayName═🎀\n✤[" + contact.displayName + "]✤\n🎀═MIDs═🎀\n✤[" + contact.mid + "]✤\n🎀═StatusContact═🎀\n✤" + contact.statusMessage + "✤")
                              
                        elif "Getbio" in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = k1.getContact(key1)
                            cu = k1.channel.getCover(key1)
                            try:
                              k1.sendMessage(msg.to,contact.statusMessage)
                            except:
                              k1.sendMessage(msg.to,contact.statusMessage)
                        elif "Gimage" in msg.text:
                          if msg._from in admin:
                            group = k1.getGroup(msg.to)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            k1.sendImageWithURL(msg.to,path)
                        elif "Getpict @" in msg.text:
                          if msg._from in admin:
                            _name = msg.text.replace("Getpict @","")
                            _nametarget = _name.rstrip('  ')
                            gs = k1.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                              if _nametarget == g.displayName:
                                targets.append(g.mid)
                            if targets == []:
                              k1.sendMessage(msg.to,"Contact not found")
                            else:
                              for target in targets:
                                try:
                                  contact = k1.getContact(target)
                                  path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                  k1.sendImageWithURL(msg.to, path)
                                except:
                                  pass
                                  
                        elif "Me" == msg.text:
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                          hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                          bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                          hr = timeNow.strftime("%A")
                          bln = timeNow.strftime("%m")
                          for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                          for k in range(0, len(bulan)):
                             if bln == str(k): bln = bulan[k-1]
                          rst = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                          k1.sendContact(msg.to,msg._from)
                          k1.sendMessage(msg.to,rst)
                          
                        elif msg.text in ["Clearban"]:
                          #if msg._from in OWNER:
                            wait["blacklist"] = {}
                            k1.sendMessage(to,"done all deleted blacklist")
#====================#
        if op.type == 5:
          if wait["autoAdd"] == True:
            #if op.param3 in k4MID:
              k1.findAndAddContactsByMid(op.param1)
              k2.findAndAddContactsByMid(op.param1)
              k3.findAndAddContactsByMid(op.param1)
              k1.sendMessage(op.param1, "MAKASIH UDAH DI ADD PLAK")
              k2.sendMessage(op.param1, "MAKASIH UDAH DI ADD PLAK")
              k3.sendMessage(op.param1, "MAKASIH UDAH DI ADD PLAK")
              k1.sendContact(op.param1, 'ubaba90be636d918cab5509685cef5c23')
                
        if op.type == 11: #Jika Ada Yang Buka QR
          if wait["ProtectQR"] == True:
              if random.choice(KAC).getGroup(op.param1).preventedJoinByTicket == False:
                if op.param2 in Bots:
                  pass
                elif op.param2 in admin:
                  pass
                else:
                  try:
                    random.choice(KAC).sendMessage(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Dont Playing Link Group Bro")
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(KAC).updateGroup(G)
                    random.choice(KAC).sendMessage(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "We Enter Into Blacklist Boss")
                    wait["blacklist"][op.param2] = True
                  except:
                    G.preventedJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).updateGroup(G)
                    wait["blacklist"][op.param2] = True
          else:
            pass
                
        if op.type == 11: #Jika Ada Yang Ganti Nama Group
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = k2.getGroup(op.param1)
                    except:
                        try:
                            G = k3.getGroup(op.param1)
                        except:
                            try:
                              G = random.choice(KAC).getGroup(op.param1)
                            except:
                              pass
                    G.name = wait['pro_name'][op.param1]
                    if op.param2 in Bots:
                      pass
                    elif op.param2 in admin:
                      pass
                    else:
                     try:
                        k2.updateGroup(G)
                     except:
                        try:
                            k3.updateGroup(G)
                        except:
                            try:
                                random.choice(KAC).updateGroup(G)
                            except:
                              pass
                    if op.param2 in Bots:
                      pass
                    elif op.param2 in admin:
                      pass
                    else:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        k1.sendMessage(op.param1,"Group name lock")
                                        random.choice(KAC).sendMessage(op.param1,"Dikunci Pe'a")
                                        random.choice(KAC).sendMessage(op.param1,"Wekawekaweka 􀜁􀅔Har Har􏿿")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        k1.sendMessage(c)
                                        
        if op.type == 13:
          if op.param3 in k1MID:
                if wait["autoJoin"] == True:
                    k1.acceptGroupInvitation(op.param1)
                else:
                    try:
                        k1.acceptGroupInvitation(op.param1)
                        k1.sendMessage(op.param1, "=====||Auto Reply||=====\nAutoJoin Off\nPlease PM Me\nThanks!!!")
                        k1.leaveGroup(op.param1)
                    except:
                        pass
#
          if op.param3 in k2MID:
                if op.param2 in admin:
                    k2.acceptGroupInvitation(op.param1)
                else:
                    pass
                    try:
                        k2.acceptGroupInvitation(op.param1)
                        k2.sendMessage(op.param1, "=====||Auto Reply||=====\nEnte Bukan Boss Ane\nJangan Suka Ngundang² Njerr")
                        k2.leaveGroup(op.param1)
                    except:
                        pass
#
          if op.param3 in k3MID:
                if op.param2 in admin:
                    k3.acceptGroupInvitation(op.param1)
                else:
                    pass
                    try:
                        k3.acceptGroupInvitation(op.param1)
                        k3.sendMessage(op.param1, "=====||Auto Reply||=====\nEnte Bukan Boss Ane\nJangan Suka Ngundang² Njerr")
                        k3.leaveGroup(op.param1)
                    except:
                        pass
                        
        if op.type == 13: #Jika Member Undang Orang
          if wait["ProtectInvite"] == True:
              group = k1.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              else:
                  try:
                    k1.cancelGroupInvitation(op.param1, gMembMids)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                  except:
                    random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
          else:
            pass
            
        if op.type == 13: #Jika Blacklist Di Invite
          if op.param3 in wait["blacklist"] == True:
            if op.param2 in Bots:
              pass
            elif op.param2 in admin:
              pass
            else:
              try:
                random.choice(KAC).sendMessage(op.param1,random.choice(KAC).getContact(op.param3).displayName + " On Blacklist Boss\nWe Will Cancel Invitation")
                random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
              except:
                random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
          else:
            pass
#============ Protect Kick ============            
        if op.type == 19:
          if op.param3 in k1MID:
            if op.param2 in Bots:
              pass
            else:
              try:
                k2.kickoutFromGroup(op.param1,[op.param2])
                G = k2.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k2.updateGroup(G)
                Ticket = k2.reissueGroupTicket(op.param1)
                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k2.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k2.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                  
          elif op.param3 in k2MID:
            if op.param2 in Bots:
              pass
            else:
              try:
                k3.kickoutFromGroup(op.param1,[op.param2])
                G = k3.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k3.updateGroup(G)
                Ticket = k3.reissueGroupTicket(op.param1)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k3.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k3.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                
          elif op.param3 in k3MID:
            if op.param2 in Bots:
              pass
            else:
              try:
                k2.kickoutFromGroup(op.param1,[op.param2])
                G = k2.getGroup(op.param1)
                G.preventedJoinByTicket = False
                k2.updateGroup(G)
                Ticket = k2.reissueGroupTicket(op.param1)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = k2.getGroup(op.param1)
                G.preventedJoinByTicket = True
                k2.updateGroup(G)
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = False
                random.choice(KAC).updateGroup(G)
                Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                G = random.choice(KAC).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(KAC).updateGroup(G)
                wait["blacklist"][op.param2] = True
                
        #elif op.type == 19: #Admin Ke Kick
          elif op.param3 in admin:
              if op.param2 in Bots:
                pass
              else:
                try:
                  kicked = k2.getContact(op.param3).mid
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  k2.findAndAddContactsByMid(kicked)
                  k2.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  kicked = random.choice(KAC).getContact(op.param3).mid
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).findAndAddContactsByMid(kicked)
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                  
        if op.type == 19: #Member Ke Kick
            if wait["Protectkick"] == True:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              else:
                try:
                  kicked = random.choice(KAC).getContact(op.param3).mid
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).findAndAddContactsByMid(kicked)
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  kicked = random.choice(KAC).getContact(op.param3).mid
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).findAndAddContactsByMid(op.param1,[op.param3])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
            else:
              pass
#============== SELESAI ===============
            
        if op.type == 32:
          if wait["Protectcancel"] == True:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              else:
                try:
                  random.choice(KAC).sendMessage(op.param1,random.choice(KAC).getContact(op.param2).displayName + " Canceled Invitation")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
          else:
            pass
            
        if op.type == 55:
          try:
            group_id = op.param1
            user_id=op.param2
            subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
          except Exception as e:
              print (e)
              
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                          if op.param2 in OWNER:
                            pass
                          else:
                            Name = k1.getContact(op.param2).displayName
                            Np = k1.getContact(op.param2).pictureStatus
                            #Kontol = k1.getContact(op.param2).mid
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        k1.sendMessage(op.param1, "Hallo...! " + "☞ " + nick[0] + " ☜" + " Lagi Stalking yaa...?")
                                        #k1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                        #mentionMembers(to, [Kontol])
                                    else:
                                        k1.sendMessage(op.param1, "Haii...! " + "☞ " + nick[1] + " ☜" + " Masuk Sini... Ngapain Ngintip-Ngintip")
                                        #k1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                        #mentionMembers(to, [Kontol])
                                else:
                                    k1.sendMessage(op.param1, "Nah " + "☞ " + Name + " ☜" + " Ngintip Aim Doain Jones Selalu.. hahaha")
                                    #k1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    #mentionMembers(to, [Kontol])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
        else:
            pass
            
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
              return
            ginfo = k1.getGroup(op.param1)
            cp = k1.getContact(op.param2)
            k1.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + cp.pictureStatus)
            k1.sendMessage(op.param1, "Ｓｅｌａｍａｔ Ｄａｔａｎｇ ❲" + str(cp.displayName) + "❳\nＤｉ Ｇｒｏｕｐ ❲ " + str(ginfo.name) +"❳\nBudayakan Baca Note\nSemoga Betah^o^\nKalo Ga Paham Tanya Aim kak yaaa...")
                
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = k1.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                                name_ = contact.displayName
                                mention = str(nama_)
                            else:
                                ret_ = "Send Message cancelled."
                           #     ret_ += "\nSend At : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nType : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nText : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n_____________UNSEND DONE______________"
                          #      sendMention(at, mention)
                                k1.sendMessage(at, str(ret_))
                            del msg_dict[msg_id]
                        else:
                            k1.sendMessage(at,"SentMessage cancelled,But I didn't have log data.\nSorry > <")
                            print("unsend aktiv")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
                    
                
        if op.type == 59:
          print (op)
#====================================
    except Exception as error:
        logError(error)
#==============================================================================#
def k1Poll():
  while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
        
    except Exception as e:
        k1.log("[SINGLE_TRACE] ERROR : " + str(e))
        
Thread(target=k1Poll).start()