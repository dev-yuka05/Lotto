import requests
import json

result = []

for i in range(1, 1076):
    url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={i}"
    response = requests.get(url)
    data = response.json()
    
    rwtNo1 = data["drwtNo1"]
    rwtNo2 = data["drwtNo2"]
    rwtNo3 = data["drwtNo3"]
    rwtNo4 = data["drwtNo4"]
    rwtNo5 = data["drwtNo5"]
    rwtNo6 = data["drwtNo6"]
    
    result.append([rwtNo1, rwtNo2, rwtNo3, rwtNo4, rwtNo5, rwtNo6])

    print(f"Fetched data for {i} 회차")

    with open("numbersData.json", "w") as file:
        json.dump(result, file)