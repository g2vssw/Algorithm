n, m = input().split()

n_rev = int(n[::-1])
m_rev = int(m[::-1])

if n_rev > m_rev:
    print(n_rev)
else:
    print(m_rev)