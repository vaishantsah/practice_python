import json
import pandas as pd
import logging
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

current=datetime.now().strftime("%Y-%m-%d")
logging.basicConfig(filename=current ,filemode='w',format='%(asctime)s - %(message)s',level=logging.INFO)

def json_catcher(path:str)->None:
    """
    Accepts a json file and returns the contents under 'dates'
    params: 
            path: takes a relative or actual path of a json file as a string and returns a data frame of
            the selected dates with a graph of the following

    """
    logging.info('Trying to open the json file')
    with open(path,'r') as f:
        data=json.load(f)
        f.close()
    print_json=json.dumps(data,indent=4)
    print(print_json)
    logging.info('Taking input from the user')
    input_date=input("Enter the date you want information on: ")
    df=pd.json_normalize(data["AN"]["dates"][input_date])
    print(df)
    logging.info('Attempting to print the data from the json file')
    logging.info('Attempting to draw a graph for the dataframe')
    plt.figure(figsize =(8,5))
    sns.barplot(df, palette='pastel',legend='auto')
    plt.show()

if __name__ == "__main__":
    path="Test.json"
    logging.info('Loading file and calling the main function')
    json_catcher(path)
    logging.info('Json has been processed')