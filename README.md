# ansible-role-jenkins

Ansible role for installing Jenkins masters.

## Requirements

* Currently only run on CentOS
* Internet access

## Role Variables

None

## Dependencies

None

## Example Playbook

Example role deployment

```yaml


    - hosts: jenkins-masters
      become: true
      roles:
         - ansible-role-jenkins
```

**Note:** Initial admin password can be found at /var/lib/jenkins/secrets/initialAdminPassword

## License

BSD

## Author Information

This role was created by George Spanos
