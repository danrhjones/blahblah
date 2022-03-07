def test_rngtest_is_installed(host):
    nginx = host.package("rng-tools")
    assert nginx.is_installed
    assert nginx.version.startswith("6.13")
