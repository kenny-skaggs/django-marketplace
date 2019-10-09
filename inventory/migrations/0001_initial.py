# Generated by Django 2.2.6 on 2019-10-09 03:36

from django.db import migrations, models
import django.db.models.deletion


def load_initial_categories(apps, schema_editor):
    Category = apps.get_model("inventory", "Category")
    Category(name="Auto").save()
    Category(name="Furniture").save()
    Category(name="Electronics").save()
    Category(name="Instruments").save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventory.Category')),
            ],
        ),
        migrations.RunPython(load_initial_categories)
    ]
