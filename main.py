import argparse

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets,uic
import subprocess
from os import listdir, path

import inference2


class Stats:

    def __init__(self):

        self.ui = uic.loadUi('main.ui')

        self.ui.button_01.clicked.connect(self.getVideo)
        self.ui.button_02.clicked.connect(self.getSound)
        self.ui.button_03.clicked.connect(self.getOutput)
        self.ui.button_cg.clicked.connect(self.change)

        self.video_path = ''
        self.sound_path = ''
        self.outfile = ''
        self.ckpoint_path = 'checkpoint.pth'


    def getVideo(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择你要上传的视频",  # 标题
            r"./",  # 起始目录
            "视频类型 (*.mp4)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.video_path=filePath
        self.ui.label_01.setText(filePath)


    def getSound(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择你要上传的音频",  # 标题
            r"./",  # 起始目录
            "音频类型 (*.wav *.mp3)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.sound_path=filePath
        self.ui.label_02.setText(filePath)

    def getOutput(self):
        filePath = QFileDialog.getExistingDirectory(self.ui, "选择存储路径")
        self.outfile=filePath
        self.ui.label_03.setText(filePath)

    def change(self):

        if self.video_path=='' or self.sound_path=='' or self.outfile=='':
            QMessageBox.information(
                self.ui,
                'err',
                '请输入完整信息')
            return
        self.ui.text_01.setText("视频正在生成中，预计3~5分钟，请耐心等待。")
        QMessageBox.information(
            self.ui,
            'info',
            '视频正在生成中，预计3~5分钟，请耐心等待。')
        inference2.inference(m_checkpoint_path=self.ckpoint_path,m_face=self.video_path,m_audio=self.sound_path,m_outfile='{}/result.mp4'.format(self.outfile))

        QMessageBox.information(
            self.ui,
            'ok',
            '视频生成成功')
        self.ui.text_01.setText("请先选择音频文件，视频文件，文件输出路径，再点击“生成视频“按钮。")


app = QApplication([])
stats = Stats()
stats.ui.show()
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