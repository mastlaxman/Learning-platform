from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', 'intialization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('question', models.CharField(max_length=600)),
                ('opt1', models.CharField(max_length=200)),
                ('opt2', models.CharField(max_length=200)),
                ('opt3', models.CharField(max_length=200)),
                ('opt4', models.CharField(max_length=200)),
                ('answer', models.CharField(choices=[('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4')], max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Course')),
            ],
        ),
    ]
