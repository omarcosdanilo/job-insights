from .jobs import read


def get_unique_job_types(path):
    job_types = []
    jobs_list = read(path)

    for job in jobs_list:
        if job['job_type'] not in job_types:
            job_types.append(job['job_type'])

    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_by_job_type = [
        job for job in jobs if job['job_type'] == job_type
    ]

    return filtered_by_job_type


def get_unique_industries(path):
    industries = []
    file_read = read(path)

    for job in file_read:
        if job['industry'] not in industries and job['industry'] != '':
            industries.append(job['industry'])

    return industries


def filter_by_industry(jobs, industry):
    filtered_by_industry = [
        job for job in jobs if job['industry'] == industry
    ]

    return filtered_by_industry


def get_max_salary(path):
    jobs = read(path)

    salary_list = [
        int(job['max_salary']) for job in jobs if (job['max_salary']).isdigit()
    ]

    return max(salary_list)


def get_min_salary(path):
    jobs = read(path)

    salary_list = [
        int(job['min_salary']) for job in jobs if (job['min_salary']).isdigit()
    ]

    return min(salary_list)


def matches_salary_range(job, salary):
    if (
        ('max_salary' not in job or 'min_salary' not in job) or
        not isinstance(job['min_salary'], int) or
        not isinstance(job['max_salary'], int) or
        not isinstance(salary, int) or
        int(job['min_salary']) > int(job['max_salary'])
    ):
        raise ValueError('Valor incorreto')

    return salary in range(int(job['min_salary']), int(job['max_salary']))


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
