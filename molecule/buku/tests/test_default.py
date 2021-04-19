def test_buku_container_is_running(host):
    assert host.docker("bukuserver").is_running
