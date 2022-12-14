# 가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 복도가 있습니다.
# 태일이는 이 복도의 바닥을 1 X 2 크기의 타일, 2 X 1 크기의 타일, 2 X 2 크기의 타일을 이용해 채우고자 합니다.
# 이 때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성해주세요.
# 예를 들어 2 X 3 크기의 바닥을 채우는 경우의 수는 5가지이고 각각의 경우는 다음과 같습니다. 
# ABC ABB ABB AAC AAB
# ABC ACC ABB BBC AAB

# 예제 입력1
# 3

# 예제 출력1
# 5

# 예제 입력2
# 5

# 예제 출력2
# 21

# 입력값 설명
# 첫째 줄에 N이 주어집니다. (1 ≤ N ≤ 1,000)

# 출력값 설명
# 첫째 줄에 2 X N 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지를 출력하세요.

import sys

N = int(sys.stdin.readline())

tile = [0] * N
tile[0] = 1
tile[1] = 3

for i in range(2, N):
    tile[i] = (tile[i - 1] + 2 * tile[i - 2]) % 796796

print(tile[N - 1])