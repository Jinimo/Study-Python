## ch03 - 22/39

### 함수 선언부 ###
# 친구 추가 함수
def add_data(friend):
    katok.append(None)     # 자리 추가
    kLen = len(katok)
    katok[kLen-1] = friend # 뒤로 데이터 추가

# 친구 삽입 함수
def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1, position, -1): # 3등인 친구까지 뺴주는 것
        katok[i] = katok[i-1]             #
        katok[i-1] = None                 # 이동된 칸에 빈 자리 생성

    katok[position] = friend

# 친구 삭제 함수
def delete_data(position):
    kLen = len(katok)
    katok[position] = None               # 해당 위치 데이터 삭제

    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]            # katok[4] = katok[5]
        katok[i] = None                  # katok[5] = None 이동된 데이터 자리 없애기

    del(katok[kLen-1]) # 마지막 칸 지우기

### 전역 변수부 ###
katok=[]
select = -1  # 1: 추가, 2: 삽입, 3:삭제, 4:종료

### 메인 코드부 ###
while (select != 4):
    select = int(input("선택 (1: 추가, 2: 삽입, 3:삭제, 4:종료)-->"))
    # 추가
    if select == 1:
        friend = input("추가할 친구: ")
        add_data(friend)
        print(katok)
    # 삽입
    elif select == 2:
        friend = input("추가할 친구: ")
        position = int(input("추가할 위치: "))
        insert_data(friend, position)
        print(katok)
    # 삭제
    elif select == 3:
        position = input("삭제할 친구 위치: ")
        delete_data(position)
        print(katok)
    # 종료
    elif select == 4:
        print(katok)
        exit

    else:
        print("1~4 중 하나를 선택해 입력해 주세요.")
        continue