## Vagrant :: Ubuntu 14.04 64 bits :: Rails Workswhop

node 'railsworkshop' {
    group { 'puppet': ensure => present }

    Exec {
        path => [ '/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/', '/usr/local/bin/' ],
        logoutput => 'on_failure'
    }

    class { 'apt': }

    # Packages
    package { [
            'fabric',
            'git',
            'postgresql',
            'postgresql-server-dev-all',
            'rbenv',
            'ruby-build'
        ]:
        ensure  => 'installed'
    }

    # Fabric folder
    file { '/opt/fabric':
        ensure  => 'directory',
        owner   => 'root',
        group   => 'root',
        mode    => 755
    } ->
    file { '/opt/fabric/fabfile.py':
        source  => "puppet:///modules/common/fabfile.py",
        owner   => 'root',
        group   => 'root',
        mode    => 644,
        ensure  => 'present'
    }

}
