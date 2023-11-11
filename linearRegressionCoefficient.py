from paprika import to_string


@to_string
class LinearRegressionCoefficient:

    def __init__(self, a: float, b: float):
        self.a: float = a
        self.b: float = b

    def __eq__(self, other):
        if isinstance(other, LinearRegressionCoefficient):
            return self.a == other.a and self.b == other.b
        return False
