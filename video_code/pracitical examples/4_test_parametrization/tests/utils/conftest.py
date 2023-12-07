def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )
    parser.addoption("--till", type=int, default=None, help="run all combinations till number")


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))
    if "param1" in metafunc.fixturenames:
        till = metafunc.config.getoption("till")
        if till is not None:
            metafunc.parametrize("param1", range(till))
