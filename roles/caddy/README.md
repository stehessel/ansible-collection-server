stehessel.server.caddy
======================

Ansible role to deploy a minimal Caddy reverse-proxy setup. Assumes that `docker-compose` is available.

Role Variables
--------------

```yaml
caddy__path: /srv/caddy
```

Path to directory that contains the Caddyfile and Caddy specific data.

```yaml
caddy__domains:
  - hesselmann.famliy
  - www.hesselmann.famliy
caddy__email: accounts@stehessel.de
caddy__port: 80
caddy__service: mealie
```

Parameters that specify the reverse proxy. `caddy__email` is used to obtain the SSL/TLS certificates via ACME.

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Set up Caddy"
      include_role:
        name: "stehessel.server.caddy"
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
