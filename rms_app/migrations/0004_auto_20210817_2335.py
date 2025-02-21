# Generated by Django 3.2.2 on 2021-08-17 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rms_app', '0003_food_food_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_number', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='food_img',
            field=models.ImageField(default='default_food.jpg', upload_to='food_pics'),
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_amount', models.PositiveIntegerField(max_length=999999)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_items', to='rms_app.invoice')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_items', to='rms_app.food')),
            ],
        ),
    ]
