from src.Types import DataType
from src.CalcDebt import CalcDebt
import pytest


class TestCalcDebt:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 60),
                    ("программирование", 50),
                ]
        }

        count_debt: int = 1

        return data, count_debt

    def test_init_calc_debt(self, input_data: tuple[DataType, int]) -> None:
        calc_rating = CalcDebt(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, int]) -> None:
        count_debt = CalcDebt(input_data[0]).calc()
        assert count_debt == input_data[1]
