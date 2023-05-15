import pandas as pd
import csv 

#this function return at that period of time of back testing,  
class average_moving_cross:	
	def __init__(self , data , mov_1 , mov_2):
		self.data = data	
		if(mov_1 > mov_2):
			temp = mov_1 
			mov_1 = mov_2
			mov_2 = temp	
		self.mov_1 = mov_1
		self.mov_2 = mov_2
		
	#this function is to calcualte the date range of the data
	def gt_range_data(self):
		sizes = self.data.shape[0]
		Date = self.data.index
		temp = self.data
		start = 0

		_init_data_moving_average = {
			'AVG_1':[],	
			'AVG_2':[],
			'Date' :Date
		}
		for i in range(self.mov_1):
			_init_data_moving_average['AVG_1'].append(0)
	
		for i in range(sizes - self.mov_1):
			temp1 = temp.iloc[start:start+self.mov_1]
			mov_avg_1 = temp1['Close'].sum()/self.mov_1
			_init_data_moving_average['AVG_1'].append(mov_avg_1)
			start = start+1
		
		for i in range(self.mov_2):		
			_init_data_moving_average['AVG_2'].append(0)
		
		start = 0
		for i in range(sizes-self.mov_2):
			temp1 = temp.iloc[start:start+self.mov_2]
			mov_avg_2 = temp1['Close'].sum()/self.mov_2
			_init_data_moving_average['AVG_2'].append(mov_avg_2)
			start = start+1		
		
		data_moving_average=pd.DataFrame(_init_data_moving_average)	
		data_moving_average=data_moving_average.set_index('Date')
		
		return data_moving_average
		 		
	def print_data(self):
		temp = self.gt_range_data()
		print(temp.head())

	def save_file(self):
		temp = self.gt_range_data()
		temp.to_csv('save.csv', index = True)


	def avg_mov_cro_test(self):
		_avg_data = self.gt_range_data()
#		for i in range(_avg_data.shape[0]):		
		pass	



	
