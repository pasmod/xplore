import inspect

from xplore.exploration.builder import PlotOnlyExploration


class PairwiseScatterPlots(PlotOnlyExploration):
    def __init__(self, target):
        super(PairwiseScatterPlots, self).__init__()
        self.target = target

    def build_name(self):
        super().build_name("pairwise_scatter_plots")

    def build_title(self):
        super().build_title("### Pairwise Scatter Plots")

    def build_plot_implementation(self):
        def pairwise_scatter_plots(df, target_values=None, features=None):
            import seaborn as sns

            sns.pairplot(df[df["{}"].isin(list(target_values))][list(features)])

        def interact():
            from ipywidgets import interactive, fixed, widgets, interact_manual
            from IPython.display import display
            from ipywidgets import AppLayout, Button, Layout

            target_values_options = list(df["{}"].unique())

            features_options = list(df.columns.values)
            features_options.remove("{}")
            w1 = widgets.SelectMultiple(
                options=target_values_options,
                value=target_values_options,
                rows=len(target_values_options),
                description="Target Values (column: {})",
                style={{"description_width": "initial"}},
                disabled=False,
            )
            w2 = widgets.SelectMultiple(
                options=features_options,
                value=features_options[0 : min(len(features_options), 2)],
                rows=len(features_options),
                description="Features",
                disabled=False,
            )

            ui = widgets.HBox([w1, w2])
            out = widgets.interactive_output(
                pairwise_scatter_plots,
                {{"df": fixed(df), "target_values": w1, "features": w2}},
            )

            display(ui, out)

        implementation = inspect.getsource(pairwise_scatter_plots).format(self.target)
        implementation += "\n"
        implementation += inspect.getsource(interact).format(
            self.target, self.target, self.target
        )
        super().build_plot_implementation(implementation)

    def build_plot_executable(self):
        def executable():
            interact()

        super().build_plot_executable(executable)
