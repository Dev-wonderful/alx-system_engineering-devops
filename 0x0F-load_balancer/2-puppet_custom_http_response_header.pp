# configure a web server to add a custom header

# updating package repository
exec {'a:update':
  provider => shell,
  command  => 'sudo apt -y update',
  before   => Exec['b:install nginx']
}

# install package
exec {'b:install nginx':
  provider => shell,
  command  => 'sudo apt -y install nginx',
  require  => Exec['a:update']
}

# Create default index file
exec {'c:create index file':
  provider => shell,
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  require  => Exec['b:install nginx']
}

# response header
exec{'d:custom-header':
  provider => shell,
  command  => "sudo sed -i '/server_name _;/a \\\tadd_header X-Served-By ${hostname};' /etc/nginx/sites-available/default",
  require  => Exec['c:create index file']
}

# restart nginx after config  update
exec {'e:restart':
  provider => shell,
  command  => 'sudo service nginx restart',
  require  => Exec['d:custom-header']
}
