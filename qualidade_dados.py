from opencage.geocoder import OpenCageGeocode
from opencage.geocoder import InvalidInputError, RateLimitExceededError, UnknownError
from pprint import pprint
key = '567331141def4c669c7b0b0ba8342942'
geocoder = OpenCageGeocode(key)

class QualidadeDados:

    def __init__(self):
        self.file = open("portalbio_export_27-08-2020-14-01-51.csv", "r")
        self.data = None
        #Cria uma lista com elementos separados por virgula
        #self.dataList = self.file.readlines()
        #Cria uma lista de listas
        #self.dataLines = [l.rstrip().split(";") for l in self.dataList]
        #Cria uma lista contendo somente o cabeçalho do arquivo
        #self.headLista = self.dataLines[0]  #Lista com os atributos da Head do arquivo
        #Cria uma lista com os dicionários, cada um representando uma linha do arquivo 
        #self.dataDictList = []


    def listdata(self):
        self.data = [[campo for campo in linha.split(';')] for linha in self.file.read().split('\n')[1:-1]]
        #print (self.data)
        self.file.close()
        
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

    def nivelTaxonomico(self): #verifica até qual nivel taxonomico a ocorrência foi identificada (0 a 6).
        if self.data is None:
            self.listdata()

        for linha in self.data:
            count = 0
            for i in linha[15:21]:
                if i == 'Sem Informações':
                    count = 0
                else:
                    count += 1
            print ("Nivel taxonômico da ocorrência : ", count)
   
    def filtros_estados(self): #CRIAR UM DICIONARIO COM A SIGLA E O NUMERO DE OCORRENCIA E AI ENVONTRAR O NUMERO DIGITANDO A SIGLA
        if self.data is None:
            self.listdata()
        #FILTRO ESTADOS
        estados = [str(linha[26]) for linha in self.data] #coluna dos estados   
        ocor = [estados.count(a) for a in estados] #coluna da ocorrencia
        dic_ocor = dict(zip(estados, ocor)) #dicionario 
        sigla = input("Digite uma sigla maiúscula: ") 
        sigla = sigla.upper()
        print(dic_ocor[sigla]) 
    def filtros_especie(self):
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
                                            
            except RateLimitExceededError as ex:
                print(ex)      

obj = QualidadeDados()
obj.listdata()
#print(obj.transformToDictList())
#print("\n")
#print(obj.dadosFaltantesPorColuna())
#obj.nivelTaxonomico()
obj.filtros_especie()
#obj.verificarCoordenadas()
