"""
Created on Wed Nov 21 12:37:58 2018

@author: Oskar
"""

import os
import threading
import urllib.request
import serial
import bluetooth
import sys
import time
import pandas as pd
import numpy as np
from keras.models import load_model

pewaktu = 30
temp = [0 for x in range(3)]
hum = [0 for x in range(3)]
xxxxx = 0

def foreverLoop():
	global pewaktu
	threading.Timer(pewaktu,foreverLoop).start()
	sNode0toSink()
	sNode1toSink()
	sNode2toSink()
	#PC2Mega2PC()
	Process_PC2Web()

	
def recvall(socke, n):
    #AGREGASI DATA YANG DITERIMA BLUETOOTH
    datas = b''
    while len(datas) < n:
        packet = socke.recv(n - len(datas))
        if not packet:
            return None
        datas += packet
    return datas

	
def sNode0toSink():
	print("\n===============Scheduling Retrive Data dari Node 0==================\n")
	
	global temp
	global hum
	
	bd_addr = "00:28:13:00:25:C9" #bluetooth 0
	port = 1
	sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	sock.connect((bd_addr, port))
	print('Connected to Node 0')
	#sock.settimeout(1.0)
	#KIRIM DATA, 
	print('Send Command to Node 0')
	sock.send("K0")
	#TERIMA DATA
	#devicedata = sock.recv(1024) #TERIMA 20 CHAR
	data = recvall(sock, 12) #TERIMA 12 CHAR DARI SOCKET
	devicedata = data.decode() #Decode ke string
	print("Data Node 0:", devicedata)
	sock.close() #CLOSE KONEKSI
	#DATA DIPARSE, HAPUS HEAD DAN TAIL, DAN DICONVERT KE FLOAT
	parsedata = devicedata.split("X")
	del parsedata[2] #DELETE TAIL DATA
	parsedata = list(map(float, parsedata)) #CONVERT TO FLOAT
	print("Parse Data:", parsedata)
	#ASSIGN DATA KE VARIABEL TERKAIT
	temp[0] = parsedata[0]
	hum[0] = parsedata[1]
	print("temp0 :", temp[0])
	print("hum0  :", hum[0])
	
	print("\n====================================================================\n\n")

def sNode1toSink():
	print("\n===============Scheduling Retrive Data dari Node 1==================\n")
	
	global temp
	global hum
		
	bd_addr = "98:D3:61:F5:E3:49" #bluetooth 1
	port = 1
	sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	sock.connect((bd_addr, port))
	print('Connected to Node 1')
	#sock.settimeout(1.0)
	#KIRIM DATA, 
	print('Send Command to Node 1')
	sock.send("K1")
	#TERIMA DATA
	#devicedata = sock.recv(1024) #TERIMA 20 CHAR
	data = recvall(sock, 12) #TERIMA 12 CHAR DARI SOCKET
	devicedata = data.decode() #Decode ke string
	print("Data Node 1:", devicedata)
	sock.close() #CLOSE KONEKSI
	#DATA DIPARSE, HAPUS HEAD DAN TAIL, DAN DICONVERT KE FLOAT
	parsedata = devicedata.split("X")
	del parsedata[2] #DELETE TAIL DATA
	parsedata = list(map(float, parsedata)) #CONVERT TO FLOAT
	print("Parse Data:", parsedata)
	#ASSIGN DATA KE VARIABEL TERKAIT
	temp[1] = parsedata[0]
	hum[1] = parsedata[1]
	print("temp1 :", temp[1])
	print("hum1  :", hum[1])
	
	print("\n====================================================================\n\n")


def sNode2toSink():
	print("\n===============Scheduling Retrive Data dari Node 2==================\n")
	
	global temp
	global hum
	
	bd_addr = "98:D3:31:F9:4E:16" #bluetooth 2
	port = 1
	sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	sock.connect((bd_addr, port))
	print('Connected to Node 2')
	#sock.settimeout(1.0)
	#KIRIM DATA, 
	print('Send Command to Node 2')
	sock.send("K2")
	#TERIMA DATA
	#devicedata = sock.recv(1024) #TERIMA 20 CHAR
	data = recvall(sock, 12) #TERIMA 12 CHAR DARI SOCKET
	devicedata = data.decode() #Decode ke string
	print("Data Node 2:", devicedata)
	sock.close() #CLOSE KONEKSI
	#DATA DIPARSE, HAPUS HEAD DAN TAIL, DAN DICONVERT KE FLOAT
	parsedata = devicedata.split("X")
	del parsedata[2] #DELETE TAIL DATA
	parsedata = list(map(float, parsedata)) #CONVERT TO FLOAT
	print("Parse Data:", parsedata)
	#ASSIGN DATA KE VARIABEL TERKAIT
	temp[2] = parsedata[0]
	hum[2] = parsedata[1]
	print("temp2 :", temp[2])
	print("hum2  :", hum[2])
	
	print("\n====================================================================\n\n")
	
	
def PC2Mega2PC():
	print("\n===============Scheduling Retrive Data dari Arduino=================\n")
	
	#INISIALISASI VARIABEL GLOBAL
	global parsedata
	
	PortMega=serial.Serial('COM5', 9600)
	time.sleep(2)
	commandMega = "X"
	print("PC2Mega, PC Command = "+commandMega)
	PortMega.write(commandMega.encode())
	print("Mega2PC.......Read Data")
	devicedata = PortMega.readline()
	devicedata = str(devicedata)
	PortMega.close()
	#DATA INPUT DARI DEVICE
	print("Input Device Data:", devicedata)
	
	#DATA DIPARSE, HAPUS HEAD DAN TAIL, DAN DICONVERT KE FLOAT
	parsedata = devicedata.split("X")
	del parsedata[0] #DELETE HEAD DATA
	del parsedata[6] #DELETE TAIL DATA
	parsedata = list(map(float, parsedata)) #CONVERT TO FLOAT
	print("Parse Data:", parsedata)
	
	print("\n====================================================================\n\n")

	
def Process_PC2Web():
	print("\n===================Process Data -> Kirim ke Web=====================\n")
	
	#INISIALISASI VARIABEL GLOBAL
	global xxxxx
	global model
	global temp
	global hum
	global pewaktu
	
	#AMBIL RATA2 TEMPERATURE DAN HUMIDITY SERTA BUAT ARRAY UNTUK PROCESSING
	Temperature = np.mean(temp)
	Humidity = np.mean(hum)
	finaldata = [0 for x in range(2)]
	finaldata[0] = Temperature
	finaldata[1] = Humidity
	print("Average Data:", finaldata)

	#LOAD DATASET DAN AMBIL NILAI MAX-MIN DARI TIAP ATRIBUT
	dataset = pd.read_excel("dataset\AirQualityUCI.xlsx")
	maxATB = dataset.max()
	minATB = dataset.min()

	#MIN MAX SCALER
	X = [0 for i in range(len(finaldata))]
	for i in range(len(finaldata)):
		if ((maxATB[i] - minATB[i]) == 0):
			X[i] = 0
		else:
			X[i] = (finaldata[i] - minATB[i]) / (maxATB[i] - minATB[i])
	print("Normalisasi Data:", X)

	#RESHAPE DULU SEBELUM MASUK NETWORK
	X = np.reshape(X, (1, -1)) #RESHAPE 2D MATRIX DENGAN 1 SAMPLE, JIKA 1 FITUR PAKAI (-1, 1)
	print("Reshape Data:", X)

	#LOAD MODEL
	print("LOAD DNN MODEL DAN MULAI PROCESS....")
	if (xxxxx==0):
		xxxxx = 1
		model = load_model("fixmodel\AQreg.h5")

	#PREDIKSI CO / ESTIMASI
	Ypred = model.predict(X)
	Y = Ypred[0][0]
	print("Estimasi Nilai CO:", Y)

	#KLASIFIKASI KONDISI UDARA BAGUS / TIDAK
	if (Y < 5):
		Note = "KONDISI_UDARA_BAGUS"
		pewaktu = 40
	else:
		Note = "KONDISI_UDARA_TIDAK_BAGUS"
		pewaktu = 20
	print("Penilaian Kondisi udara:", Note)

	#SEND DATA TO WEB
	print("Send Data To Web oskarnatan.pasca.student.pens.ac.id/WSN2018")
	print("Temperature:", Temperature)
	print("Humidity:", Humidity)
	print("Estimasi CO:", Y)
	print("Note:", Note)
	print("Ambil data lagi dalam waktu:", pewaktu, "detik")
	#Note = "-UJI_COBA_SISTEM-"
	urllib.request.urlopen("http://oskarnatan.pasca.student.pens.ac.id/WSN2018/add_data.php?Temperature="+str(Temperature)+"&Humidity="+str(Humidity)+"&CO="+str(Y)+"&Note="+Note).read()

	print("\n====================================================================\n\n")



foreverLoop()







