stehessel.server.caddy
======================

Ansible role to deploy a minimal Caddy webserver setup. Assumes that `docker-compose` is available.
Sets up `ufw` rules for http (80) and https (443) ports.

Role Variables
--------------

```yaml
caddy__path: /srv/caddy
```

Path to directory that contains the Caddyfile and Caddy specific data.

```yaml
caddy__domain: hesselmann.famliy
```

The domain name.

```yaml
caddy__email: accounts@stehessel.de
```

Email address that is used to obtain the SSL/TLS certificates via ACME.

```yaml
caddy__auth_user: user
caddy__auth_secret: user
```

Basic authentication credentials. `caddy__auth_secret` needs to be hashed via `caddy hash-password --plaintext <my-password>`.

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
