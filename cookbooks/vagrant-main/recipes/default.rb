# enter custom commands here

execute "update language-pack-en-base" do
  command "sudo apt-get install -q -y language-pack-en-base"
  command "sudo apt-get install python-dev" 
  command "sudo apt-get install libjpeg62-dev" 
  command "sudo locale-gen"
  command "sudo update-locale --locale-file=/etc/default/locale LANG=en_US.utf8"
end
