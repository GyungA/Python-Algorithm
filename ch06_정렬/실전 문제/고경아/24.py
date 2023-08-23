### 안테나
import sys

input = sys.stdin.readline

# 집의 수 N
n = input().strip()

# N채의 집의 위치
house = list(map(int, input().split()))

# 각 집의 위치를 돌면서, 다른 집들과의 거리의 총합의 최솟값을 구한다. (X)
# 최솟값을 만드는 집의 위치를 구한다. 여러 곳이면 작은 값. (O)
min_distance = 1e9
distance = 0
antenna = 0

for i in range(len(house)):
    for j in range(len(house)):
        if i == j:
            continue # 자기 자신은 피하기
        else:
            distance += abs(house[i] - house[j])
    if distance < min_distance:
        min_distance = distance
        antenna = house[i]
    elif distance == min_distance:
        antenna = house(min(antenna, house[i])) # 최솟값이 같으면 작은 값으로 도출
        print(f"antenna = {antenna}")

print(antenna)

"""
입력값
4
5 1 7 9
"""