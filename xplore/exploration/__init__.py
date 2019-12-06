from xplore.exploration.builder import Director
from xplore.exploration.steps.base import ColumnTypes, Head, Read, Shape
from xplore.exploration.steps.classification import DistributionOfTargetVariable
from xplore.exploration.steps.correlation import PairwiseCorrelationBetweenColumns
from xplore.exploration.steps.missing_values import PercentageOfMissingValuesInColumns
from xplore.exploration.steps.scatter import PairwiseScatterPlots
from xplore.notebook.validation import (
    _check_if_target_is_set_when_mode_is_classification,
)

director = Director()


def explore(path, mode=None, target=None):
    _check_if_target_is_set_when_mode_is_classification(mode=mode, target=target)

    explorations = list()

    # Basic
    explorations.append(director.construct(Read(path)))
    explorations.append(director.construct(Head()))
    explorations.append(director.construct(Shape()))
    explorations.append(director.construct(ColumnTypes()))

    # Missing Values
    explorations.append(director.construct(PercentageOfMissingValuesInColumns()))

    # Correlation
    explorations.append(director.construct(PairwiseCorrelationBetweenColumns()))

    # Scatter
    explorations.append(director.construct(PairwiseScatterPlots(target=target)))

    # Classification EDA
    explorations.append(director.construct(DistributionOfTargetVariable(target=target)))

    return explorations
