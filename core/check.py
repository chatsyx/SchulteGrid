class ClickChecker:
    def __init__(self, total_num, mode="number"):
        """v1.1新增mode参数，支持number（数字）/letter（字母）模式"""
        self.total_num = total_num  # 总数量n²
        self.mode = mode
        self.current_target = self._get_init_target()  # 初始目标值

    def _get_init_target(self):
        """初始化目标（数字从1，字母从a）"""
        return 1 if self.mode == "number" else "a"

    def check(self, click_content):
        """校验点击内容，数字传int，字母传str"""
        # 数字模式校验（原有逻辑，保留）
        if self.mode == "number":
            click_num = int(click_content)
            if click_num == self.current_target:
                self.current_target += 1
                is_finish = self.current_target > self.total_num
                return True, is_finish
            return False, False
        
        # v1.1新增：字母模式校验（按a→b→c顺序）
        if self.mode == "letter":
            if click_content == self.current_target:
                # 字母目标自增（a→b，z后继续aa，适配7阶49个字母）
                self.current_target = chr(ord(self.current_target) + 1)
                is_finish = ord(self.current_target) > ord("a") + self.total_num - 1
                return True, is_finish
            return False, False