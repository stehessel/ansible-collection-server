def test_sshd_service_is_running(host):
    assert host.service("sshd").is_running


def test_sshd_service_is_enabled(host):
    assert host.service("sshd").is_enabled
