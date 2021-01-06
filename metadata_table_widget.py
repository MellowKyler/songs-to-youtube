# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from song_tree_widget_item import TreeWidgetItemData
from const import CustomDataRole


class MetadataTableWidget(QTableWidget):
    def __init__(self, *args):
        super().__init__(*args)

    def from_data(self, data: TreeWidgetItemData):
        for key, value in data.metadata.items():
            self.insertRow(self.rowCount())
            key_item = QTableWidgetItem(key)
            key_item.setFlags(Qt.ItemIsEnabled | Qt.ItemNeverHasChildren)
            value_item = QTableWidgetItem(value)
            value_item.setFlags(Qt.ItemIsEnabled | Qt.ItemNeverHasChildren | Qt.ItemIsEditable | Qt.ItemIsSelectable)
            self.setItem(self.rowCount() - 1, 0, key_item)
            self.setItem(self.rowCount() - 1, 1, value_item)

    def resizeEvent(self, event):
        for c in range(self.columnCount()):
            self.setColumnWidth(c, event.size().width() // self.columnCount())
