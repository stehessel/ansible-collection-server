def test_prometheus_container_is_running(host):
    assert host.docker("prometheus").is_running
