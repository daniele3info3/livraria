# Generated by Django 4.1.1 on 2022-10-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_livro_capa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autor",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="livro",
            name="isbn",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="livro",
            name="preco",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=7, null=True
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="quantidade",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
