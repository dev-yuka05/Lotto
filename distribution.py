import json
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def plot_number_distribution(data):
    number_counts = np.zeros(45)
    for numbers in data:
        for number in numbers:
            number_counts[number - 1] += 1
    
    x = np.arange(1, 46)
    plt.bar(x, number_counts)
    plt.xlabel('Number')
    plt.ylabel('Count')
    plt.title('Number Distribution')
    plt.show()

# numbersData.json 파일에서 데이터 로드
file_path = "numbersData.json"
data = load_data(file_path)

# 숫자 분포도 그리기
plot_number_distribution(data)