import yfinance as yf
import numpy as np
import pandas as pd
import os 

from avg_mov_cro import average_moving_cross

os.system('clear')

while (1):
#import data
	stock_check = input("INPUT THE STOCK YOU WANT TO CHECK: [-1 to quit] ")
	
	if(stock_check == "-1"):
		break
	
	start_date  = input("The begining of the data you want: [YYYY-MM-DD] ")
	end_date = input("The end of the date you want: [YYYY-MM-DD] ")

	data = yf.download(stock_check,start=start_date , end=end_date)
	while(1):
		user_input = int(input("\nINPUT OPTION: \n 1. Read data \n 2. Specific Column \n"))
		
		if(user_input == 1):
			print(data.tail())
		if(user_input == 2):
			arr = []
			while(1):
				user_specific_column = input("\nOpen , Close , High , Low , Volume : one time input one , finsih input -1\n")
				if(user_specific_column == "-1"):
					break
				else:
					arr.append(user_specific_column)
			temp = data[arr]
			print(temp)
		if(user_input == 3):
			avg_mov_cro= average_moving_cross(data , 10 , 20)			
			avg_mov_cro.gt_range_data()

		
		if(user_input == -1):
			break

