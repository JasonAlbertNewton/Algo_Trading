import yfinance as yf
import os 

os.system('clear')

while (1):
#import datas
	stock_check = input("INPUT THE STOCK YOU WANT TO CHECK: ")
	start_date  = input("The begining of the data you want: [YYYY-MM-DD] ")
	end_date = input("The end of the date you want: [YYYY-MM-DD] ")

	data = yf.download(stock_check,start=start_date , end=end_date)
	
	user_input = int(input("\nINPUT OPTION: \n 1. Read data \n 2. Analysis Data \n"))
	
	if(user_input == 1):
		print(data.tail())
	if(user_input == 2):
		print(data[0])
	
	if(user_input == -1):
		break

