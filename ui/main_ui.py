from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QComboBox, QRadioButton, QButtonGroup)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class SchulteUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("舒尔特方格（注意力训练）v1.1")
        self.resize(550, 600)  # 微调窗口大小，适配模式栏
        self.main_layout = QVBoxLayout()

        # 1. v1.1新增：训练模式切换栏（数字/字母单选）
        self.mode_layout = QHBoxLayout()
        self.mode_label = QLabel("训练模式：")
        self.num_radio = QRadioButton("数字模式（默认）")
        self.letter_radio = QRadioButton("字母模式")
        self.num_radio.setChecked(True)  # 默认数字模式
        # 按钮组，确保单选
        self.mode_group = QButtonGroup()
        self.mode_group.addButton(self.num_radio)
        self.mode_group.addButton(self.letter_radio)
        self.mode_layout.addWidget(self.mode_label)
        self.mode_layout.addWidget(self.num_radio)
        self.mode_layout.addWidget(self.letter_radio)
        self.main_layout.addLayout(self.mode_layout)

        # 2. 网格规格选择栏（原有功能，保留）
        self.select_layout = QHBoxLayout()
        self.level_label = QLabel("网格规格：")
        self.level_combo = QComboBox()
        self.level_combo.addItems(["3×3", "4×4", "5×5", "6×6", "7×7"])
        self.select_layout.addWidget(self.level_label)
        self.select_layout.addWidget(self.level_combo)
        self.main_layout.addLayout(self.select_layout)

        # 3. 网格展示区（原有核心，保留，居中效果不变）
        self.grid_container = QWidget()
        self.grid_layout = QVBoxLayout(self.grid_container)
        self.main_layout.addWidget(self.grid_container, alignment=Qt.AlignmentFlag.AlignCenter)

        # 4. 结果显示区（原有功能，保留）
        self.result_label = QLabel("训练结果：未开始")
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.result_label)

        # 5. 控制按钮区（原有功能，保留）
        self.btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("开始训练")
        self.reset_btn = QPushButton("重置网格")
        self.btn_layout.addWidget(self.start_btn)
        self.btn_layout.addWidget(self.reset_btn)
        self.main_layout.addLayout(self.btn_layout)

        self.setLayout(self.main_layout)

    def create_grid_buttons(self, grid, n):
        """生成网格按钮（兼容数字/字母，原有逻辑复用）"""
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        for row in range(n):
            row_layout = QHBoxLayout()
            for col in range(n):
                content = grid[row][col]  # 兼容数字/字母
                btn = QPushButton(str(content))
                btn.setFont(QFont("Arial", 16))
                btn.setFixedSize(60, 60)
                row_layout.addWidget(btn)
            self.grid_layout.addLayout(row_layout)
    
    # v1.1新增：获取当前选中模式
    def get_current_mode(self):
        """返回当前选中模式：number/letter"""
        return "number" if self.num_radio.isChecked() else "letter"