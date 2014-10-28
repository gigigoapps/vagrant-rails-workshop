# -*- mode: ruby -*-
# vi: set ft=ruby :

## Vagrant :: Ubuntu 14.04 64 bits :: Rails Workswhop

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config| 

    config.vm.box = "puppetlabs/ubuntu-14.04-64-puppet"

    # VM config
    config.vm.define :railsworkshop do |railsworkshop|
        railsworkshop.vm.network :private_network, ip: "10.11.12.13"
        railsworkshop.vm.network :forwarded_port, host: 27017, guest: 27017

        railsworkshop.vm.hostname = "railsworkshop"

        railsworkshop.vm.provider 'virtualbox' do |v|
            v.customize ['modifyvm', :id, '--name', 'ubuntu1404-rails-workshop']
            v.customize ['modifyvm', :id, '--cpus', '1']
            v.customize ['modifyvm', :id, '--memory', 1024]
            v.customize ['modifyvm', :id, '--ioapic', 'off']
            v.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
            v.customize ['modifyvm', :id, '--nictype1', 'virtio']
            v.customize ['modifyvm', :id, '--nictype2', 'virtio']
        end

        # Update package list
        railsworkshop.vm.provision :shell, :inline => 'if [[ ! -f /apt-get-run ]]; then apt-get update && sudo touch /apt-get-run; fi'

        # Puppet provision
        railsworkshop.vm.provision :puppet do |puppet|
            puppet.manifests_path   = 'manifests'
            puppet.module_path      = 'modules'
            puppet.options          = ['--verbose']
        end
    end
end
