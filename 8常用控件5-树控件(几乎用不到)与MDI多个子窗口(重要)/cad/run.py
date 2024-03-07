from PySide2.QtWidgets import QApplication, QMessageBox,QMdiSubWindow,QInputDialog,QMainWindow,QTreeWidgetItem,QLineEdit

from utils import g_ui_loader


class Main:


    def __init__(self,app):
        self.app = app
        self.ui = g_ui_loader.load('main.ui')

        self.wins = [] # 保存openocc 处理类对象

        self.loadTree()

        self.ui.notesTree.itemDoubleClicked.connect(self.itemDoubleClicked)


    def openocc_bottle(self):        
        from oocc_bottle import OOCC_Bottle
        win = OOCC_Bottle(self)
        win.setPara()
        win.render()

        self.wins.append(win)

    def openocc_surface(self):        
        from oocc_surface import OOCC_Surface
        win = OOCC_Surface(self)
        win.setPara()
        win.render()

        self.wins.append(win)


    def itemDoubleClicked(self, item, column):
        # 获取被点击的节点文本
        clickedText = item.text(column)

        if 'bottle' in clickedText:
            self.openocc_bottle()
        elif 'surface' in clickedText:
            self.openocc_surface()


    def loadTree(self):

        root = self.ui.notesTree.invisibleRootItem()

        # 准备一个folder节点
        folderItem = QTreeWidgetItem()

        
        # 设置该节点  第1个column 文本
        folderItem.setText(0, '基础几何体')
        
        root.addChild(folderItem) # 添加到树的不可见根节点下，就成为第一层节点
        
        folderItem.setExpanded(True) # 设置该节点为展开状态

        
        leafItem = QTreeWidgetItem()  # 准备一个 叶子 节点            
        leafItem.setText(0, '立方体') # 设置该节点  第1个column 文本
        folderItem.addChild(leafItem) # 添加到目录节点中

        
        leafItem = QTreeWidgetItem()  # 准备一个 叶子 节点  
        leafItem.setText(0, '球体')
        folderItem.addChild(leafItem)
        
        leafItem = QTreeWidgetItem()  # 准备一个 叶子 节点  
        leafItem.setText(0, '圆柱')
        folderItem.addChild(leafItem)

        leafItem = QTreeWidgetItem()  # 准备一个 叶子 节点  
        leafItem.setText(0, '圆锥')
        folderItem.addChild(leafItem)

        leafItem = QTreeWidgetItem()  # 准备一个 叶子 节点  
        leafItem.setText(0, '弧面surface')
        folderItem.addChild(leafItem)

        
        
        # 准备一个folder节点
        folderItem = QTreeWidgetItem()
        folderItem.setText(0, '物品3D建模')
        root.addChild(folderItem)
        folderItem.setExpanded(True)

        leafItem = QTreeWidgetItem()   
        leafItem.setText(0, '桌椅') 
        folderItem.addChild(leafItem)
        
        leafItem = QTreeWidgetItem()   
        leafItem.setText(0, '1号瓶体bottle')
        folderItem.addChild(leafItem)
        
        leafItem = QTreeWidgetItem()   
        leafItem.setText(0, '3号瓶体bottle')
        folderItem.addChild(leafItem)

        leafItem = QTreeWidgetItem()   
        leafItem.setText(0, '防盗门')
        folderItem.addChild(leafItem)


    # 关闭窗口
    def closeEvent(self, event):
        event.accept()


app = QApplication([])
main = Main(app)
main.ui.show()
app.exec_()