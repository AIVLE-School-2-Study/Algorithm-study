# 치훈이는 정사각형 모양의 땅을 구입했습니다.
# 그러다 치훈이는 산 땅의 면적만이 기억나고, 한 변의 길이를 까먹고 말았습니다.
# 치훈이가 산 땅의 면적이 입력으로 주어졌을 때, 치훈이를 위해 치훈이가 산 땅의 한 변의 길이가 얼마인지 출력하는 프로그램을 작성해주세요.

import sys
import math

n = int(sys.stdin.readline())

print(int(math.sqrt(n)))