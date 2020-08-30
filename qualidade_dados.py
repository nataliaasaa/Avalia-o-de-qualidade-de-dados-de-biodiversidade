'''
Para cada coluna identique a quantidade de linhas com dados faltantes (em alguns casos, o dado faltante é uma string vazia, em outros casos é uma string contendo algum valor do tipo: "sem informação"). Faça um método que retorna a média de dados faltantes por coluna
'''

class QualidadeDados:

       
    # Método que implementa um objeto, e o atribui à um arquivo
    def __init__(self):
        self.file = open("portalbio_export_27-08-2020-14-01-51.csv", "r")

        self.dataList = self.file.readlines()
        self.dataLines = [l.rstrip().split(";") for l in self.dataList]
        #print(self.dataList)
        #print(self.dataLines)
        self.headLista = self.dataLines[0]  #Lista com os atributos da Head do arquivo
        self.dataDictList = []


    #Retorna a representação do objeto, sendo chamada com 'print(objeto)'
    def __str__(self):
        print('Dados em lista: ' + str(type(self.dataLines)))
        return 'Representação dos dados nas classes'


    #Tranformar dados em uma lista com dicionários:
    def transformToDictList(self):

        if len(self.dataDictList) == 0:

            #print(self.dataLines[:1])
            #print("\n")

            #linha = objeto
            for linha in self.dataLines[1:]:
                dataDict = {}
                #Montar um único dicionário por linha
                for i, key in enumerate(self.headLista):
                #for (i=0, i++, i < len(headLista))
                    #key = headLista[i] 
                    dataDict[key] = linha[i]
                    
                self.dataDictList.append(dataDict)

        return self.dataDictList
    

    #Identificar a quantidade de linhas com dados faltantes para cada coluna, e fazer a média desses dados:

    def dadosFaltantesPorColuna(self):
        
        totalPorColuna = len(self.dataDictList)
        dictFaltantes = {} 

        for coluna in self.headLista:

            count = len([item for item in self.dataDictList if item[coluna] == "Sem Informações"])
            #print(coluna, count)
            print(len(self.dataDictList))
            dictFaltantes[coluna] = count

        print (dictFaltantes)    
        
        #Dividir todos os valores do dictFaltantes / totalPorColuna 
        somaItensFalantesPorColuna = sum(dictFaltantes.values())

        #somaItensFalantesPorColuna / dividir por len(self.headLista)
        mediaItensFalantesPorColuna = somaItensFalantesPorColuna / len(self.headLista)


        return (somaItensFalantesPorColuna, mediaItensFalantesPorColuna)


    '''   
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
        print("A quatidade total de atributos faltantes é: " + str(contadorFaltante))
        
        atributosTotais = countObj * countAtb        
        print("A quatidade de atributos é: " + str(atributosTotais))

        media = contadorFaltante/atributosTotais * 100
        print("A média de atributos faltantes é: " + str(media))

        return atributosTotais, contadorFaltante
        '''


objeto1 = QualidadeDados()
print(objeto1)
print("\n")
#print(objeto1.contarInformacoesFaltantes())
print("")
#print(objeto1.transformToDictList())
print("\n")

#Exibir todas as localidades :
localidades = [item["Localidade"] for item in objeto1.transformToDictList()]
print("localidade:\n", localidades)

#Exibir todas as localidades onde a categoria de ameaça é vulnerável
localidadesVulneraveis = [item["Localidade"] for item in objeto1.transformToDictList() if item["Categoria de Ameaca"] == "Vulnerável"]
print("localidadeVulneraveis:\n", localidadesVulneraveis)

 #Para cada coluna identique a quantidade de linhas com dados faltantes
print(objeto1.dadosFaltantesPorColuna())

