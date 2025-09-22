from Types import DataType


class CalcDebt:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.condition = lambda x: x < 61

    def calc(self) -> int:
        count_debt = 0
        for key in self.data:
            for _, score in self.data[key]:
                if self.condition(score):
                    count_debt += 1
                    break
        return count_debt
