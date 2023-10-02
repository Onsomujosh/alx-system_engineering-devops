# Puppet manifest to install and configure Nginx with a 301 redirect

# Install Nginx package
package { 'nginx':
  ensure => 'present',
}

# Create the default Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => template('nginx/default.erb'),
}

# Define a custom Nginx configuration template
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
}

# Create the document root directory
file { '/var/www/html':
  ensure => 'directory',
}

# Create an index.html file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}
