# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Ubuntu 12.04 (Precise Pangolin) box.
  config.vm.box = "hashicorp/precise32"

  # Forwarded port mapping.
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Setup a provisioning shell script.
  config.vm.provision :shell, path: "vagrant_provisioning.sh"

end
