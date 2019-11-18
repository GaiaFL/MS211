import matplotlib.pyplot as plt

h = 1

#   Calculo da populacao atual com Kutta    #
def u(f, x, y):
    k1 = h*f(x, y)
    k2 = h*f(x + h * 0.5, y + k1 * 0.5)
    k3 = h*f(x + h * 0.5, y + k2 * 0.5)
    k4 = h*f(x + h, y + k3)
    k = (k1+2*k2+2*k3+k4)/6.0
    return x + k

#   Calculo das presas e predadores #
def presa_predadores(x0, y0, n_iteracoes):
    valores_x = []# Quantidade de presas  #
    valores_y = []# Quantidade de predadores #
    valores_x.append(x0)#   Inicializa listas   #
    valores_y.append(y0)
    i = 0
    while(i < n_iteracoes):
        valores_x.append(u(f1, valores_x[i], valores_y[i]))
        valores_y.append(u(f2, valores_y[i], valores_x[i]))
        i += 1
    return valores_x, valores_y

#  Função das presas em relação ao tempo   #
def f1(x, y):
    c1 = 0.1
    d1 = 0.1
    return c1*x - d1*x*y

#  Função dos predadores em relação ao tempo #
def f2(y, x):
    c2 = 0.05
    d2 = 0.05
    return c2*x*y - d2*y

def calc_tempos(n_iteracoes):
    tempos = []
    tempos.append(0)
    i = 1
    while(i < n_iteracoes):
        tempos.append(tempos[i-1] + h)
        i += 1
    return tempos

#   Chamada das funcoes    #
x0 = 3.0
y0 = 1.0
n_it = 1000

tempos = calc_tempos(n_it)
valores_ps, valores_pd = presa_predadores(x0, y0, n_it)

#   Plotagem do gráfico    #
#plt.plot(valores_ps, color = 'blue')
#plt.plot(valores_pd, color = 'red')
plt.plot(valores_ps, valores_pd, 'k--', color = 'black')
plt.xlabel("Presas")
plt.ylabel("Predadores")
plt.show()
