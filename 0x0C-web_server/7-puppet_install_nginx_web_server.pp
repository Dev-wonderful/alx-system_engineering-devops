# configure nginx in ubuntu server

# installing package
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
}

# install package
exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get -y nginx',
}

# redirect permanently
exec {'redirect':
  provider => shell,
  command  => 'sudo sed -i "/server_name _;/a \\n\trewrite ^\/redirect_me \/ permanent;" /etc/nginx/sites-available/default',
}

# Create default index file
exec {'create index file':
  provider => shell,
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
}

# start nginx
exec {'start':
  provider => shell,
  command  => 'sudo service nginx start',
}
