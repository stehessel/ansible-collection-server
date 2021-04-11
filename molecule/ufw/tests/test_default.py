def test_ufw_service_is_running(host):
    assert host.service("ufw").is_running


def test_ufw_service_is_enabled(host):
    assert host.service("ufw").is_enabled
