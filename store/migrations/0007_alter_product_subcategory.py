# Generated by Django 4.1.1 on 2023-08-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_subcategory_alter_product_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(choices=[('tops', 'tops'), ('shorts', 'shorts'), ('pants', 'pants'), ('underwear', 'underwear'), ('accessories', 'accessories'), ('suit', 'suit'), ('caps', 'caps'), ('socks', 'socks'), ('shoes', 'shoes'), ('helmet', 'helmet')], default='', max_length=20),
        ),
    ]
