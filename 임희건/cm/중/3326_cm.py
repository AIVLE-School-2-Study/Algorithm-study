# 어린이 또리는 그래프를 너무나도 사랑합니다. 특히 아름답다고 생각하는 그래프도 있어서, 그 그래프를 그려서 벽에 붙여놓기까지 했습니다. 하지만 어린이 또리에겐 그래프는 너무 비싸서 용돈을 모아서는 영원히 살 수 없습니다.
# 또리의 아버지는 크리스마스 선물로 또리에게 그래프를 사주려고 합니다. 특히 또리가 벽에 붙여놓은 그래프와 같은 그래프를 사주면 기뻐할 것입니다.
# 그래프 상점에 온 또리의 아버지는 수많은 그래프들이 놓여있는 것을 보았습니다. 이 그래프들 중 하나와 또리가 벽에 붙여놓은 그래프가 주어질 때 두 그래프가 같은 그래프인지 출력하는 프로그램을 작성해주세요.
# 한 그래프의 정점 번호를 적절히 바꾸었을 때 두 그래프의 정점의 집합과 간선의 집합이 서로 같다면, 두 그래프는 같은 그래프입니다.

# 예제 입력1
# 3 2
# 1 2
# 2 3
# 3 2
# 3 1
# 2 1
# 예제 출력1
# YES

# 예제 입력2
# 4 4
# 1 2
# 2 3
# 3 4
# 4 1
# 4 4
# 1 2
# 2 3
# 3 1
# 1 4
# 예제 출력2
# NO

# 입력값 설명
# 첫 번째 줄에 첫 번째 그래프의 정점의 개수 N1와 간선의 개수 M1가 주어집니다. (1 ≤ N1 ≤ 10, 0 ≤ M1 ≤ 45)
# 이후 M1줄에 걸쳐, 첫 번째 그래프의 간선을 나타내는 (u, v)가 공백으로 구분되어 주어집니다. (1 ≤ u,v ≤ N1)
# 그 다음 줄에 두 번째 그래프의 정점의 개수 N2와 간선의 개수 M2가 주어집니다. (1 ≤ N2 ≤ 10, 0 ≤ M2 ≤ 45)
# 이후 M2줄에 걸쳐, 두 번째 그래프의 간선을 나타내는 (u, v)가 공백으로 구분되어 주어닙니다. (1 ≤ u,v ≤ N2)
# 주어지는 모든 그래프에는 self-loop와 multiple edge가 존재하지 않습니다.

# 출력값 설명
# 두 그래프가 같으면 "YES", 그렇지 않으면 "NO"를 출력합니다.