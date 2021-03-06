# -*- coding: UTF-8 -*-
import pygame
from pygame.locals import *

class Resource(object):
	#anime{}
	#image{}
	#pic{}
	#file_name

	def __init__(self):
		file_name=[
			"background.png",
			"bubble.png",
			"bullet1.png",
			"bullet2.png",
			"bullet3.png",
			"cirno-fly.png",
			"cirno-left.png",
			"cirno-right.png",
			"enemy.png",
			"enemy2.png",
			"front00.png",
			"loading.jpg",
			"point.png",
			"quitb.png",
			"quitd.png",
			"resource.png",
			"startb.png",
			"startd.png",
			"ziji.png",
			"bg.png",
			"stg3bg.png",
			"stg3bg2.png",
			"stg3bg3.png",
			"stg3bg4.png",
			"eff02.png",
		]
		self.anime={}
		self.image={}
		self.pic={}

		for i in file_name:
			self.pic[i]=pygame.image.load("pic\\"+i).convert_alpha()

		self.image["background"]=self.pic["background.png"]
		self.image["loading"]=self.pic["loading.jpg"]
		self.image["quitb"]=self.pic["quitb.png"]
		self.image["quitd"]=self.pic["quitd.png"]
		self.image["startb"]=self.pic["startb.png"]
		self.image["startd"]=self.pic["startd.png"]
		self.image["front00"]=self.pic["front00.png"]
		self.image["bg"]=self.pic["bg.png"]

		self.image["bg1"]=self.pic["stg3bg.png"]
		self.image["bg2"]=self.pic["stg3bg2.png"]
		self.image["bg3"]=self.pic["stg3bg3.png"]
		self.image["bg4"]=self.pic["stg3bg4.png"]
#		self.image["bg5"]=self.pic["eff02.png"]
		self.image["bg5"]=pygame.image.load("pic\\eff02.png").convert()


		self.pic["reimu.png"]=pygame.image.load("pic\\reimu.png").convert()
		self.pic["reimu.png"].set_colorkey((0,0,0))
		self.pic["cirno.png"]=pygame.image.load("pic\\cirno.png").convert()
		self.pic["cirno.png"].set_colorkey((0,0,0))
		self.image["reimu"]=self.pic["reimu.png"].subsurface((0,0,128,256))
		self.image["cirno"]=self.pic["cirno.png"].subsurface((0,0,128,256))


		tmp=Rect(0,0,16,16)
		tp=self.pic["bullet1.png"]
		self.image["bullet1"]=[]
		for i in range(12):
			self.image["bullet1"].append([])
			for j in range(16):
				self.image["bullet1"][i].append(tp.subsurface(tmp))
				tmp.left+=16
			tmp.top+=16
			tmp.left-=256
		tmp=Rect(0,240,8,8)
		self.image["bullet1"].append([])
		for i in range(16):
			self.image["bullet1"][12].append(tp.subsurface(tmp))
			tmp.left+=8
			if(i==7):
				tmp=Rect(0,248,8,8)

		tmp=Rect(0,0,32,32)
		tp=self.pic["bullet2.png"]
		self.image["bullet2"]=[]
		for i in range(6):
			self.image["bullet2"].append([])
			for j in range(8):
				self.image["bullet2"][i].append(tp.subsurface(tmp))
				tmp.left+=32
			tmp.top+=32
			tmp.left-=256
		tmp=Rect(0,192,64,64)
		self.image["bullet2"].append([])
		for i in range(4):
			self.image["bullet2"][6].append(tp.subsurface(tmp))
			tmp.left+=64

		tmp=Rect(0,0,32,32)
		tp=self.pic["resource.png"]
		self.image["resource"]=[]
		for i in range(5):
			self.image["resource"].append([])
			for j in range(4):
				self.image["resource"][i].append(tp.subsurface(tmp))
				tmp.left+=32
			tmp.top+=32
			tmp.left-=128



		self.anime["bubble"]=[]
		tp=self.pic["bubble.png"]
		tmp=tp.get_rect()
		tmp.width/=8
		tmpw=tmp.width
		for i in range(8):
			self.anime["bubble"].append(tp.subsurface(tmp))
			tmp.left+=tmpw


		self.anime["cirno"]=[[],[],[]] #stay left right
		tp=self.pic["cirno-fly.png"]
		tmp=tp.get_rect()
		tmp.width/=4
		tmpw=tmp.width
		for i in range(4):
			self.anime["cirno"][0].append(tp.subsurface(tmp))
			tmp.left+=tmpw
		tp=self.pic["cirno-left.png"]
		tmp=tp.get_rect()
		tmp.width/=4
		tmpw=tmp.width
		for i in range(4):
			self.anime["cirno"][1].append(tp.subsurface(tmp))
			tmp.left+=tmpw
		tp=self.pic["cirno-right.png"]
		tmp=tp.get_rect()
		tmp.width/=4
		tmpw=tmp.width
		for i in range(4):
			self.anime["cirno"][2].append(tp.subsurface(tmp))
			tmp.left+=tmpw

		tmp=Rect(0,0,32,32)
		tp=self.pic["enemy.png"]
		self.anime["enemy"]=[]
		for i in range(8):
			self.anime["enemy"].append([[],[],[],[],[]])
			for j in range(3):
				for k in range(4):
					self.anime["enemy"][i][j].append(tp.subsurface(tmp))
					tmp.left+=32
			for j in range(2):
				for k in range(4):
					self.anime["enemy"][i][j+3].append(pygame.transform.flip(self.anime["enemy"][i][j][k],True,False))
			tmp.top+=32
			tmp.left-=384
			if i == 3:
				tmp.topleft=(0,256)

		self.anime["enemy"].append([])
		tmp=Rect(0,384,64,64)
		for i in range(5):
			self.anime["enemy"][8].append(tp.subsurface(tmp))
			tmp.left+=64
			
		tmp=Rect(64,128,32,32)
		self.anime["enemy"].append(tp.subsurface(tmp))
		tmp=Rect(96,128,32,32)
		self.anime["enemy"].append(tp.subsurface(tmp))
		tmp=Rect(64,160,32,32)
		self.anime["enemy"].append(tp.subsurface(tmp))
		tmp=Rect(64,160,32,32)
		self.anime["enemy"].append(tp.subsurface(tmp))

		tp=self.pic["enemy2.png"]
		self.anime["enemy2"]=[]
		tmp=Rect(0,0,32,32)
		for i in range(4):
			self.anime["enemy2"].append([])
			for j in range(8):
				self.anime["enemy2"][i].append(tp.subsurface(tmp))
				tmp.left+=32
			tmp.left=0
			tmp.top+=32



		tmp=Rect(0,0,32,48)
		tp=self.pic["ziji.png"]
		self.anime["ziji"]=[[],[],[]] #stay left right point tama bullet1 bullet2
		for i in range(3):
			for j in range(8):
				self.anime["ziji"][i].append(tp.subsurface(tmp))
				tmp.left+=32
			tmp.top+=48
			tmp.left-=256
		tmp=Rect(0,16,64,64)
		self.anime["ziji"].append(self.pic["point.png"].subsurface(tmp))
		tmp=Rect(96,144,16,16)
		self.anime["ziji"].append(tp.subsurface(tmp))
		tmp=Rect(0,176,64,16)
		self.anime["ziji"].append(tp.subsurface(tmp))
		tmp=Rect(64,176,64,16)
		self.anime["ziji"].append(tp.subsurface(tmp))




		self.se={}
		se_name=[
			"se_bonus.wav",
			"se_cardget.wav",
			"se_cat00.wav",
			"se_nep00.wav",
			"se_select00.wav",
			"se_pldead00.wav",
			"se_cancel00.wav",
			"se_damage00.wav",
			"se_pause.wav",
			"se_extend.wav",
		]
		se_myname=[
			"bonus",
			"cardget",
			"connect",
			"wudi",
			"select",
			"miss",
			"cancel",
			"damage",
			"pause",
			"extend"
		]
		for i in range(len(se_name)):
			self.se[se_myname[i]]=pygame.mixer.Sound("se\\"+se_name[i])
