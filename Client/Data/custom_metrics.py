class CustomMetric():
    def __init__(self, name, value):
       self.name = name
       self.value = value

    def put_value(value):
        self.value = value

class CustomMetrics():
    def __init__(self, custom_metrics:list):
        self.custom_metrics = custom_metrics

    def get_custom_metrics():
        # Implement custom metric logic
        return self.custom_metrics

if __name__ == "__main__":
    Metric1 = Metric("1", 1)
    Metric2 = Metric("2", 2)
    Metric3 = Metric("3", 3)
    cms = CustomMetrics([Metric1, Metric2, Metric3])
