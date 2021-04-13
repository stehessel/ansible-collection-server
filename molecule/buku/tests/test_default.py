def test_caddy_container_is_running(host):
    assert host.docker("bukuserver").is_running
