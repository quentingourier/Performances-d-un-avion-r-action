from math import *
import matplotlib.pyplot as pp
import numpy as np

#------------------------------------------------------
#----------------DEFINITIONS----------------------------
#------------------------------------------------------

#courbe planeur
def cplaneur(m, g, s, rhô):
    x, y = [], []
    v, F_list = [150, 175, 200, 225, 245, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500], []
    for i in range(len(v)):
        cz = (2*m*g)/(rhô*s*v[i]**2)
        cx = 0.0125+0.05*cz**2
        F = 0.5*rhô*s*v[i]**2*cx
        F_list.append(F)
        x.append(v[i])
        y.append(F_list[i])
    pp.plot(x, y, label = "Pousée requise en fonction de la vitesse de vol", color = 'r')
    axes = pp.gca()
    axes.set_xlim(50, 600)
    axes.set_ylim(0, 3*10**5)
    pp.scatter(245, F_list[4], c ='g', marker= 'x', label ='point de poussée minimale correspondant à la finesse max')
    pp.hlines(y = F_list[4], xmin = 0, xmax = 245, color ='g')
    pp.vlines(x = 245, ymin = 0, ymax = F_list[4], color ='g')
    pp.xlabel('Vitesse de vol (m/s)')
    pp.ylabel('Poussée requise (N)')
    pp.title('Courbe planeur à 10000m')
    pp.legend()
    pp.show()
   
#enveloppe de vol
def cenveloppe(m, g, s):
    x, x2, y = [], [], []
    #VMIN
    vmin_list = []
    rhô_0, czmax_0, czmax = 1.225, 2.6, 1.524
    alt = [0, 1*10**3, 2*10**3, 3*10**3, 4*10**3, 5*10**3, 6*10**3, 7*10**3, 8*10**3, 9*10**3, 10*10**3, 11*10**3, 12*10**3, 13*10**3, 14*10**3, 15*10**3, 16*10**3, 17200]
    T = [288.16, 281.66, 275.16, 268.67, 262.18, 255.69, 249.20, 242.71, 236.23, 229.74, 223.26, 216.78, 216.66, 216.66, 216.66, 216.66, 216.66, 216.66]
    rhô = [1.225, 1.111, 1.0066, 0.909, 0.81935, 0.7364, 0.66, 0.59, 0.5258, 0.4671, 0.4135, 0.3648, 0.31194, 0.26659, 0.22785, 0.19475, 0.16647, 0.1423]
    #calcul pour altitude 0m
    vmin0 = ((2*m*g)/(rhô_0*s*czmax_0))**0.5
    vmin_list.append(vmin0)
    #calculs pour toutes les autres altitudes
    for i in range(len(rhô)):  
        vmin = ((2*m*g)/(rhô[i]*s*czmax))**0.5
        vmin_list.append(vmin)
        x.append(vmin_list[i])
    #VMAX
    vmax_list = []
    for i in range(len(rhô)):
        vmax = 0.9*(1.4*287*T[i])**0.5 #308.7m/s correspond à 0.9Mach
        vmax_list.append(vmax)
        x2.append(vmax_list[i])
    #PLAFOND SUSTENTATION
    Ps_val_inf = (2*m*g)/(1.4*s*0.79**2*czmax)
    plafsus = 17200 #equivalence sur le tableau
    for i in range(len(rhô)):
        y.append(alt[i])
    #GRAPHE
    pp.plot(x, y, label = "Vitesse de décrochage", color = 'b')
    pp.plot(x2, y, label = "Vitesse maximale", color = 'r')
    axes = pp.gca()
    axes.set_xlim(0, 350)
    axes.set_ylim(0, 18000)
    pp.hlines(y = plafsus, xmin = x[-1], xmax = x2[-1], color ='g', label='Plafond de sustentation', linewidth = 2)
    pp.xlabel('Vitesse de vol (m/s)')
    pp.ylabel('Altitude (m)')
    pp.title('Enveloppe de vol')
    pp.legend()
    pp.show()

def cdomainevol(m, g, s, rhô):
    czmax1 = 2.6
    czmax2 = 1.524
    VS = 135
    V = ((2*m*g)/(rhô*s*czmax1))**0.5
    liste_n, liste_V1 = [0],[0]
    V1 = 0
    n=0 
    while V1< VS:
        n = n+0.1
        n = round(n,1)
        V1 = V*(n)**0.5
        liste_n.append(n)
        liste_V1.append(V1)
    V = ((2*m*g)/(rhô*s*czmax2))**0.5
    liste_n1, liste_V2 = [0],[0]    
    V2 = 0    
    n = int(0) 
    while n!=2.5:
        n = n+ 0.1
        n = round(n,1)
        V2 = V*(n)**0.5
        if n ==1.8:
            Vh=V2
        liste_n1.append(n)
        liste_V2.append(V2)
    liste_n3, liste_V3 = [0],[0]
    V3 = 0
    n=0 
    while V3< VS and n!=1.0:
        n = n+0.1
        n= round(n,1)
        V3 = V*(n)**0.5
        liste_n3.append(-n)
        liste_V3.append(V3)
    #GRAPHE
    axes = pp.gca()
    axes.set_xlim(0, 580)
    axes.set_ylim(-2, 3)
    pp.plot(liste_V1,liste_n, label = "volets sortis",color ="g")
    pp.plot(liste_V2,liste_n1, label = "volets rentrés",color="r")
    pp.plot(liste_V3,liste_n3,color="r")
    pp.hlines(y= -1,xmin=max(liste_V3),xmax=387,color="r")
    pp.hlines(y=1.8,xmin=max(liste_V1),xmax=Vh,color ="g")
    pp.hlines(y=2.5,xmin=max(liste_V2),xmax=537,color="r")
    pp.hlines(y= 0,xmin=0, xmax= 580, color="black")
    pp.vlines(x=537,ymin=0,ymax=2.5,color="r")
    pp.plot([387,537],[-1,0],color="r")
    pp.xlabel("Vitesse (m/s)")
    pp.ylabel("Facteur de charge n")
    pp.legend()
    pp.title('Domaine de vol')
    pp.show()

#------------------------------------------------------
#----------------PROGRAMME----------------------------
#------------------------------------------------------

#données
m, g, s,  rhô = 212000, 9.81, 363, 0.4135

choix=0
while choix not in ['1','2','3','4'] or choix!='4':
    print("\nQue choisissez-vous ?")
    print('1 - Courbe planeur')
    print('2 - Enveloppe de vol')
    print('3 - Domaine de vol')
    print('4 - Quitter')
    choix = input('Choix : ')
    if choix == '1':
        cplaneur(m, g, s, rhô)
    if choix == '2':
        cenveloppe(m, g, s)
    if choix == '3':
        cdomainevol(m, g, s, rhô)   
    if choix == '4' :
        break
