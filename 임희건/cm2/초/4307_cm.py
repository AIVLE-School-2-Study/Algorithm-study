# 호준이는 지난주에 인터넷 쇼핑으로 마음에 드는 물건을 잔뜩 샀습니다.
# 하지만 정신을 차리고 보니 충동적으로 구매했지만 마음에 들지 않는 물건들 투성이였습니다.
# 인터넷 쇼핑몰은 반품신청을 하고 일주일 안에 물건을 다시 보내면 환불을 받을 수 있습니다.
# 호준이는 가격이 높은 물건부터 차례대로 모든 물건에 대해 반품을 시도합니다.
# 단, 반품신청한 물건들의 가격의 합이 택배회사에서 정한 금액을 초과하면 해당 물건은 반품이 불가능합니다.
# 회사에서 정한 금액이 주어질 때, 호준이가 최대 몇 개의 물건을 반품할 수 있는지 알아내는 프로그램을 작성해주세요.

# 예제 입력1
# 10 35000
# 9366
# 5733
# 1555
# 4569
# 4386
# 6525
# 7335
# 6865
# 3448
# 1170

# 예제 출력1
# 5

# 예제 입력2
# 15 50000
# 7221
# 6483
# 6577
# 537
# 5287
# 4886
# 5378
# 3187
# 5365
# 8066
# 5600
# 6358
# 1364
# 9688
# 9676

# 예제 출력2
# 8

# 입력값 설명
# 첫 번째 줄에 호준이가 반품하려고 하는 물건의 수 N과, 회사에서 정한 금액 M이 각각 자연수로 주어집니다. (1 ≤ N ≤ 500) (1 ≤ M ≤ 1,000,000)
# 둘째 줄부터 N개의 줄에 걸쳐 물건들의 가격 P(i)가 자연수로 주어집니다.(1 ≤ P(i) ≤ 10,000)

# 출력값 설명
# 호준이가 반품할 수 있는 물건의 최대 개수를 출력합니다.

import sys

N, M = map(int, sys.stdin.readline().split())
P = [int(sys.stdin.readline()) for _ in range(N)]
p = 0
count = 0

P.sort(reverse = True)

for i in range(N):
    if p + P[i] <= M:
        p += P[i]
        count += 1

print(count)