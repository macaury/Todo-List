# Generated by Django 5.2.4 on 2025-07-18 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0004_tarefas_data_finalizacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefas',
            name='data_finalizacao',
        ),
        migrations.AddField(
            model_name='tarefas',
            name='status',
            field=models.CharField(choices=[('sprint semanal', 'sprint_semanal'), ('sprint mensal', 'sprint_mensal'), ('sprint anual', 'sprint_anual')], default='sprint semanal', max_length=14),
        ),
    ]
