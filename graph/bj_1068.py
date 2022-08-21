import sys
input = sys.stdin.readline

def dfs(start, queue): # 삭제할 노드들은 -2로 바꿔줌
    queue[start] = -2
    for i in range(len(queue)):
        if start == queue[i]:
            dfs(i, queue)


tree_size = int(input().rstrip()) # 트리 노드 개수
tree_info = list(map(int, input().split())) # 트리 정보
remove_node = int(input().rstrip()) # 지울 노드 정보
count = 0

dfs(remove_node, tree_info)
for i in range(tree_size):
    if tree_info[i] != -2 and i not in tree_info:
        count += 1

print(count)