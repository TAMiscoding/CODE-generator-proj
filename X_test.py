def generate_emoji_triangle():
    N=5
    E="😊"
    L=[]
    for i in range(1,N+1):
        C=2*i-1
        S=N-i
        L.append("  "*S+E*C)
    return "\n".join(L)

print(generate_emoji_triangle())