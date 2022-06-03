## ch03 - 4/39
# 데이터 리스트 추가

katok = []

## 친구 추가 함수
def add_data(friend):
    katok.append(None)     # 자리 추가
    kLen = len(katok)
    katok[kLen-1] = friend # 뒤로 데이터 추가

# 친구 추가
add_data('다현')
add_data('정연')
add_data('사나')
add_data('지효')
add_data('모모')
print(katok)

