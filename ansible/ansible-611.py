---
 - hosts: fries

   tasks:
    - name: "bastet  -install figlet"
      apt:
        name: bastet
        state: present
      become: True
