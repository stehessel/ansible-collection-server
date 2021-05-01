def test_papermerge_container_is_running(host):
    assert host.docker("papermerge_app").is_running
    assert host.docker("papermerge_worker").is_running
