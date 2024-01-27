from utils.dicts import get_val


def test_get_val(dict_fixture):
    assert get_val(dict_fixture, "vcs") == 'mercurial'
    assert get_val(dict_fixture, "vcs", "git") == 'mercurial'
    assert get_val({}, "vcs", "git") == 'git'
    assert get_val({}, "vcs", "bazaar") == 'bazaar'
    assert get_val(dict_fixture, "test", "git") == 'git'


