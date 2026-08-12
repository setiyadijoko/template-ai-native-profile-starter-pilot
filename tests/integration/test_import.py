from starter_pilot import health_status


def test_installed_package_imports() -> None:
    assert health_status()
