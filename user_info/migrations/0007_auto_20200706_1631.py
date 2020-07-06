# Generated by Django 3.0.8 on 2020-07-06 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0006_auto_20200706_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useruser',
            name='main_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user_info.User'),
        ),
        migrations.AlterUniqueTogether(
            name='useruser',
            unique_together={('main_user_id', 'vice_user_id')},
        ),
    ]