"""
[1113] 수영장 만들기: https://www.acmicpc.net/problem/1113
"""

import sys
from collections import deque


# BFS
def pour_water(row, col):
    global cnt, flag

    # 큐 선언 및 초기화
    Q = deque()
    Q.append((row, col))

    # 방문 체크
    visited[row][col] = 1

    while Q:
        row, col = Q.popleft()

        # 4방위 탐색
        for d in range(4):
            nrow, ncol = row + dy[d], col + dx[d]

            # 2. 테두리에 도달한다면
            if not (1 <= nrow < N - 1 and 1 <= ncol < M - 1):
                # 그 중에서도 물이 흘러 넘치는 상황이라면
                if POOL[nrow][ncol] < depth:
                    # 카운팅에서 제외
                    flag = 0
                continue

            # 1. 아직 방문하지 않은, 다음 위치의 높이가 depth 레벨보다 낮다면: 물이 채워지는 곳
            if POOL[nrow][ncol] < depth and not visited[nrow][ncol]:
                visited[nrow][ncol] = 1  # 방문 체크
                cnt += 1  # 카운트
                Q.append((nrow, ncol))  # 큐에 추가


# input
N, M = map(int, sys.stdin.readline().split())
POOL = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

# 4방위 탐색용 배열
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

ans = 0  # 최종 결과

# 높이 방향(z축)으로 1 레벨씩 물 채우기
for depth in range(2, 10):
    cnt, flag = 1, 1  # 각 레벨별 카운팅 값, flag variable
    visited = [[0] * M for _ in range(N)]  # 방문 체크용 배열

    # xy 평면 기준 시작점 찾기
    for r in range(1, N-1):
        for c in range(1, M-1):
            # 시작점 조건
            if POOL[r][c] < depth and not visited[r][c]:
                # BFS
                pour_water(r, c)

                # flag의 값이 1로 유지가 되었다면
                if flag:
                    # 최종 결과에 카운팅 더하기
                    ans += cnt
                cnt, flag = 1, 1  # 초기화

# output
print(ans)
