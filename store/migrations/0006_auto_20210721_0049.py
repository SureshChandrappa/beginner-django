# Generated by Django 3.2.5 on 2021-07-20 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210720_1306'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
            VALUES ('collection1')
        """, 
        """ DELETE from store_collection
        where title = 'collection1' """
        )
    ]