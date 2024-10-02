import sys
input = sys.stdin.readline  # 빠른 입력을 위해 사용

# n: 구간의 수, m: 쿼리의 수, t: 최대 시간
n, m, t = map(int, input().split())
a = []  # 시작 시간 리스트
b = []  # 종료 시간 리스트

# 각 구간의 시작과 종료 시간을 입력 받음
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

# 시간 t에 대한 카운트를 초기화
cnt = [0] * t

# 각 쿼리 처리
for _ in range(m):
    c, d = map(int, input().split())
    c -= 1  # 인덱스 조정 (0부터 시작)
    d -= 1  # 인덱스 조정
    l = max(a[c], a[d])  # 두 구간의 시작 시간 중 최대값
    r = min(b[c], b[d])  # 두 구간의 종료 시간 중 최소값
   
    # 겹치는 구간이 있을 경우 카운트
    if l < r:
        cnt[l] += 1  # 겹치는 시작 지점에서 1 추가
        if r < t:
            cnt[r] -= 1  # 겹치는 종료 지점에서 1 제거

# 구간 합을 통해 각 시간에 대한 총 카운트 계산
for k in range(1, t):
    cnt[k] += cnt[k - 1]

# 결과 출력
print('\n'.join(map(str, cnt)))