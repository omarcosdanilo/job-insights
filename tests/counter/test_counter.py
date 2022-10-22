from src.counter import count_ocurrences


def test_counter():
    path = (
        '/home/marcos/Documentos/Projetos/' +
        '4-Ciencia-da-Computacao/' +
        '1-Job-Insights/sd-019-b-project-job-insights/src/jobs.csv'
        )
    assert count_ocurrences(path, 'TRAINEE') == 5
