# Generated by Django 4.0.2 on 2022-06-06 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('education', 'Education'), ('biography', 'Biography'), ('history', 'History'), ('novel', 'Novel'), ('scifi', 'Sci-Fi'), ('self-help', 'Self-Help')], default='education', max_length=30),
        ),
    ]