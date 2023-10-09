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