import csv
import json
from math import log
from math import sqrt
from matplotlib import pyplot as plt

dados_up = []
dados_down = []
media_down, media_up, variancia_down = 0, 0, 0
variancia_up, desvio_down, desvio_up = 0, 0, 0
num_dados_up = 0
num_dados_down = 0
with open("dataset_chromecast.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Cabeçalho: " + str(linha))
        else:
            #print("Valor: " + str(linha))
            if float(linha[2]) != 0:
                media_up += log(float(linha[2]), 10)
                dados_up += [log(float(linha[2]), 10)]
                num_dados_up += 1
            else:
                media_up += 0
                dados_up += [0]
                num_dados_up += 1
            if float(linha[3]) != 0:
                media_down += log(float(linha[3]), 10)
                dados_down += [log(float(linha[3]), 10)]
                num_dados_down += 1
            else:
                media_down += 0
                dados_down += [0]
                num_dados_down += 1
    media_up = media_up/(i)
    media_down = media_down/(i)
with open("dataset_chromecast.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Cabeçalho: " + str(linha))
        else:
            #print("Valor: " + str(linha))
            if float(linha[2]) != 0:
                variancia_up += (log(float(linha[2]), 10) - media_up)**2
            else:
                variancia_up += (0 - media_up)**2
            if float(linha[3]) != 0:
                variancia_down += (log(float(linha[3]), 10) - media_down)**2
            else:
                variancia_down += (0 - media_down)**2
    variancia_up = variancia_up/(i)
    desvio_up = sqrt(variancia_up)
    variancia_down = variancia_down/(i)
    desvio_down = sqrt(variancia_down)
    num_bin_up = (1 + 3.322*(log(num_dados_up, 10)))
    num_bin_down = (1 + 3.322*(log(num_dados_down, 10)))
plt.hist(dados_up, round(num_bin_up), rwidth=0.9)
plt.show()
plt.hist(dados_down, round(num_bin_down), rwidth=0.9)
plt.show()
data = [dados_up, dados_down]
fig, ax = plt.subplots()
ax.boxplot(data)
plt.show()

dados = {
    "media_upload": media_up,
    "media_download": media_down,
    "variancia_upload": variancia_up,
    "variancia_download": variancia_down,
    "desvio_upload": desvio_up,
    "desvio_download": desvio_down,
    "dados_upload": num_dados_up,
    "dados_download": num_dados_down,
    "Num_bin_up": num_bin_up,
    "Num_bin_down": num_bin_down
}
with open("dados_chrome.json", 'w') as file:
    json.dump(dados, file, indent=4)
    
