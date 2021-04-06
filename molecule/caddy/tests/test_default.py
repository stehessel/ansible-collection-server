def test_caddyfile_has_been_created(host):
    caddyfile = host.file("/srv/caddy/Caddyfile")

    assert caddyfile.exists


def test_caddyfile_has_valid_email(host):
    caddyfile = host.file("/srv/caddy/Caddyfile")

    assert "email accounts@stehessel.de" in caddyfile.content_string


def test_listening_on_http_ports(host):
    assert host.socket("tcp://80").is_listening
    assert host.socket("tcp://443").is_listening
