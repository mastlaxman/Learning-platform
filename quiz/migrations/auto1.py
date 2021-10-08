from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', 'delete_student_status'),
        ('quiz', 'result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Course'),
        ),
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
