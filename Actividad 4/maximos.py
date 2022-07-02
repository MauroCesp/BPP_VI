import pdb

pdb.set_trace()
def tarea4(lista):
    for i in lista:
        maximo = [x for x in i if x == max(i)]
        print(maximo)

if __name__ == '__main__':
    lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
    tarea4(lista)
