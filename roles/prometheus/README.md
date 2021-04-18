stehessel.server.prometheus
===========================

Sets up `prometheus` monitoring.

Role Variables
--------------

```yaml
prometheus__path: /srv/prometheus
```

Host path to Prometheus base directory.

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Set up prometheus"
      include_role:
        name: "stehessel.server.prometheus"
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
