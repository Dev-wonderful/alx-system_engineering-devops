# fix the internal server error
exec {'Fix wordpress':
  path    => '/usr/bin:/bin',
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php'
}
