# Fix the no of maximum open files per process

exec { 'fix--for-nginx':
  command   => "/bin/sed -i /etc/default/nginx -e 's/15/3000/'"
  onlyif    => 'test -e /etc/default/nginx',
  logoutput => true,
}

exec { 'restart nginx':
  command   => '/usr/sbin/service nginx restart',
  require   => Exec['fix--for-nginx']
  logoutput => true,
}
