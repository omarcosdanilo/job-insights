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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
