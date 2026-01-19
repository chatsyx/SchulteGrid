class ClickChecker:
    def __init__(self, total_num):
        self.current_target = 1
        self.total_num = total_num

    def check(self, click_num):
        if click_num == self.current_target:
            self.current_target += 1
            is_finish = self.current_target > self.total_num
            return True, is_finish
        return False, False