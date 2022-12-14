# 철수는 본인이 운영하는 쇼핑몰의 광고 영상을 TV에 게재하려고 합니다.광고 영상은 시작부터 끝까지 총 K초이고, 반드시 연속해서 재생해야 합니다. 즉, 영상을 두 개 이상의 구간으로 나눠서 재생할 수 없습니다.
# 방송국에 문의한 결과, 두 방송 프로그램 사이 광고 시간 N초 중에서 원하는 구간을 초 단위로 선택하라는 답변을 받았습니다.
# 단, 이미 다른 광고가 예약되어 있는 시간에는 광고를 게재할 수 없습니다.
# 철수는 고도로 발전된 AI 기술을 통해 광고 효과를 예측하는 데 성공했습니다. 따라서 철수는 어떤 시점에 광고를 진행했을 때 얼만큼의 구매가 발생하는지 정확히 알고 있습니다.
# 철수의 광고를 통해 발생할 수 있는 구매량의 최댓값이 얼마인지 구하는 프로그램을 작성해주세요.

# 예제 입력1
# 5 2
# 1 2 10 1 3
# 예제 출력1
# 12

# 예제 입력2
# 5 3
# 100 0 1 2 3
# 예제 출력2
# 6

# 입력값 설명
# 첫째 줄에 전체 광고 시간과 철수가 게재하려는 광고 영상의 길이를 의미하는 두 개의 양의 정수 N과 K가 공백으로 구분되어 주어집니다. (1 ≤ K ≤ N ≤ 20)
# 둘째 줄에는 광고 효과를 의미하는 N개의 정수 a_1, a_2, …, a_N이 공백으로 구분되어 주어집니다. a_i는 i-1초에서 i초 사이에 발생하는 구매량을 의미합니다. a_i = 0인 경우, i-1초에서 i초 사이에 이미 다른 광고가 예약되어 있음을 의미합니다. (0 ≤ a_i ≤ 1,000)
# 단, 철수가 광고를 진행하지 못하는 경우는 입력으로 주어지지 않습니다.

# 출력값 설명
# 첫째 줄에 정답을 출력합니다.