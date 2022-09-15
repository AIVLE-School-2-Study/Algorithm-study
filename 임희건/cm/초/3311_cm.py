# 또리는 클럽의 관리자입니다.
# 클럽은 xy 좌표계로 표현할 수 있으며, N명의 각 사람이 서 있는 위치를 (x, y) 형태의 좌표로 나타낼 수 있습니다. 반지름이 R인 원에 최대한 많은 사람을 포함시킬 수 있도록 원의 위치를 적절히 정했을 때, 이 원을 Hot place라고 합니다.
# 이때 Hot place의 중심의 좌표를 공백으로 구분하여 출력하세요.
# 단, Hot place의 중심은 정수 좌표여야 합니다.


# 예제 입력1
# 4 1
# 1 0
# 0 1
# -1 0
# 0 -1
# 예제 출력1
# 0 0

# 예제 입력2
# 4 4
# 1 0
# 0 1
# -1 0
# 0 -1
# 예제 출력2
# -3 0

# 입력값 설명
# 첫째줄에 두 정수 N과 R (1 ≤ N, R ≤ 20) 이 주어집니다.
# 둘째줄부터 N개의 줄에 걸쳐 사람의 위치를 나타내는 두 정수 x, y (-100 ≤ x, y ≤ 100) 가 주어집니다.

# 출력값 설명
# 사람을 가장 많이 포함하는 Hot place의 중심의 좌표를 공백을 구분하여 출력하세요.
# 답이 여러 개면 사전순으로 가장 앞서는 좌표를 출력하세요.
# 두 순서쌍 (x, y), (a, b) 에 대해 x < a 이거나 (x = a 이고 y < b) 일 때 (x, y)가 (a, b) 보다 사전순으로 앞선다고 표현합니다.