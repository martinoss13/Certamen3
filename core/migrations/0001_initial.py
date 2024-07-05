# Generated by Django 4.2.13 on 2024-07-05 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(choices=[('MAÑANA', 'AM'), ('TARDE', 'PM'), ('NOCHE', 'MM')], max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.planta')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_combustible', models.CharField(choices=[('GASOLINA93', 'G93'), ('GASOLINA95', 'G95'), ('GASOLINA97', 'G97'), ('DIESEL_C', 'DIE'), ('DIESEL_AR', 'DIP'), ('JET', 'JA1'), ('AVGAS', 'AVG')], max_length=10)),
                ('litros', models.FloatField()),
                ('hora_registro', models.DateTimeField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
