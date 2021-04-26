fichero=open("datos.txt")
def eliminar(tam,linea):
    lin=linea[tam-1]
    devolver=""
    for i in lin:
        if i!="\n":
            devolver=devolver+i
    linea[tam-1]=devolver
    return linea
def concadenar(a,b):
    devo=""
    for i in a:
        devo=devo+i+" "
    for i in b:
        devo=devo+i+" "
    return devo


par=True
final=""
fichero2 = open("datosBien.txt","w")
for e in fichero:
    split=e.split(" ")
    solu=eliminar(len(split), split)
    
    if par:
        linea=solu
        par=False
    else:
        lina=concadenar(linea,solu)
        linea=(lina+"\n")
        par=True
        fichero2.write(linea)
        linea=""


