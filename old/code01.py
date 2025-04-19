# 入力を受け取る
import sys
input = sys.stdin.read
data = input().split()

# NとKを取得
N = int(data[0])
K = int(data[1])

# 配列Aの要素を取得し、Kを加算
A = []
for i in range(2, 2 + N):
    A.append(int(data[i]) + K)

# 結果を出力
for value in A:
    print(value)
