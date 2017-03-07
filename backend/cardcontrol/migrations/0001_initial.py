# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('middle_initial', models.CharField(max_length=1)),
                ('utln', models.CharField(max_length=10)),
                ('student_type', models.CharField(max_length=20)),
                ('jumbocash_id', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('school', models.CharField(max_length=30)),
                ('class_year', models.IntegerField()),
                ('barcode', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=120)),
                ('building_name', models.CharField(max_length=120)),
                ('door_name', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('utln', models.CharField(max_length=10, unique=True)),
                ('manager_level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_created_by', to='cardcontrol.ManagerAccount')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_modified_by', to='cardcontrol.ManagerAccount')),
                ('new_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardcontrol.Card')),
                ('new_doors', models.ManyToManyField(to='cardcontrol.Door')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('utln', models.CharField(max_length=10, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardcontrol.Card')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useraccount_created_by', to='cardcontrol.ManagerAccount')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useraccount_modified_by', to='cardcontrol.ManagerAccount')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardcontrol.UserAccount'),
        ),
        migrations.AddField(
            model_name='door',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='door_created_by', to='cardcontrol.ManagerAccount'),
        ),
        migrations.AddField(
            model_name='door',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='door_modified_by', to='cardcontrol.ManagerAccount'),
        ),
        migrations.AddField(
            model_name='card',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_created_by', to='cardcontrol.ManagerAccount'),
        ),
        migrations.AddField(
            model_name='card',
            name='doors',
            field=models.ManyToManyField(to='cardcontrol.Door'),
        ),
        migrations.AddField(
            model_name='card',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_modified_by', to='cardcontrol.ManagerAccount'),
        ),
        migrations.AlterUniqueTogether(
            name='door',
            unique_together=set([('address', 'building_name', 'door_name')]),
        ),
    ]
