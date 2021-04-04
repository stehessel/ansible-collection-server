stehessel.server.docker
=======================

Ansible role to deploy a minimal docker setup. Installs `docker` and `docker-compose` from distribution repositories.
Includes a cron job to periodically prune unused docker data.

Role Variables
--------------

```yaml
docker__package: docker.io
docker__state: present
docker__service_enabled: yes
```

`docker__package` should be the name of the Docker package provided by the distribution repositories.
`docker_state` can be chosen as `latest` if the package manager supports it. The docker service  can be
enabled by setting `docker__service_enabled`.

```yaml
docker__users: []
```

List of users that should be added to the `docker` group.

```yaml
docker__config:
  log-driver: "{{ docker__log_driver | default('journald') }}"
```

Explicit daemon configuration can be set via `docker__config`. The log driver can be configured via
`docker__log_driver` (defaults to `journald`).

```yaml
docker__cron_jobs:
  - name: "Docker disk clean up"
    job: "docker system prune -af"
    schedule: ["0", "0", "*", "*", "0"]
    user: "{{ (docker__users | first) | default('root') }}"
```

Cron jobs can be added via `docker__cron_jobs`. By default disk clean up is set up to run once a week.

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Include docker"
      include_role:
        name: "stehessel.server.docker"
      vars:
        docker__users:
          - sudouser
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
