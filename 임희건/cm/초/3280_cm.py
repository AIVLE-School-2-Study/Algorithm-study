# 철수의 취미는 독서입니다. 그런데 책을 워낙 많이 읽다보니 어느 순간부터 읽었던 책의 내용이 잘 기억나지 않게 되었습니다. 
# 따라서 철수는 책에서 등장한 키워드와 해당 키워드가 위치한 페이지를 종이에 적어두고, 필요할 때마다 종이를 참고하기로 했습니다. 매번 종이에서 키워드를 찾느라 고생하는 철수를 본 당신은 철수를 위해 프로그램을 만들기로 했습니다.
# 키워드를 검색했을 때, 해당 키워드가 어느 페이지에 있는지 알려주는 프로그램을 작성해주세요.

# 예제 입력1
# 5
# abc 1
# word 10
# love 2
# like 5
# happy 30
# like
# 예제 출력1
# 5

# 예제 입력2
# 5
# abc 1
# word 10
# love 2
# like 5
# happy 30
# sky
# 예제 출력2
# -1

# 입력값 설명
# 첫째 줄에 키워드의 개수 N이 주어집니다. (1 ≤ N ≤ 1,000)
# 이어서 N개의 줄에 키워드와 해당 키워드가 위치한 페이지가 공백으로 구분되어 주어집니다. 중복되는 키워드는 존재하지 않습니다. 페이지는 10만 이하의 양의 정수입니다.
# 이어서 N+2번째 줄에 철수가 찾고 싶어하는 키워드가 주어집니다.
# 입력으로 주어지는 모든 키워드는 알파벳 소문자 1개 이상 10개 이하로 구성됩니다.

# 출력값 설명
# 키워드가 종이에 존재하면 해당 키워드가 위치한 페이지를 출력합니다.
# 키워드가 종이에 존재하지 않으면 -1을 출력합니다.