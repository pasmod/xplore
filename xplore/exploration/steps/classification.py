import inspect

from xplore.exploration.builder import PlotableExploration


class DistributionOfTargetVariable(PlotableExploration):
    def __init__(self, target):
        super(DistributionOfTargetVariable, self).__init__()
        self.target = target

    def build_name(self):
        super().build_name("distribution_of_target_variable")

    def build_title(self):
        super().build_title("### Distribution of Target Variable")

    def build_implementation(self):
        def distribution_of_target_variable(df):
            return df["{}"].value_counts()

        implementation = inspect.getsource(distribution_of_target_variable).format(
            self.target
        )
        super().build_implementation(implementation)

    def build_executable(self):
        def executable():
            dist_target_variable = distribution_of_target_variable(df)
            dist_target_variable

        super().build_executable(executable)

    def build_plot_implementation(self):
        def plot_distribution_of_target_variable(dist_target_variable):
            import matplotlib.pyplot as plt

            df["{}"].value_counts().plot(kind="bar")
            plt.xticks(rotation="horizontal")
            plt.xlabel("Target Variable: {}")
            plt.ylabel("Count")
            plt.title("Distribution of Target Variable: {}")
            plt.show()

        implementation = inspect.getsource(plot_distribution_of_target_variable).format(
            self.target, self.target, self.target
        )
        super().build_plot_implementation(implementation)

    def build_plot_executable(self):
        def executable():
            plot_distribution_of_target_variable(dist_target_variable)

        super().build_plot_executable(executable)
