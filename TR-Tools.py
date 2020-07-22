#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py_compile

var = 1 
while var == 1 :
	os.system("clear")
	print("\033[31m")
	os.system("figlet TR-Tools by Crefax")
	print("""
\033[92m
1) Port İşlemleri
2) Web Saldırıları
3) Diğer

0) Setup & Update
00) Çıkış
-df) Daha fazla bilgi alın.
	""")
	kategori = raw_input("İşlem no seçin: ")
	if(kategori == "1"): #Port İşlemleri başlangıç
		os.system("figlet Port İşlemleri")
		print("""
1) Port Tarama
2) Port Kaba Kuvvet Saldırısı

		""")
		islem = raw_input("İşlem no seçin: ")
		if(islem == "1"):
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
		elif(islem == "2"):
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

	elif(kategori == "2"): #Web saldırıları başlangıç
		os.system("clear")
		os.system("figlet Web Attack tools")
		print("""
1) WebSitesi Zaafiyet Taraması
2) WebSitesi uzantı tespit
3) WebSitesi GÜvenlik Duvarı Tespit
4) VPN Kontrol
5) Wordpress Taraması
		""")		
		islem = raw_input("İşlem no girin: ")
		if(islem == "1"):
			os.system("clear")
			os.system("figlet Zaafiyet Tespit")
			print("""
Bu Programda nikto aracı ile zaafiyet tespiti yapılıyor.
			""")

			hedefip = raw_input("Hedef ip girin: ")
			os.system("nikto -h " + hedefip)
		elif(islem == "2"):
			os.system("clear")
			os.system("figlet Dirb")
			dirburl = raw_input("Taranacak web sitesinin urlsi: ")
			os.system("dirb " + dirburl)
		elif(islem == "3"):
			os.system("clear")
			os.system("figlet Guvenlik Duvari Tespit")
			site = raw_input("Site Adresini Girin: ")
			os.system("wafw00f " + site)
		elif(islem == "4"):
			os.system("clear")
			os.system("figlet VPN Kontrol")
			print("""
	VPN Kontrol Programına Hoş Geldiniz.
			""")

			hedefip = raw_input("Hedef İp Girin: ")

			os.system("ike-scan " + hedefip)
		elif(islem == "5"):
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


	elif(kategori == "3"):
		os.system("clear")
		os.system("figlet Diğer")

		print("""
1) Mac Adresi değiştirme
2) Python derleyici
		""")
		islem = raw_input("İşlem no girin: ")

		if(islem == "1"):
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

		elif(islem == "2"):
			os.system("clear")
			os.system("figlet Derleyici")

			print("""
	Python dosyalarınızı derleyerek kodlarını okunmaz hale getirin py uznatısını pyc olarak değiştirir.
			""")

			derle = raw_input("Dosyanızın İsmini Girin: ")

			py_compile.compile(derle)


	elif(kategori == "0"):
		os.system("apt-get install figlet")
		os.system("apt-get install nikto")
		os.system("apt-get install wpscan")
		os.system("apt-get install nmap")
		os.system("apt-get install wafw00f")
		os.system("git clone https://github.com/Crefax/tr-tools.git")
		os.system("cp tr-tools/tr-tools.py .")
		os.system("rm -r tr-tools")
	elif(kategori == "00"):
		break
	elif(kategori == "-df"):
		os.system("clear")
		print("""
-setup : sadece gerekli programları indirir. githubdan yeni indirdiyseniz gerekli olabilir.
-update : toolları günceller githubdan yeni aldıysanız ihtiyacınız yoktur.
-v : programın verion bilgisini gösterir.

		""")
		enter = raw_input("Geri dönmek için enter tuşuna basınız.")

	elif(kategori == "-v" or kategori == "-V"):
		os.system("clear")
		print("\033[96mTR-Tools version: 1.0.8")
		enter = raw_input("\033[96mGeri dönmek için enter tuşuna basınız.")
	elif(kategori == "-update"):
		os.system("clear")
		os.system("git clone https://github.com/Crefax/tr-tools.git")
		os.system("cp tr-tools/TR-Tools.py .")
		os.system("rm -r tr-tools")
		print("""\033[96mGüncelleme tamamlandı, çalışmayan tool var ise -setup ile gerekli programların kurulumunu yapabilirsin. veya 0 parametresi ile her ikisinide yapabilirsin.""")
		enter = raw_input("\033[96mGeri dönmek için enter tuşuna basınız.")
	elif(kategori == "-setup"):
		os.system("clear")
		os.system("apt-get install figlet")
		os.system("apt-get install nikto")
		os.system("apt-get install wpscan")
		os.system("apt-get install nmap")
		os.system("apt-get install wafw00f")
		print("\033[96mKurulum tamamlandı, Peki TR-Tools güncel mi ? -update ile güncelleyebilirsin.")
		enter = raw_input("\033[96mGeri dönmek için enter tuşuna basınız.")
