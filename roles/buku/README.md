stehessel.server.buku
=====================

Sets up a 'buku' bookmark server.

Role Variables
--------------

```yaml
buku__path: /srv/buku
```

Buku host path.

```yaml
buku__port: 5001
```

Buku server port.

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Set up buku"
      include_role:
        name: "stehessel.server.buku"
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
