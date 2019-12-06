import inspect

from xplore.exploration.builder import ExplorationBuilder
from xplore.exploration.utils import get_function_body


class Shape(ExplorationBuilder):
    def build_name(self):
        super().build_name("shape")

    def build_title(self):
        super().build_title("### Shape of the Dataframe")

    def build_implementation(self):
        def shape(df):
            return df.shape

        implementation = inspect.getsource(shape)
        super().build_implementation(implementation)

    def build_executable(self):
        def executable():
            shape(df)

        super().build_executable(executable)


class Read(ExplorationBuilder):
    def __init__(self, path):
        super(Read, self).__init__()
        self.path = path

    def build_name(self):
        super().build_name("read")

    def build_title(self):
        super().build_title("### Read the Data into a Dataframe")

    def build_implementation(self):
        def read():
            import pandas as pd

            df = pd.read_csv("{}", low_memory=False)
            return df

        implementation = inspect.getsource(read).format(self.path)
        super().build_implementation(implementation)

    def build_executable(self):
        def executable():
            df = read()

        super().build_executable(executable)


class Head(ExplorationBuilder):
    def build_name(self):
        super().build_name("head")

    def build_title(self):
        super().build_title("### Head of the Dataframe")

    def build_implementation(self):
        def head(df):
            return df.head()

        implementation = inspect.getsource(head)
        super().build_implementation(implementation)

    def build_executable(self):
        def executable():
            head(df)

        super().build_executable(executable)


class ColumnTypes(ExplorationBuilder):
    def build_name(self):
        super().build_name("column_types")

    def build_title(self):
        super().build_title("### Types of Columns")

    def build_implementation(self):
        def column_types(df):
            import numpy as np

            numerical_columns = list(df.select_dtypes(include=[np.number]).columns)
            non_numerical_columns = list(df.select_dtypes(exclude=[np.number]).columns)
            return numerical_columns, non_numerical_columns

        implementation = inspect.getsource(column_types)
        super().build_implementation(implementation)

    def build_executable(self):
        def executable():
            numerical_columns, non_numerical_columns = column_types(df)
            print("Numerical columns:", numerical_columns)
            print("Non-numerical columns:", non_numerical_columns)

        super().build_executable(executable)
