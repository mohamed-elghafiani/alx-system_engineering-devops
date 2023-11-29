file { '/tmp/school':
  path => '/tmp/school',
  mode => '0744',
  owner => 'www-data',
  groupe => 'www-data',
  content => 'I love Puppet'
}
