arr = [1, 1, 6, 6, 1]
st = {}
res = set()
for i in arr:
    st[i] = st.get(i, 0) + 1
    res.add(i if st[i] < 2 else str(i) * st[i])
print(*res)
print(st)








