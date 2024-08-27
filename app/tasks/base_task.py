import abc

class BaseTask(abc.ABC):
    def __init__(self, params):
        self.params = params

    @abc.abstractmethod
    def execute(self, data):
        pass
