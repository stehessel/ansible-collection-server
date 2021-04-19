stehessel.server.watchtower
===========================

Sets up `watchtower` to monitor and update running Docker containers.

Role Variables
--------------

```yaml
```

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Set up Watchtower"
      include_role:
        name: "stehessel.server.watchtower"
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
