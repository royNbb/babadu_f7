# Generated by Django 4.1 on 2023-05-06 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('babadu', '0002_rename_barangwishlist_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='userid',
        ),
        migrations.AddField(
            model_name='member',
            name='is_atlet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_pelatih',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_umpire',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Umpire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('negara', models.CharField(max_length=50)),
                ('member', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='babadu.member')),
            ],
        ),
        migrations.CreateModel(
            name='Pelatih',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_mulai', models.DateField(default=django.utils.timezone.now)),
                ('member', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='babadu.member')),
            ],
        ),
        migrations.CreateModel(
            name='Atlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngr_asal', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField(default=django.utils.timezone.now)),
                ('play_right', models.BooleanField(default=False)),
                ('height', models.IntegerField(default=0)),
                ('jenis_kelamin', models.BooleanField(default=False)),
                ('world_rank', models.IntegerField(blank=True, null=True)),
                ('member', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='babadu.member')),
            ],
        ),
    ]
