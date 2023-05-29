# Generated by Django 4.1.7 on 2023-05-15 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="academicyear",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                #("academicyear",models.CharField(max_length=100, null=True, unique=True),)

            ],
        ),
        migrations.CreateModel(
            name="Score",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.FloatField()),
                ("academicyear", models.CharField(max_length=100, null=True)),
                ("grademark", models.CharField(max_length=100)),
                ('year', models.ForeignKey(to='dashboard.Year', on_delete=models.CASCADE)),

            ],
        ),
        migrations.CreateModel(
            name="Year",
            fields=[
                ("yearid", models.AutoField(primary_key=True, serialize=False)),
                (
                    "year",
                    models.IntegerField(
                        choices=[(9, "9th"), (10, "10th"), (11, "11th"), (12, "12th")]
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="grades_pdf",
        ),
        migrations.RemoveField(
            model_name="class",
            name="classgrade",
        ),
        migrations.RemoveField(
            model_name="class",
            name="classyear",
        ),
        migrations.AddField(
            model_name="class",
            name="credit",
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="score",
            name="classes_taken",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dashboard.class"
            ),
        ),
        migrations.AddField(
            model_name="score",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dashboard.student"
            ),
        ),
        migrations.AddField(
            model_name="score",
            name="yearid",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dashboard.year"
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="academicyear",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scores",
                to="dashboard.academicyear",
            ),
        ),
    ]
