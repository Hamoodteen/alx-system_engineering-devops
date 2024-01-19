# create_a_file.pp

exec { 'pkill':
  command     => 'pkill -9 -f "killmenow"',
  path        => ['/bin', '/usr/bin'],
  provider => 'shell',
}
