import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', [
    'python3'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed


def test_file(host):
    file = host.file('/usr/bin/az')
    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
