# Generated by Django 2.0.5 on 2018-05-29 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filter1', '0003_subcat_p_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsubcat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=150)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filter1.Subcat')),
            ],
        ),
    ]