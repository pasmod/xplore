import inspect

from xplore.exploration.builder import SimpleExploration


class PairwiseCorrelationBetweenColumns(SimpleExploration):
    def build_name(self):
        super().build_name("pairwise_correlation_between_columns")

    def build_title(self):
        super().build_title("### Pairwise Correlation between columns")

    def build_implementation(self):
        def pairwise_correlation_between_columns(df):
            import seaborn as sns

            sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True)

        implementation = inspect.getsource(pairwise_correlation_between_columns)
        super().build_implementation(implementation)

    def build_executable(self):
        def executable():
            pairwise_correlation_between_columns(df)

        super().build_executable(executable)
