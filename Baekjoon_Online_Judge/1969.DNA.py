"""
[1969] DNA: https://www.acmicpc.net/problem/1969
"""

import sys

# 카운팅에 활용할 딕셔너리
CODES = {'A': 0, 'C': 1, 'G': 2, 'T': 3}  # 뉴클레오티드 -> 인덱스
CODES_RVS = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}  # 인덱스 -> 뉴클레오티드

# input
N, M = map(int, sys.stdin.readline().split())
INFO = [sys.stdin.readline().rstrip() for _ in range(N)]

# 카운팅 결과를 저장할 2차원 리스트
codes_count = [[0] * 4 for _ in range(M)]
# print(codes_count): [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ...]
for data in range(N):
    # print(INFO[data]): ATGTTACCAT
    for code in range(M):
        # print(INFO[data][code]): A
        codes_count[code][CODES[INFO[data][code]]] += 1  # [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ...]
# print(codes_count)

ans_code = ''  # 최종 결과: DNA
ans_hd = 0  # 최종 결과: hamming distance 누적 합

# 인덱스별 카운팅 결과들에 대해 순회
for code_count in codes_count:
    # 특정 인덱스의 카운팅 결과에서 가장 빈도가 큰 code 찾아내기
    max_idx = 0  # 해당 code의 인덱스
    for i in range(1, 4):
        if code_count[max_idx] < code_count[i]:
            max_idx = i

    ans_code += CODES_RVS[max_idx]  # 코드 붙이기
    ans_hd += (N - code_count[max_idx])  # 해당 위치에서의 hamming distance 누적시키기

# output
print(ans_code)
print(ans_hd)
