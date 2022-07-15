
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SafetyEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.building')),

            ],
        ),
        migrations.CreateModel(
            name='NoiseEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.building')),

            ],
        ),
        migrations.CreateModel(
            name='LocationEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.building')),

            ],
        ),
        migrations.CreateModel(
            name='CleanlinessEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.building')),
            ],
        ),
    ]
