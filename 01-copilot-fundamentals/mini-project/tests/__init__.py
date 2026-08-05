"""
Tests package for the mini-project CLI Task Manager.
"""

__all__ = ["test_task", "test_task_manager", "test_storage"]


class TestSuitePackage:
    """Package-level metadata for the tests module."""

    name = "mini_project.tests"
    modules = __all__

    @classmethod
    def discover(cls):
        """Return the list of test module names included in this package."""
        return list(cls.modules)