# Database models for Course, Teacher, Resource, Activity

class Course:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Resource:
    def __init__(self, title, url):
        self.title = title
        self.url = url

class Activity:
    def __init__(self, title, date):
        self.title = title
        self.date = date
