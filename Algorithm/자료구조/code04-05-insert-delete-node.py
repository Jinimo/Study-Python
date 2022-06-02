
## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end='  ')
    while (current.link != None):
        current = current.link
        print(current.data, end='  ')
    print("~~END~~")

## 전역
memory = []  # 파이썬에서는 불필요 but C 언어는 필요!
# ** 중요) head: 첫번째 노드, pre:현재 처리중인 노드 바로 앞 노드, current: 현제 처리중인 노드
head, pre, current = None, None, None          # 처음은 초기화
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # 데이터 배열 가정 -> 실제로 사용할 경우는 더 많아, 형태 맞춰서 사용

## 메인
node = Node() # 첫 노드
node.data = dataArray[0]   # 데이터 배열의 첫번쨰 데이터
head = node                # 첫 노드를 head로 지정해줌!
memory.append(node)        # 부가 옵션

for data in dataArray[1:]: # ['정연' 부터 ~]
    pre = node             # 현재 노드를 전 노드로 잡고 있고
    node = Node()          # node 변수 재활용
    node.data = data
    pre.link = node
    memory.append(node)    # 부가 옵션

# printNodes(head)

#### 함수 ####
## 노드 삽입 함수
def insertNode(findData, insertData):
    global  memory, head, pre, current

    # 1) 첫 노드 앞에 삽입.... (예: '다현', '화사')
    if findData == head.data:
        node = Node()
        node.data = insertData # 새 노드 생성 ('화사')
        node.link = head       # 새 노드의 링트 -> head 노드가 가리키는 노드를 지정
        head = node            # head -> 새 노드로 지정 (head='화사')
        memory.append(node)    # 부가 옵션
        return

    # 2) 중간 노드 삽입.... (예: '사나', '솔라')
    current = head                   # head를 현재 위치로
    while current.link != None:      # 현재 노드가 빈 노드가 아니라면
        pre = current                # 우선 pre 노드가 current 노드 잡고 있고
        current = current.link       # 현재 노드를 다음 노드로 이동
        if current.data == findData: # current 데이터가 내가 찾고 있는 데이터라면
            node = Node()
            node.data = insertData   # 새 노드 생성 ('솔라')
            node.link = current      # 이전 노드의 링크를 새 노드의 링크로 지정 (pre='쯔위', current='사나')
            pre.link = node          # 이전 노드의 링크를 새 노으로 지정 ('쯔위'->'솔라'->'사나')
            memory.append(node)      # 부가 옵션

    # 3) 마지막 노드 삽입(=findData 없음)....(예: '재남', '문별')
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

## 노드 삭제 함수
def deleteNode(deleteData):
    global memory, head, pre, current
    # 1) 첫 노드 삭제.... (예: '다현')
    if deleteData == head.data:
        current = head
        head = head.link
        del(current)
        return
    # 2) 두번째 이후 노드 삭제... (예: '쯔위')
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

## 노드 검색 함수
def findNode(findData):
    global memory, head, pre, current
    current = head               # 현재 노드를 첫번째 노드로 동일하게 만들기
    if current.data == findData: # 현재 노드가 검색할 노드와 동일하다면
        return current           # 현재 노드 반환
    while current.link != None:  # 현재 노드가 빈 노드가 아니라면 (마지막 노드 전까지 반복)
        current = current.link   # 다음 노드를 현재 노드로
        if current.data == findData:
            return current
    return Node()                # 검색 데이터 찾지 못했다면 -> 빈 노드 return

##########################################
#### 결과 확인 ####
##########################################

## 노드 삽입
# 1) '다현' 앞에 '화사' 추가
insertNode('다현', '화사')
printNodes(head)
#=> 화사  다현  정연  쯔위  사나  지효

# 2) '사나' 앞에 '솔라' 추가
insertNode('사나', '솔라')
printNodes(head)
#=> 화사  다현  정연  쯔위  솔라  사나  지효  솔라

# 3) 마지막 노드에 '문별' 삽입
insertNode('재남', '문별') # '재남'은 없는 데이터!
printNodes(head)
#=> 화사  다현  정연  쯔위  솔라  사나  지효  솔라  문별

## 노드 삭제
#
deleteNode('다현')
printNodes(head)
#=> 화사  정연  쯔위  솔라  사나  지효  솔라  문별
#
deleteNode('쯔위')
printNodes(head)
#=> 화사  정연  솔라  사나  지효  솔라  문별

#
deleteNode('재남')
printNodes(head)

#
fNode = findNode('쯔위')
print(fNode.data)