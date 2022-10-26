# 지방선거날이 돌아왔습니다.
# 각 정당과 무소속 후보들이 출마하였습니다.
# 수많은 사람들이 투표에 참여하였기 때문에 선거관리위원회에서는 효율적으로 당선인을 알아내려고 합니다.
# 투표를 한 사람들의 수와, 각각이 뽑은 후보 번호가 주어졌을 때, 어느 후보가 당선이 되었는지 알아내는 프로그램을 작성해주세요. 
# 득표 수가 동점일 경우에는 후보 번호가 작은 후보가 당선인이 됩니다.

# 예제 입력1
# 8
# 1
# 2
# 1
# 2
# 2
# 3
# 3
# 2

# 예제 출력1
# 2

# 예제 입력2
# 3
# 1
# 2
# 3

# 예제 출력2
# 1

# 입력값 설명
# 첫째 줄에 투표를 한 사람들의 수 N (1 ≤ N ≤ 1,000)이 주어집니다.
# 둘째 줄부터 N개의 줄에 걸쳐서 투표 용지에 적혀있는 후보 번호 i (1 ≤ i ≤ 1,000)가 주어집니다.

# 출력값 설명
# 첫째 줄에 당선인의 후보 번호를 출력합니다.

import sys

N = int(sys.stdin.readline())

I = [int(sys.stdin.readline()) for _ in range(N)]

vote = [0] * N

for j in I:
    vote[j - 1] += 1

print(vote.index(max(vote)) + 1)

# I_max = 0

# for j in range(1, N):
#     if I[I_max] < I[j]:
#         I_max = j

# I_max += 1

# print(I_max)