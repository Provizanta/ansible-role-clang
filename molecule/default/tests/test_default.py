import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_clang_versions(host):
    for clang_version in ['7', '8', '10', '11', '12']:
        clang_cc = host.file(f'/usr/bin/clang-{clang_version}')
        clang_cpp = host.file(f'/usr/bin/clang++-{clang_version}')
        clang_lld = host.file(f'/usr/bin/lld-{clang_version}')

        assert clang_cc.is_file
        assert clang_cpp.is_file
        assert clang_lld.is_file
