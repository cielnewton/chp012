from PySide6 import QtWidgets
import sys
import sqlite3
	

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.dataBase = sqlite3.connect("parkin.db")
        
        self.resize(300,100)
        self.setWindowTitle("BTS SNIR2 - QDialog")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()


    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()
        self.layoutH6 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.lbl_nom = QtWidgets.QLabel("Nom")
        self.LEdit_nom = QtWidgets.QLineEdit("")
        self.LEdit_nom.setPlaceholderText("Saisir votre nom")

        self.lbl_prenom = QtWidgets.QLabel("Prénom")
        self.LEdit_prenom = QtWidgets.QLineEdit("")
        self.LEdit_prenom.setPlaceholderText("Saisir votre prénom")

        self.btn_Enregistrer = QtWidgets.QPushButton("Enregistrer")
        self.btn_Afficher = QtWidgets.QPushButton("Afficher")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

        self.lbl_nom_display = QtWidgets.QLabel("Nom")
        self.lbl_prenom_display = QtWidgets.QLabel("Prénom")
        self.LEdit_nom_display = QtWidgets.QLineEdit()
        self.LEdit_nom_display.setDisabled(True)
      
        self.LEdit_prenom_display = QtWidgets.QLineEdit()
        self.LEdit_prenom_display.setDisabled(True)



    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_nom)
        self.layoutH1.addWidget(self.LEdit_nom)
        self.layoutH2.addWidget(self.lbl_prenom)
        self.layoutH2.addWidget(self.LEdit_prenom)
        self.layoutH3.addWidget(self.btn_Enregistrer)
        self.layoutH3.addWidget(self.btn_Afficher)
        self.layoutH4.addWidget(self.btn_Quitter)
        self.layoutH5.addWidget(self.lbl_nom_display)
        self.layoutH5.addWidget(self.lbl_prenom_display)
        self.layoutH6.addWidget(self.LEdit_nom_display)
        self.layoutH6.addWidget(self.LEdit_prenom_display)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)
        self.layoutV.addLayout(self.layoutH6)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(self.quitter)
        self.btn_Afficher.clicked.connect(self.afficher)
        self.btn_Enregistrer.clicked.connect(self.enregister)

    def enregister(self):
        
        if self.LEdit_nom.text() =="" or self.LEdit_prenom.text() =="":
            self.messageChampsVides = QtWidgets.QMessageBox()       
            self.messageChampsVides.setText("Erreur de saisie\nVeuillez resaisir des valeurs correctes")  
            self.messageChampsVides.show() 
        else:
            login_saisie =self.LEdit_nom.text() 
            mdp_saisie = self.LEdit_prenom.text()
            cursorObject = self.dataBase.cursor()

            # contre injection sql
            query = "INSERT INTO users (login, mot_de_pass) VALUES (?, ?)"
            cursorObject.execute(query, (login_saisie, mdp_saisie))
            self.dataBase.commit()
          

     

        # vulnérable aux  injections sql
            # query = f"INSERT INTO users (login, mot_de_pass) VALUES ('{login_saisie}', '{mdp_saisie}')"
            # cursorObject .execute(query)
            # self.dataBase.commit()
      
            self.clearEdit()
    

    def afficher(self):
        # preparing a cursor object
        cursorObject = self.dataBase.cursor()

        # selecting query
        query = "SELECT login, mot_de_pass FROM users ORDER BY idx DESC LIMIT 1"
        cursorObject.execute(query)
        myresult = cursorObject.fetchall()
        print(myresult)
        self.LEdit_nom_display.setText(myresult[0][0])
        self.LEdit_prenom_display.setText(myresult[0][1])

    def clearEdit(self):
        self.LEdit_nom.setText("")
        self.LEdit_prenom.setText("")

                
    def quitter(self):
        self.dataBase.close()
        self.close()


    

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()s