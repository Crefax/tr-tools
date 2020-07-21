#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py_compile

var = 1 
while var == 1 :

	print("""
\033[92m1) Port Tarama
2) Zaafiyet
3) VPN Kontrol
4) WordPress Tarama
5) Mac değiştirme
6) Güvenlik Duvarı tespit

9) Python derleyici
0) Setup & Update
00) Çıkış
	""")
	anaislem = raw_input("İşlem no seçin: ")

	if(anaislem == "1"):
		os.system("clear")
		os.system("figlet Port Tarama")

		print ("""
1) Hızlı tarama
2) Servis ve Versiyon Bilgisi
3) İşletim Sistemi Bilgisi

Bu Program nmap aracını kullanarak port tarama vb işlemleri yapar.
		""")

		islemno = raw_input("İşlem girin: ")

		if(islemno == "1"):
			hedefip = raw_input("Hedef ip girin: ")
			os.system("nmap " + hedefip)

		elif(islemno == "2"):
			hedefip = raw_input("Hedef ip girin: ")
			os.system("nmap -sS -sV " + hedefip)

		elif(islemno == "3"):
			hedefip = raw_input("Hedef ip girin: ")
			os.system("nmap -O " + hedefip)

	elif(anaislem == "2"):
		os.system("apt-get install figlet")
		os.system("clear")
		os.system("figlet Zaafiyet Tespit")
		print("""
Bu Programda nikto aracı ile zaafiyet tespiti yapılıyor.
		""")

		hedefip = raw_input("Hedef ip girin: ")
		os.system("nikto -h " + hedefip)


	elif(anaislem == "3"):
		os.system("clear")
		os.system("figlet VPN Kontrol")
		print("""
VPN Kontrol Programına Hoş Geldiniz.
		""")

		hedefip = raw_input("Hedef İp Girin: ")

		os.system("ike-scan " + hedefip)
	elif(anaislem == "4"):
		os.system("clear")
		os.system("figlet WORDPRESS TARAMA")
		print("""
Wordpress Tarama Programına Hoş Geldiniz. 

1) Hızlı Tarama
2) Eklenti Tarama
3) Tema Tarama
4) Yönetici Kullanıcı Adı Tarama
		""")

		islemno = raw_input("İşlem Numarasını Girin: ")

		if(islemno=="1"):
			site = raw_input("Site Adresi Girin: ")
			os.system("wpscan --url " + site)

		elif(islemno == "2"):
			site = raw_input("Site Adresi Girin: ")
			os.system("wpscan --url " + site + " --enumerate p")

		elif(islemno == "3"):
			site = raw_input("Site Adresi Girin: ")
			os.system("wpscan --url " + site + " --enumerate t")

		elif(islemno == "4"):
			site = raw_input("Site Adresi Girin: ")
			os.system("wpscan --url " + site + " --enumerate u")

		else:
			print("Hatalı Seçim Yaptınız. Program Kapatılıyor.")

	elif(anaislem == "5"):
		os.system("clear")
		os.system("figlet MAC Degistirme")
		print("""
MAC Adres Değiştirme Programına Hoş Geldiniz. 

1) MAC Adresi Random Belirle
2) MAC Adresi Elle Belirle
3) MAC Adresi Orijinale Döndür
		""")

		islemno = raw_input("İşlem No Girin: ")

		if(islemno=="1"):
			os.system("ifconfig eth0 down")
			os.system("macchanger -r eth0")
			os.system("ifconfig eth0 up")
			print("\033[92mYeni MAC Adresi Random Belirlendi.")


		if(islemno=="2"):
			macadres = raw_input("Yeni MAC Adres Girin: ")
			os.system("ifconfig eth0 down")
			os.system("macchanger --mac " + macadres + " eth0")
			os.system("ifconfig eth0 up")
			print("\033[92mYeni MAC Adresi Elle Belirlendi.")

		if(islemno=="3"):
			os.system("ifconfig eth0 down")
			os.system("macchanger -p eth0")
			os.system("ifconfig eth0 up")
			print("\033[92mMAC Adresi Orijinale Döndürüldü.")
	elif(anaislem == "9"):
		import os
		os.system("clear")
		os.system("figlet Derleyici")

		print("""
Python dosyalarınızı derleyerek kodlarını okunmaz hale getirin py uznatısını pyc olarak değiştirir.
		""")

		derle = raw_input("Dosyanızın İsmini Girin: ")

		py_compile.compile(derle)

	elif(anaislem == "6"):
		os.system("clear")
		os.system("figlet Guvenlik Duvari Tespit")
		print("""

		""")

		site = raw_input("Site Adresini Girin: ")
		os.system("wafw00f " + site)
	elif(anaislem == "7"):
		os.system("clear")
		os.system("figlet Port Kaba Kuvvet")
		print("""
		1) FTP
		2) SSH
		3) Telnet
		4) HTTP
		5) SMB
		6) RDP
		7) MySQL
		""")

		islemno = raw_input("İşlem No Girin: ")
		hedefip = raw_input("Hedef İp Girin: ")
		kullaniciadi = raw_input("Kullanıcı Adı Dosya Yolu: ")
		sifre = raw_input("Sifrelerin Bulunduğu Dosya Yolu: ")

		if(islemno == "1"):
			os.system("ncrack -p 21 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

		if(islemno == "2"):
			os.system("ncrack -p 22 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

		if(islemno == "3"):
			os.system("ncrack -p 23 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)
		if(islemno == "4"):
			os.system("ncrack -p 80 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)
		if(islemno == "5"):
			os.system("ncrack -p 139 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)
		if(islemno == "6"):
			os.system("ncrack -p 3389 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)
		if(islemno == "7"):
			os.system("ncrack -p 3306 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)


	elif(anaislem == "0"):
		os.system("apt-get install figlet")
		os.system("apt-get install nikto")
		os.system("apt-get install wpscan")
		os.system("apt-get install nmap")
		os.system("apt-get install wafw00f")
		os.system("git clone https://github.com/Crefax/tr-tools.git")
		os.system("cp tr-tools/crefax.py .")
		os.system("rm -r tr-tools")
	elif(anaislem == "00"):
		break
