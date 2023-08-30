from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import apprcc_rc
from PyQt5 import QtCore, QtGui, QtWidgets,uic
import subprocess


class Stats:

    def __init__(self):

        self.ui = uic.loadUi('main_3.ui')

        self.ui.button_01.clicked.connect(self.getVideo)
        self.ui.button_02.clicked.connect(self.getSound)
        self.ui.button_03.clicked.connect(self.getOutput)
        self.ui.button_cg.clicked.connect(self.change)

        self.video_path = ''
        self.sound_path = ''
        self.output_path = ''
        self.ckpoint_path = 'ckpoints/checkpoint_step000001000.pth'


    def getVideo(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择你要上传的视频",  # 标题
            r"./",  # 起始目录
            "视频类型 (*.mp4)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.video_path=filePath
        print(filePath)
        print(_)

    def getSound(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择你要上传的音频",  # 标题
            r"./",  # 起始目录
            "音频类型 (*.mp4 *.wav *.mp3)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.sound_path=filePath
        print(filePath)
        print(_)

    def getOutput(self):
        filePath = QFileDialog.getExistingDirectory(self.ui, "选择存储路径")
        self.output_path=filePath
        print(filePath)

    def change(self):
        # inference.main(checkpoint_path=self.ckpoint_path,face=self.video_path,audio=self.sound_path,outfile=self.output_path)


        command = "python ../inference.py --checkpoint_path {} --face {} --audio {} --outfile {}".format(self.ckpoint_path,self.video_path,self.sound_path,self.output_path)
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

        print("output",output)
        print("error",error)

        QMessageBox.critical(
            self.ui,
            'ok',
            '视频生成成功')

app = QApplication([])
stats = Stats()
# stats.ui.show()
stats.ui.showMaximized()
app.exec_()


'''
pyinstaller httpclient.py --noconsole --hidden-import PySide2.QtXml --icon="logo.ico"
然后手动导ui文件

#加上图标
from PySide2.QtGui import  QIcon
app = QApplication([])
app.setWindowIcon(QIcon('logo.png'))



pyrcc5 apprcc.qrc -o apprcc_rc.py
'''