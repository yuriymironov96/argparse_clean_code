class SchemaError(Exception):
    message = "Schema error."


class SchemaNotParsedError(Exception):
    message = "Cannot access schema bacause it is not parsed yet."
