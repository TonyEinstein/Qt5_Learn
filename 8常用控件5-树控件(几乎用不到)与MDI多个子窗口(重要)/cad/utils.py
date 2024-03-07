from OCC.Display.backend import load_backend, get_qt_modules
load_backend('qt-pyside2')
from OCC.Display.qtDisplay import qtViewer3d

from PySide2.QtUiTools import QUiLoader
g_ui_loader = QUiLoader()        
g_ui_loader.registerCustomWidget(qtViewer3d)