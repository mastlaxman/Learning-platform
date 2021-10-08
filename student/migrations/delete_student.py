from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('student', 'intialization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='status',
        ),
    ]
