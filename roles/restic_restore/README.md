stehessel.server.restic_restore
===============================

Restores from `restic` backups that are saved in B2 storage.

Role Variables
--------------

```yaml
restic__repos:
    - bucket: bucket-name
      account_id: b2-account-id
      account_key: b2-account-key
      password: repo-password
      path: local-path-to-restore
```

Backup repositories in B2 cloud.

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Restore from restic backup"
      include_role:
        name: "stehessel.server.restic-restore"
```

License
-------

BSD-3-Clause

Author Information
------------------

[hesselmann.dev](https://www.hesselmann.dev)
