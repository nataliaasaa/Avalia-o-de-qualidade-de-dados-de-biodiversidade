from opencage.geocoder import OpenCageGeocode
from pprint import pprint
key = '942bc37914024732927948522464540e'
geocoder = OpenCageGeocode(key)

class QualidadeDados:

    def __init__(self):
        self.file = open("portalbio_export_27-08-2020-14-01-51.csv", "r")
        self.data = None

    def listdata(self):
        self.data = [[campo for campo in linha.split(';')] for linha in self.file.read().split('\n')[1:-1]]
        #print (self.data)
        self.file.close()

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
                    #if coord == linha[26]:
                        #print ("A coordenada corresponde ao estado.")
                    if coord != linha[26]:
                        print ("A coordenada da ocorrência", count+1, "não correspode ao estado da ocorrência")
                                            
            except RateLimitExceededError as ex:
                print(ex)





obj = QualidadeDados()
obj.listdata()
#obj.nivelTaxonomico()
obj.verificarCoordenadas()
