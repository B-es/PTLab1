from Types import DataType
from DataReader import DataReader
from json import load


class JsonDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            json_data = load(file)
            for key, value in json_data.items():
                self.students[key] = [(subj, score) for subj, score in
                                      value.items()]

        return self.students
