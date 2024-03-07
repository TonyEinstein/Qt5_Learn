from utils import g_ui_loader
from PySide2.QtWidgets import  QMessageBox,QMdiSubWindow,QTableWidgetItem
from PySide2 import QtGui,QtCore
import math


from OCC.Core.gp import gp_Pnt
from OCC.Core.GeomAPI import GeomAPI_PointsToBSpline
from OCC.Core.TColgp import TColgp_Array1OfPnt
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_MakePipe



class OOCC_Surface:
   
    def __init__(self,main):        
        form = g_ui_loader.load('form3d.ui')    
        
        form.viewer3d.InitDriver()  
        
        subWindow = QMdiSubWindow()
        subWindow.setWidget(form)
        subWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        main.ui.mdiArea.addSubWindow(subWindow)
        subWindow.setWindowTitle("3段曲面设计" )
        subWindow.show()

 
        self.form = form

        # 信号

        form.render_button.clicked.connect(self.render)

    # 设置参数表格
    def setPara(self):
        form = self.form
        
        item = QTableWidgetItem()
        item.setText('曲面1弧度')
        form.table.setItem(0, 0, item)        
        item = QTableWidgetItem()
        item.setText('曲面1弧度')
        form.table.setItem(1, 0, item)
        item = QTableWidgetItem()
        item.setText('曲面1弧度')
        form.table.setItem(2, 0, item)

        
        item = QTableWidgetItem()
        item.setText('15.3')
        form.table.setItem(0, 1, item)        
        item = QTableWidgetItem()
        item.setText('22.4')
        form.table.setItem(1, 1, item)
        item = QTableWidgetItem()
        item.setText('78.2')
        form.table.setItem(2, 1, item)

        
        item = QTableWidgetItem()
        item.setText('最左边曲面弧度')
        form.table.setItem(0, 2, item)        
        item = QTableWidgetItem()
        item.setText('中间曲面弧度')
        form.table.setItem(1, 2, item)
        item = QTableWidgetItem()
        item.setText('最右边曲面弧度')
        form.table.setItem(2, 2, item)

    # 展示3d图形 
    def render(self):

        form = self.form
        display = form.viewer3d._display

        form.viewer3d._display.EraseAll()
        # form.viewer3d.qApp = main.app

        
        
        # the bspline path, must be a wire
        array2 = TColgp_Array1OfPnt(1, 3)
        array2.SetValue(1, gp_Pnt(0, 0, 0))
        array2.SetValue(2, gp_Pnt(0, 1, 2))
        array2.SetValue(3, gp_Pnt(0, 2, 3))
        bspline2 = GeomAPI_PointsToBSpline(array2).Curve()
        path_edge = BRepBuilderAPI_MakeEdge(bspline2).Edge()
        path_wire = BRepBuilderAPI_MakeWire(path_edge).Wire()

        # the bspline profile. Profile mist be a wire
        array = TColgp_Array1OfPnt(1, 5)
        array.SetValue(1, gp_Pnt(0, 0, 0))
        array.SetValue(2, gp_Pnt(1, 2, 0))
        array.SetValue(3, gp_Pnt(2, 3, 0))
        array.SetValue(4, gp_Pnt(4, 3, 0))
        array.SetValue(5, gp_Pnt(5, 5, 0))
        bspline = GeomAPI_PointsToBSpline(array).Curve()
        profile_edge = BRepBuilderAPI_MakeEdge(bspline).Edge()

        # pipe
        pipe = BRepOffsetAPI_MakePipe(path_wire, profile_edge).Shape()

        display.DisplayShape(profile_edge, update=False)
        display.DisplayShape(path_wire, update=False)
        display.DisplayShape(pipe, update=True)


        