class QualidadeDados:

    def __init__(self):
        self.file = open("portalbio_export_27-08-2020-14-01-51.csv", "r")
        self.data = None
        self.file.close()

    def listdata(self):
        self.file = open("portalbio_export_27-08-2020-14-01-51.csv", "r")
        self.data = [[campo for campo in linha.split(';')] for linha in self.file.read().split('\n')[1:-1]]
        #print (self.data)
        self.file.close()

    def nivelTaxonomico(self):
        if self.data is None:
            self.listdata()
        coluna1 = [str(linha[15]) for linha in self.data]
        print (coluna1)
   
    def filtros(self): #CRIAR UM DICIONARIO COM A SIGLA E O NUMERO DE OCORRENCIA E AI ENVONTRAR O NUMERO DIGITANDO A SIGLA
        if self.data is None:
            self.listdata()
        #FILTRO ESTADOS
        estados = [str(linha[26]) for linha in self.data] #coluna dos estados   
        ocor = [estados.count(a) for a in estados] #coluna da ocorrencia
        dic_ocor = dict(zip(estados, ocor)) #dicionario 
        sigla = input("Digite uma sigla maiúscula: ") #ver questao da letra maiuscula e minuscula
        sigla = sigla.upper()
        print(dic_ocor[sigla]) 
        #FILTRO ESPECIE - CATEGORA de AMEAÇA
        especie = [str(linha[21]) for linha in self.data] #coluna das especies trans em linha
        especie = especie[0]
        categoria = [str(linha[23]) for linha in self.data] #coluna das especies trans em linha
        categoria = categoria[0]
        nome = input("Digite especie: ")
        if nome in especie:
            print(categoria) 
        else:
            print("Nome da especie esta escrita errada")
obj = QualidadeDados()
obj.listdata()
#obj.nivelTaxonomico()
obj.filtros()