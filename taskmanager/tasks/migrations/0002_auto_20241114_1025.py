# Generated by Django 5.1.3 on 2024-11-14 10:25

from django.db import migrations
from django.contrib.auth.models import Group, Permission


def create_groups(apps, schema_editor):
    editor_group = Group.objects.create(name='Editor')
    change_task_permission = Permission.objects.get(codename='change_task')
    editor_group.permissions.add(change_task_permission)
    admin_group = Group.objects.create(name='Admin')
    all_permissions = Permission.objects.filter(content_type__app_label='tasks')
    admin_group.permissions.set(all_permissions)

class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [ migrations.RunPython(create_groups),
    ]