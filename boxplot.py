import csv
from math import log
from math import sqrt
from matplotlib import pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

dados_up_chrome = []
dados_down_chrome = []
dados_up_smart = []
dados_down_smart = []

with open("dataset_chromecast.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Cabeçalho: " + str(linha))
        else:
            #print("Valor: " + str(linha))
            if float(linha[2]) != 0:
                dados_up_chrome += [log(float(linha[2]), 10)]
            else:
                dados_up_chrome += [0]
            if float(linha[3]) != 0:
                dados_down_chrome += [log(float(linha[3]), 10)]
            else:
                dados_down_chrome += [0]

with open("dataset_smart-tv.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Cabeçalho: " + str(linha))
        else:
            #print("Valor: " + str(linha))
            if float(linha[2]) != 0:
                dados_up_smart += [log(float(linha[2]), 10)]
            else:
                dados_up_smart += [0]
            if float(linha[3]) != 0:
                dados_down_smart += [log(float(linha[3]), 10)]
            else:
                dados_down_smart += [0]
data = [dados_up_chrome, dados_down_chrome, dados_up_smart, dados_down_smart]
fig, ax = plt.subplots()
ax.boxplot(data)
plt.show()
ecdf = ECDF(dados_up_chrome)
plt.step(ecdf.x, ecdf.y)
plt.show()
ecdf = ECDF(dados_down_chrome)
plt.step(ecdf.x, ecdf.y)
plt.show()
ecdf = ECDF(dados_up_smart)
plt.step(ecdf.x, ecdf.y)
plt.show()
ecdf = ECDF(dados_down_smart)
plt.step(ecdf.x, ecdf.y)
plt.show()


