# create_a_file.pp

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['update_pip3'], # Optional: Ensure pip3 is up-to-date before installing Flask
}

exec { 'update_pip3':
  command     => 'pip3 install --upgrade pip',
  refreshonly => true,
  path        => ['/usr/local/bin', '/usr/bin'],
}
