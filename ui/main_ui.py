from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QComboBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class SchulteUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 窗口基础设置
        self.setWindowTitle("舒尔特方格（注意力训练）v1.0")
        self.resize(500, 550)
        self.main_layout = QVBoxLayout()  # 总垂直布局

        # 1. 网格规格选择栏
        self.select_layout = QHBoxLayout()
        self.level_label = QLabel("选择网格规格：")
        self.level_combo = QComboBox()
        self.level_combo.addItems(["3×3", "4×4", "5×5", "6×6", "7×7"])
        self.select_layout.addWidget(self.level_label)
        self.select_layout.addWidget(self.level_combo)
        self.main_layout.addLayout(self.select_layout)

        # 2. 网格展示区
        self.grid_container = QWidget()  
        self.grid_layout = QVBoxLayout(self.grid_container)  
        self.main_layout.addWidget(self.grid_container, alignment=Qt.AlignmentFlag.AlignCenter)  

        # 3. 训练结果显示区
        self.result_label = QLabel("训练结果：未开始")
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.result_label)

        # 4. 功能控制按钮区
        self.btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("开始训练")
        self.reset_btn = QPushButton("重置网格")
        self.btn_layout.addWidget(self.start_btn)
        self.btn_layout.addWidget(self.reset_btn)
        self.main_layout.addLayout(self.btn_layout)

        self.setLayout(self.main_layout)

    def create_grid_buttons(self, grid, n):
        """生成n×n数字按钮网格，自动清空旧网格"""
        # 清空原有网格按钮，防止重复叠加
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        # 逐行生成按钮，保证界面整齐
        for row in range(n):
            row_layout = QHBoxLayout()
            for col in range(n):
                num = grid[row][col]
                btn = QPushButton(str(num))
                btn.setFont(QFont("Arial", 16))
                btn.setFixedSize(60, 60)
                row_layout.addWidget(btn)
            self.grid_layout.addLayout(row_layout)