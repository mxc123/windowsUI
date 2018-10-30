# *_*coding:utf-8 *_*
import sys
import os
import time
import win32file
from PySide import QtGui,QtCore

PATH=os.path.abspath(os.path.dirname(__file__))
PATH_STR=PATH.replace("\\",'/')
###############################################File Class######################################################
class FileMenuDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent=parent)
        self.setWindowFlags(QtCore.Qt.Popup)
        self.setWindowTitle('FileMenu')
        xiangxBtn=QtGui.QToolButton()
        xiangxBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        xiangxBtn.setText(u"打开新窗口")
        xiangxBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))

        xiangxBtn.setMinimumHeight(50)
        xiangxBtn.setAutoRaise(True)
        yulBtn=QtGui.QToolButton()
        yulBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        yulBtn.setText(u'打开Windows PowerShell(R)')
        yulBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        yulBtn.setAutoRaise(True)
        paixBtn=QtGui.QToolButton()
        paixBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        paixBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        paixBtn.setText(u"更该文件夹和和搜索选项")
        paixBtn.setAutoRaise(True)
        helpBtn=QtGui.QToolButton()
        helpBtn.setText(u'帮助')
        helpBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        helpBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        helpBtn.setAutoRaise(True)
        closeBtn=QtGui.QToolButton()
        closeBtn.setText(u'关闭')
        closeBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        closeBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        closeBtn.setAutoRaise(True)

        layout=QtGui.QVBoxLayout()
        layout.addWidget(xiangxBtn)
        layout.addWidget(yulBtn)
        layout.addWidget(paixBtn)
        layout.addWidget(helpBtn)
        layout.addWidget(closeBtn)
        self.setLayout(layout)

class HomeMenuDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent=parent)
        self.setWindowFlags(QtCore.Qt.Popup)
        self.setWindowTitle('FileMenu')
        dingBtn=QtGui.QToolButton()
        dingBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        dingBtn.setText(u"固定到\n“快速访问”")
        dingBtn.setAutoRaise(True)
        dingBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        deWlab_map=QtGui.QLabel()
        deWlab_map.setPixmap(QtGui.QPixmap('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        copylab=QtGui.QLabel(u'复制')

        pastelab_map=QtGui.QLabel()
        pastelab_map.setPixmap(QtGui.QPixmap('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        pastelab=QtGui.QLabel(u"粘贴")

        xiangxBtn=QtGui.QToolButton()
        xiangxBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        xiangxBtn.setText(u'删除')
        xiangxBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))

        xiangxBtn.setMinimumHeight(50)
        xiangxBtn.setAutoRaise(True)

        daohBtn=QtGui.QToolButton()
        daohBtn.setText(u"新建\n文件夹")
        daohBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        daohBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        daohBtn.setAutoRaise(True)
        yulBtn = QtGui.QToolButton()
        yulBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        yulBtn.setText(u'属性')
        yulBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        yulBtn.setAutoRaise(True)
        paixBtn = QtGui.QToolButton()
        paixBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        paixBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        paixBtn.setText(u'历史记录')
        paixBtn.setAutoRaise(True)
        layout_Vcop=QtGui.QVBoxLayout()
        layout_Vcop.addWidget(deWlab_map)
        layout_Vcop.addWidget(copylab)
        layout_Vyul=QtGui.QVBoxLayout()
        layout_Vyul.addWidget(pastelab_map)
        layout_Vyul.addWidget(pastelab)

        layout=QtGui.QHBoxLayout()
        layout.addWidget(dingBtn)
        layout.addLayout(layout_Vcop)
        layout.addLayout(layout_Vyul)

        layout.addWidget(xiangxBtn)

        layout.addWidget(daohBtn)
        layout.addWidget(yulBtn)
        layout.addWidget(paixBtn)
        self.setLayout(layout)

class ShareMenuDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent=parent)
        self.setWindowFlags(QtCore.Qt.Popup)
        self.setWindowTitle('FileMenu')

        deWlab_map=QtGui.QLabel()
        deWlab_map.setPixmap(QtGui.QPixmap('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        deWlab=QtGui.QLabel(u'共享')

        songlab_map=QtGui.QLabel()
        songlab_map.setPixmap(QtGui.QPixmap('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        songlab=QtGui.QLabel(u"发送\n邮件")

        presslab_map=QtGui.QLabel()
        presslab_map.setPixmap(QtGui.QPixmap('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        presslab=QtGui.QLabel(u'压缩')


        kelulab_map=QtGui.QLabel()
        kelulab_map.setPixmap(QtGui.QPixmap('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))

        daohBtn=QtGui.QToolButton()
        daohBtn.setText(u"刻录到光盘")
        daohBtn.setAutoRaise(True)

        dayinlab_map=QtGui.QLabel()
        dayinlab_map.setPixmap(QtGui.QPixmap('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        dayinlab=QtGui.QLabel(u"打印")
        ChZh_map=QtGui.QLabel()
        ChZh_map.setPixmap(QtGui.QPixmap('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        ChZh_lab=QtGui.QLabel(u'传真')

        yulBtn = QtGui.QToolButton()
        yulBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        yulBtn.setText(u'属性')
        yulBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        yulBtn.setAutoRaise(True)

        xiangxBtn = QtGui.QToolButton()
        xiangxBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        xiangxBtn.setText(u'删除\n访问')
        xiangxBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))

        xiangxBtn.setMinimumHeight(50)
        xiangxBtn.setAutoRaise(True)
        paixBtn = QtGui.QToolButton()
        paixBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        paixBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        paixBtn.setText(u'高级安全')
        paixBtn.setAutoRaise(True)

        layout_Vyul=QtGui.QVBoxLayout()
        layout_Vyul.addWidget(deWlab_map)
        layout_Vyul.addWidget(deWlab)
        layout_Vsong=QtGui.QVBoxLayout()
        layout_Vsong.addWidget(songlab_map)
        layout_Vsong.addWidget(songlab)
        layout_Vpress=QtGui.QVBoxLayout()
        layout_Vpress.addWidget(presslab_map)
        layout_Vpress.addWidget(presslab)

        layout_Hkelu=QtGui.QHBoxLayout()
        layout_Hkelu.addWidget(kelulab_map)
        layout_Hkelu.addWidget(daohBtn)

        layout_Hdayin=QtGui.QHBoxLayout()
        layout_Hdayin.addWidget(dayinlab_map)
        layout_Hdayin.addWidget(dayinlab)
        layout_HChZh=QtGui.QHBoxLayout()
        layout_HChZh.addWidget(ChZh_map)
        layout_HChZh.addWidget(ChZh_lab)

        layout_Vke=QtGui.QVBoxLayout()
        layout_Vke.addLayout(layout_Hkelu)
        layout_Vke.addLayout(layout_Hdayin)
        layout_Vke.addLayout(layout_HChZh)



        layout=QtGui.QHBoxLayout()

        layout.addLayout(layout_Vyul)
        layout.addLayout(layout_Vsong)
        layout.addLayout(layout_Vpress)
        layout.addLayout(layout_Vke)

        layout.addWidget(xiangxBtn)
        layout.addWidget(yulBtn)
        layout.addWidget(paixBtn)
        self.setLayout(layout)
class ViewMenuDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent=parent)
        self.setWindowFlags(QtCore.Qt.Popup)
        self.setWindowTitle('FileMenu')
        daohBtn = QtGui.QToolButton()
        daohBtn.setText(u"导航窗格")
        daohBtn.setAutoRaise(True)
        daohBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        daohBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))

        yulBtn = QtGui.QToolButton()
        yulBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        yulBtn.setText(u'预览窗格')
        yulBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        yulBtn.setAutoRaise(True)

        xiangxBtn = QtGui.QToolButton()
        xiangxBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        xiangxBtn.setText(u'详细信息窗格')
        xiangxBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        xiangxBtn.setAutoRaise(True)
        windowlable=QtGui.QLabel(u'             窗格           ')


        paixBtn = QtGui.QToolButton()
        paixBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        paixBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        paixBtn.setText(u'排序方式')
        paixBtn.setAutoRaise(True)

        fenzBtn=QtGui.QToolButton()
        fenzBtn.setText(u'分组依据')
        fenzBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        fenzBtn.setAutoRaise(True)
        fenzBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))

        addlBtn=QtGui.QToolButton()
        addlBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        addlBtn.setText(u'添加列')
        addlBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        addlBtn.setAutoRaise(True)

        hesBtn=QtGui.QToolButton()
        hesBtn.setText(u'将所有列调整为合适的大小')
        hesBtn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        hesBtn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        hesBtn.setAutoRaise(True)
        danglabel=QtGui.QLabel(u'           当前视图          ')

        xiang_chBox=QtGui.QCheckBox()
        xiang_chBox.setText(u'项目复选框')

        wenj_chBox = QtGui.QCheckBox()
        wenj_chBox.setText(u'文件扩展名')

        yinc_chBox = QtGui.QCheckBox()
        yinc_chBox.setText(u'隐藏的项目')
        yinc_Btn=QtGui.QToolButton()
        yinc_Btn.setText(u'隐藏\n所有项目')
        yinc_Btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        yinc_Btn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        yinc_Btn.setAutoRaise(True)
        xory_label=QtGui.QLabel(u"         显示/隐藏         ")
        Xx_Btn=QtGui.QToolButton()
        Xx_Btn.setText(u"选项")
        Xx_Btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        Xx_Btn.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/paste.png'))
        Xx_Btn.setAutoRaise(True)
        layout_Vyul = QtGui.QVBoxLayout()
        layout_Vyul.addWidget(yulBtn)
        layout_Vyul.addWidget(xiangxBtn)

        layout_Vfen = QtGui.QVBoxLayout()
        layout_Vfen.addWidget(fenzBtn)
        layout_Vfen.addWidget(addlBtn)
        layout_Vfen.addWidget(hesBtn)

        layout_Vxing = QtGui.QVBoxLayout()
        layout_Vxing.addWidget(xiang_chBox)
        layout_Vxing.addWidget(wenj_chBox)
        layout_Vxing.addWidget(yinc_chBox)


        layout_Hdao = QtGui.QHBoxLayout()
        layout_Hdao.addWidget(daohBtn)
        layout_Hdao.addLayout(layout_Vyul)
        layout_Hfen =QtGui.QHBoxLayout()
        layout_Hfen.addWidget(paixBtn)
        layout_Hfen.addLayout(layout_Vfen)

        layout_Hxing =QtGui.QHBoxLayout()
        layout_Hxing.addLayout(layout_Vxing)
        layout_Hxing.addWidget(yinc_Btn)
        layout_Hxing.addWidget(Xx_Btn)

        layout_VDmain=QtGui.QVBoxLayout()
        layout_VDmain.addLayout(layout_Hdao)
        layout_VDmain.addWidget(windowlable)

        layout_VFmain=QtGui.QVBoxLayout()
        layout_VFmain.addLayout(layout_Hfen)
        layout_VFmain.addWidget(danglabel)

        layout_VXmain=QtGui.QVBoxLayout()
        layout_VXmain.addLayout(layout_Hxing)
        layout_VXmain.addWidget(xory_label)
        layout_main=QtGui.QHBoxLayout()
        layout_main.addLayout(layout_VDmain)
        layout_main.addLayout(layout_VFmain)
        layout_main.addLayout(layout_VXmain)
        self.setLayout(layout_main)
###############################################左边获取本地盘符以及树状列表的Class#####################################
class DirBrowser(QtGui.QTreeWidget):
    def __init__(self, parent=None):
        QtGui.QTreeWidget.__init__(self, parent=parent)
        self.itemExpanded.connect(self.expand)
        self.root=QtGui.QTreeWidgetItem(self)
        self.root.setText(0,u"此电脑")
        for d in self.getDrives():
            item = QtGui.QTreeWidgetItem(self.root, [d])
            item.path = d
            QtGui.QTreeWidgetItem(item, '')

    def getDrives(self):
        result = []
        for d in QtCore.QDir.drives():
            result.append(d.filePath())
        return result
    
    def expand(self, item):
        print "********************************"
        if item.text(0)==u'此电脑':
            pass
        else:
            if hasattr(item, 'takeChildren'):
                item.takeChildren()
            files = os.listdir(item.path)
            files.sort()
            for f in files:
                path = item.path.rstrip('/') + '\\' + f   # item.path.rstrip("/")为去除“/”并且是字符串右边的
                if os.path.isdir(path):
                    flag = win32file.GetFileAttributes(path)
                    if flag&2!=0:
                        pass
                    else:
                        Iconitem=QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/open.png')
                        newItem = QtGui.QTreeWidgetItem(item, [f])
                        newItem.setIcon(0,Iconitem)
                        newItem.path = path
                        QtGui.QTreeWidgetItem(newItem,'')


###############################################右边连接左边列表文件夹的树状列表的Class##################################

class FileBrowers(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent=parent)
        self.setGeometry(400,200,800,500)
        self.setWindowTitle(u"Windows界面")
        self.chose_Path = []
        self.Path = []
        self.setWindowIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/open.png'))
        self.tableWidget=QtGui.QTabWidget()
        self.tableWidget.setMaximumHeight(100)
        self.tab_file=QtGui.QWidget()
        self.list_file=QtGui.QListWidget(self.tab_file)
        self.list_file.setGeometry(QtCore.QRect(-1, -1, 800, 100))
        self.list_file.setIconSize(QtCore.QSize(10,20))
        self.l_button=QtGui.QPushButton()
        self.l_button.setIcon(QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/open.png'))
        self.l_layout=QtGui.QHBoxLayout(self.list_file)
        self.l_layout.addWidget(self.l_button)

        self.file_Btn=QtGui.QToolButton()
        self.file_Btn.setText(u'文件')

        self.file_Btn.setAutoRaise(True)
        self.file_Btn.clicked.connect(self.showFileMenu_file)

        self.home_Btn=QtGui.QToolButton()
        self.home_Btn.setText(u'主页')
        self.home_Btn.setAutoRaise(True)
        self.home_Btn.clicked.connect(self.showFileMenu_home)
        self.share_Btn = QtGui.QToolButton()
        self.share_Btn.setText(u'共享')
        self.share_Btn.setAutoRaise(True)
        self.share_Btn.clicked.connect(self.showFileMenu_share)
        self.view_Btn = QtGui.QToolButton()
        self.view_Btn.setText(u'查看')
        self.view_Btn.setAutoRaise(True)
        self.view_Btn.clicked.connect(self.showFileMenu_view)
        self.Hspacer =QtGui.QSpacerItem(228, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        self.Btn_layout=QtGui.QHBoxLayout()
        self.Btn_layout.addWidget(self.file_Btn)
        self.Btn_layout.addWidget(self.home_Btn)
        self.Btn_layout.addWidget(self.share_Btn)
        self.Btn_layout.addWidget(self.view_Btn)
        self.Btn_layout.addItem(self.Hspacer)

        self.Hlayout=QtGui.QVBoxLayout()

        self.Hlayout.addLayout(self.Btn_layout)

        self.button_left = QtGui.QToolButton()
        self.button_left.setIcon(QtGui.QIcon("D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/back.png"))
        self.button_left.setAutoRaise(True)
        self.button_left.clicked.connect(self.__backSignal)


        self.button_right=QtGui.QToolButton()
        self.button_right.setIcon(QtGui.QIcon("D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/move.png"))
        self.button_right.setAutoRaise(True)
        self.button_right.clicked.connect(self.__goSignal)

        self.button_return=QtGui.QToolButton()
        self.button_return.setIcon(QtGui.QIcon("D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/hou.png"))
        self.button_return.setAutoRaise(True)
        self.button_return.clicked.connect(self.__backSignal)

        self.refresh_Btn=QtGui.QToolButton()
        self.refresh_Btn.setIcon(QtGui.QIcon("D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/refresh.png"))
        self.refresh_Btn.setAutoRaise(True)
        self.refresh_Btn.clicked.connect(self.__refreshSignal)


        self.lineEdite=QtGui.QLineEdit()
        self.searchEdite=QtGui.QLineEdit()

        self.searchEdite.textChanged.connect(self.__searchSignal)

        self.gride_layout=QtGui.QHBoxLayout()
        self.grideH_layout=QtGui.QHBoxLayout()
        self.grideH_layout.addWidget(self.button_left)
        self.grideH_layout.addWidget(self.button_right)
        self.grideH_layout.addWidget(self.button_return)
        self.grideH_layout.addWidget(self.refresh_Btn)

        self.spliter_layout=QtGui.QSplitter()
        self.spliter_layout.addWidget(self.lineEdite)
        self.spliter_layout.addWidget(self.searchEdite)
        self.spliter_layout.setStretchFactor(0,5)
        self.spliter_layout.setStretchFactor(1,1)
        self.gride_layout.addLayout(self.grideH_layout)
        self.gride_layout.addWidget(self.spliter_layout)
        self._browser = DirBrowser()
        self._browser.setHeaderHidden(True)
        self.Vsplit_lay=QtGui.QSplitter()
        self.treeWidget = QtGui.QTreeWidget()
        self.treeWidget.setMinimumHeight(500)
        self.treeWidget.setHeaderLabels([u"名称",u"修改日期",u"类型",u"大小"])
        self.treeWidget.setColumnWidth(0,260)

        self.treeWidget.itemDoubleClicked.connect(self.__chooseDir)
        self._browser.itemClicked.connect(self.__chooseDir)


        self.Vsplit_lay.addWidget(self._browser)
        self.Vsplit_lay.addWidget(self.treeWidget)
        self.Vsplit_lay.setStretchFactor(0,2)
        self.Vsplit_lay.setStretchFactor(1, 5)
        self.treeLayout=QtGui.QVBoxLayout()
        self.treeLayout.addWidget(self.Vsplit_lay)
        mainLayout=QtGui.QHBoxLayout()
        self.baseLayout = QtGui.QVBoxLayout()
        self.muity_layout=QtGui.QVBoxLayout()
        self.muity_layout.addLayout(self.Hlayout)
        self.muity_layout.addLayout(self.gride_layout)
        self.Vlayout = QtGui.QVBoxLayout()
        self.Vlayout.addLayout(self.muity_layout)
        self.Vlayout.addLayout(self.treeLayout)
        mainLayout.addLayout(self.Vlayout)
        self.setLayout(mainLayout)
    def __backSignal(self):
        self.treeWidget.clear()
        if len(self.Path)<=1:
            self.treeWidget.clear()
        else:

            files=os.listdir(self.Path[len(self.Path)-2])
            files.sort()
            filesdir=[]
            files_name=[]
            for f in files:
                if os.path.isfile(self.Path[len(self.Path)-1])==False:
                    files_name.append(f)
                    filesdir.append(self.Path[len(self.Path)-1])
                    texts = [f, '', '']
                    Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)

                    Item.setIcon(0, QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/open.png'))
                else:
                    texts = [f, '', '']
                    Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)

            self.Path.remove(self.Path[len(self.Path)-1])
            if len(self.Path)<=0:
                self.lineEdite.setText(self.Path[len(self.Path)])
            else:

                self.lineEdite.setText(self.Path[len(self.Path)-1])
    def __goSignal(self):
        if len(self.chose_Path)==0:
            pass
        else:
            self.treeWidget.clear()

        if len(self.Path)==1:
            if 0<len(self.chose_Path)<1:

                self.treeWidget.clear()
            elif len(self.chose_Path)==0:
                pass

            else:
                files = os.listdir(self.chose_Path[len(self.chose_Path) - len(self.chose_Path)])
                print len(self.chose_Path)
                files.sort()
                filesdir = []
                files_name = []

                for f in files:
                    path=os.path.join(self.chose_Path[0],f)

                    if os.path.isdir(path) == True:
                        files_name.append(f)
                        filesdir.append(self.chose_Path[0])
                        texts = [f, '', '']
                        Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)
                        Item.setIcon(0, QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/open.png'))

                    else:
                        texts = [f, '', '']
                        Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)
        else:

            files = os.listdir(self.chose_Path[len(self.chose_Path)-(len(self.chose_Path)-1)])
            files.sort()
            filesdir = []
            files_name = []
            for f in files:
                path_name=os.path.join(self.chose_Path[len(self.chose_Path)-(len(self.chose_Path)-1)],f)
                if os.path.isfile(path_name) == False:
                    files_name.append(f)
                    filesdir.append(path_name)
                    texts = [f, '', '']
                    Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)

                    Item.setIcon(0, QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/open.png'))
                else:
                    texts = [f, '', '']
                    Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)

        if len(self.chose_Path)<1:
            pass
        else:
            self.lineEdite.setText(self.chose_Path[0])
            self.chose_Path.remove(self.chose_Path[0])

    def __chooseDir(self, item,column):#向treewidget列表中添加文件夹和文件

        try:
            if item.path == []:
                pass
            else:

                self.treeWidget.clear()
                files = os.listdir(item.path)
                self.chose_Path.append(item.path)
                files.sort()
                filesdir=[]
                files_name=[]
                for f in files:
                    path=os.path.join(item.path,f)
                    if os.path.isfile(path)==False:
                        flag = win32file.GetFileAttributes(path)
                        if flag & 2 != 0:
                            pass
                        else:
                            statinfo = os.stat(path)
                            timestamp = statinfo.st_mtime
                            # 转换成localtime
                            time_local = time.localtime(timestamp)
                            # 转换成新的时间格式(2016-05-05 20:28:54)
                            dt = time.strftime("%Y/%m/%d %H:%M:%S", time_local)
                            files_name.append(f)
                            filesdir.append(path)

                            texts = [f, '', '']
                            Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)

                            Item.setIcon(0,QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/open.png'))

                            Item.setText(1,dt)
                            Item.setText(2,u"文件夹")
                            Item.path = path
                    else:
                        statinfo = os.stat(path)
                        timestamp = statinfo.st_mtime

                        # 转换成localtime
                        time_local = time.localtime(timestamp)
                        # 转换成新的时间格式(2016-05-05 20:28:54)
                        dt = time.strftime("%Y/%m/%d %H:%M:%S", time_local)
                        files_name.append(f)
                        filesdir.append(path)
                        texts = [f, '', '']
                        Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)
                        fname=os.path.splitext(path)
                        Item.setText(1,dt)
                        for ii in fname:
                            if "." in ii:
                                Item.setText(2, fname[1].split(".")[1])
                            else:
                                pass
                        file_size = os.stat(path)
                        filename_size = file_size.st_size / 1024
                        if filename_size==0:
                            filename_str=str(filename_size+1)+"kb"
                        else:
                            if filename_size < 1024:
                                filename_str = str(filename_size) + "kb"
                            elif filename_size > 1024 and filename_size < 1048576:
                                filename_str = str(filename_size/1024) + "M"
                            else:
                                filename_str=str(filename_size/1048576)+"G"
                        Item.setText(3,filename_str)
                        Item.path=[]
                    self.lineEdite.setText(self.chose_Path[len(self.chose_Path)-1])
                    self.Path = [i for i in self.chose_Path]
        except AttributeError:
            pass

    def __searchSignal(self):
        self.treeWidget.clear()
        self.sousuo_text = self.lineEdite.text()
        self.sou_text=self.sousuoEdite.text()
        self.sou_str=str(self.sou_text)
        files=os.listdir(self.sousuo_text)

        for ii in files:
            path=os.path.join(self.sousuo_text,ii)
            if self.sou_str in ii:
                if os.path.isfile(path)==False:
                    texts=[ii,'','']
                    Item=QtGui.QTreeWidgetItem(self.treeWidget,texts)
                    Item.setIcon(0, QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/open.png'))
                else:
                    texts = [ii, '', '']
                    Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)
    def __refreshSignal(self):
        self.treeWidget.clear()
        self.text=self.lineEdite.text()
        files = os.listdir(self.text)
        print self.text
        print files
        for f in files:
            path=os.path.join(self.text,f)
            if os.path.isfile(path)==False:
                texts = [f, '', '']
                Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)
                Item.setIcon(0,QtGui.QIcon('D:/python2.7/Lib/site-packages/PySide/examples/demos/qtdemo/images/open.png'))
            else:
                texts = [f, '', '']
                Item = QtGui.QTreeWidgetItem(self.treeWidget, texts)

    def showFileMenu_file(self):
        dialog = FileMenuDialog(self)
        mouse_xy = self.file_Btn.mapToGlobal(self.file_Btn.pos())  # 获取self.toolButton的相对位置
        x = mouse_xy.x()-6
        y = mouse_xy.y()+11
        dialog.move(x, y)  # 移动self.popup_window的位置，通过改x，y的值
        dialog.show()
    def showFileMenu_home(self):
        dialog = HomeMenuDialog(self)
        mouse_xy = self.home_Btn.mapToGlobal(self.home_Btn.pos())  # 获取self.toolButton的相对位置
        x = mouse_xy.x()-65
        y = mouse_xy.y()+11
        dialog.move(x, y)  # 移动self.popup_window的位置，通过改x，y的值
        dialog.show()
    def showFileMenu_share(self):
        dialog = ShareMenuDialog(self)
        mouse_xy = self.share_Btn.mapToGlobal(self.share_Btn.pos())  # 获取self.toolButton的相对位置
        x = mouse_xy.x()-125
        y = mouse_xy.y()+11
        dialog.move(x, y)  # 移动self.popup_window的位置，通过改x，y的值
        dialog.show()
    def showFileMenu_view(self):
        dialog = ViewMenuDialog(self)
        mouse_xy = self.view_Btn.mapToGlobal(self.view_Btn.pos())  # 获取self.toolButton的相对位置
        x = mouse_xy.x()-185
        y = mouse_xy.y()+11
        dialog.move(x, y)  # 移动self.popup_window的位置，通过改x，y的值
        dialog.show()


if __name__ =="__main__":
    app=QtGui.QApplication(sys.argv)
    filebrowers=FileBrowers()
    filebrowers.show()
    sys.exit(app.exec_())

