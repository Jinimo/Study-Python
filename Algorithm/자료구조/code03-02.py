## ch03 - 5/39
# '미나' 3번째 위치에 삽입

katok = ['다현', '정연', '쯔위', '사나', '지효', '모모']

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1, position, -1): # 3등인 친구까지 뺴주는 것
        katok[i] = katok[i-1]             #
        katok[i-1] = None                 # 이동된 칸에 빈 자리 생성

    katok[position] = friend

insert_data(3, '미나') # 3번 자리에 '미나' 삽입
print(katok)

