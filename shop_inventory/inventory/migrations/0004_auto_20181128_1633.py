# Generated by Django 2.1.3 on 2018-11-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20181128_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('security', models.CharField(max_length=100)),
                ('resolution', models.CharField(max_length=20)),
                ('connectivity', models.CharField(max_length=50)),
                ('status', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='laptop',
            name='battery',
            field=models.CharField(default=(('Battery Present', 'Present'), ('Battery Absent', 'Absent')), max_length=15),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='hdd_cover',
            field=models.CharField(choices=[('Cover Present', 'Present'), ('Cover Absent', 'Absent')], max_length=15),
        ),
    ]
