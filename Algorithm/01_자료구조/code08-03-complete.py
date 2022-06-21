## ch08 -22/47
## 이진 탐색 트리
# 중요한 코드!!! 활용 가능해 !!
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

### 함수 ###

### 전역 ###
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스'] # 여기에 활용하는 데이터 넣어주면 돼!

### 메인 ###
# 루트 노드 만들기
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node) # 파이썬에서는 불필요하지만 C언어는 필요!
# 나머지 노드
for name in nameAry[1:]: # '블랙핑크' 제외 나머지
    node = TreeNode()
    node.data = name
    # 작은 것은 왼쪽, 큰 것은 오른쪽
    current = root                   # 현재는 루트 노드
    while True:
        if name < current.data:      # 가나다 순서..
            if current.left == None : # 왼쪽 자리 비어있으면
                current.left = node
                break                # 빠져나가기
            current = current.left   # 비어있지 않으면 현재 노드 왼쪽 아래로 변경

        else:                        # 같은 것도 있지만 일단 name > current.data 경우
            if current.right == None:# 오른쪽 자리 비어있으면
                current.right = node
                break
            current = current.right  # 비어있지 않으면 현재 노드 오른쪽 아래로 변경

    memory.append(node)

print('이진 탐색 트리 구성 완료!')

findData = '마마무'

current = root
while True : # 몇번 검색해야 하는지 모르니 while
    if findData == current.data :
        print(findData, " 찾음 ^^")
        break
    elif findData < current.data :
        if current.left == None :
            print(findData, " 없음 ㅠㅠ")
            break
        current = current.left
    else :
        if current.right == None :
            print(findData, " 없음 ㅠㅠ")
            break
        current = current.right