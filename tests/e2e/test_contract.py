from starter_pilot import health_status


def test_health_contract_end_to_end() -> None:
    assert {"status": health_status()} == {"status": "ok"}
