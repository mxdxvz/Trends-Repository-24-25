# app/models.py
from django.db import models

class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = False  # Do not let Django alter this table
        db_table = 'app_member'  # Existing table name
