def test_watchtower_container_is_running(host):
    assert host.docker("watchtower").is_running
