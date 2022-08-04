def test_is_importable():
    import urllib3_secure_extra
    assert isinstance(urllib3_secure_extra.__version__, str)
