# All CentOS specific tests go here
import testinfra
import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ansible-role-jenkins-centos')

@pytest.mark.parametrize('name,version', [
    ('java-1.8.0-openjdk-devel',''),
    ('initscripts',''),
    ('git',''),
    ('jenkins','')
])
def test_package_is_installed(host, name, version):
    package = host.package(name)
    assert package.is_installed

def test_service_is_enabled_started(host):
    jenkins_service = host.service('jenkins')
    assert jenkins_service.is_running
    assert jenkins_service.is_enabled

def test_jenkins_user(host):
    jenkins_user = host.user('jenkins')
    assert jenkins_user.exists

def test_var_lib_jenkins_dir(host):
    path = host.file('/var/lib/jenkins')
    assert path.exists
    assert path.is_directory
    assert path.user == 'jenkins'
    assert path.group == 'jenkins'
    assert path.mode == 0o755