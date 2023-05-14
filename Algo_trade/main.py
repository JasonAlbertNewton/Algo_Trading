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
		exit(0)
	
	start_date  = input("The begining of the data you want: [YYYY-MM-DD] ")
	end_date = input("The end of the date you want: [YYYY-MM-DD] ")

	data = yf.download(stock_check,start=start_date , end=end_date)
	while(1):
		try:
			user_input = int(input("\nINPUT OPTION: \n 1. Read data \n 2. Specific Column \n 3. moving average \n OPTION: \n"))
		except:
			break

		available_choice = [1,2,3]		

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
			try:
				temp = data[arr]
				print(temp)
			except:
				print("INPUT FAIL ! RETURN TO MAIN PAGE .......... ")
				break
		if(user_input == 3):
			mov_1 = int(input("\n INPUT SMALLER MOVING AVEGERE ONE \n"))
			mov_2 = int(input("\n INPUT LARGER MOVING AVERAGE TWO \n"))
			avg_mov_cro= average_moving_cross(data , mov_1 , mov_2)			
			avg_mov_cro.save_file()
		
		if(user_input == -1):
			exit(0)
		
		if(user_input not in available_choice):
			break	
		
		

	
