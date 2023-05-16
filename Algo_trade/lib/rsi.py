import numpy as np
import pandas as pd


#check with RSI strategies
class RSI:

	def __init__(self ,data, time_slot_one):
		self.data = data
		self.time_slot_one = time_slot_one

	def RSI_calc(self):
		sizes = self.data.shape[0]
		data_close = self.data['Close']
		self.time_slot_one
		#test the data set is large enough or not
		if(data_close.shape[0] < self.time_slot_one):
			return -1
		RSI_DATA = {
			"Umean": [0],
			"Dmean": [0],
			"Date" : self.data.index,
	#		"RSI_INDEX": [],
		}
		#do a loop get the first time_slot_one_data Umean and Dmean
		for i in range(1,sizes):
			dt1 = data_close.iloc[i-1]
			dt2 = data_close.iloc[i]
			percentage_change = self.RSI_percentage_change(dt1, dt2)

			if(percentage_change > 0):
				RSI_DATA["Umean"].append(dt2)
				RSI_DATA["Dmean"].append(0)
			else:
				RSI_DATA["Umean"].append(0)
				RSI_DATA["Dmean"].append(dt2)

		for i in range(self.time_slot_one):
			RSI_DATA['RSI_INDEX'].append(0)

        start = 0

        for i in range(self.time_slot_one, sizes):
            pass


		RSI_DATA = pd.DataFrame(data=RSI_DATA)
		RSI_DATA = RSI_DATA.set_index('Date')

		print(RSI_DATA)
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

