def kminimizante(i, j, matrizC):
    minimo = matrizC[i][j-1] + matrizC[j][j]
    kmin = 0
    #print("\ni=", i, "j=", j)
    for k in range((i+1),j+1):
        temp = matrizC[i][k-1] + matrizC[k][j]
        #print("\ntemp =", temp, ", minimo =", minimo)
        if(temp <= minimo):
            minimo = temp
            kmin = k
            
    return [minimo, kmin]
    
#--------------------------
#dados de entrada do problema
j = 5
jlinha = 5
vetorj = [0,10,1,3,2]
vetorjlinha = [2,1,1,1,1]
#fim dados de entrada 
#--------------------------

matrizC = [ [0 for i in range(jlinha)] for h in range(j)]
matrizF = [ [0 for i in range(jlinha)] for h in range(j)]
matrizK = [ [0 for i in range(jlinha)] for h in range(j)]

#inicializando matriz C com diagonal zero
#inicializando matriz F com diagonal vetor jlinha
for i in range(jlinha):
    matrizC[i][i] =0
    matrizF[i][i] =vetorjlinha[i]

#iniciando a programacao dinamica...
for d in range(1,jlinha,1):    
    for i in range(jlinha-d):        
        j = i+d
        matrizF[i][j] = matrizF[i][j-1] + vetorj[j] + vetorjlinha[j]
        #print("\nvalor d=",d)
        lista = kminimizante(i,j, matrizC)
        #print (lista[1])
        matrizC[i][j] = lista[0] + matrizF[i][j]
        matrizK[i][j] = lista[1]
       # print (matrizF[i][j])


print ("matriz C=", matrizC)
print ("matriz F=", matrizF)
print ("matriz K=", matrizK)



