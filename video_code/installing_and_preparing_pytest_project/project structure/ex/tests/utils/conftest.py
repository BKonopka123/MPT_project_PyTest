from tests.utils import test_example


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, test_example.Foo) and isinstance(right, test_example.Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            f"   vals: {left.val} != {right.val}",
        ]