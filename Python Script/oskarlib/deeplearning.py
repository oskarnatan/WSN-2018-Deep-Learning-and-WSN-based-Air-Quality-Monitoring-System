"""
Created on Thu Nov 29 10:13:45 2018

@author: Oskar
"""

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Reshape, Flatten, Activation
from keras.layers.advanced_activations import LeakyReLU, PReLU
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization



class MLP: #MULTI LAYER PERCEPTRON
	@staticmethod
	def Wide(input, output):
		#DEFINE MODEL DAN INISIALISASI INPUT NEURON = JUMLAH ATRIBUT
		model = Sequential()
		model.add(Dense(25, input_dim=input, activation='relu')) #HIDDEN LAYER 1 dan INPUT LAYER
		model.add(Dense(output, activation='sigmoid')) #OUTPUT LAYER, JUMLAH NEURON = JUMLAH CLASS
		return model

	def Deep(input, output):
		#DEFINE MODEL DAN INISIALISASI INPUT NEURON = JUMLAH ATRIBUT
		model = Sequential()
		model.add(Dense(5, input_dim=input, activation='relu')) #HIDDEN LAYER 1 dan INPUT LAYER
		model.add(Dense(5, activation='relu')) #HIDDEN LAYER 2
		model.add(Dense(5, activation='relu')) #HIDDEN LAYER 3
		model.add(Dense(5, activation='relu')) #HIDDEN LAYER 4
		model.add(Dense(5, activation='relu')) #HIDDEN LAYER 5
		model.add(Dense(output, activation='sigmoid')) #OUTPUT LAYER, JUMLAH NEURON = JUMLAH CLASS
		return model

	def DeepWide(input, output):
		#DEFINE MODEL DAN INISIALISASI INPUT NEURON = JUMLAH ATRIBUT
		model = Sequential()
		model.add(Dense(25, input_dim=input, activation='relu')) #HIDDEN LAYER 1 dan INPUT LAYER
		model.add(Dense(25, activation='relu')) #HIDDEN LAYER 2
		model.add(Dense(25, activation='relu')) #HIDDEN LAYER 3
		model.add(Dense(25, activation='relu')) #HIDDEN LAYER 4
		model.add(Dense(25, activation='relu')) #HIDDEN LAYER 5
		model.add(Dense(output, activation='sigmoid')) #OUTPUT LAYER, JUMLAH NEURON = JUMLAH CLASS
		return model

	def Custom(input, output):
		#DEFINE MODEL DAN INISIALISASI INPUT NEURON = JUMLAH ATRIBUT
		model = Sequential()
		model.add(Dense(10, input_dim=input)) #HIDDEN LAYER 1 dan INPUT LAYER
		model.add(LeakyReLU())
		model.add(Dense(20, activation='relu')) #HIDDEN LAYER 2
		model.add(BatchNormalization())
		model.add(Dense(30)) #HIDDEN LAYER 3
		model.add(LeakyReLU())
		model.add(Dropout(0.25))
		model.add(Dense(30, activation='relu')) #HIDDEN LAYER 4
		model.add(BatchNormalization())
		model.add(Dense(20)) #HIDDEN LAYER 5
		model.add(LeakyReLU())
		model.add(Dense(10, activation='relu')) #HIDDEN LAYER 6
		model.add(BatchNormalization())
		model.add(Dropout(0.25))
		model.add(Dense(output, activation='sigmoid')) #OUTPUT LAYER, JUMLAH NEURON = JUMLAH CLASS
		return model


		
class CNN: #CONVOLUTIONAL NEURAL NETWORK / CONVNET
	@staticmethod
	def LeNet(inputw, inputh, inputd, output):
		# INISIALISASI
		model = Sequential()
		inputShape = (inputh, inputw, inputd)
 		#URUTAN R-G-B CHANNEL
		if K.image_data_format() == "channels_first":
			inputShape = (inputd, inputh, inputw) #UKURAN INPUT LAYER
 		#CONV1 -> ACTIVATE -> POOLING1
		model.add(Conv2D(20, (5, 5), padding="same", input_shape=inputShape))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
		#CONV2 -> ACTIVATE -> POOLING2
		model.add(Conv2D(50, (5, 5), padding="same"))
		model.add(Activation("relu"))
		model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
		#HIDDEN LAYER 1
		model.add(Flatten())
		model.add(Dense(500))
		model.add(Activation("relu"))
		#OUTPUT LAYER
		model.add(Dense(output)) #OUTPUT LAYER, JUMLAH NEURON = JUMLAH CLASS
		model.add(Activation("softmax"))
		return model
	
	def VGGNet(inputw, inputh, inputd, output):
		# INISIALISASI
		model = Sequential()
		inputShape = (inputh, inputw, inputd)
		chanDim = -1
		#URUTAN R-G-B CHANNEL
		if K.image_data_format() == "channels_first":
			inputShape = (inputd, inputh, inputw) #UKURAN INPUT LAYER
			chanDim = 1
		#1 (CONV -> ACTIVATE -> NORMALIZE) x2 -> POOL -> DROPOUT
		model.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(32, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(3, 3)))
		model.add(Dropout(0.25))
		#2 (CONV -> ACTIVATE -> NORMALIZE) x2 -> POOL -> DROPOUT
		model.add(Conv2D(64, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(64, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(3, 3)))
		model.add(Dropout(0.25))
		#3 (CONV -> ACTIVATE -> NORMALIZE) x3 -> POOL -> DROPOUT
		model.add(Conv2D(128, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(128, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(128, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))
		#4 CONV -> ACTIVATE -> NORMALIZE) x3 -> POOL -> DROPOUT
		model.add(Conv2D(256, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(256, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(256, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))
		#5 CONV -> ACTIVATE -> NORMALIZE) x3 -> POOL -> DROPOUT
		model.add(Conv2D(512, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(512, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(512, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))
        # 3 HIDDEN LAYER (RELU, NORMALIZE) -> DROPOUT
		model.add(Flatten())
		model.add(Dense(1024))
		model.add(Activation("relu"))
		model.add(BatchNormalization())
		model.add(Dense(2048))
		model.add(Activation("relu"))
		model.add(BatchNormalization())
		model.add(Dense(512))
		model.add(Activation("relu"))
		model.add(BatchNormalization())
		model.add(Dropout(0.5))
		#OUTPUT LAYER
		model.add(Dense(output)) #OUTPUT LAYER, JUMLAH NEURON = JUMLAH CLASS
		model.add(Activation("softmax"))
		return model
	
	##########============ CUSTOM ARCHITECTURE, STUDENT EXCHANGE T.U.T. JAPAN 2018 ============##########
	def OsNet(inputw, inputh, inputd, output): 
		# INISIALISASI
		model = Sequential()
		inputShape = (inputh, inputw, inputd) 
		chanDim = -1
 		#URUTAN R-G-B CHANNEL
		if K.image_data_format() == "channels_first":
			inputShape = (inputd, inputh, inputw) #UKURAN INPUT LAYER
			chanDim = 1
		#1 (CONV -> ACTIVATE -> NORMALIZE) x1 -> POOL -> DROPOUT
		model.add(Conv2D(50, (2, 2), padding="same", input_shape=inputShape))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.2))
		#2 (CONV -> ACTIVATE -> NORMALIZE) x2 -> POOL -> DROPOUT
		model.add(Conv2D(100, (2, 2), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(100, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(3, 3)))
		model.add(Dropout(0.25))
        #3 (CONV -> ACTIVATE -> NORMALIZE) x3 -> POOL -> DROPOUT
		model.add(Conv2D(150, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(150, (2, 2), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(150, (3, 3), padding="same"))
		model.add(Activation("relu"))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(3, 3)))
		model.add(Dropout(0.3))
        # 3 HIDDEN LAYER (RELU, NORMALIZE) -> DROPOUT
		model.add(Flatten())
		model.add(Dense(100))
		model.add(Activation("relu"))
		model.add(BatchNormalization())
		model.add(Dense(200))
		model.add(Activation("relu"))
		model.add(BatchNormalization())
		model.add(Dense(50))
		model.add(Activation("relu"))
		model.add(BatchNormalization())
		model.add(Dropout(0.4))
 		# OUTPUT LAYER
		model.add(Dense(output)) #OUTPUT LAYER, JUMLAH NEURON = JUMLAH CLASS
		model.add(Activation("softmax"))
		return model


		
class DNN: #DEEP NEURAL NETWORK, DEEP LEARNING, FOR THESIS NEEDS B-)
	@staticmethod
	#FULL MLP SAJA,
	def Regressor(input, output): 
		#DEFINE MODEL DAN INISIALISASI INPUT NEURON = JUMLAH ATRIBUT
		model = Sequential()
		model.add(Dense(20, input_dim=input, activation='relu')) #HIDDEN LAYER 1 dan INPUT LAYER
		model.add(Dense(30, activation='relu')) #HIDDEN LAYER 2
		model.add(Dense(40, activation='relu')) #HIDDEN LAYER 3
		model.add(Dense(50, activation='relu')) #HIDDEN LAYER 4
		model.add(Dense(40, activation='relu')) #HIDDEN LAYER 5
		model.add(Dense(30, activation='relu')) #HIDDEN LAYER 6
		model.add(Dense(20, activation='relu')) #HIDDEN LAYER 7
		model.add(Dense(10, activation='relu')) #HIDDEN LAYER 8
		model.add(Dense(output, activation='linear')) #OUTPUT LAYER,  OUTPUT NEURON DIBUAT LINEAR / ACTIVATION NONE, SUPAYA LINEAR
		return model
	
	
	#MIX ARCHITECTURE, (EXPAND NETWORK + RESHAPE + CONVNET + FLATTEN) x2 + FULLY CONNECTED LAYER MLP DIAKHIR
	def Classifier(input, output):
		#DEFINE MODEL DAN INISIALISASI INPUT LAYER = JUMLAH ATRIBUT
		model = Sequential()
		model.add(Dense(100, input_dim=input)) #HIDDEN LAYER 1 dan INPUT LAYER

		#EXPAND NETWORK /"EXTRACT FEATURE" DENGAN MENAMBAH BEBERAPA HIDDEN LAYER
		model.add(Dense(300)) #HIDDEN LAYER 2
		model.add(Dense(900)) #HIDDEN LAYER 3
		model.add(Activation("linear"))

		#UBAH DIMENSI NETWORK DARI 1D KE 2D
		model.add(Reshape((30, 30, 1)))

		#PROSES CNN (CONVOLUTIONAL NEURAT NETWORK)
		#(CONV -> ACTIVATE -> NORMALIZE) x2 -> POOLING -> DROP
		model.add(Conv2D(100, kernel_size=(3, 3))) #HIDDEN LAYER 4
		model.add(LeakyReLU(alpha=0.1))
		model.add(BatchNormalization())
		model.add(Conv2D(25, kernel_size=(2, 2))) #HIDDEN LAYER 5
		model.add(LeakyReLU(alpha=0.1))
		model.add(BatchNormalization())
		model.add(MaxPooling2D(pool_size=(2, 2))) #HIDDEN LAYER 6
		model.add(Dropout(0.3))

		#UBAH DIMENSI NETWORK DARI 2D KE 1D
		model.add(Flatten())

		#EXPAND NETWORK LAGI /"EXTRACT FEATURE" DENGAN MENAMBAH BEBERAPA HIDDEN LAYER
		model.add(Dense(100)) #HIDDEN LAYER 7
		model.add(Dense(200)) #HIDDEN LAYER 8
		model.add(Dense(400)) #HIDDEN LAYER 9
		model.add(Activation("linear"))

		#UBAH DIMENSI NETWORK DARI 1D KE 2D
		model.add(Reshape((20, 20, 1)))

		#PROSES CNN LAGI (CONVOLUTIONAL NEURAT NETWORK)
		#(CONV -> ACTIVATE -> NORMALIZE) x2 -> POOLING -> DROP
		model.add(Conv2D(100, kernel_size=(2, 2))) #HIDDEN LAYER 10
		model.add(LeakyReLU(alpha=0.1))
		model.add(BatchNormalization())
		model.add(Conv2D(25, kernel_size=(2, 2))) #HIDDEN LAYER 11
		model.add(LeakyReLU(alpha=0.1))
		model.add(BatchNormalization())
		model.add(MaxPooling2D(pool_size=(2, 2))) #HIDDEN LAYER 12
		model.add(Dropout(0.3))

		#UBAH DIMENSI NETWORK DARI 2D KE 1D
		model.add(Flatten())

		#FULLY CONNECTED LAYER, MLP
		model.add(Dense(15, activation='relu')) #HIDDEN LAYER 13
		model.add(Dense(30, activation='relu')) #HIDDEN LAYER 14
		model.add(Dense(20)) #HIDDEN LAYER 15
		model.add(LeakyReLU(alpha=0.01))
		model.add(Dense(20, activation='relu')) #HIDDEN LAYER 16
		model.add(Dense(30, activation='relu')) #HIDDEN LAYER 17
		model.add(Dense(15)) #HIDDEN LAYER 18
		model.add(LeakyReLU(alpha=0.01))

		#OUTPUT LAYER, AKHIR
		model.add(Dense(output, activation='sigmoid')) #OUTPUT LAYER
		
		return model

	#========================COBA - COBA UNTUK TUGAS WSN 2018========================#
	#########################CONVNET UNTUK REGRESI#################
	def RegressorV2(input, output):
		#DEFINE MODEL DAN INISIALISASI INPUT LAYER = JUMLAH ATRIBUT
		model = Sequential()
		model.add(Dense(100, input_dim=input)) #HIDDEN LAYER 1 dan INPUT LAYER

		#EXPAND NETWORK /"EXTRACT FEATURE" DENGAN MENAMBAH BEBERAPA HIDDEN LAYER
		model.add(Dense(300)) #HIDDEN LAYER 2
		model.add(Dense(900)) #HIDDEN LAYER 3
		model.add(Activation("linear"))

		#UBAH DIMENSI NETWORK DARI 1D KE 2D
		model.add(Reshape((30, 30, 1)))

		#PROSES CNN (CONVOLUTIONAL NEURAT NETWORK)
		#(CONV -> ACTIVATE -> NORMALIZE) x2 -> POOLING -> DROP
		model.add(Conv2D(100, kernel_size=(3, 3))) #HIDDEN LAYER 4
		model.add(LeakyReLU(alpha=0.1))
		model.add(BatchNormalization())
		model.add(Conv2D(25, kernel_size=(2, 2))) #HIDDEN LAYER 5
		model.add(LeakyReLU(alpha=0.1))
		model.add(BatchNormalization())
		model.add(MaxPooling2D(pool_size=(2, 2))) #HIDDEN LAYER 6
		model.add(Dropout(0.3))

		#UBAH DIMENSI NETWORK DARI 2D KE 1D
		model.add(Flatten())

		#EXPAND NETWORK LAGI /"EXTRACT FEATURE" DENGAN MENAMBAH BEBERAPA HIDDEN LAYER
		model.add(Dense(100)) #HIDDEN LAYER 7
		model.add(Dense(200)) #HIDDEN LAYER 8
		model.add(Dense(400)) #HIDDEN LAYER 9
		model.add(Activation("linear"))

		#UBAH DIMENSI NETWORK DARI 1D KE 2D
		model.add(Reshape((20, 20, 1)))

		#PROSES CNN LAGI (CONVOLUTIONAL NEURAT NETWORK)
		#(CONV -> ACTIVATE -> NORMALIZE) x2 -> POOLING -> DROP
		model.add(Conv2D(100, kernel_size=(2, 2))) #HIDDEN LAYER 10
		model.add(LeakyReLU(alpha=0.1))
		model.add(BatchNormalization())
		model.add(Conv2D(25, kernel_size=(2, 2))) #HIDDEN LAYER 11
		model.add(LeakyReLU(alpha=0.1))
		model.add(BatchNormalization())
		model.add(MaxPooling2D(pool_size=(2, 2))) #HIDDEN LAYER 12
		model.add(Dropout(0.3))

		#UBAH DIMENSI NETWORK DARI 2D KE 1D
		model.add(Flatten())

		#FULLY CONNECTED LAYER, MLP
		model.add(Dense(15, activation='relu')) #HIDDEN LAYER 13
		model.add(Dense(30, activation='relu')) #HIDDEN LAYER 14
		model.add(Dense(20)) #HIDDEN LAYER 15
		model.add(LeakyReLU(alpha=0.01))
		model.add(Dense(20, activation='relu')) #HIDDEN LAYER 16
		model.add(Dense(30, activation='relu')) #HIDDEN LAYER 17
		model.add(Dense(15)) #HIDDEN LAYER 18
		model.add(LeakyReLU(alpha=0.01))

		#OUTPUT LAYER, AKHIR
		model.add(Dense(output, activation='linear')) #OUTPUT LAYER
		
		return model

		
class Autoencoder:
	@staticmethod
	def decoder(input, output):
		#SINGLE PERCEPTRON ONLY
		model = Sequential()
		model.add(Dense(1, input_dim=3, activation='relu')) 
		return model





































