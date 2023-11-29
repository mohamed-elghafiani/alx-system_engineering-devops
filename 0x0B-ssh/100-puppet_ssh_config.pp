# Client configuration file (w/ Puppet)

file { '~/.ssh/config':
  path    => '~/.ssh/config',
  content => 'Host *\n    PasswordAuthentication no\n    IdentityFile ~/.ssh/school',
}
