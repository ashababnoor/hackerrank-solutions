'''
Laptop Battery Life
Link: https://www.hackerrank.com/challenges/battery/problem
'''

import requests
import sys
from sklearn.linear_model import LinearRegression

url = "https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt" 

response = requests.get(url)

output = None
if response.status_code == 200:
    output = response.content.decode()
else:
    sys.exit("Failed to download the file.")

data = output.split("\n")
x = [list(map(float, datum.split(",")[0:-1])) for datum in data if datum != ""]
y = list(map(float, [datum.split(",")[-1] for datum in data if datum != ""]))


regressor = LinearRegression()
regressor.fit(x, y)

test_data = float(input())

results = regressor.predict([[test_data]])

for result in results:
    print(result)
    

'''
This code gives the wrong result
Upon visualizing the data from https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt
we see that the battery life is always double of how time was charged for with a threshold of 8

Therefore, the solution is as simple as the following -

x = float(input())
y = x*2
threshold = 8.0

if y > threshold:
    print(threshold)
else:
    print(y)
'''

'''
Alternative method from another participant -

import sys
import pandas as pd
from sklearn import linear_model

if __name__ == '__main__':
    timeCharged = float(input().strip())

    dataset = pd.read_csv('trainingdata.txt', header=None)


    # According to the chart, we must remove items with a 
    # duration of time greater than eight.
    dataset = dataset[dataset.iloc[:,1] < 8]

    # Add bias
    dataset.insert(0, len(dataset.columns), 0)

    # Separe variables dependet and independent
    X = dataset.iloc[:,0:2]
    Y = dataset.iloc[:,2]

    # Create the classifier model
    model = linear_model.LinearRegression()
    model.fit(X, Y)

    # Set new value to predict
    
    result = model.predict([[0, timeCharged]])
    if result[0] > 8:
        print (8.0)
    else:
        print (round(result[0],2))
'''