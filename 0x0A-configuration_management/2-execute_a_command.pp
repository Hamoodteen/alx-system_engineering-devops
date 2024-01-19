# create_a_file.pp

exec { 'pkill':
  command     => 'pkill -f "killmenow"',
  path        => ['/bin', '/usr/bin'],
  provider => 'shell',
}
