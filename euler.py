import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    f=np.zeros(shape=(2,1))

    c1=0.1
    d1=0.05
    c2=0.1
    d2=0.05

    f[0,0]=c1*x-d1*x*y
    f[1,0]=c2*x*y-d2*y

    return f


def euler(t_ini,t_fini,x0,y0,h,N):
    x=np.zeros(shape=(N,1))
    y=np.zeros(shape=(N,1))

    for i in range(N):
        elem = h*f(x0,y0)
        x[i,0]=x0 + elem[0,0]
        y[i,0]=y0 + elem[1,0]

        #Atualizando os novos valores
        x0=x[i,0]
        y0=y[i,0]

    return x,y

def plot(x,y,t,N):
    """
    Função para plotar
    """

    #Abre uma figura com dois axis para plotar
    fig,ax=plt.subplots(1,2)                     

    #Primeiro axis (populações vs tempo)
    ax[0].plot(t,x,'b',label='Presas')                   #Plotando as presas
    ax[0].plot(t,y,'r',label='Predadores')               #Plotando os predadores 
    ax[0].legend()                                       #Colocando uma legenda bacana
    ax[0].set_xlabel("Tempo [dias]")                     #Não se esqueça de colocar o nome nos eixos
    ax[0].set_ylabel("População [hab]")                  #
    ax[0].set_title("Número de pontos N={}".format(N))   #Um breve título explicando o plot

    #Segundo axis (presas vs predadores)
    ax[1].plot(x,y,'m')                                  #Plotando presas e predadores
    ax[1].set_xlabel("Presas [hab]")                     #Nome dos eixos
    ax[1].set_ylabel("Predadores [hab]")                 #
    ax[1].set_title("Número de pontos N={}".format(N))   #Um breve título explicando o plot
    fig.tight_layout()                                   #Otimizando o espaço
    plt.savefig('EULER: N{}.png'.format(N))                     # Savando a figura pra ficar um relatorio bonito

    

# ========================================================================================== #
# ===================================== M  A  I  N  ======================================== #
# ========================================================================================== #

# Para simplicidade vamos chamar u1 de x e u2 de y.


#Dados do problema
t_ini=0
t_fini=365

#Condições iniciais
x0=3
y0=1

#Caso1
N1=365
h1=(t_fini-t_ini)/N1
t1=np.linspace(t_ini,t_fini,N1) #cria um array com N1 pontos entre os valores t_ini e t_fini

#Caso2
N2=3650
h2=(t_fini-t_ini)/N2
t2=np.linspace(t_ini,t_fini,N2)

#Caso3
N3=36500
h3=(t_fini-t_ini)/N3
t3=np.linspace(t_ini,t_fini,N3)

"""...Tentar mais casos e ver o que acontece..."""

#Solver
x1,y1 = euler(t_ini,t_fini,x0,y0,h1,N1)
x2,y2 = euler(t_ini,t_fini,x0,y0,h2,N2)
x3,y3 = euler(t_ini,t_fini,x0,y0,h3,N3)

# ========================================================================================== #
# ===================================== P  L  O  T  ======================================== #
# ========================================================================================== #

#plotando os casos
plot(x1,y1,t1,N1)

plot(x2,y2,t2,N2)

plot(x3,y3,t3,N3)
plt.show() #Mostra a figura (tem que ter se não estiver usando o spyder)
