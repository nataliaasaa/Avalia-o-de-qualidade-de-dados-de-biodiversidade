#Para utilizar uma função presente no pacote:
#Primeiro passo: pip install -i https://test.pypi.org/simple/ qualidadedados
#pip install opencage (Pacote utilizado na classe)

#from nome do pacote import nome do arquivo
from qualidadedados import qualidade_dados

#Nome_do_arquivo.classe().função()

#Mostra a média de dados Sem informação por coluna
qualidade_dados.QualidadeDados().dadosFaltantesPorColuna() 

#Mostra o nivelTaxonomico da ocorrencia
qualidade_dados.QualidadeDados().nivelTaxonomico()

#Recebe um estado (sigla) e retorna o número de indivíduos do arquivo registrados no estado indicado
qualidade_dados.QualidadeDados().filtros_estados()

#Recebe uma especie e retorna o nivel de ameaça
qualidade_dados.QualidadeDados().filtros_especie()

#Verifica se as coordenadas indicadas correspondem ao estado indicado
qualidade_dados.QualidadeDados().verificarCoordenadas()

