ANSIBLE-ROLE-AZURECLI
=====================

Ansible role install Azure Cli.


## Howto use this role?
This role need to be include in a playbook. 

Call this **Galaxy** role  like this:

````bash
ansible-galaxy install -r requirements.yml 
````

Inside requirements.yml
````yaml
- src: redbeard28.azurecli.git
````

More info => [Ansible Docs](https://docs.ansible.com/ansible-container/roles/access.html)

## Requirements

 * Ansible 2.9+


Role Variables
--------------

```yaml
---
# Put role variables
```

Dependencies
------------

none

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - { role: redbeard28.azurecli, tags: mytags }


Molecule testing framework
--------------------------

You can use molecule to test this role.
```bash
namespace=redbeard28 image=debian tag="buster-basetools" molecule converge 
namespace=redbeard28 image=debian tag="buster-basetools" molecule verify 
```

Author Information
------------------

Jeremie CUADRADO[¹](mailto:info@redbeard-consulting.fr) from Redbeard-Consulting
