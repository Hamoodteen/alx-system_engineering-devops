file { 'school':
  path       => '/tmp/school',
  permission => '0744',
  owner      => 'www-data',
  group      => 'www-data',
  contain    => 'I love Puppet',
}
