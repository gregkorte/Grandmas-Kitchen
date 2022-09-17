# Generated by Django 3.2.5 on 2022-09-17 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grandmas_kitchen', '0002_familymember_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grandmas_kitchen.category')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grandmas_kitchen.family')),
                ('family_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grandmas_kitchen.familymember')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grandmas_kitchen.type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=5000)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grandmas_kitchen.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMemberRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_member', models.ManyToManyField(to='grandmas_kitchen.FamilyMember')),
                ('relation', models.ManyToManyField(to='grandmas_kitchen.Relation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
