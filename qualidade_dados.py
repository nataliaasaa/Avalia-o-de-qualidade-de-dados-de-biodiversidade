
class QualidadeDados:

    # Método que implementa um objeto, e o atribui à um arquivo
    def __init__(self):
        self.file = open("portalbio_export_27-08-2020-14-01-51.csv", "r")
    

    #Ler o arquivo e retorna uma lista[]
    def readData(self):
        self.dataList = self.file.readlines()
        self.dataLines = [l.rstrip().split(";") for l in self.dataList]
        #print(self.dataList)
        #print(self.dataLines)
        return self.dataLines
    

    #Retorna a representação do objeto, sendo chamada com 'print(objeto)'
    def __str__(self):
        print('Dados em lista: ' + str(type(self.readData())))
        return 'Representação dos dados nas classes'


    #Tranformar dados em uma lista com dicionários:
    def transformToDict(self):

        print(self.dataLines[0:1])
        print("\n")

        dataDict = {}

        for (object) in self.dataLines:
            dataDict[object[0]] = object[1:]
        return (dataDict)
    
       
    #Atividade 01 - Retorna os Dados Faltantes:

    def contarInformacoesFaltantes(self):

        #print(self.dataLines[:1])
        #print(self.dataLines[2])
        #print(self.dataLines[3])

        countObj = 0 #Contador de objetos da lista
        countAtb = 0 #Contador atributos do objeto
        contadorFaltante = 0
        contFaltantePorColuna = [] # Implementar esta Parte

        media = 0

        for object in self.dataLines:
            countObj += 1         

            for atribute in object:
                countAtb += 1

                if not atribute or atribute == 'Sem Informações':                    
                    contadorFaltante += 1    

        
        #print(countObj)
        #print(countAtb)
        print("A quatidade de atributos é: " + str(contadorFaltante))
        
        atributosTotais = countObj * countAtb        
        print("A quatidade de atributos é: " + str(atributosTotais))

        media = contadorFaltante/atributosTotais * 100
        print("A média de atributos faltantes é: " + str(media))

        return atributosTotais, contadorFaltante


objeto1 = QualidadeDados()
print(objeto1)
print("\n")
print(objeto1.contarInformacoesFaltantes())
print("")


