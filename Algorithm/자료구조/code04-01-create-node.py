## 단순 연결 리스트
## ch04 - 8/52

### 노드(데이터+링크) 생성 함수
class Node():
    def __int___(self):
        self.data = None
        self.link = None

### 메인
node1 = Node()     # 새 노드 생성
node1.data = '다현' # 데이터 생성

node2 = Node()
node2.data = '정연'
node1.link = node2 # 노드1 -> 노드2 연결 링크 생성

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# '쯔위' 노드 삭제
node2.link = node3.link # '쯔위' 힝크를 '정연' 링크로 복사
del(node3)              # '쯔위' 삭제

# 새로운 노드 '재남' -> 센터에 넣고 싶을때
# 정얀->쯔위 => 정연->재남->쯔위
# newNode = Node()
# newNode.data = '재남'
# newNode.link = node2.link  # '재남' 노드 링크에 '정연' 노드 링크 복사
# node2.link  = newNode      # '정연' 노드 링크에 '재남' 노드 지정

# 노드1의 데이터만 알면 나머지 알 수 있음!
# 노드1의 데이터로 접근해야 함!

# print(node1.data, end = ' ')
# print(node1.link.data, end = ' ')
# print(node1.link.link.data, end = ' ')
# print(node1.link.link.link.data, end = ' ')
# print(node1.link.link.link.link.data, end = ' ')

current = node1
print(current.data, end=' ')
while (current.link != None):
    current = current.link
    print(current.data, end = ' ')
print("~~END~~")