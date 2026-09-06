"""Tests for hello_world module."""


def test_hello_world_prints_expected_message(capsys):
    """Importing hello_world should print 'Hello, World!'."""
    import hello_world

    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
