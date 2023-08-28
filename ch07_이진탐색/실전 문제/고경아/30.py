### 가사 검색
import sys

input = sys.stdin.readline

words = input().split()
queries = input().split()

def solution(words, queries):
    # words와 queries를 각각 알파벳순으로 정렬한다
    # queries를 하나씩 꺼내어 words를 돈다. 첫 글자가 일치하면 단어를 비교한다? -> 이진탐색 단원이고 이렇게 하면 너무 오래 걸림
    # queries를 하나씩 꺼내어 words의 중간부터 이진탐색을 돌며 첫 글자가 일치하는 순간부터 단어를 비교한다? -> 첫 글자가 와일드이면 안됨..

    # words와 queries를 글자 수 기준으로 정렬한다. query를 들고 word에서 이진 탐색을 돌며 글자 수가 같은 것만 글자를 비교한다.
    #   자칫 다시 완전탐색에 빠지지 않도록 유의!(글자수가 같은 모든 값을 한 번에 꺼낸다든가 하는...)
    sorted_words = sorted(words, key=len) # 정렬
    sorted_queries = sorted(queries, key=len)
    start = 0
    end = len(sorted_words)

    answer = []
    temp_answer = 0
    for q in queries:
        mid = (start + end) // 2
        if len(sorted_words[mid]) > len(q):
            end = mid - 1
        elif len(sorted_words[mid]) < len(q):
            start = mid + 1
        elif len(sorted_words[mid]) == len(q):
            idx = mid
            # 글자수가 같은 것들 덩어리에서 가장 왼쪽으로 간다 (이렇게 추잡해지면 일단 모범답안은 아니겠지만...)
            while len(sorted_words[idx]) == len(q):
                idx -= 1
                if idx == 0: # words 원소의 맨 앞까지 가도 여전히 글자 수가 같으면, 더 왼쪽으로 가지 말고 나온다.
                    break

        for i in range(idx, len(sorted_words) + 1): # 글자 수가 같은 부분부터 가사를 돈다
            for j in range(len(q)): # 한 글자씩 비교한다




    # 글자 수가 같은 가사 원소의 가장 왼쪽부터, 글자 수가 달라질 때까지 오른쪽으로 이동하며, 글자가 같으면 카운트한다.
    while len()
        answer.append(temp_answer) # 각 쿼리별로 일치하는 가사의 개수를 순서대로 저장한다.
    # 글자 비교는 와일드카드 문자가 있는 쪽의 반대편부터 시작한다.


    return answer

solution(words, queries)

"""
입력값
frodo front frost frozen frame kakao
fro?? ????o fr??? fro??? pro?
"""