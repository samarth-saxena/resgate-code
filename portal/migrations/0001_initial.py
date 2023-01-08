# Generated by Django 4.1.5 on 2023-01-08 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_Student', models.BooleanField(default=False)),
                ('is_Professor', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portal.userprofile')),
                ('program', models.CharField(choices=[('B', 'BTech'), ('M', 'MTech'), ('P', 'PhD')], default='B', max_length=1)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('CSD', 'CSD'), ('CSB', 'CSB'), ('CSSS', 'CSSS'), ('CSAI', 'CSAI'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('CB', 'CB')], default='CSE', max_length=4)),
                ('batch', models.IntegerField(default=2022)),
                ('tags', models.JSONField(null=True)),
            ],
            bases=('portal.userprofile',),
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=5000)),
                ('available', models.BooleanField()),
                ('domain', models.ManyToManyField(related_name='projects', to='portal.domain')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='portal.student')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portal.userprofile')),
                ('website', models.URLField(max_length=300)),
                ('interests', models.JSONField(null=True)),
                ('lab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profs', to='portal.lab')),
                ('projects', models.ManyToManyField(related_name='profs', to='portal.projects')),
            ],
            bases=('portal.userprofile',),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openingDate', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('R', 'Rejected'), ('A', 'Accepted')], default='P', max_length=1)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='portal.projects')),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='portal.resume')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='portal.student')),
            ],
        ),
    ]
