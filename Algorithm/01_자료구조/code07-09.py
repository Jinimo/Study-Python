## ch07 - 23/50

### 함수 ###
# 큐 꽉 찼는지 확인하는 함수
def isQueueFull():
    global SIZE, queue, front, rear
    # 1) rear 뒤에 여유가 있는 상태
    if (rear != SIZE -1):
        return False
    # 2) 큐가 꽉찬 상태
    elif (rear == SIZE-1 and front == -1):
        return True                      # 꽉 찼음
    # 3) rear는 끝이지만 앞쪽에 여유가 있는 경우
    else:
        for i in range(front+1, SIZE, 1):
            queue[i-1] = queue[i]         # 한칸씩 앞으로 떙기고
            queue[i] = None               # 전에 있던 자리는 비우기
        front -= 1
        rear -= 1
        return False                      # 비어있음

# 데이터 삽입 함수
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐 꽉 찼음!')
        return
    rear += 1
    queue[rear] = data

# 큐 비어있는지 확인하는 함수
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (rear == SIZE): # 비어있다면
        return True
    else:
        return False

# 데이터 추출 함수
def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비어있습니다.')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

# 다음 추출할 데이터 확인 함수
def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비어있습니다.')
        return None
    return queue[front +1]


### 전역 ###
SIZE = 5
queue =[None for _ in range(SIZE)]
front = rear = -1

### 메인 ###
# 데이터 삽입
print('----- enQueue -----')
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미') # 원더걸스
print('출구<--', queue, '<--입구')

# 데이터 추출
print('----- deQueue -----')
retData = deQueue()
print("디큐 ==> ", retData)
retData = deQueue()
print("디큐 ==> ", retData)
print('출구<--', queue, '<--입구')

enQueue('재남')
print('출구<--', queue, '<--입구')

enQueue('길동')
print('출구<--', queue, '<--입구')

enQueue('소희')
print('출구<--', queue, '<--입구')