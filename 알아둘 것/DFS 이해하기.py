

# DFS(Depth First Search)는 이름 그대로, 깊이 우선 탐색 알고리즘

# Node의 연결 관계를 Tree 형태로 만든 뒤, 재귀 함수를 이용
 

# Node 별 연결 관계가 담긴 2차원 List를 입력으로 받았을 때는 Tree 형태로 입력값의 적절한 변환이 필요함.
# Example (프로그래머스 완전탐색-전력망 나누기의 입력 값을 예시로 사용)


N , wires = 9 , [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]


# 빈 Tree 생성(2차원 List) 
# (N+1)만큼의 가지를 생성하는 이유는 Node의 index를 맞춰주기 위함이라고 이해하면 편함
tree = [ [] for _ in range(N+1) ]

# 최초 입력값인 wires를 2차원 Tree로 변환 

for wire in wires:

 a , b = wire
 tree[a].append(b)  # a번째 가지에 연결된 b를 추가
 tree[b].append(a)  # b번째 가지에 연결된 a를 추가 


print(tree)
> [[], [3], [3], [1, 2, 4], [3, 5, 6, 7], [4], [4], [4, 8, 9], [7], [7]]

# DFS 사용을 위한 함수 정의

# 방문 처리를 위한, visited 생성
# 마찬가지로, 여기서도 (N+1)을 하는 이유는 Node의 index를 맞춰주기 위함이라고 이해하면 편함

visited = [False] * (N+1)

# DFS function 

def dfs(tree , v , visited):

 # print(v , end = ' ')  # 방문 순서를 보기 위한 출력
 visited[v] = True  # 방문 처리 (초기값은 1이다) 

 for i in tree[v]: # 현재 방문한 tree에서 가지를 뻗어나가기 위함
  
  if not visited[i]:  # 만약 현재 가지에 연결된 가지들을 아직 방문하지 않았다면 
   dfs(tree , i , visited)  # 그 가지를 방문하고 , 그 가지에 연결된 가지로 다시 뻗어나감






# Node1에서 시작 
dfs(tree , 1 , visited)

> 1 3 2 4 5 6 7 8 9 
