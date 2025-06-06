#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:

    def __init__(self, name="Jane", job="Sales"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self._name = None
        else:
            self._name = name.title()
    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs." )
        self._job = job #saves job if in job list.
        
    job = property(get_job, set_job)


        
guido = Person()