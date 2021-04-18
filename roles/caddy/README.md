stehessel.server.caddy
======================

Ansible role to deploy a minimal `Caddy` webserver setup. Assumes that `docker-compose` is available.
Sets up `ufw` rules for http (80) and https (443) ports.

Role Variables
--------------

```yaml
caddy__path: /srv/caddy
```

Path to directory that contains the Caddyfile and Caddy specific data.
Access logs are written to `{{ caddy__path }}/log`.

```yaml
caddy__email: mail@example.com
```

Email address that is used to obtain the SSL/TLS certificates via ACME.

```yaml
caddy__services:
    - domain: example-file-server.com
      type: file_server
      auth_user: user
      auth_secret: <hashed-password>

    - domain: example-reverse-proxy.com
      type: reverse_proxy
      proxy_name: example
      proxy_port: 9000
      auth_user: user
      auth_secret: <hashed-password>
```

List of services that should be served either via reverse-proxy or web server.
Basic authentication credentials are optional. `auth_secret` needs to be hashed via
`caddy hash-password --plaintext <my-password>`.

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
