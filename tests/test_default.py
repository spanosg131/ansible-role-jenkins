import testinfra
import pytest

@pytest.mark.parametrize("name,version", [
    ("java-1.8.0-openjdk-devel",""),
    ("initscripts",""),
    ("git",""),
    ("jenkins","")
])
def test_package_is_installed(host, name, version):
    package = host.package(name)
    assert package.is_installed

def test_service_is_enabled_started(host):
    jenkins_service = host.service("jenkins")
    assert jenkins_service.is_running
    assert jenkins_service.is_enabled
    


