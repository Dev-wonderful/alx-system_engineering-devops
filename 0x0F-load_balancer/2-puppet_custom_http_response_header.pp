# configure a web server to add a custom header

exec{'custom-header':
  provider => shell,
  command  => "sudo sed -i '/server_name _;/a \\\tadd_header X-Served-By ${hostname};' /etc/nginx/sites-available/default",
}

# restart nginx
exec {'start':
  provider => shell,
  command  => 'sudo service nginx start',
}
