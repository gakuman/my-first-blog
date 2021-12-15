# Generated by Django 3.2.3 on 2021-11-29 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printapp.printmodel', verbose_name='対象の投稿'),
        ),
    ]
