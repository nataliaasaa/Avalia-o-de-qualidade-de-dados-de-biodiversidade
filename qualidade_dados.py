'''
Para cada coluna identique a quantidade de linhas com dados faltantes (em alguns casos, o dado faltante é uma string vazia, em outros casos é uma string contendo algum valor do tipo: "sem informação"). Faça um método que retorna a média de dados faltantes por coluna
'''

class QualidadeDados:

       
    # Método que implementa um objeto, e o atribui à um arquivo
    def __init__(self):
        self.file = open("portalbio_export_27-08-2020-14-01-51.csv", "r")

        #Cria uma lista com elementos separados por virgula
        self.dataList = self.file.readlines()
        #Cria uma lista de listas
        self.dataLines = [l.rstrip().split(";") for l in self.dataList]
        
        #print(self.dataList)
        #print(self.dataLines)
        
        #Cria uma lista contendo somente o cabeçalho do arquivo
        self.headLista = self.dataLines[0]  #Lista com os atributos da Head do arquivo
        #Cria uma lista com os dicionários, cada um representando uma linha do arquivo 
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

        return (self.dataDictList)
    

    #Identificar a quantidade de linhas com dados faltantes para cada coluna, e fazer a média desses dados:

    def dadosFaltantesPorColuna(self):
        
        totalPorColuna = len(self.dataDictList)
        dictFaltantes = {} 

        for coluna in self.headLista:

            count = len([item for item in self.dataDictList if item[coluna] == "Sem Informações"])
            #print(coluna, count)
            #print(len(self.dataDictList))
            dictFaltantes[coluna] = count

        #Dicionários dos items faltantes em cada coluna:
        #print(dictFaltantes)    
        
        #Soma todos os valores de items faltantes nas colunas(dictFaltantes.values()): 
        somaItensFalantesPorColuna = sum(dictFaltantes.values())
        #print("A soma dos itens faltantes: " + str(somaItensFalantesPorColuna))

        #somaItensFalantesPorColuna / dividir por len(self.headLista):
        mediaItensFalantesPorColuna = somaItensFalantesPorColuna / len(self.headLista)
        print("A médoa dos itens faltantes por coluna: " + str(mediaItensFalantesPorColuna))

        return(dictFaltantes)


#Tests: 

objeto1 = QualidadeDados()
print(objeto1)
print("\n")

#Mostrar a lista com os dicinários:
print(objeto1.transformToDictList())
print("\n")

#Exibir todas as localidades :
#localidades = [item["Localidade"] for item in objeto1.transformToDictList()]
#print("localidade:\n", localidades)

#Exibir todas as localidades onde a categoria de ameaça é vulnerável
#localidadesVulneraveis = [item["Localidade"] for item in objeto1.transformToDictList() if item["Categoria de Ameaca"] == "Vulnerável"]
#print("localidadeVulneraveis:\n", localidadesVulneraveis)

#Para cada coluna identique a quantidade de linhas com dados faltantes, e a média de dados faltantes por coluna
print(objeto1.dadosFaltantesPorColuna())


