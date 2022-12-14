# 어느 날 선생님이 프로그래밍 숙제를 내주셨습니다. 학생들은 자바와 파이썬 중 원하는 언어를 하나 골라 프로그램을 작성해야 합니다. 수업에 집중하지 않은 재승이는 자바로도 숙제를 하고 파이썬으로도 숙제를 한 뒤에야 둘 중 하나만 제출할 수 있음을 깨달았습니다.
# 재승이는 결국 둘 중 수행 시간이 상대적으로 짧은 프로그램을 제출하려고 합니다. 만일 똑같다면 자바로 작성한 프로그램을 제출하기로 합니다. 두 프로그램의 수행 시간이 주어지면 어느 언어로 작성한 프로그램을 제출해야 할지 알려주세요.
# 수행 시간은 "정수 부분.소수 부분s" 형식으로 주어집니다. 정수 부분은 1이상 1000이하이고, 소수 부분은 1자리 이상 4자리 이하임이 보장됩니다. s는 초단위로 측정했음을 의미합니다.

import sys

J = sys.stdin.readline()
P = sys.stdin.readline()

J = J[:-2]
P = P[:-2]

if float(J) <= float(P):
    print("JAVA")
    
else:
    print("PYTHON")