# modify user limit
exec {'holberton hard limit mod':
  provider => 'shell',
  command  => 'sed -i "s/hard nofile 5/hard nofile 4096/" /etc/security/limits.conf'
}

# soft limit
exec {'holberton soft limit mod':
  provider => 'shell',
  command  => 'sed -i "s/soft nofile 4/soft nofile 100/" /etc/security/limits.conf'
}
