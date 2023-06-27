# configure nginx in ubuntu server

# run update before installing package
exec {'update':
  path    => '/usr/bin:/bin',
  command => 'sudo apt-get -y update'
}

# install package
exec {'install nginx':
  command => 'sudo apt-get -y nginx',
  path    => '/usr/bin:/bin'
}

# redirect permanently
exec {'redirect':
  command => 'sed -i "/server_name _;/a \\n\trewrite ^\/redirect_me \/ permanent;" /etc/nginx/sites-available/default',
  path    => ['/usr/bin', '/bin']
}

# Create default index file
exec {'create index file':
  command => 'echo "Hello World!" > /var/www/html/index.html',
  path    => '/usr/bin:/bin'
}

# start nginx
exec {'start':
  command => 'service nginx start',
  path    => '/usr/bin:/bin'
}
