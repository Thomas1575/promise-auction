# Generated by Django 3.2.4 on 2021-06-15 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0006_item_promiser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidding.item')),
            ],
        ),
    ]
