# 민겸이는 학생들을 가르치는 교사입니다.
# 민겸이는 N명의 학생들을 일렬로 세워 쪽지 시험을 보게 했습니다. 쪽지 시험에서 P점 이상을 받은 학생들은 상을 받습니다. 또한 P점 미만의 학생들 중에서도 좌우로 인접한 P점 이상의 점수를 받은 학생이 한 명 이상이면 그 학생은 상을 받습니다.
# 민겸이가 상을 줄 수 있는 학생의 수의 최댓값은 K입니다. K명 이하의 학생에게 상을 주면서 가능한 한 많은 학생들이 상을 받을 수 있는 P의 최댓값을 구하세요.
# 이때, 상을 받는 학생이 없을 수도 있습니다.

# 예제 입력1
# 5 3
# 50 30 40 50 70
# 예제 출력1
# 70

# 예제 입력2
# 5 4
# 80 60 100 75 70
# 예제 출력2
# 80

# 입력값 설명
# 입력의 첫 번째 줄에는 학생의 수 N, 합격시킬 학생의 수 K가 공백으로 구분되어 주어집니다. (1 ≤ K ≤ N ≤ 10)
# 입력의 두 번째 줄에는 1번째, 2번째, …, N번째 학생의 점수가 1 이상 100 이하의 정수로 공백으로 구분되어 주어집니다.

# 출력값 설명
# K명 이하의 학생에게 상을 주면서 가능한 한 많은 학생들이 상을 받을 수 있게 하는 커트라인 중 가장 큰 것을 출력하세요. 이때, 상을 받을 수 있는 학생이 없을 수도 있다는 사실에 유의하세요.