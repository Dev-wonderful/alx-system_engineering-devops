# change ULIMIT (user limit) for Nginx
# to increase the number of File Descriptor (FD)
# available to Nginx to open files to serve request

# change ULimit from 15 to 4096
exec {'Fix-Nginx-ULimit':
  provider => 'shell',
  command  => 'sed -i "s/-n 15/-n 4096/g" /etc/default/nginx'
}

# restart Nginx to work with the new configuration
exec {'Restart Nginx':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}
