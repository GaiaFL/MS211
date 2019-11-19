import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    """
    Função que define o sistema predador presa, essa função retorna um array
    com duas linhas e uma coluna, representando o sistema apresentado no problema
    """

    #Alocar memória para o nparray
    f=np.zeros(shape=(2,1))

    #Definindo as constantes
    c1=0.1
    d1=0.1
    c2=0.05
    d2=0.05

    #Definindo a função f(x,y)
    f[0,0]=c1*x-d1*x*y
    f[1,0]=c2*x*y-d2*y

    return f


def RK(t_ini,t_fini,x0,y0,h,N):
    """
    Integrador usando o método Runge-Kutta apresentado na pag 331 da Rugiero
    e estendido para um sistema de equações na pag 354 da mesma Rugiero
    """

    #Pegamos os valores de x0 e y0
    x=np.zeros(shape=(N,1))
    y=np.zeros(shape=(N,1))
    
    for i in range(N):        
        
        #Definindo os famosos coeficientes de RK
        k1=h*f(x0,y0)                                    
        k2=h*f(x0+h/2,y0+k1[1,0]/2)                       #como k1 é um array [2x1], vamos mandar só o k1 relativo ao y
        k3=h*f(x0+h/2,y0+k2[1,0]/2)                       #
        k4=h*f(x0+h,y0+k3[1,0])                           #

        #salvando os valores os valores
        x[i,0]=x0+1/6*(k1[0,0]+2*k2[0,0]+2*k3[0,0]+k4[0,0])
        y[i,0]=y0+1/6*(k1[1,0]+2*k2[1,0]+2*k3[1,0]+k4[1,0])

        #Atualizando os novos valores
        x0=x[i,0]
        y0=y[i,0]

    return x,y


def EULER(t_ini,t_fini,x0,y0,h,N):
    """
    Integrador usando o método Euler Explícito
    """

    #Pegamos os valores de x0 e y0
    x=np.zeros(shape=(N,1))
    y=np.zeros(shape=(N,1))
    
    for i in range(N):
        elem = h*f(x0,y0)
        x[i,0]=x0+elem[0,0]
        y[i,0]=y0+elem[1,0]

        #Atualizando os novos valores
        x0=x[i,0]
        y0=y[i,0]

    return x,y


def plot(x,y,t,N, prefix):
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
    plt.savefig('{}_N{}.png'.format(prefix, N))                     # Savando a figura pra ficar um relatorio bonito

    

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
rk_x1,rk_y1 = RK(t_ini,t_fini,x0,y0,h1,N1)
rk_x2,rk_y2 = RK(t_ini,t_fini,x0,y0,h2,N2)
rk_x3,rk_y3 = RK(t_ini,t_fini,x0,y0,h3,N3)

euler_x1,euler_y1 = EULER(t_ini,t_fini,x0,y0,h1,N1)
euler_x2,euler_y2 = EULER(t_ini,t_fini,x0,y0,h2,N2)
euler_x3,euler_y3 = EULER(t_ini,t_fini,x0,y0,h3,N3)

# ========================================================================================== #
# ===================================== P  L  O  T  ======================================== #
# ========================================================================================== #

#plotando os casos
plot(rk_x1,rk_y1,t1,N1,'RK')
plot(rk_x2,rk_y2,t2,N2,'RK')
plot(rk_x3,rk_y3,t3,N3,'RK')

plot(euler_x1,euler_y1,t1,N1,'EULER')
plot(euler_x2,euler_y2,t2,N2,'EULER')
plot(euler_x3,euler_y3,t3,N3,'EULER')

plt.show() #Mostra a figura (tem que ter se não estiver usando o spyder)
