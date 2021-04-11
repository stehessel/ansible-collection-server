def test_rsync_service_is_running(host):
    assert host.service("rsync").is_running


def test_rsync_service_is_enabled(host):
    assert host.service("rsync").is_enabled


def test_rsyncdconf_has_been_created(host):
    assert host.file("/etc/rsyncd.conf").exists


def test_listening_on_rsync_port(host):
    assert host.socket("tcp://873").is_listening
