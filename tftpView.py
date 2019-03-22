from tftpUserInterface import *
import ftplib
import tempfile
import settings

class MainWindow(QtWidgets.QMainWindow, Ui_Consultar_Scripts):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.label.setText("INGRESA LOS NUMEROS SERIALES")
        self.resultDict={}
        self.errorMessage=QtWidgets.QErrorMessage()
        self.label_2.setText("SCRIPTS ASIGNADOS")
        self.queryScripts.clicked.connect(self.findScript)   

    def getFile(self,ftp, filename,directory):
        try:
            ftp.retrbinary("RETR " + filename ,open(directory+"/"+filename, 'wb').write)                            
        except Exception:
            self.resultDict[filename[0:12]]="NO TIENE SCRIPT ASIGNADO"
        try:            
            with open(directory+"/"+filename) as f:
                for line in f:
                    line=line.split()
                    self.resultDict[filename[0:12]]=line[len(line)-1]
        except Exception:
            print()

    def findScript(self):
        tftp_server =settings.FTP_SERVER
        user=settings.FTP_USER
        password=settings.FTP_PWD        
        try:
         ftp = ftplib.FTP(tftp_server,user,password)
        except OSError:
            self.errorMessage.setWindowTitle("ERROR")
            self.errorMessage.showMessage("SE REQUIERE CONEXION A LA VPN TSO")
            pass        
        else:
            serials=self.serialNumber.toPlainText().split()        
            self.assignedScripts.setRowCount(len(serials))
            self.assignedScripts.setColumnCount(2)
            self.assignedScripts.setHorizontalHeaderLabels(("SERIAL", "SCRIPT ASIGNADO"))
            tmpdir=tempfile.TemporaryDirectory()
            self.assignedScripts.setColumnWidth(1,510)
            for serial in serials:
                if (serial.isnumeric() and len(serial) == 12 ):
                    serial=serial+".cfg"
                    self.getFile(ftp,serial,tmpdir.name)
                else:
                    self.resultDict[serial]="NO ES UN SERIAL VALIDO"
            i=0
            for key,value in self.resultDict.items():
                self.assignedScripts.setItem(i,0, QtWidgets.QTableWidgetItem(key))
                self.assignedScripts.setItem(i,1, QtWidgets.QTableWidgetItem(value))
                i=i+1
            self.statusBar.showMessage("LISTO", 2000)
            ftp.close()
            del tmpdir
            self.resultDict={}            
        finally:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()