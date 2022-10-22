from src.counter import count_ocurrences


def test_counter():
    path = ('src/jobs.csv')
    assert count_ocurrences(path, 'Python') == 1639
    assert count_ocurrences(path, 'PYTHON') == 1639
    assert count_ocurrences(path, 'python') == 1639
    assert count_ocurrences(path, 'Javascript') == 122
    assert count_ocurrences(path, 'JAVASCRIPT') == 122
    assert count_ocurrences(path, 'javascript') == 122
