## Queremos criar um algorítmo para ordenar as abas dos bonés de uma torcida
## Portanto, ou todos devem estar virador para Frente ou Atras

def Conform(lista_individuos):

    
    for i in range(len(lista_individuos)):

        if lista_individuos[i] != lista_individuos[i-1]:                    ## passar o if por agrupamentos de F's e A's
            if lista_individuos[i] != lista_individuos[0]:                    ## bifurcar as ações condicionais para os grupos F's ou A's

                print('From, ', i , end=' ')

            else:

                print(' till ', i-1, ', you must turn')

##note que o algoritmo só paraa uma vez, positivamente, pelo segundo if. 

lista_individuos = [ 'F', 'F', 'F', 'F', 'A', 'A', 'F', 'A', 'F', 'A', 'A', 'F', 'A', 'F']
Conform(lista_individuos)


    
