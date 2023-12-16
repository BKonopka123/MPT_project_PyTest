from tests.utils import test_code

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, test_code.Foo) and isinstance(right, test_code.Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            f"   vals: {left.val} != {right.val}",
        ]