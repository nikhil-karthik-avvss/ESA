# Generated by Django 3.2.18 on 2024-05-13 04:27

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='School_Name',
        ),
        migrations.AddField(
            model_name='student',
            name='School_Name_10th',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='School_Name_12th',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choicelisttable',
            name='Program',
            field=models.CharField(choices=[('B.E. Computer Science and Engineering', 'Bachelor of Engineering in Computer Science and Engineering'), ('B.Tech. Computer Science and Engineering', 'Bachelor of Technology in Computer Science and Engineering'), ('B.E. Information Technology', 'Bachelor of Engineering in Information Technology'), ('B.Tech. Information Technology', 'Bachelor of Technology in Information Technology'), ('B.E. Artificial Intelligence and Machine Learning', 'Bachelor of Engineering in Artificial Intelligence and Machine Learning'), ('B.Tech. Artificial Intelligence and Machine Learning', 'Bachelor of Technology in Artificial Intelligence and Machine Learning'), ('B.E. Data Science and Analytics', 'Bachelor of Engineering in Data Science and Analytics'), ('B.Tech. Data Science and Analytics', 'Bachelor of Technology in Data Science and Analytics'), ('B.E. Cybersecurity', 'Bachelor of Engineering in Cybersecurity'), ('B.Tech. Cybersecurity', 'Bachelor of Technology in Cybersecurity'), ('B.E. Electronics and Communication Engineering', 'Bachelor of Engineering in Electronics and Communication Engineering'), ('B.Tech. Electronics and Communication Engineering', 'Bachelor of Technology in Electronics and Communication Engineering'), ('B.E. Robotics and Automation', 'Bachelor of Engineering in Robotics and Automation'), ('B.Tech. Robotics and Automation', 'Bachelor of Technology in Robotics and Automation'), ('B.E. Biotechnology', 'Bachelor of Engineering in Biotechnology'), ('B.Tech. Biotechnology', 'Bachelor of Technology in Biotechnology'), ('B.E. Nanotechnology', 'Bachelor of Engineering in Nanotechnology'), ('B.Tech. Nanotechnology', 'Bachelor of Technology in Nanotechnology'), ('B.E. Renewable Energy Engineering', 'Bachelor of Engineering in Renewable Energy Engineering'), ('B.Tech. Renewable Energy Engineering', 'Bachelor of Technology in Renewable Energy Engineering'), ('B.E. Aerospace Engineering', 'Bachelor of Engineering in Aerospace Engineering'), ('B.Tech. Aerospace Engineering', 'Bachelor of Technology in Aerospace Engineering'), ('B.E. Gaming Technology', 'Bachelor of Engineering in Gaming Technology'), ('B.Tech. Gaming Technology', 'Bachelor of Technology in Gaming Technology'), ('B.E. Mobile Application Development', 'Bachelor of Engineering in Mobile Application Development'), ('B.Tech. Mobile Application Development', 'Bachelor of Technology in Mobile Application Development'), ('B.E. Augmented Reality and Virtual Reality', 'Bachelor of Engineering in Augmented Reality and Virtual Reality'), ('B.Tech. Augmented Reality and Virtual Reality', 'Bachelor of Technology in Augmented Reality and Virtual Reality'), ('B.E. Internet of Things (IoT)', 'Bachelor of Engineering in Internet of Things (IoT)'), ('B.Tech. Internet of Things (IoT)', 'Bachelor of Technology in Internet of Things (IoT)'), ('B.E. Biomedical Engineering', 'Bachelor of Engineering in Biomedical Engineering'), ('B.Tech. Biomedical Engineering', 'Bachelor of Technology in Biomedical Engineering'), ('B.E. Environmental Engineering', 'Bachelor of Engineering in Environmental Engineering'), ('B.Tech. Environmental Engineering', 'Bachelor of Technology in Environmental Engineering'), ('B.E. Petroleum Engineering', 'Bachelor of Engineering in Petroleum Engineering'), ('B.Tech. Petroleum Engineering', 'Bachelor of Technology in Petroleum Engineering'), ('B.E. Mining Engineering', 'Bachelor of Engineering in Mining Engineering'), ('B.Tech. Mining Engineering', 'Bachelor of Technology in Mining Engineering'), ('B.E. Nuclear Engineering', 'Bachelor of Engineering in Nuclear Engineering'), ('B.Tech. Nuclear Engineering', 'Bachelor of Technology in Nuclear Engineering'), ('B.E. Software Engineering', 'Bachelor of Engineering in Software Engineering'), ('B.Tech. Software Engineering', 'Bachelor of Technology in Software Engineering'), ('B.E. Systems Engineering', 'Bachelor of Engineering in Systems Engineering'), ('B.Tech. Systems Engineering', 'Bachelor of Technology in Systems Engineering'), ('B.E. Telecommunication Engineering', 'Bachelor of Engineering in Telecommunication Engineering'), ('B.Tech. Telecommunication Engineering', 'Bachelor of Technology in Telecommunication Engineering'), ('B.E. Instrumentation Engineering', 'Bachelor of Engineering in Instrumentation Engineering'), ('B.Tech. Instrumentation Engineering', 'Bachelor of Technology in Instrumentation Engineering'), ('B.E. Power Engineering', 'Bachelor of Engineering in Power Engineering'), ('B.Tech. Power Engineering', 'Bachelor of Technology in Power Engineering'), ('B.E. Civil Engineering', 'Bachelor of Engineering in Civil Engineering'), ('B.Tech. Civil Engineering', 'Bachelor of Technology in Civil Engineering'), ('B.E. Electrical and Electronics Engineering', 'Bachelor of Engineering in Electrical and Electronics Engineering'), ('B.Tech. Electrical and Electronics Engineering', 'Bachelor of Technology in Electrical and Electronics Engineering'), ('B.E. Mechanical Engineering', 'Bachelor of Engineering in Mechanical Engineering'), ('B.Tech. Mechanical Engineering', 'Bachelor of Technology in Mechanical Engineering'), ('B.E. Industrial Engineering', 'Bachelor of Engineering in Industrial Engineering'), ('B.Tech. Industrial Engineering', 'Bachelor of Technology in Industrial Engineering'), ('B.E. Electronics and Instrumentation Engineering', 'Bachelor of Engineering in Electronics and Instrumentation Engineering'), ('B.Tech. Electronics and Instrumentation Engineering', 'Bachelor of Technology in Electronics and Instrumentation Engineering'), ('B.E. Chemical Engineering', 'Bachelor of Engineering in Chemical Engineering'), ('B.Tech. Chemical Engineering', 'Bachelor of Technology in Chemical Engineering'), ('B.E. Textile Engineering', 'Bachelor of Engineering in Textile Engineering'), ('B.Tech. Textile Engineering', 'Bachelor of Technology in Textile Engineering'), ('B.E. Agricultural Engineering', 'Bachelor of Engineering in Agricultural Engineering'), ('B.Tech. Agricultural Engineering', 'Bachelor of Technology in Agricultural Engineering'), ('B.E. Food Technology', 'Bachelor of Engineering in Food Technology'), ('B.Tech. Food Technology', 'Bachelor of Technology in Food Technology'), ('B.E. Marine Engineering', 'Bachelor of Engineering in Marine Engineering'), ('B.Tech. Marine Engineering', 'Bachelor of Technology in Marine Engineering'), ('B.E. Nuclear Engineering', 'Bachelor of Engineering in Nuclear Engineering'), ('B.Tech. Nuclear Engineering', 'Bachelor of Technology in Nuclear Engineering'), ('B.E. Telecommunication Engineering', 'Bachelor of Engineering in Telecommunication Engineering'), ('B.Tech. Telecommunication Engineering', 'Bachelor of Technology in Telecommunication Engineering'), ('B.E. Instrumentation Engineering', 'Bachelor of Engineering in Instrumentation Engineering'), ('B.Tech. Instrumentation Engineering', 'Bachelor of Technology in Instrumentation Engineering'), ('B.E. Power Engineering', 'Bachelor of Engineering in Power Engineering'), ('B.Tech. Power Engineering', 'Bachelor of Technology in Power Engineering')], max_length=100),
        ),
        migrations.AlterField(
            model_name='seatmatrix',
            name='Program',
            field=models.CharField(choices=[('B.E. Computer Science and Engineering', 'Bachelor of Engineering in Computer Science and Engineering'), ('B.Tech. Computer Science and Engineering', 'Bachelor of Technology in Computer Science and Engineering'), ('B.E. Information Technology', 'Bachelor of Engineering in Information Technology'), ('B.Tech. Information Technology', 'Bachelor of Technology in Information Technology'), ('B.E. Artificial Intelligence and Machine Learning', 'Bachelor of Engineering in Artificial Intelligence and Machine Learning'), ('B.Tech. Artificial Intelligence and Machine Learning', 'Bachelor of Technology in Artificial Intelligence and Machine Learning'), ('B.E. Data Science and Analytics', 'Bachelor of Engineering in Data Science and Analytics'), ('B.Tech. Data Science and Analytics', 'Bachelor of Technology in Data Science and Analytics'), ('B.E. Cybersecurity', 'Bachelor of Engineering in Cybersecurity'), ('B.Tech. Cybersecurity', 'Bachelor of Technology in Cybersecurity'), ('B.E. Electronics and Communication Engineering', 'Bachelor of Engineering in Electronics and Communication Engineering'), ('B.Tech. Electronics and Communication Engineering', 'Bachelor of Technology in Electronics and Communication Engineering'), ('B.E. Robotics and Automation', 'Bachelor of Engineering in Robotics and Automation'), ('B.Tech. Robotics and Automation', 'Bachelor of Technology in Robotics and Automation'), ('B.E. Biotechnology', 'Bachelor of Engineering in Biotechnology'), ('B.Tech. Biotechnology', 'Bachelor of Technology in Biotechnology'), ('B.E. Nanotechnology', 'Bachelor of Engineering in Nanotechnology'), ('B.Tech. Nanotechnology', 'Bachelor of Technology in Nanotechnology'), ('B.E. Renewable Energy Engineering', 'Bachelor of Engineering in Renewable Energy Engineering'), ('B.Tech. Renewable Energy Engineering', 'Bachelor of Technology in Renewable Energy Engineering'), ('B.E. Aerospace Engineering', 'Bachelor of Engineering in Aerospace Engineering'), ('B.Tech. Aerospace Engineering', 'Bachelor of Technology in Aerospace Engineering'), ('B.E. Gaming Technology', 'Bachelor of Engineering in Gaming Technology'), ('B.Tech. Gaming Technology', 'Bachelor of Technology in Gaming Technology'), ('B.E. Mobile Application Development', 'Bachelor of Engineering in Mobile Application Development'), ('B.Tech. Mobile Application Development', 'Bachelor of Technology in Mobile Application Development'), ('B.E. Augmented Reality and Virtual Reality', 'Bachelor of Engineering in Augmented Reality and Virtual Reality'), ('B.Tech. Augmented Reality and Virtual Reality', 'Bachelor of Technology in Augmented Reality and Virtual Reality'), ('B.E. Internet of Things (IoT)', 'Bachelor of Engineering in Internet of Things (IoT)'), ('B.Tech. Internet of Things (IoT)', 'Bachelor of Technology in Internet of Things (IoT)'), ('B.E. Biomedical Engineering', 'Bachelor of Engineering in Biomedical Engineering'), ('B.Tech. Biomedical Engineering', 'Bachelor of Technology in Biomedical Engineering'), ('B.E. Environmental Engineering', 'Bachelor of Engineering in Environmental Engineering'), ('B.Tech. Environmental Engineering', 'Bachelor of Technology in Environmental Engineering'), ('B.E. Petroleum Engineering', 'Bachelor of Engineering in Petroleum Engineering'), ('B.Tech. Petroleum Engineering', 'Bachelor of Technology in Petroleum Engineering'), ('B.E. Mining Engineering', 'Bachelor of Engineering in Mining Engineering'), ('B.Tech. Mining Engineering', 'Bachelor of Technology in Mining Engineering'), ('B.E. Nuclear Engineering', 'Bachelor of Engineering in Nuclear Engineering'), ('B.Tech. Nuclear Engineering', 'Bachelor of Technology in Nuclear Engineering'), ('B.E. Software Engineering', 'Bachelor of Engineering in Software Engineering'), ('B.Tech. Software Engineering', 'Bachelor of Technology in Software Engineering'), ('B.E. Systems Engineering', 'Bachelor of Engineering in Systems Engineering'), ('B.Tech. Systems Engineering', 'Bachelor of Technology in Systems Engineering'), ('B.E. Telecommunication Engineering', 'Bachelor of Engineering in Telecommunication Engineering'), ('B.Tech. Telecommunication Engineering', 'Bachelor of Technology in Telecommunication Engineering'), ('B.E. Instrumentation Engineering', 'Bachelor of Engineering in Instrumentation Engineering'), ('B.Tech. Instrumentation Engineering', 'Bachelor of Technology in Instrumentation Engineering'), ('B.E. Power Engineering', 'Bachelor of Engineering in Power Engineering'), ('B.Tech. Power Engineering', 'Bachelor of Technology in Power Engineering'), ('B.E. Civil Engineering', 'Bachelor of Engineering in Civil Engineering'), ('B.Tech. Civil Engineering', 'Bachelor of Technology in Civil Engineering'), ('B.E. Electrical and Electronics Engineering', 'Bachelor of Engineering in Electrical and Electronics Engineering'), ('B.Tech. Electrical and Electronics Engineering', 'Bachelor of Technology in Electrical and Electronics Engineering'), ('B.E. Mechanical Engineering', 'Bachelor of Engineering in Mechanical Engineering'), ('B.Tech. Mechanical Engineering', 'Bachelor of Technology in Mechanical Engineering'), ('B.E. Industrial Engineering', 'Bachelor of Engineering in Industrial Engineering'), ('B.Tech. Industrial Engineering', 'Bachelor of Technology in Industrial Engineering'), ('B.E. Electronics and Instrumentation Engineering', 'Bachelor of Engineering in Electronics and Instrumentation Engineering'), ('B.Tech. Electronics and Instrumentation Engineering', 'Bachelor of Technology in Electronics and Instrumentation Engineering'), ('B.E. Chemical Engineering', 'Bachelor of Engineering in Chemical Engineering'), ('B.Tech. Chemical Engineering', 'Bachelor of Technology in Chemical Engineering'), ('B.E. Textile Engineering', 'Bachelor of Engineering in Textile Engineering'), ('B.Tech. Textile Engineering', 'Bachelor of Technology in Textile Engineering'), ('B.E. Agricultural Engineering', 'Bachelor of Engineering in Agricultural Engineering'), ('B.Tech. Agricultural Engineering', 'Bachelor of Technology in Agricultural Engineering'), ('B.E. Food Technology', 'Bachelor of Engineering in Food Technology'), ('B.Tech. Food Technology', 'Bachelor of Technology in Food Technology'), ('B.E. Marine Engineering', 'Bachelor of Engineering in Marine Engineering'), ('B.Tech. Marine Engineering', 'Bachelor of Technology in Marine Engineering'), ('B.E. Nuclear Engineering', 'Bachelor of Engineering in Nuclear Engineering'), ('B.Tech. Nuclear Engineering', 'Bachelor of Technology in Nuclear Engineering'), ('B.E. Telecommunication Engineering', 'Bachelor of Engineering in Telecommunication Engineering'), ('B.Tech. Telecommunication Engineering', 'Bachelor of Technology in Telecommunication Engineering'), ('B.E. Instrumentation Engineering', 'Bachelor of Engineering in Instrumentation Engineering'), ('B.Tech. Instrumentation Engineering', 'Bachelor of Technology in Instrumentation Engineering'), ('B.E. Power Engineering', 'Bachelor of Engineering in Power Engineering'), ('B.Tech. Power Engineering', 'Bachelor of Technology in Power Engineering')], max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='Board_12th',
            field=models.CharField(choices=[('CBSE', 'Central Board of Secondary Education (CBSE)'), ('CISCE', 'Council for the Indian School Certificate Examinations (CISCE)'), ('NIOS', 'National Institute of Open Schooling (NIOS)'), ('MSBSHSE', 'Maharashtra State Board of Secondary and Higher Secondary Education (MSBSHSE)'), ('TNBHSE', 'Tamil Nadu State Board of Higher Secondary Education (TNBHSE)'), ('UPMSP', 'Uttar Pradesh Madhyamik Shiksha Parishad (UPMSP)')], max_length=60),
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_ID',
            field=models.IntegerField(default=pages.models.Student.get_student_id, primary_key=True, serialize=False),
        ),
    ]
