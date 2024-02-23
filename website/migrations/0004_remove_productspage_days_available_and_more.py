# Generated by Django 4.0.7 on 2022-09-28 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('website', '0003_productsindexpage_productspage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productspage',
            name='days_available',
        ),
        migrations.AddField(
            model_name='productspage',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productspage',
            name='sku',
            field=models.CharField(default='sku placeholder', max_length=225),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SnipcartSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(help_text='Your Snipcart public API key', max_length=255)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
