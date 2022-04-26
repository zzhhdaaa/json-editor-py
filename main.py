"""
This is the main window to launch the editor
The whole UI mainly divided by two part:
1. Browser(json) on the left
2. Model(table) on the right
"""

"""
References:
This JSON Editor Tool highly relies on packages: QJsonModel, jsonViewer,
which provide classes and methods to display and control dictionary-like,
hierarchical data structure.
QJsonModel: https://github.com/dridk/QJsonModel.git
jsonViewer: https://github.com/leixingyu/jsonEditor.git
"""

# Required: Qt.py (pip install Qt.py)
import sys
import os
import json
import ast
import webbrowser
import xmltodict
import Qt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from jsonViewer.qjsonmodel import QJsonModel
from jsonViewer.qjsonview import QJsonView
from jsonViewer.qjsonnode import QJsonNode

# High dpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# Set UI file (QT designer)
MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
UI_PATH = os.path.join(MODULE_PATH, 'ui', 'jsonEditor.ui')

# Default JSON file
with open("_test.json", "r") as f:
    TEST_DICT = json.load(f)
with open("_new.json", "r") as f:
    NEW_DICT = json.load(f)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load UI file
        Qt._loadUi(UI_PATH, self)

        # Set the model(table) StyleSheet & add it to layout
        self.ui_tree_view = QJsonView()
        self.ui_tree_view.setStyleSheet(
            'QWidget{font: 10pt "Consolas";}'
            "QTreeView { show-decoration-selected: 1; }"
            "QTreeView::item:hover { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 lightgray, stop: 1 white); }"
            "QTreeView::item:selected:active { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 lightgray, stop: 1 lightgray); color: black; }"
            "QTreeView::item:selected:!active { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 lightgray, stop: 1 lightgray); color: black;}")
        self.ui_tree_view.setAnimated(True)
        self.ui_grid_layout.addWidget(self.ui_tree_view, 0, 2)

        # Load initial TEST_DICT
        root = QJsonNode.load(TEST_DICT)
        self._model = QJsonModel(root, self)

        # Proxy model
        self._proxyModel = QtCore.QSortFilterProxyModel(self)
        self._proxyModel.setSourceModel(self._model)
        self._proxyModel.setDynamicSortFilter(False)
        self._proxyModel.setSortRole(QJsonModel.sortRole)
        self._proxyModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self._proxyModel.setFilterRole(QJsonModel.filterRole)
        self._proxyModel.setFilterKeyColumn(0)

        # Filter
        self.ui_filter_edit.textChanged.connect(
            self._proxyModel.setFilterRegExp)

        # Buttons
        self.ui_updateBrowser_btn.clicked.connect(self.updateBrowser)
        self.ui_updateModel_btn.clicked.connect(self.updateModel)
        self.ui_expand.clicked.connect(self.expandAll)
        self.ui_collapse.clicked.connect(self.collapseAll)

        # Create Actions in Menubar
        # self.menuFile.addAction(self.actionOpen)
        # self.menuFile.addAction(self.actionSave)

        # Menubar
        self.actionNew.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionImport_xml.triggered.connect(self.importXML)
        self.actionCopy.triggered.connect(self.ui_tree_view.copy)
        # TODO: Paste Shortcut
        # self.actionPaste.triggered.connect(self.ui_tree_view.paste(0))
        self.actionUser_Manual.triggered.connect(lambda: self.openWebpage('https://github.com/zzhhdaaa/JSON_Editor_Py/blob/main/README.md'))
        self.actionDeveloper.triggered.connect(lambda: self.openWebpage('https://www.daaa.one/'))

        # Json Viewer
        self.ui_tree_view.setModel(self._proxyModel)
        self.updateBrowser()
        self.filePath = ['', '']

    # Open file
    def openFile(self):
        print("Open!")
        self.filePath = QFileDialog.getOpenFileName(self, "Open JSON", self.filePath[0], "JSON Files (*.json)")
        print(self.filePath)
        if self.filePath[0] != '':
            file = open(self.filePath[0], 'r')
            self.ui_view_edit.clear()
            output = json.load(file)
            jsonDict = json.dumps(output, indent=3, sort_keys=True)
            self.ui_view_edit.setPlainText(str(jsonDict))
            self.updateModel()
            self.setWindowTitle(self.filePath[0])

    # Import .xml and convert to .json
    def importXML(self):
        print("Open!")
        self.filePath = QFileDialog.getOpenFileName(self, "Import XML", self.filePath[0], "XML Files (*.xml)")
        print(self.filePath)
        if self.filePath[0] != '':
            with open(self.filePath[0]) as xml_file:
                data_dict = xmltodict.parse(xml_file.read())
            self.ui_view_edit.clear()
            jsonDict = json.dumps(data_dict, indent=3, sort_keys=True)
            self.ui_view_edit.setPlainText(str(jsonDict))
            self.updateModel()
            self.setWindowTitle(self.filePath[0])

    # Save file
    def saveFile(self):
        print("Save!")
        self.filePath = QFileDialog.getSaveFileName(self, "Save JSON", self.filePath[0], "JSON Files (*.json)")
        if self.filePath[0] != '':
            file = open(self.filePath[0], 'w')
            file.write(self.ui_view_edit.toPlainText())
            self.setWindowTitle(self.filePath[0])

    # New file, using NEW_DICT as template
    def newFile(self):
        print("New!")
        self.filePath = QFileDialog.getSaveFileName(self, "Save JSON", self.filePath[0], "JSON Files (*.json)")
        if self.filePath[0] != '':
            file = open(self.filePath[0], 'w')
            self.ui_view_edit.clear()
            jsonDict = json.dumps(NEW_DICT, indent=3, sort_keys=True)
            self.ui_view_edit.setPlainText(str(jsonDict))
            file.write(self.ui_view_edit.toPlainText())
            self.updateModel()
            self.setWindowTitle(self.filePath[0])

    # Collapse
    def collapseAll(self):
        self.ui_tree_view.collapseAll()

    # Expand
    def expandAll(self):
        self.ui_tree_view.expandAll()

    # Update the Table on the right
    def updateModel(self):
        text = self.ui_view_edit.toPlainText()
        jsonDict = ast.literal_eval(text)
        root = QJsonNode.load(jsonDict)
        self._model = QJsonModel(root)
        self._proxyModel.setSourceModel(self._model)

    # Update the Browser on the left
    def updateBrowser(self):
        self.ui_view_edit.clear()
        output = self.ui_tree_view.asDict(None)
        jsonDict = json.dumps(output, indent=3, sort_keys=True)
        self.ui_view_edit.setPlainText(str(jsonDict))

    def openWebpage(self, link):
        webbrowser.open_new(link)

    '''
    def pprint(self):
        output = self.ui_tree_view.asDict(
            self.ui_tree_view.getSelectedIndices())
        jsonDict = json.dumps(output, indent=4, sort_keys=True)

        print(jsonDict)
    '''


def show():
    global window
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show()
