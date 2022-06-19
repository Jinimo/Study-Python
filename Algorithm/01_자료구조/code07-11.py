##### 원형 큐 #####
# rear+1 = front  경우 원형 큐가 꽉 찬것으로 처리
# rear = front  경우 원형 큐가 꽉 찼지만 큐가 비어있다는 의미로 해석! (잘못된 예)


### 함수 ###
# 큐 꽉 찼는지 확인하는 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear + 1) % SIZE == front): # rear+1 = front 같은 경우 원형 큐가 꽉 찬것으로 처리
        return True
    else:
        return False
# 데이터 삽입 함수
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐 꽉 찼음!')
        return
    rear = (rear + 1) % SIZE
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
    front  = (front + 1) % SIZE
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
front = rear = 0 # 초기값

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
