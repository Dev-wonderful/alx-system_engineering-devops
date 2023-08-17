# modify user limit
exec {'holberton user limit mod':
  provider => 'shell',
  command  => 'sed -i "s/hard nofile 5/hard nofile 4096/" /etc/security/limits.conf'
}
