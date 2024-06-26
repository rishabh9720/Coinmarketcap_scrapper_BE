# Generated by Django 4.2.13 on 2024-05-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='circulating_supply',
            field=models.CharField(help_text='The circulating supply of the cryptocurrency.', max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='The datetime when the object was created.'),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='currency_name',
            field=models.CharField(help_text='The name of the cryptocurrency.', max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='current_price',
            field=models.CharField(help_text='The current price of the cryptocurrency.', max_length=64),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='daily_change',
            field=models.CharField(help_text="The daily change in the cryptocurrency's price.", max_length=64),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='hourly_change',
            field=models.CharField(help_text="The hourly change in the cryptocurrency's price.", max_length=64),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='logo',
            field=models.URLField(blank=True, help_text="URL of the cryptocurrency's logo.", null=True),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='market_capital',
            field=models.CharField(help_text='The market capitalization of the cryptocurrency.', max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='symbol',
            field=models.CharField(help_text='The symbol of the cryptocurrency.', max_length=64),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='trade_volume_crypto',
            field=models.CharField(help_text='The trading volume in cryptocurrency.', max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='trade_volume_usd',
            field=models.CharField(help_text='The trading volume in USD.', max_length=255),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='The datetime when the object was last updated.'),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='weekly_change',
            field=models.CharField(help_text="The weekly change in the cryptocurrency's price.", max_length=64),
        ),
    ]
