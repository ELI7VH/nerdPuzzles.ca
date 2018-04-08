from django.db import models

class Client(models.Model):

    def __init__(self,name):
        self.name = name

class LifePhots(models.Model):

    def __init__(self, date):
        self.date = date
