# Generated by Django 4.0.3 on 2022-06-14 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('Angular', 'Angular'), ('Flask', 'Flask'), ('Ruby', 'Ruby')], default=1, max_length=15),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
