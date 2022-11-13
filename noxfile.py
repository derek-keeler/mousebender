import nox

python_versions = ["3.7", "3.8", "3.9", "3.10", "3.11"]


@nox.session(python=python_versions)
def test(session, coverage=False):
    """Run the test suite."""
    session.run("pytest", *(["--cov"] if coverage else []))


@nox.session(python=python_versions)
def coverage(session):
    """Run the test suite under coverage."""
    test(session, coverage=True)


@nox.session
def check_types(session):
    """Type check."""
    session.install("-e", ".")
    session.install("mypy")
    session.run("mypy", "mousebender")


@nox.session
def format(session, check=False):
    """Format the code."""
    for tool in ("black", "isort"):
        session.install(tool)
        args = ["--check"] if check else []
        args.append(".")
        session.run(tool, *args)


@nox.session
def check_format(session):
    """Check that the code is properly formatted."""
    format(session, check=True)
