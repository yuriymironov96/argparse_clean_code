from typing import TYPE_CHECKING

from src.exceptions import SchemaNotParsedError

from src.argument import Argument


class Args:
    _arguments: dict[str, Argument]

    def __init__(self, schema: str, raw_args: list[str]):
        self.arguments = {}
        self.parse_schema(schema)
        self.parse_args(raw_args)

    def parse_schema(self, schema: str):
        for schema_item in schema.split(","):
            argument_name, datatype = (schema_item[0], schema_item[1:])
            argument = Argument.resolve_class_by_datatype(datatype)
            self.arguments[argument_name] = argument(argument_name)

    def parse_args(self, raw_args: list[str]):
        if not self.arguments:
            raise SchemaNotParsedError()
        for arg in raw_args:
            key, value = arg.split("=")
            self.arguments[key].set(value)

    def get_boolean(self, key: str) -> bool:
        key = self.arguments[key]
        try:
            return bool(key.get())
        except ValueError:
            return False

    def get_string(self, key: str) -> str:
        return str(self.arguments[key].get())

    def get_int(self, key: str) -> int:
        return int(self.arguments[key].get())
