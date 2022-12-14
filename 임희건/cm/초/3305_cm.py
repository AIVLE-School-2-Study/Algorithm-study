# 파스칼 피라미드는 파스칼의 삼각형을 3차원으로 확장한 개념으로 정수가 나열된 사면체의 모양을 하고 있습니다.
# 논의를 간단하게 하기 위해 밑면이 직각이등변삼각형인 삼각뿔 모양이라고 가정하겠습니다. 파스칼 피라미드를 만드는 방법은 다음과 같습니다.
# 1. 먼저 삼각뿔 맨꼭대기(1층)에 1행 1열에 1을 써넣습니다. 
# 2. 그 아래층의 i행 j열에는 바로 윗층 i행 j열, i-1행 j열, i행 j-1열의 요소들을 더한 값을 써넣습니다. 만약 윗층에 해당 요소가 없다면 0으로 간주합니다. 
# 파스칼 피라미드의 각 층을 분리해서 4층까지 표현하면 다음과 같습니다. 
# <1층>
# 1
# <2층>
# 1 1
# 1
# <3층>
# 1 2 1
# 2 2
# 1
# <4층>
# 1 3 3 1
# 3 6 3
# 3 3
# 1
# 정수 n이 입력될 때, 파스칼 피라미드 n층을 출력하는 프로그램을 작성해주세요.

# 예제 입력1
# 3
# 예제 출력1
# 1 2 1
# 2 2
# 1

# 예제 입력2
# 4
# 예제 출력2
# 1 3 3 1
# 3 6 3
# 3 3
# 1

# 입력값 설명
# 정수 n이 입력됩니다. (1 ≤ n ≤ 15)

# 출력값 설명
# 문제 예시와 같이 n줄에 걸쳐서 파스칼 피라미드의 n층을 출력합니다.

# 참고자료
# https://kingofbackend.tistory.com/94
# https://kingofbackend.tistory.com/93

import sys

n = int(sys.stdin.readline())   # 층 입력
ary = [[0] * 16 for _ in range(16)]    # 층을 표현할 리스트
ary[1][1] = 1    # 1층 초기값

# 2층 이상 리스트 연산
if n > 1:
    for _ in range(1, n):
        tmp = [[0] * 16 for _ in range(16)]

        for a in range(1, 16):
            for b in range(1, 16):
                tmp[a][b] = ary[a][b] + ary[a - 1][b] + ary[a][b - 1]

        ary = tmp.copy()

# 결과 출력
remove_set = {0}    # 임시로 넣어둔 0 삭제

for i in range(1, n + 1):
    result = [j for j in ary[i] if j not in remove_set]
    print(*result, sep = ' ')