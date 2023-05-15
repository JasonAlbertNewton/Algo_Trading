import pandas as pd 
import numpy as np

#check with RSI strategies
class RSI:
	
	def __init__(self ,data, time_slot_one):
		self.data = data
		self.time_slot_one = time_slot_one

	def RSI_calc(self):
		data_close = self.data['Close']
		self.time_slot_one
		#test the data set is large enough or not		
		if(data_close.shape[0] < self.time_slot_one):
			return -1 
		
		#do a loop get the first time_slot_one_data Umean and Dmean 		
		
			
		#do a loop
			#seperate the data into the time slot		
	
			#caluclate Umean 
			#calcalute Dmean 	
			


	def RSI_percentage_change(self, dt1 , dt2):
		return (dt2-dt1)/dt1*100
		 

#UNIT TEST
if __name__ == "__main__":
	data = pd.read_csv('save.csv')
	try:
		RSI=RSI(data , 10)
		print("Pass: RSI class insert .... .... ....")
	except:
		print("Fail: RSI class insert .... .... ....")
			
	try:
		time_slot_one = 20
		RSI.time_slot_one=time_slot_one
		print("Pass: RSI change time slot pass .... .... ....")
	except:
		print("Fail: RSI change tiem slot fail .... .... ....")
	try:
		time_slot_one = 1000000
		RSI.time_slot_one=time_slot_one
		test=RSI.RSI_calc()	
		if(test==-1):
			print("Pass: RSI HUGE NUMBER TEST.... .... ....")
		else: 
			print("Fail: RSI HUGE NUMBER TEST.... .... ....")
	except:
		print ("Fail: RSI HUGE NUMBER TIME SLOT SETTING .... .... ....")
