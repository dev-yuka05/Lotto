import json

# numbersData.json 파일 로드
with open('numbersData.json') as file:
  numbers_data = json.load(file)

  for i in range(6):
    result = [subarray[i] for subarray in numbers_data]
    
    with open(f'number{i+1}.json', 'w') as file:
      json.dump(result, file)