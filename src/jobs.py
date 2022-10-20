from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path, mode='r') as file:
        jobs_list = []
        jobs_read = csv.DictReader(file, delimiter=',', quotechar='"')

        for job in jobs_read:
            jobs_list.append(job)
    return jobs_list
