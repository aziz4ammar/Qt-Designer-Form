from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def somme(n):
    s=0
    for i in range (1,n+1):
        if(n%i==0):
            s+=i
    return s
def haut(n):
    sd=somme(n)
    i=2
    test=True
    while(i<n)and(test):
        if(somme(i)>=sd):
            test=False
        else:
            i+=1
    return test
def verifier():
    ch=fen.nb.text()
    if(ch=="")or(ch.isdigit()==False):
        fen.res.setText("Veuillez saisir un entier")
    elif (ch!="")and(ch[1:].isdigit())and(ch[0]=="-")or(ch=="1"):
        fen.res.setText("Veuillez saisir un entier > 1")
    else:
        n=int(ch)
        if(not haut(n)):
            fen.res.setText(str(n)+"nest pas hautement-abondant")
        else:
            fen.res.setText(str(n)+"est hautement-abondant")
    
    
app=QApplication([])
fen=loadUi("Nombre hauteur abondant.ui")
fen.show()
fen.verif.clicked.connect(verifier)
app.exec_()