def fun2(*elementy):
    lista = []
    for i in elementy[0]:
        for j in elementy[1:]:
            if i not in j:
                break
        else:
            lista.append(i)
    return lista

print(fun2([1,2,3], (1,3,5), [3,2,1]))
print(fun2([1,2,3], (1,3,5), [3,2]))