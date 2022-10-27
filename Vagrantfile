## Toute commande doit-ere exécution dans le répertoire contenant le Vagrantfile
# vagrant up : lancer
# vagrant halt : arrêter
# vagrant destroy : détruit la vm
# vagrant global-config : affiche la config de l'utilisateur vagrant sur la vm
# vagrant ssh: connexion sur le compte vagrant de la vm
#--------------------------------------------------------
# le réptoire courant est partagé sur la vm dans /vagrant
#--------------------------------------------------------
# vagrant ssh [NAME|ID]
# access-token: myusine xYph6TpAt1yJ1hJiS3QN
Vagrant.configure(2) do |config|

  [
    ["gitlab.formation.lan", "6144", "4", "ubuntu/focal64"],
  ].each do |vmname,mem,cpu,os|
    config.vm.define "#{vmname}" do |machine|

      machine.vm.provider "virtualbox" do |v|
        v.memory = "#{mem}"
        v.cpus = "#{cpu}"
        v.name = "#{vmname}"
        v.customize ["modifyvm", :id, "--ioapic", "on"]
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      end
      machine.vm.box = "#{os}"
      machine.vm.hostname = "#{vmname}"
      machine.vm.network "public_network"
      machine.ssh.insert_key = false
    end
  end
end
