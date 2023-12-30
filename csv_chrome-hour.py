import csv
import json
from math import log
from math import sqrt
from matplotlib import pyplot as plt

medias_up = []
medias_down = []
variancia_up = []
variancia_down = []
desvio_up = []
desvio_down = []
hora = 0
dados_hora = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
         [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
         [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
with open("dataset_chromecast.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Cabeçalho: " + str(linha))
        else:
            hora = int(linha[1][11:13])
            #if i == 2000:
            #    break
            #print("Valor: " + str(linha))
            #print(hora)
            if float(linha[2]) != 0:
                dados_hora[hora][0] += log(float(linha[2]), 10)
            else:
                dados_hora[hora][0] += 0
            if float(linha[3]) != 0:
                dados_hora[hora][1] += log(float(linha[3]), 10)
            else:
                dados_hora[hora][1] += 0
    for bah in range(len(dados_hora)):
        dados_hora[bah][0] = dados_hora[bah][0]/i
        dados_hora[bah][1] = dados_hora[bah][1]/i
with open("dataset_chromecast.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Cabeçalho: " + str(linha))
        else:
            hora = int(linha[1][11:13])
            #if i == 5:
            #    break
            #print("Valor: " + str(linha))
            if float(linha[2]) != 0:
                dados_hora[hora][2] += (log(float(linha[2]), 10) - dados_hora[hora][0])**2
            else:
                dados_hora[hora][2] += (0 - dados_hora[hora][0])**2
            if float(linha[3]) != 0:
                dados_hora[hora][3] += (log(float(linha[3]), 10) - dados_hora[hora][1])**2
            else:
                dados_hora[hora][3] += (0 - dados_hora[hora][1])**2
    for bah in range(len(dados_hora)):
        dados_hora[bah][2] = dados_hora[bah][2]/i
        dados_hora[bah][3] = dados_hora[bah][3]/i
        dados_hora[bah][4] = sqrt(dados_hora[bah][2])
        dados_hora[bah][5] = sqrt(dados_hora[bah][3])
        medias_up += [[bah, dados_hora[bah][0]]]
        medias_down += [[bah, dados_hora[bah][1]]]
        variancia_up += [[bah, dados_hora[bah][2]]]
        variancia_down += [[bah, dados_hora[bah][3]]]
        desvio_up += [[bah, dados_hora[bah][4]]]
        desvio_down += [[bah, dados_hora[bah][5]]]
#data = [zip(medias_up), zip(variancia_up), zip(desvio_up)]
#print(data)
#fig, ax = plt.subplots()
#ax.plot(data)
plt.plot(*zip(*medias_up))
plt.scatter(*zip(*medias_up))
plt.plot(*zip(*variancia_up))
plt.scatter(*zip(*variancia_up))
plt.plot(*zip(*desvio_up))
plt.scatter(*zip(*desvio_up))
plt.show()

plt.plot(*zip(*medias_down))
plt.scatter(*zip(*medias_down))
plt.plot(*zip(*variancia_down))
plt.scatter(*zip(*variancia_down))
plt.plot(*zip(*desvio_down))
plt.scatter(*zip(*desvio_down))
plt.show()

dados = {
    "00:00": {
        "media_upload": dados_hora[0][0],
        "media_download": dados_hora[0][1],
        "variancia_upload": dados_hora[0][2],
        "variancia_download": dados_hora[0][3],
        "desvio_upload": dados_hora[0][4],
        "desvio_download": dados_hora[0][5]
    },
    "01:00": {
        "media_upload": dados_hora[1][0],
        "media_download": dados_hora[1][1],
        "variancia_upload": dados_hora[1][2],
        "variancia_download": dados_hora[1][3],
        "desvio_upload": dados_hora[1][4],
        "desvio_download": dados_hora[1][5]
    },
    "02:00": {
        "media_upload": dados_hora[2][0],
        "media_download": dados_hora[2][1],
        "variancia_upload": dados_hora[2][2],
        "variancia_download": dados_hora[2][3],
        "desvio_upload": dados_hora[2][4],
        "desvio_download": dados_hora[2][5]
    },
    "03:00": {
        "media_upload": dados_hora[3][0],
        "media_download": dados_hora[3][1],
        "variancia_upload": dados_hora[3][2],
        "variancia_download": dados_hora[3][3],
        "desvio_upload": dados_hora[3][4],
        "desvio_download": dados_hora[3][5]
    },
    "04:00": {
        "media_upload": dados_hora[4][0],
        "media_download": dados_hora[4][1],
        "variancia_upload": dados_hora[4][2],
        "variancia_download": dados_hora[4][3],
        "desvio_upload": dados_hora[4][4],
        "desvio_download": dados_hora[4][5]
    },
    "05:00": {
        "media_upload": dados_hora[5][0],
        "media_download": dados_hora[5][1],
        "variancia_upload": dados_hora[5][2],
        "variancia_download": dados_hora[5][3],
        "desvio_upload": dados_hora[5][4],
        "desvio_download": dados_hora[5][5]
    },
    "06:00": {
        "media_upload": dados_hora[6][0],
        "media_download": dados_hora[6][1],
        "variancia_upload": dados_hora[6][2],
        "variancia_download": dados_hora[6][3],
        "desvio_upload": dados_hora[6][4],
        "desvio_download": dados_hora[6][5]
    },
    "07:00": {
        "media_upload": dados_hora[7][0],
        "media_download": dados_hora[7][1],
        "variancia_upload": dados_hora[7][2],
        "variancia_download": dados_hora[7][3],
        "desvio_upload": dados_hora[7][4],
        "desvio_download": dados_hora[7][5]
    },
    "08:00": {
        "media_upload": dados_hora[8][0],
        "media_download": dados_hora[8][1],
        "variancia_upload": dados_hora[8][2],
        "variancia_download": dados_hora[8][3],
        "desvio_upload": dados_hora[8][4],
        "desvio_download": dados_hora[8][5]
    },
    "09:00": {
        "media_upload": dados_hora[9][0],
        "media_download": dados_hora[9][1],
        "variancia_upload": dados_hora[9][2],
        "variancia_download": dados_hora[9][3],
        "desvio_upload": dados_hora[9][4],
        "desvio_download": dados_hora[9][5]
    },
    "10:00": {
        "media_upload": dados_hora[10][0],
        "media_download": dados_hora[10][1],
        "variancia_upload": dados_hora[10][2],
        "variancia_download": dados_hora[10][3],
        "desvio_upload": dados_hora[10][4],
        "desvio_download": dados_hora[10][5]
    },
    "11:00": {
        "media_upload": dados_hora[11][0],
        "media_download": dados_hora[11][1],
        "variancia_upload": dados_hora[11][2],
        "variancia_download": dados_hora[11][3],
        "desvio_upload": dados_hora[11][4],
        "desvio_download": dados_hora[11][5]
    },
    "12:00": {
        "media_upload": dados_hora[12][0],
        "media_download": dados_hora[12][1],
        "variancia_upload": dados_hora[12][2],
        "variancia_download": dados_hora[12][3],
        "desvio_upload": dados_hora[12][4],
        "desvio_download": dados_hora[12][5]
    },
    "13:00": {
        "media_upload": dados_hora[13][0],
        "media_download": dados_hora[13][1],
        "variancia_upload": dados_hora[13][2],
        "variancia_download": dados_hora[13][3],
        "desvio_upload": dados_hora[13][4],
        "desvio_download": dados_hora[13][5]
    },
    "14:00": {
        "media_upload": dados_hora[14][0],
        "media_download": dados_hora[14][1],
        "variancia_upload": dados_hora[14][2],
        "variancia_download": dados_hora[14][3],
        "desvio_upload": dados_hora[14][4],
        "desvio_download": dados_hora[14][5]
    },
    "15:00": {
        "media_upload": dados_hora[15][0],
        "media_download": dados_hora[15][1],
        "variancia_upload": dados_hora[15][2],
        "variancia_download": dados_hora[15][3],
        "desvio_upload": dados_hora[15][4],
        "desvio_download": dados_hora[15][5]
    },
    "16:00": {
        "media_upload": dados_hora[16][0],
        "media_download": dados_hora[16][1],
        "variancia_upload": dados_hora[16][2],
        "variancia_download": dados_hora[16][3],
        "desvio_upload": dados_hora[16][4],
        "desvio_download": dados_hora[16][5]
    },
    "17:00": {
        "media_upload": dados_hora[17][0],
        "media_download": dados_hora[17][1],
        "variancia_upload": dados_hora[17][2],
        "variancia_download": dados_hora[17][3],
        "desvio_upload": dados_hora[17][4],
        "desvio_download": dados_hora[17][5]
    },
    "18:00": {
        "media_upload": dados_hora[18][0],
        "media_download": dados_hora[18][1],
        "variancia_upload": dados_hora[18][2],
        "variancia_download": dados_hora[18][3],
        "desvio_upload": dados_hora[18][4],
        "desvio_download": dados_hora[18][5]
    },
    "19:00": {
        "media_upload": dados_hora[19][0],
        "media_download": dados_hora[19][1],
        "variancia_upload": dados_hora[19][2],
        "variancia_download": dados_hora[19][3],
        "desvio_upload": dados_hora[19][4],
        "desvio_download": dados_hora[19][5]
    },
    "20:00": {
        "media_upload": dados_hora[20][0],
        "media_download": dados_hora[20][1],
        "variancia_upload": dados_hora[20][2],
        "variancia_download": dados_hora[20][3],
        "desvio_upload": dados_hora[20][4],
        "desvio_download": dados_hora[20][5]
    },
    "21:00": {
        "media_upload": dados_hora[21][0],
        "media_download": dados_hora[21][1],
        "variancia_upload": dados_hora[21][2],
        "variancia_download": dados_hora[21][3],
        "desvio_upload": dados_hora[21][4],
        "desvio_download": dados_hora[21][5]
    },
    "22:00": {
        "media_upload": dados_hora[22][0],
        "media_download": dados_hora[22][1],
        "variancia_upload": dados_hora[22][2],
        "variancia_download": dados_hora[22][3],
        "desvio_upload": dados_hora[22][4],
        "desvio_download": dados_hora[22][5]
    },
    "23:00": {
        "media_upload": dados_hora[23][0],
        "media_download": dados_hora[23][1],
        "variancia_upload": dados_hora[23][2],
        "variancia_download": dados_hora[23][3],
        "desvio_upload": dados_hora[23][4],
        "desvio_download": dados_hora[23][5]
    }
}
with open("dados_chrome-hour.json", 'w') as file:
    json.dump(dados, file, indent=4)
    
