# 민겸이는 맥주를 잔에 따르려고 합니다. 이때, 민겸이가 맥주를 잔에 따르면 따른 양의 절반만큼 거품이 생깁니다.
# 컵의 용량이 주어질 때, 민겸이가 따른 맥주의 양과 생기는 거품의 양의 합이 컵의 용량보다 크지 않도록 따르는 양의 최댓값을 구하세요.

import sys

K = int(sys.stdin.readline())

print(int(K / 3 * 2))