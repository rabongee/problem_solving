n = int(input()) # len(n_list)
n_list = set(map(int, input().split()))
m = int(input()) # len(m_list)
m_list = list(map(int, input().split()))
for i in m_list:
    print(1) if i in n_list else print(0)