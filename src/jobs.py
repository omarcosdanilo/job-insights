from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path, mode='r') as file:
        jobs_read = csv.DictReader(file, delimiter=',', quotechar='"')

        jobs_list = [job for job in jobs_read]

    return jobs_list
