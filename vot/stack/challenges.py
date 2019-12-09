

from vot.stack import Stack
from vot.experiment import SupervisedExperiment

class VOT2013(Stack):

    deprecated = True
    dataset = "vot2013"

    def __init__(self):
        super().__init__(SupervisedExperiment("baseline"))

class VOT2014(Stack):

    deprecated = True
    dataset = "vot2014"

    def __init__(self):
        super().__init__(SupervisedExperiment("baseline"))