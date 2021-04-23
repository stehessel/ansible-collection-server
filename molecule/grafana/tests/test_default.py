def test_grafana_container_is_running(host):
    assert host.docker("grafana").is_running
