def qoshilish(n,m):
    n.insert(1, 'Bread')
    n.insert(3,'Bread')
    n.append(m)
    return n
print(qoshilish(["tuna", "ham", "tomato"], "ham"))
print(qoshilish(["cheese", "lettuce"], "cheese"))