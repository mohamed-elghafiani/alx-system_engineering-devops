# Install a package

package { 'flask':
  ensure          => installed,
  name            => 'flask==2.1.0',
  provider        => 'pip3',
  install_options => ['werkzeug==2.2.2']
}
