# Client configuration file (w/ Puppet)

class ssh_config {
  package { 'augeas-tools':
    ensure => installed,
  }

  augeas { 'turn_off_passwd_auth':
    context => '/files/etc/ssh/ssh_config',
    changes => [
      'set Host/*[. = "*"]/PasswordAuthentication no',
    ],
    notify  => Service['ssh'],
  }

  augeas { 'declare_identity_file':
    context => '/files/etc/ssh/ssh_config',
    changes => [
      'set Host/*[. = "*"]/IdentityFile ~/.ssh/school',
    ],
    notify  => Service['ssh'],
  }

  file_line { 'Turn off passwd auth':
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    match   => '^#?\s*PasswordAuthentication',
    notify  => Service['ssh'],
  }

  file_line { 'Declare identity file':
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/school',
    match   => '^#?\s*IdentityFile',
    notify  => Service['ssh'],
  }

  service { 'ssh':
    ensure  => 'running',
    enable  => true,
    require => [Augeas['turn_off_passwd_auth'], Augeas['declare_identity_file']],
  }
}

