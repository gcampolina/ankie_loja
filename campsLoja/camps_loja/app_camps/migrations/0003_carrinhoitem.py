# Generated by Django 4.2.6 on 2024-04-14 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_camps', '0002_produto_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarrinhoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_camps.produto')),
            ],
        ),
    ]