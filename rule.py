class Rule:


    def __init__(self, winPos):
        self.winPos = winPos

    def winByEquality2(self, gb):
        for win in self.winPos:
            if len(win) == 2 and gb[win[0]] == gb[win[1]]:
                return True
        return False

    def winByEquality3(self, gb):
        for win in self.winPos:
            if len(win) == 3 and gb[win[0]] == gb[win[1]] and gb[win[1]] == gb[win[2]]:
                return True
        return False

    def winByEquality4(self, gb):
        for win in self.winPos:
            if len(win) == 4 and gb[win[0]] == gb[win[1]] and gb[win[1]] == gb[win[2]] and gb[win[2]] == gb[win[3]]:
                return True
        return False