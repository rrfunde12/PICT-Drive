__author__ = 'happy'
from os.path import expanduser
import shutil
import ntpath
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import QSize, center
from PyQt4.QtGui import QIcon, QMessageBox
from PyQt4.QtGui import QPixmap
import threading
import urllib2
import time
#**************************GLOBAL VARIABLES
fname=""
filename=""
subject=""
radio=0
Rsub6=QtGui.QRadioButton
Rsub1=QtGui.QRadioButton
Rsub5=QtGui.QRadioButton
Rsub3=QtGui.QRadioButton
Rsub2=QtGui.QRadioButton
Rsub4=QtGui.QRadioButton
other=QtGui.QLineEdit

#Defining Subject names globally

sub1="PCDP"
sub2="EOS"
sub3="CN"
sub4="SE"
sub5="DSP"
sub6="Other"
id=""
subject=""
fname=""
#****************************************OVERIDING METHOD OF QPUSHBUTTON TO IMPLEMENT DRAG AND DROP

class Button(QtGui.QPushButton,QMessageBox):

    global id,subject,fname
    def Mysend(self):Send()			                    #calling external function for sending
    
    def __init__(self, title, parent):

	self.title=title
        super(Button, self).__init__(title, parent)
        self.setAcceptDrops(True)			            #enabling drops



#*************************************ACTION AFTER DRAGGING SOMETHING
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:						#* Accept only files
            e.setDropAction(QtCore.Qt.CopyAction)
            e.accept()
            global fname;
            fname=e.mimeData().text()
        else:
            e.ignore()

#***************************************TAKING CARE OF ATTACHMENT NAMING AND SENDING
    def dropEvent(self, e):
           global fname;
           global filename
           fname=e.mimeData().text()
           for url in e.mimeData().urls():
               path = url.toLocalFile().toLocal8Bit().data()
               if os.path.isfile(path):
                    fname= path
                    global filename
                    filename= ntpath.basename(path)
           if "a"=="a":
                if Rsub6.isChecked():
                    subject="Other"
               # subject=str(subject)


               # if subject=="":
                #    subject=time.asctime( time.localtime(time.time()) )

                elif Rsub5.isChecked():
                    subject=sub5
                elif Rsub1.isChecked():
                    subject=sub1
                elif Rsub3.isChecked():
                    subject=sub3
                elif Rsub2.isChecked():
                    subject=sub2
                elif Rsub4.isChecked():
                    subject=sub4

                home=expanduser("~")
                path=home+"/PICT/"+subject+"/"
                if(os.path.exists(path)):
                    shutil.copy(fname,path)
                else:
                    os.makedirs(path)
                    shutil.copy(fname,path)


           if(self.Internet()):


#                wt=WorkThread()
 #               wt.start()
                 self.Mysend()
           else:
               msg1=QMessageBox()
               msg1.setGeometry(400,400,60,30)
               msg1.setText("sorry Internet not working Try again")
               msg1.exec_()



    def Internet(self):

           try:
               urllib2.urlopen("http://drive.google.com",timeout=3)

               return True
           except urllib2.URLError:pass
           return False



class GUI(QtGui.QWidget):     #********************************CLASS FOR DESIGNING GUI AND PERFORM OPERTIONS
    global id,subject
    def MySend(self): Send()   #*******************************ACCESSING EXTERNAL FUNCTION IN CLASS

    def __init__(self):
        super(GUI, self).__init__(None,QtCore.Qt.WindowStaysOnTopHint)
        global fname
        self.fname=fname
        self.initUI()
        global radio,Rsub6


    def Browse(self):           #******************************FILE INPUT DIALOG FOR USER FILE SELECTION


        global fname,filename,Rsub6,Rsub5,Rsub1,Rsub2,Rsub4,Rsub3,other

        try:

            fname=QtGui.QFileDialog.getOpenFileName(self,options=QtGui.QFileDialog.DontUseNativeDialog)
            QtGui.QFileDialog.close()
        except:
            pass
        finally:

            if(fname!=""):

                fname=str(fname)
                filename=ntpath.basename(fname)

            if "a"=="a":
                if Rsub6.isChecked():
                    subject="Other"
               # subject=str(subject)


               # if subject=="":
                #    subject=time.asctime( time.localtime(time.time()) )

                elif Rsub5.isChecked():
                    subject=sub5
                elif Rsub1.isChecked():
                    subject=sub1
                elif Rsub3.isChecked():
                    subject=sub3
                elif Rsub2.isChecked():
                    subject=sub2
                elif Rsub4.isChecked():
                    subject=sub4

#AUTHENTICATION WITH GOOGLE SERVER
                home=expanduser("~")
                path=home+"/PICT/"+subject+"/"
                if(os.path.exists(path)):
                    shutil.copy(fname,path)
                else:
                    os.makedirs(path)
                    shutil.copy(fname,path)



                if(self.Internet()):
                    self.MySend()

                   # self.Title3.setText("Successfully send")

                else:
                    msg1=QMessageBox()
                    msg1.setGeometry(400,400,60,30)
                    msg1.setText("sorry Internet not working Try again")
                    msg1.exec_()





            else:
                mms=QtGui.QMessageBox()
                mms.setGeometry(750,400,60,30)
                mms.setText("Please choose a file OR drag one")

                mms.exec_()



    def Internet(self):

           try:
               urllib2.urlopen("http://drive.google.com",timeout=3)

               return True
           except urllib2.URLError:pass
           return False



            #    self.destroy(True)




    def initUI(self):               #****************************************UI DESIGNING

        global fname,filename,Rsub6,Rsub5,Rsub1,Rsub2,Rsub4,Rsub3,other

								#********************BUTTON FOR TAKING ATTACHMENT
        self.button = Button("", self)
        self.button.move(20, 395)
        self.button.resize(510,290)

        icon = QIcon("Drag.png")
        self.button.setIcon(icon)
        self.button.setIconSize(QSize(510,300))
        self.button.clicked.connect(self.Browse)


#***************************RADIO BUTTONS FOR SELECTING SUBJECT

        Title=QtGui.QLabel(self)
        pixmap=QPixmap("PICT.png")
        Title.move(60,0)
        Title.resize(470,100)
        spixmap=pixmap.scaled(Title.size(),QtCore.Qt.KeepAspectRatio)
        Title.setPixmap(spixmap)


        Title1=QtGui.QLabel("Computer Department",self)
        font = self.font()
        font.setPixelSize(25)
        Title1.setFont(font)
        Title1.move(200,70)
        Title1.resize(570,100)

        Title2=QtGui.QLabel("TE3",self)
        font = self.font()
        font.setPixelSize(17)
        Title2.setFont(font)
        Title2.move(300,99)
        Title2.resize(600,100)






        font = self.font()
        font.setPixelSize(self.height() * 0.11)
        Title.setFont(font)


        Rsub1=QtGui.QRadioButton("%s"%sub1,self)
        Rsub2= QtGui.QRadioButton("%s"%sub2,self)
        Rsub3=QtGui.QRadioButton("%s"%sub3,self)
        Rsub4=QtGui.QRadioButton("%s"%sub4,self)
        Rsub5=QtGui.QRadioButton("%s"%sub5,self)
        Rsub6=QtGui.QRadioButton("%s"%sub6,self)

        Rsub1.setChecked(True)

        #other=QtGui.QLineEdit(self)
        #other.setPlaceholderText("enter Subject")
        #other.move(160,223)
        #other.resize(115,25)
        #other.setDragEnabled(True)


        Rsub1.move(100,180)
        Rsub2.move(100,200)
        Rsub3.move(100,220)
        Rsub4.move(100,240)
        Rsub5.move(100,260)
        Rsub6.move(100,280)


        self.LAY=QtGui.QVBoxLayout()


        self.LAY.addWidget(Rsub1)

        self.LAY.addWidget(Rsub5)
        self.LAY.addWidget(Rsub4)
        self.LAY.addWidget(Rsub2)
        self.LAY.addWidget(Rsub3)
        self.LAY.addWidget(Rsub6)

        self.FRAME=QtGui.QFrame(self)
        self.FRAME.setLayout(self.LAY)
        self.FRAME.setGeometry(100,200,100,200)
        self.FRAME.show()


#*************************************MAIN WINDOW

        self.setWindowTitle('AutoMat ')
        self.setGeometry(800, 300, 600, 800)
        self.setMaximumWidth(600)
        self.show()


#*******************************Threding

class WorkThread(QtCore.QThread):
 def __init__(self):
  QtCore.QThread.__init__(self)

 def MySend(self): Send()
 def run(self):
  self.MySend()

#**********************************EXTERNAL FUNCTION FOR SENDING ATTACHMENT

def Send():


           global subject,Rsub5, Rsub1,Rsub3,Rsub2,Rsub4,other
           id=""
           msg1=QMessageBox()

           if "a"=="a":
            if Rsub6.isChecked():
                subject="Other"
               # subject=str(subject)


               # if subject=="":
                #    subject=time.asctime( time.localtime(time.time()) )
                id="0Bx8BFa4-Ejy_YWlxTWl1UlU5OEU"
                print subject
            elif Rsub5.isChecked():
                subject=sub5
                id="0Bx8BFa4-Ejy_cHpwd3ZqY2toWlE"
            elif Rsub1.isChecked():
                subject=sub1
                id="0Bx8BFa4-Ejy_b0haa3ZsTG5LSG8"
            elif Rsub3.isChecked():
                subject=sub3
                id="0Bx8BFa4-Ejy_MGUydkJfano0dVk"
            elif Rsub2.isChecked():
                subject=sub2
                id="0Bx8BFa4-Ejy_ektlT0gxclJ3R28"
            elif Rsub4.isChecked():
                subject=sub4
                id="0Bx8BFa4-Ejy_TkZLSlYyaDhrSlk"

#AUTHENTICATION WITH GOOGLE SERVER
            home=expanduser("~")
            path=home+"/PICT/"+subject+"/"
            if(os.path.exists(path)):
                shutil.copy(fname,path)
            else:
                os.makedirs(path)
                shutil.copyfile(fname,path+fname)

            auth=GoogleAuth()

            auth.LoadCredentialsFile("cred.txt")
            if auth.credentials is None:

                auth.LocalWebserverAuth()

            elif auth.access_token_expired:
                auth.Refresh()

            else:
                auth.Authorize()
            auth.SaveCredentialsFile("cred.txt")
            drive = GoogleDrive(auth)



            files=drive.CreateFile({'title':'%s'%filename,'mimeType':'text/csv',
                "parents": [{"kind": "drive#TE3#%s"%subject,"id": '%s'%id}]})
            files.SetContentFile("%s"%fname)
            files.Upload()

         #   file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
          #  for file1 in file_list:
           #     print 'title: %s, id: %s' % (file1['title'], file1['id'])


            msg1.setGeometry(500,400,60,30)
            msg1.setText("Successfully Send")
            msg1.exec_()
            msg1.destroy()

#********************************MAIN FUNCTION
def main():
    with open("cred.txt","w+") as file:
    	file.truncate()
    app = QtGui.QApplication([])
    ex = GUI()
    target=app.exec_()


#*****************************LOOP FOR SHOWING WINDOW

if __name__ == '__main__':
    main()
