import numpy as np
import pandas as pd


#check with RSI strategies
class RSI:

	def __init__(self ,data, time_slot_one):
		self.data = data
		self.time_slot_one = time_slot_one


	#Return RSI_DATA: a panda dataframe
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
			"RSI_INDEX": [],
			"AVG_GAIN": [],
			"AVG_LOSE": [],
		}
		#do a loop get the first time_slot_one_data Umean and Dmean
		for i in range(1,sizes):
			dt1 = data_close.iloc[i-1]
			dt2 = data_close.iloc[i]
			percentage_change = self.RSI_percentage_change(dt1, dt2)

			if(percentage_change > 0):
				RSI_DATA["Umean"].append(percentage_change)
				RSI_DATA["Dmean"].append(0)
			else:
				RSI_DATA["Umean"].append(0)
				RSI_DATA["Dmean"].append(percentage_change)

		for i in range(self.time_slot_one):
			RSI_DATA['RSI_INDEX'].append(0)
			RSI_DATA['AVG_GAIN'].append(0)
			RSI_DATA['AVG_LOSE'].append(0)

		start = 0

		#calculating RSI index
		for i in range(self.time_slot_one, sizes):
			#reset loop 
			Umean_temp=[]
			RS_INDEX = 0
			Dmean_temp=[]
			number_of_Deman = 0
			number_of_Umean = 0

			#umean and deman caluclation 
			for j in range(self.time_slot_one):
				if(RSI_DATA["Umean"][j+start] != 0):
					number_of_Umean += 1
					Umean_temp.append(RSI_DATA["Umean"][j+start])
					Dmean_temp.append(0)
				else:
					number_of_Deman += 1
					Dmean_temp.append(RSI_DATA["Dmean"][j+start]*-1)
					Umean_temp.append(0)
			#average gain and lost calculation 
			numpy_Umean_temp = np.array(Umean_temp)
			numpy_Dmean_temp = np.array(Dmean_temp)
			Avg_Gain = np.mean(numpy_Umean_temp)
			Avg_Loss = np.mean(numpy_Dmean_temp)

			#RSI Data Calcalution
			RSI_DATA["AVG_GAIN"].append(Avg_Gain)
			RSI_DATA["AVG_LOSE"].append(Avg_Loss)	
			RS_INDEX = Avg_Gain/Avg_Loss
			RSI_DATA["RSI_INDEX"].append(100 - 100/(1+RS_INDEX))

			#loop counter
			start += 1

		#change the dataframe
		RSI_DATA = pd.DataFrame(data=RSI_DATA)
		RSI_DATA = RSI_DATA.set_index('Date')

		return RSI_DATA
	

	#Back TESTING win rate and basic return
	def RSI_Backtesting(self): 
		pass


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

	