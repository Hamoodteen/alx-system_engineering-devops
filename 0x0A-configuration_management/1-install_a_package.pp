# create_a_file.pp

package { 'flask':
  ensure   => '3.0.1',
  provider => 'pip3',
}
