# Generated by Django 3.1.3 on 2020-11-30 09:28

from django.db import migrations, models
import django.db.models.deletion
import user_system.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('field', models.CharField(max_length=50)),
                ('search_frequency', models.CharField(choices=[('', ''), ('frequently', '每天使用多次'), ('usually', '平均每天使用一次'), ('sometimes', '每周偶尔使用两三次'), ('rarely', '平均每周使用不超过一次')], max_length=50)),
                ('search_history', models.CharField(choices=[('', ''), ('very long', '5年以上'), ('long', '3年~5年'), ('short', '1年~3年'), ('very short', '1年以内')], max_length=50)),
                ('signup_time', models.DateTimeField()),
                ('last_login', models.DateTimeField()),
                ('login_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ResetPasswordRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=user_system.models.KeyGenerator(12), max_length=50)),
                ('expire', models.IntegerField(default=user_system.models.TimestampGenerator(108000))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_system.user')),
            ],
        ),
    ]
