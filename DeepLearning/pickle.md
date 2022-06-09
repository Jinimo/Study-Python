텍스트 상태 데이터 X 파이썬 객체 자체 저장 

Binary 형태로 저장 



```py
import pickle

my_data = ['a','b','c']
 
### 피클 파일로 저장할 때 ###
with open("data.pickle","wb") as fw:
    pickle.dump(my_list, fw)
 
### 피클 파일 불러오기 ###
with open("data.pickle","rb") as fr:
    data = pickle.load(fr)

print(data)
#['a', 'b', 'c']
```

