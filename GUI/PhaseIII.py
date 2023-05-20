import sys
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QTableView, QComboBox, QLineEdit, QHBoxLayout, QLabel, QWidget, QMainWindow, QVBoxLayout, QPushButton



class DataFrameModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data):
        super(DataFrameModel, self).__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None


class MainWidget(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.initUI()

    def initUI(self):
        self.setWindowTitle('NFL Players Data')

        # Create the central widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Apply stylesheet
        self.centralWidget.setStyleSheet("background-color: lightgray;")

        # Create the layout
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        # Create the filter widgets
        self.positionLabel = QLabel('Position:')
        self.positionComboBox = QComboBox()
        self.positionComboBox.addItems(['All Positions', 'QB', 'RB', 'WR', 'TE', 'OT', 'OG', 'C', 'DE', 'DT', 'LB', 'CB', 'S'])
        self.nameLabel = QLabel('Name:')
        self.nameLineEdit = QLineEdit()
        self.filterButton = QPushButton('Filter')
        self.clearButton = QPushButton('Clear')

        # Add the filter widgets to the layout
        filterLayout = QHBoxLayout()
        filterLayout.addWidget(self.positionLabel)
        filterLayout.addWidget(self.positionComboBox)
        filterLayout.addWidget(self.nameLabel)
        filterLayout.addWidget(self.nameLineEdit)
        filterLayout.addWidget(self.filterButton)
        filterLayout.addWidget(self.clearButton)
        self.layout.addLayout(filterLayout)

        # Create the table view
        self.tableView = QTableView()
        self.model = DataFrameModel(self.data)
        self.tableView.setModel(self.model)
        
        self.tableView.setStyleSheet("""
            QHeaderView::section {
                background-color: #2C3E50;
                color: white;
                font-size: 12pt;
            }

            QTableView {
                background-color: white;
                color: black;
                font-size: 12pt;
            }

            QTableView::item:selected {
                background-color: #3498DB;
                color: white;
            }

            QTableView::item:hover {
                background-color: #ECF0F1;
                color: black;
            }
        """)


        # Set the stretch factors for the table view
        self.layout.addWidget(self.tableView)
        self.layout.setStretchFactor(self.tableView, 1)

        # Connect the filter and clear buttons to their respective methods
        self.filterButton.clicked.connect(self.filterData)
        self.clearButton.clicked.connect(self.clearFilters)

        # Enable sorting on the table view
        self.tableView.setSortingEnabled(True)

        # Apply stylesheet to table view
        self.tableView.setStyleSheet("font-size: 12pt;")

    def sortData(self, index):
        self.model.sort(index, Qt.AscendingOrder if self.model.sortOrder(index) == Qt.DescendingOrder else Qt.DescendingOrder)

    def filterData(self):
        position = self.positionComboBox.currentText()
        name = self.nameLineEdit.text()

        if position == 'All Positions':
            filteredData = self.data
        else:
            filteredData = self.data[self.data['position'] == position]

        if name != '':
            filteredData = filteredData[filteredData['name'].str.contains(name, case=False)]

        self.tableView.setModel(DataFrameModel(filteredData))

    def clearFilters(self):
        self.positionComboBox.setCurrentIndex(0)
        self.nameLineEdit.setText('')
        self.tableView.setModel(DataFrameModel(self.data))
        
if __name__ == '__main__':
    # Load the data from CSV file
    data = pd.read_csv('clean_playerdata.csv')

    # Create the application and main window
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    mainWindow.setWindowTitle('NFL Player Stats')
    mainWidget = MainWidget(data)
    mainWindow.setCentralWidget(mainWidget)
    mainWindow.show()

    # Run the application
    sys.exit(app.exec_())

