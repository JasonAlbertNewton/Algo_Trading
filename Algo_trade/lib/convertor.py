import numpy as np
import pandas as pd
 
def csv_to_numpy(csv_data):
    numpy_data = np.genfromtxt(csv_data, delimiter=",", skip_header=1)
    return numpy_data

def numpy_to_csv(numpy_data):
    csv_data = np.savetxt('data.csv', numpy_data, delimiter=",")
    return csv_data

def pandas_to_numpy(df):
    numpy_data = pd.to_numpy(df)
    return numpy_data
    
def numpy_to_pandas(numpy_data):
    df = pd.DataFrame(numpy_data)
    return (df)
