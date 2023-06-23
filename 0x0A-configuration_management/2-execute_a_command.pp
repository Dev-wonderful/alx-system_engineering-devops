# kill a process
exec {'pkill -15 killmenow':
  path => '/usr/bin:/bin'
}
