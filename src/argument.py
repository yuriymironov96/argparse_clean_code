class Argument:
    raw_value: str

    def __init__(self, raw_value: str):
        self.raw_value = raw_value

    def get(self):
        return self.value

    def set(self, value):
        raise NotImplementedError

    @classmethod
    def resolve_class_by_datatype(self, datatype):
        if datatype == "#":
            return IntegerArgument
        elif datatype == "*":
            return StringArgument
        elif datatype == "":
            return BooleanArgument
        else:
            raise ValueError(f"Unknown datatype: {datatype}")


class BooleanArgument(Argument):
    value: bool

    def set(self, value: str):
        if value in ["false", "0"]:
            self.value = False
        else:
            self.value = bool(value)


class IntegerArgument(Argument):
    value: int

    def set(self, value: str):
        self.value = int(value)


class StringArgument(Argument):
    value: str

    def set(self, value: str):
        self.value = value
