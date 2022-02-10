class FieldCoord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_correct = self.is_correct()

    def is_in(self, find):
        count = 1
        for item in find:
            if item.x == self.x and item.y == self.y:
                return count
            count += 1
        return None

    def is_correct(self):
        try:
            return 0 <= self.x <= 16 and 0 <= self.y <= 16
        except Exception:
            return False
