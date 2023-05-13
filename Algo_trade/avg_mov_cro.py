import pandas as pd
import numpy as np

#this function return at that period of time of back testing,  
class average_moving_cross:	
	def __init__(self , data , mov_1 , mov_2):
		self.data = data
		self.mov_1 = mov_1
		self.mov_2 = mov_2
		
	#this function is to calcualte the date range of the data
	def gt_range_data(self):
		print(self.data.head(self.mov_1))	

	def avg_mov_cro(self):
		Close_level = data['Close']
	
		mov_1 = int(self.mov_1)
		mov_2 = int(self.mov_2)

		if(Close_level.size < self.mov_1 or Close_level.size < self.mov_2):
			return []



	
