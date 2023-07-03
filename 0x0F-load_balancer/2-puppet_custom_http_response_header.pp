# configure a web server to add a custom header

# updating package repository
exec {'update':
  provider => shell,
  command  => 'apt -y update',
}

# install package
exec {'install nginx':
  provider => shell,
  path     => '/usr/bin:/bin',
  command  => 'apt-get -y install nginx',
}

# Create default index file
exec {'create index file':
  provider => shell,
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
}

# response header
exec{'custom-header':
  provider => shell,
  command  => "sudo sed -i '/server_name _;/a \\\tadd_header X-Served-By ${hostname};' /etc/nginx/sites-available/default",
}

# restart nginx after config  update
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
