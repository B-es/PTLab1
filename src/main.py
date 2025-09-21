import argparse
import sys
from CalcRating import CalcRating
from JsonDataReader import JsonDataReader
from TextDataReader import TextDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def print_data(students, rating):
    print("Students: ", students)
    print("Rating: ", rating)


def main():
    path = get_path_from_arguments(sys.argv[1:])
    if "json" in path:
        reader = JsonDataReader()
    else:
        reader = TextDataReader()
    students = reader.read(path)
    rating = CalcRating(students).calc()
    print_data(students, rating)


if __name__ == "__main__":
    main()
