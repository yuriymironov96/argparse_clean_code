import unittest

from src.argument import (
    Argument,
    BooleanArgument,
    IntegerArgument,
    StringArgument,
    FloatArgument
)


class TestStringMethods(unittest.TestCase):

    def test_resolve_class_by_datatype(self):
        self.assertEquals(
            Argument.resolve_class_by_datatype("#"), IntegerArgument)
        self.assertEquals(
            Argument.resolve_class_by_datatype("*"), StringArgument)
        self.assertEquals(
            Argument.resolve_class_by_datatype(""), BooleanArgument)
        self.assertRaises(
            ValueError, Argument.resolve_class_by_datatype, "unknown")
        try:
            Argument.resolve_class_by_datatype("unknown")
            assert False, "Should raise ValueError"
        except ValueError:
            pass
        except Exception:
            assert False, "Should raise ValueError"

    def test_boolean_argument(self):
        arg = BooleanArgument("l")
        arg.set("true")
        self.assertTrue(arg.get())
        arg.set("false")
        self.assertFalse(arg.get())
        arg.set("1")
        self.assertTrue(arg.get())
        arg.set("0")
        self.assertFalse(arg.get())
        arg.set("abc")
        self.assertTrue(arg.get())

    def test_integer_argument(self):
        arg = IntegerArgument("p")
        arg.set("123")
        self.assertEquals(arg.get(), 123)
        self.assertRaises(ValueError, arg.set, "abc")
        try:
            arg.set("abc")
            arg.get()
            assert False, "Should raise ValueError"
        except ValueError:
            pass
        except Exception:
            assert False, "Should raise ValueError"

    def test_string_argument(self):
        arg = StringArgument("d")
        arg.set("/usr/logs")
        self.assertEquals(arg.get(), "/usr/logs")
        arg.set("123")
        self.assertEquals(arg.get(), "123")
        arg.set("abc")
        self.assertEquals(arg.get(), "abc")

    def test_float_argumnet(self):
        arg = FloatArgument("f")
        arg.set("3.14")
        self.assertEquals(arg.get(), 3.14)
        self.assertRaises(ValueError, arg.set, "abc")
        try:
            arg.set("abc")
            arg.get()
            assert False, "Should raise ValueError"
        except ValueError:
            pass
        except Exception:
            assert False, "Should raise ValueError"
