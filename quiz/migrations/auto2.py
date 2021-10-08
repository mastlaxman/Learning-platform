from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', 'auto1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
