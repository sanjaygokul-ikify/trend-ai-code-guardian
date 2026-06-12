import typing

class MetricsCollector:
    def __init__(self) -> None:
        self.metrics: typing.Dict[str, int] = {}

    def increment_metric(self, metric_name: str) -> None:
        if metric_name in self.metrics:
            self.metrics[metric_name] += 1
        else:
            self.metrics[metric_name] = 1