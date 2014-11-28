# Vagrant :: Ubuntu 14.04 64 bits :: Rails Workshop

This project uses Vagrant to mount and deploy a workshop environment with Ubuntu 14.04 

## Initial Requirements

### You will need:

  * Git 1.7+
  * Vagrant v1.6.5 + (http://vagrantup.com)
  * Virtualbox v4.3.18 + (https://www.virtualbox.org/)

## Do the work

### Clone this repositoriy with submodules (they are puppet submodules)

    $ git clone --recursive https://github.com/pedroamador/ubuntu1404-rails-workshop.git
    [...]
    $ cd ubuntu1404-rail-sworkshop
    [...]

### Start the VM

    ubuntu1404-rails-workshop$ vagrant up
    Bringing machine 'rails-workshop' up with 'virtualbox' provider...
    ==> rails-workshop: Importing base box 'puppetlabs/ubuntu-14.04-64-puppet'...
    ==> rails-workshop: Matching MAC address for NAT networking...
    ==> rails-workshop: Checking if box 'puppetlabs/ubuntu-14.04-64-puppet' is up to date...
    [...]

### Initial configuration

You should enter the following command to complete the VM configuration

        
    ubuntu1404-rails-workshop$ vagrant ssh -c "sudo fab -f /opt/fabric/fabfile.py initialdeploy"
    Vas a realizar el despliegue inicial. Esta tarea sólo se puede ejecutar una vez
    ¿Estás seguro? [Y/n] y
    Desplegando...
    [localhost] local: chattr +i deployed
    chattr: Operación no permitida mientras se ponían las banderas en deployed

    
    Despliegue inicial realizado
    ESTA TAREA NO SE VA A EJECUTAR DE NUEVO

    Done.

### Access to the VM

You can go to VM "inside" with shell prompt in console mode

    ubuntu1404-rails-workshop$ vagrant ssh
    Welcome to Ubuntu 14.04 LTS (GNU/Linux 3.13.0-24-generic x86_64)

     * Documentation:  https://help.ubuntu.com/
    vagrant@railsworkshop:~$ 
    

With "vagrant ssh" you are logged in the VM with "vagrant" user. 
But you can enter `sudo -i` command to became "root" user
Or you can also exec `sudo [command]` commands.

---

## Notes

The MV starts with the local IP 10.11.12.13. If you publish a service into the machine, you should access with

http://10.11.12.13:3000

---

## Known issues

---

## ToDo

