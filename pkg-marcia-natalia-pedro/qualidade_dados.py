from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError
from pprint import pprint

key = '5b7a26bfcd904e07a49f085037f6d7ba'
geocoder = OpenCageGeocode(key)

class QualidadeDados:

    def __init__(self):
        self.path = input("Digite o caminho do arquivo: ")
        self.file = open(self.path, "r")
        self.data = None
        #Cria uma lista com elementos separados por virgula

        self.dataList = self.criarLista()

        #Cria uma lista de listas
        self.dataLines = [l.rstrip().split(";") for l in self.dataList]
        #Cria uma lista contendo somente o cabeçalho do arquivo
        self.headLista = self.dataLines[0]  #Lista com os atributos da Head do arquivo
        #Cria uma lista com os dicionários, cada um representando uma linha do arquivo 
        self.dataDictList = []

    def listdata(self):
        self.data = [[campo for campo in linha.split(';')] for linha in self.file.read().split('\n')[1:-1]]
        #print (self.data)
        self.file.close()

    #Retorna a representação do objeto, sendo chamada com 'print(objeto)'
    def __str__(self):
        print('Dados em lista: ' + str(type(self.dataLines)))
        return 'Representação dos dados nas classes'

    #Método que cria uma lista com items separados por virgula
    def criarLista(self):
        with open (self.path, "r") as file:
            dataList = file.readlines()
            return dataList

    #Tranformar dados em uma lista com dicionários:
    def transformToDictList(self):

        if len(self.dataDictList) == 0:

            #linha = objeto
            for linha in self.dataLines[1:]:
                dataDict = {}
                #Montar um único dicionário por linha
                for i, key in enumerate(self.headLista):
                    dataDict[key] = linha[i]
                    
                self.dataDictList.append(dataDict)
        return (self.dataDictList)
    

    #Identificar a quantidade de linhas com dados faltantes para cada coluna, e fazer a média desses dados:

    def dadosFaltantesPorColuna(self):
        
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
        #print("A médoa dos itens faltantes por coluna: " + str(mediaItensFalantesPorColuna))

        return(mediaItensFalantesPorColuna)    

    def nivelTaxonomico(self): #verifica até qual nivel taxonomico a ocorrência foi identificada (0 a 6).
        if self.data is None:
            self.listdata()
        num = 0
        for linha in self.data:
            count = 0
            num += 1
            for i in linha[15:21]:
                if i == 'Sem Informações':
                    count = 0
                else:
                    count += 1
            print ("Nivel taxonômico da ocorrência", num+1, ": ", count)
   

    def filtros_estados(self): #CRIAR UM DICIONARIO COM A SIGLA E O NUMERO DE OCORRENCIA E AI ENVONTRAR O NUMERO DIGITANDO A SIGLA
        if self.data is None:
            self.listdata()
        #FILTRO ESTADOS
        estados = [str(linha[26]) for linha in self.data] #coluna dos estados   
        ocor = [estados.count(a) for a in estados] #coluna da ocorrencia
        dic_ocor = dict(zip(estados, ocor)) #dicionario 
        sigla = input("Digite o estado desejado (sigla): ") 
        sigla = sigla.upper()
        if sigla in estados:
            print("Número de espécies em", sigla, ":", dic_ocor[sigla]) 
        else:
            print ("Sigla não encontrada.")
    
    def filtros_especie(self):
        if self.data is None:
          self.listdata()
        #FILTRO ESPECIE - CATEGORA de AMEAÇA
        especie = [str(linha[21]) for linha in self.data] #coluna das especies trans em linha
        especie_prim = [str.split(linha[21])[0] for linha in self.data]#coluna do primeiro nome das especies trans em linha
        especie_seg = [str.split(linha[21])[1] for linha in self.data]#coluna do segundo nome das especies trans em linha
        categoria = [str(linha[23]) for linha in self.data] #coluna das categorias de ameaça trans em linha
        dic_cat = dict(zip(especie, categoria)) #dicionario
        dic_cat_prim = dict(zip(especie_prim, categoria)) #dicionario
        dic_cat_seg = dict(zip(especie_seg, categoria)) #dicionario
        nome = input("Digite especie: ")
        if nome in dic_cat:
            print(dic_cat[nome]) 
        elif nome in dic_cat_prim:
            print(dic_cat_prim[nome])
        elif nome in dic_cat_seg:
            print(dic_cat_seg[nome])
        else:
            print("Nome inexistente")        

    def numTotalIndividuos(self): #Retorna o número total de indivíduos do arquivo.
        if self.data is None:
            self.listdata()
        
        individuos = [int(linha[14]) for linha in self.data]
        print ("Número total de indivíduos no arquivo: ", sum(individuos))

    def verificarCoordenadas(self): #Verifica se as coordenadas da ocorrência correspondem ao estado indicado. 
        if self.data is None:
            self.listdata()
        count = 0
        for linha in self.data:
            try:
                results = geocoder.reverse_geocode(float(linha[29]), float(linha[30]), language='pt')
                if results and len(results):
                    count += 1
                    coord = (results[0]['components']['state_code'])
                    #print (coord)
                    #if coord == linha[26]:
                     #   print ("A coordenada corresponde ao estado.")
                if coord != linha[26]:
                    print ("A coordenada da ocorrência", count+1, "não correspode ao estado da ocorrência")
                                            
            except InvalidInputError as ex:
                print(ex)      


obj = QualidadeDados()
obj.listdata()
#obj.transformToDictList()
#print("A média dos dados faltantes por coluna: " + str(obj.dadosFaltantesPorColuna()))
#obj.nivelTaxonomico()
#obj.filtros_estados()
#obj.filtros_especie()
#obj.verificarCoordenadas()
#obj.numTotalIndividuos()
