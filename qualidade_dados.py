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

obj = QualidadeDados()
obj.listdata()
obj.nivelTaxonomico()