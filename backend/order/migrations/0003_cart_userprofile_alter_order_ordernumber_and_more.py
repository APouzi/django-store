# Generated by Django 4.0.3 on 2022-04-03 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_shippingaddress_street_and_more'),
        ('order', '0002_alter_order_ordernumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='userProfile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userprofile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderNumber',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='orderItems',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='orderItems',
            field=models.ManyToManyField(to='order.order'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.cart')),
            ],
        ),
    ]
