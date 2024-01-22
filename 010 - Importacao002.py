from datetime import datetime

data_texto = "20/07/2024"

formato_data = datetime.strptime(data_texto, "%d/%m/%Y").date()

print(formato_data, type(formato_data))

outra_data_texto = '2022-04-20'

outro_formato_data = datetime.strptime(outra_data_texto, "%Y-%m-%d").date()

print(outro_formato_data, type(outro_formato_data))

#81