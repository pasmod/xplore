import inspect

from xplore.exploration.builder import SimpleExploration


class PercentageOfMissingValuesInColumns(SimpleExploration):
    def build_name(self):
        super().build_name("percentage_of_missing_values_in_columns")

    def build_title(self):
        super().build_title("### Percentage of Missing Values in Columns")

    def build_implementation(self):
        def missing_values_percentage(df):
            import pandas as pd

            percent_missing = df.isnull().sum() * 100 / len(df)
            missing_value_df = pd.DataFrame(
                {"column_name": df.columns, "percent_missing": percent_missing}
            )
            return missing_value_df

        implementation = inspect.getsource(missing_values_percentage)
        super().build_implementation(implementation)

    def build_executable(self):
        def executable():
            missing_values_percentage_df = missing_values_percentage(df)
            missing_values_percentage_df

        super().build_executable(executable)
