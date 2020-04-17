import json
import pathlib

import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor

from xplore.exploration.builder import (
    SimpleExploration,
    PlotOnlyExploration,
    PlotableExploration,
)


def markdown_cell(content):
    return nbf.v4.new_markdown_cell(content)


def code_cell(content):
    return nbf.v4.new_code_cell(content)


class Notebook:
    def __init__(self, explorations):
        self.explorations = explorations
        self._name = None
        self._tongue = None
        self._mode = None
        self._target = None

    def name(self, name):
        self._name = name
        return self

    def tongue(self, tongue="en"):
        path = pathlib.Path(__file__).parent / "resources"
        if "en" == tongue:
            with open(path / "en.json", mode="r") as file:
                self._tongue = json.load(file)
        else:
            raise ValueError("Language {} is not supported!".format(tongue))
        return self

    def build(self):
        nb = nbf.v4.new_notebook()
        headline = self._tongue["headline"]
        introduction = self._tongue["introduction"]
        nb["cells"] = [markdown_cell(headline), markdown_cell(introduction)]

        for exploration in self.explorations:
            title = exploration.title
            if title:
                nb["cells"].append(markdown_cell(title))
            if isinstance(exploration, SimpleExploration) or isinstance(
                exploration, PlotableExploration
            ):
                implementation = exploration.implementation
                if implementation:
                    nb["cells"].append(code_cell(implementation))
                executable = exploration.executable
                if executable:
                    nb["cells"].append(code_cell(executable))
            if isinstance(exploration, PlotableExploration):
                plot_implementation = exploration.plot_implementation
                nb["cells"].append(code_cell(plot_implementation))
                plot_executable = exploration.plot_executable
                nb["cells"].append(code_cell(plot_executable))
            if isinstance(exploration, PlotOnlyExploration):
                plot_implementation = exploration.plot_implementation
                nb["cells"].append(code_cell(plot_implementation))
                plot_executable = exploration.plot_executable
                nb["cells"].append(code_cell(plot_executable))

        nbf.write(nb, "{}.ipynb".format(self._name))
        return self

    def execute(self):
        with open("{}.ipynb".format(self._name)) as f:
            nb = nbf.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": "."}})
        with open("{}.ipynb".format(self._name), "wt") as f:
            nbf.write(nb, f)
