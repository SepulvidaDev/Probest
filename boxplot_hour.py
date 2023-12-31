import csv
from math import log
from math import sqrt
from matplotlib import pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

hora = 0
dados_hora_up_chrome = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
dados_hora_down_chrome = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
dados_hora_up_smart = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
dados_hora_down_smart = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

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
                dados_hora_up_chrome[hora] += [log(float(linha[2]), 10)]
            else:
                dados_hora_up_chrome[hora] += [0]
            if float(linha[3]) != 0:
                dados_hora_down_chrome[hora] += [log(float(linha[3]), 10)]
            else:
                dados_hora_down_chrome[hora] += [0]

with open("dataset_smart-tv.csv", "r") as arquivo:
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
                dados_hora_up_smart[hora] += [log(float(linha[2]), 10)]
            else:
                dados_hora_up_smart[hora] += [0]
            if float(linha[3]) != 0:
                dados_hora_down_smart[hora] += [log(float(linha[3]), 10)]
            else:
                dados_hora_down_smart[hora] += [0]
data = dados_hora_up_chrome
fig, ax = plt.subplots()
ax.boxplot(data)
plt.show()

data = dados_hora_down_chrome
fig, ax = plt.subplots()
ax.boxplot(data)
plt.show()

data = dados_hora_up_smart
fig, ax = plt.subplots()
ax.boxplot(data)
plt.show()

data = dados_hora_down_smart
fig, ax = plt.subplots()
ax.boxplot(data)
plt.show()

num_bin_up = (1 + 3.322*(log(len(dados_hora_up_chrome[22]), 10)))
num_bin_down = (1 + 3.322*(log(len(dados_hora_down_chrome[22]), 10)))
num_bin_up2 = (1 + 3.322*(log(len(dados_hora_up_smart[21]), 10)))
num_bin_down2 = (1 + 3.322*(log(len(dados_hora_up_smart[21]), 10)))

plt.hist(dados_hora_up_chrome[22], round(num_bin_up), rwidth=0.9)
plt.show()
plt.hist(dados_hora_down_chrome[22], round(num_bin_down), rwidth=0.9)
plt.show()
plt.hist(dados_hora_up_smart[21], round(num_bin_up2), rwidth=0.9)
plt.show()
plt.hist(dados_hora_down_smart[21], round(num_bin_down2), rwidth=0.9)
plt.show()


