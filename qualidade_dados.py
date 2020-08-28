class QualidadeDados:

    def __init__(self):
        self.file = open("portalbio_export_27-08-2020-14-01-51.csv", "r")
        self.data = None

    def listdata(self):
        self.data = [[campo for campo in linha.split(';')] for linha in self.file.read().split('\n')[1:-1]]
        #print (self.data)
        self.file.close()

    def nivelTaxonomico(self): #verifica até qual nivel taxonomico a ocorrência foi identificada (0 a 6) 
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
             
obj = QualidadeDados()
obj.listdata()
obj.nivelTaxonomico()