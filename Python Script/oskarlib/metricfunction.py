# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:13:45 2018

@author: Oskar
"""

from keras import backend as K


class RegMetric: #METRIC UNTUK KASUS REGRESI
	@staticmethod
	def R2(Y, Yhat): #RUMUS R2 R_SQUARED BACA DI https://en.wikipedia.org/wiki/Coefficient_of_determination
		SSres = K.sum(K.square(Y - Yhat))
		SSreg = K.sum(K.square(Yhat - K.mean(Y)))
		SStot = K.sum(K.square(Y - K.mean(Y))) 
		R2Score = 1 - (SSres/SStot)
		#R2Score = SSreg/SStot
		return R2Score