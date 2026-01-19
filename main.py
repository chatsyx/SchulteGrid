import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from ui.main_ui import SchulteUI
from core.grid_gen import generate_grid
from core.timer import SchulteTimer
from core.check import ClickChecker

class SchulteGame:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui = SchulteUI()
        self.timer = SchulteTimer()
        self.checker = None
        self.grid = None
        self.n = 3
        self.bind_events()

    def bind_events(self):
        self.ui.start_btn.clicked.connect(self.start_game)
        self.ui.reset_btn.clicked.connect(self.reset_game)
        self.ui.level_combo.currentTextChanged.connect(self.change_level)

    def change_level(self):
        level_text = self.ui.level_combo.currentText()
        self.n = int(level_text.split("×")[0])
        self.reset_game()

    def start_game(self):
        self.reset_game()
        self.grid = generate_grid(self.n)
        self.ui.create_grid_buttons(self.grid, self.n)
        # 绑定网格按钮点击事件
        for i in range(self.ui.grid_layout.count()):
            row_layout = self.ui.grid_layout.itemAt(i).layout()
            for j in range(row_layout.count()):
                btn = row_layout.itemAt(j).widget()
                btn.clicked.connect(lambda _, b=btn: self.click_grid(b))
        self.checker = ClickChecker(self.n * self.n)
        self.ui.result_label.setText("训练结果：计时中...")

    def click_grid(self, btn):
        click_num = int(btn.text())
        is_correct, is_finish = self.checker.check(click_num)
        if not is_correct:
            QMessageBox.warning(self.ui, "提示", "顺序错误，请点击当前目标数字！")
            return
        if click_num == 1:
            self.timer.start()
        if is_finish:
            cost_time = self.timer.stop()
            self.show_result(cost_time)
            return
        btn.setEnabled(False)

    def show_result(self, cost_time):
        if self.n ==5:
            if cost_time <=30:
                grade = "优秀"
            elif cost_time <=40:
                grade = "良好"
            elif cost_time <=50:
                grade = "一般"
            else:
                grade = "需加强"
            result_text = f"训练结果：{cost_time}秒（{grade}）"
        else:
            result_text = f"训练结果：{cost_time}秒"
        self.ui.result_label.setText(result_text)
        QMessageBox.information(self.ui, "完成", f"训练完成！总用时：{cost_time}秒")

    def reset_game(self):
        self.timer = SchulteTimer()
        self.checker = None
        self.grid = None
        while self.ui.grid_layout.count():
            child = self.ui.grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.ui.result_label.setText("训练结果：未开始")

    def run(self):
        self.ui.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    game = SchulteGame()
    game.run()