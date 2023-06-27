# configure nginx in ubuntu server

# run update before installing package
exec {'update':
  path    => '/usr/bin:/bin',
  command => 'sudo apt-get -y update'
}

# install package
package {'nginx':
  ensure          => 'installed',
  provider        => 'apt',
  install_options => '-y'
}

# redirect permanently
exec {'redirect':
  command => 'sed -i "/server_name _;/a \\n\trewrite ^\/redirect_me \/ permanent;" /etc/nginx/sites-available/default',
  path    => ['/usr/bin', '/bin']
}

# Create default index file
file {'index file':
  ensure  => file,
  path    => '/var/www/html/index.html',
  mode    => '0644',
  content => 'Hello World!'
}

# start nginx
exec {'start':
  command => 'service nginx start',
  path    => '/usr/bin:/bin'
}
