from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', 'delete_student_status'),
        ('quiz', 'question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('exam', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.Course')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
