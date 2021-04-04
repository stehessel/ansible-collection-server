def test_run_hello_world_container(host):
    with host.sudo():
        hello_world = host.run("docker run hello-world")

    assert "Hello from Docker!" in hello_world.stdout


def test_user_added_to_docker_group(host):
    assert host.group("docker").exists
    assert "docker" in host.user("sudouser").groups


def test_docker_config_has_been_created(host):
    config_file = host.file("/etc/docker/daemon.json")

    assert config_file.exists
    assert '"log-driver": "journald"' in config_file.content_string


def test_docker_cleanup_cron_job_has_been_created(host):
    crontab = host.run("crontab -l")

    assert "docker system prune -af" in crontab.stdout
