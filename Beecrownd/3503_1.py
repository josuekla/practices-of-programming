from collections import deque
fila = deque()
            

X, Y, N = map(int, input().split())

A = list(map(int, input().split()))

fila.append((X,0))

visitados = [False] * 100001
visitados[X] = True 
find = False

while fila:
    numero, passos = fila.popleft()
    if numero == Y:
        print(passos)
        find = True
        break

    novo_passo = passos + 1
    
    for valor in A:
        novo = numero + valor
        if 1 <= novo <= 100000 and not visitados[novo]:
            visitados[novo] = True
            fila.append((novo, novo_passo))
            
        novo = numero - valor
        if 1 <= novo <= 100000 and not visitados[novo]:
            visitados[novo] = True
            fila.append((novo, novo_passo))
            
        if numero <= 100000 // valor:
            novo = numero * valor
        if 1 <= novo <= 100000 and not visitados[novo]:
            visitados[novo] = True
            fila.append((novo, novo_passo))
            
        if numero % valor == 0:
            novo = numero // valor
            if 1 <= novo <= 100000 and not visitados[novo]:
                visitados[novo] = True
                fila.append((novo, novo_passo))
            
        
    # fila.append(soma(X, valor))
    # fila.append(sub(X, valor))
    # fila.append(mul(X, valor))
    # fila.append(div(X, valor))
    
if not find: print(-1)
# print(fila)
# print(visitados)