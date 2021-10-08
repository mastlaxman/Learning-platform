"""
LearningPlatform Including fucntions like Login of the Teacher and Student
And Registration of the teacher and Student and
Modification of Courses done by teacher
Students can access courses and give exams for a particular course
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearningPlatform.settings')
application = get_assg_application()
