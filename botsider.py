# -*- coding: utf-8 -*-


import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

cl = LINETCR.LINE() #Luffy
cl.login(token='')
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="")
ki5.loginResult()

print "login Bot"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""-==================-
[•]Cctv [Start Check Sider]
[•]Ciduk [Liat Hasil Sider]
[•]Creator [Melihat Creator Bot]
[•]@bye/Bot out [Untuk Keluarkan Bot]
-==================-
"""
KAC=[cl,ki,ki2,ki3,ki4,ki5]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid

Bots=[mid, kimid, ki2mid, ki3mid, ki4mid,ki5mid]
owner=["ub1e94db89396dd6cbd72190f371c1ecd"]
admin=["ub1e94db89396dd6cbd72190f371c1ecd"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cName2":"",
    "cName3":"",
    "cName4":"",
    "cName5":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":False,
    "Protectcancl":False,
    "protectionOn":False,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            cl.acceptGroupInvitation(op.param1)
            cl.sendText(op.param1, "Ketik Help Untuk Liat Menu")

        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"

        if op.type == 22:
            if wait["leaveRoom"] == False:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == False:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == False:
                    cl.leaveRoom(msg.to)

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Admin menu"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])

            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            
    #---------------------------------------
            elif "Bot say " in msg.text:
                if msg.from_ in admin:
                  bctxt = msg.text.replace("Bot say ", "")
                  cl.sendText(msg.to, (bctxt))
                  ki.sendText(msg.to, (bctxt))
                  ki2.sendText(msg.to, (bctxt))
                  ki3.sendText(msg.to, (bctxt))
                  ki4.sendText(msg.to, (bctxt))
                  ki5.sendText(msg.to, (bctxt))

    #-------------- Add Friends ------------
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                 
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")                
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
    #--------------= SC Ganti nama Owner=--------------
            elif "Myname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")

            elif "Bcc " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bcc ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
                    ki.sendText(manusia, (bctxt))
                    ki2.sendText(manusia, (bctxt))
                    ki3.sendText(manusia, (bctxt))
                    ki4.sendText(manusia, (bctxt))
                    ki5.sendText(manusia, (bctxt))

            elif msg.text in ["Bot?"]: #Ngirim Semua Kontak Bot
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)

            elif "jointicket " in msg.text.lower():
                rplace=msg.text.lower().replace("jointicket ")
                if rplace == "on":
                    wait["atjointicket"]=True
                elif rplace == "off":
                    wait["atjointicket"]=False
                cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links=[]
                for l in links:
                    if l not in n_links:
                        n_links.append(l)
                for ticket_id in n_links:
                    if wait["atjointicket"] == True:
                        group=cl.findGroupByTicket(ticket_id)
                        cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))

            elif "My mid" == msg.text:
              if msg.from_ in admin:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "Mid Bot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
	  
            elif msg.text in ["Join on","Auto join on"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join off","Auto join off"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
           
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                    ki.rejectGroupInvitation(i)
                    ki2.rejectGroupInvitation(i)
                    ki3.rejectGroupInvitation(i)
                    ki4.rejectGroupInvitation(i)
                    ki5.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"Refuse denied")
        #--------------------------------#

            elif msg.text == "Cctv":
              #if msg.from_ in admin:
                cl.sendText(msg.to, "Cek Sider On")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "Ciduk":
                # if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "|Readers||%s\n\n\n||Ignored||\n%s\n||\n\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv dulu\nBaru Ketik Ciduk")

       #------------ Keluarin Bot----------------------#
            elif msg.text.lower() == 'Pulang':
                if msg.toType == 2:
                      ginfo = cl.getGroup(msg.to)
                      try:
                          cl.sendText(msg.to, "Good bye guys")
                          ki.leaveGroup(msg.to)
                          ki2.leaveGroup(msg.to)
                          ki3.leaveGroup(msg.to)
                          ki4.leaveGroup(msg.to)
                      except:
                          pass
    #---------------------------------------------#
            elif msg.text.lower() == 'Masuk':
                          G = cl.getGroup(msg.to)
                          ginfo = cl.getGroup(msg.to)
                          G.preventJoinByTicket = False
                          cl.updateGroup(G)
                          invsend = 0
                          Ticket = cl.reissueGroupTicket(msg.to)
                          ki.acceptGroupInvitationByTicket(msg.to, Ticket)
                          time.sleep(0.01)
                          ki2.acceptGroupInvitationByTicket(msg.to, Ticket)
                          time.sleep(0.01)
                          ki3.acceptGroupInvitationByTicket(msg.to, Ticket)
                          time.sleep(0.01)
                          ki4.acceptGroupInvitationByTicket(msg.to, Ticket)
                          time.sleep(0.01)
                          ki5.acceptGroupInvitationByTicket(msg.to, Ticket)
                          time.sleep(0.01)
                          G = cl.getGroup(msg.to)
                          ginfo = cl.getGroup(msg.to)
                          G.preventJoinByTicket = True
                          random.choice(KAC).updateGroup(G)
                          print "Masuk Gaes"
                          G.preventJoinByTicket(G)
                          random.choice(KAC).updateGroup(G)

            elif msg.text.lower() == 'Pulang':
                          if msg.toType == 2:
                              ginfo = cl.getGroup(msg.to)
                              try:
                                  cl.sendText(msg.to, "􀠁Bye Bye " + str(ginfo.name) + "")
                                  ki.leaveGroup(msg.to)
                                  ki2.leaveGroup(msg.to)
                                  ki3.leaveGroup(msg.to)
                                  ki4.leaveGroup(msg.to)
                                  ki5.leaveGroup(msg.to)
                              except:
                                  pass
      #-------------Creator------------------#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'ub1e94db89396dd6cbd72190f371c1ecd'}
              cl.sendMessage(msg)
              cl.sendText(msg.to,"Itu Kak Creator Bot Kami")
      #-------------Finish----------------#
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
