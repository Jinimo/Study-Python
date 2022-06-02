## ch03 - 6/39
# '사나' 삭제 후 칸 제거

katok = ['다현', '정연', '쯔위', '미나', '사나', '지효', '모모']

def delete_data(position):
    kLen = len(katok)
    katok[position] = None               # 해당 위치 데이터 삭제

    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]            # katok[4] = katok[5]
        katok[i] = None                  # katok[5] = None 이동된 데이터 자리 없애기

    del(katok[kLen-1]) # 마지막 칸 지우기

delete_data(4)
print(katok)
