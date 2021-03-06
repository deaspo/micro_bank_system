# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-27 15:18
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_address', models.TextField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField(max_length=10)),
                ('tel_no', models.IntegerField(blank=True, max_length=10)),
                ('resident_town', models.CharField(max_length=20)),
                ('estate', models.CharField(max_length=20)),
                ('house_no', models.IntegerField(blank=True, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='ATMCard',
            fields=[
                ('number', models.IntegerField(auto_created=True, editable=False, max_length=7, primary_key=True,
                                               serialize=False)),
                ('expiry_date', models.DateTimeField()),
                ('csv', models.IntegerField(max_length=3)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentAccount',
            fields=[
                ('account_number',
                 models.IntegerField(auto_created=True, editable=False, max_length=7, primary_key=True,
                                     serialize=False)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Economic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_status', models.CharField(
                    choices=[('employed', 'employed'), ('self-employed', 'self-employed'),
                             ('not working', 'not working')], default='employed', max_length=50)),
                ('employer_name', models.CharField(blank=True, max_length=50)),
                ('employer_address', models.CharField(blank=True, max_length=50)),
                ('monthly_income', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('other_economic',
                 models.CharField(blank=True, choices=[('Farming', 'Farming'), ('SMEs', 'SMEs'), ('Others', 'Others')],
                                  max_length=50)),
                ('econ_life', models.IntegerField(max_length=2)),
                ('other_econ', models.CharField(blank=True, max_length=50)),
                ('gen_income', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('electricity', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('water', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('transport', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('phone', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('entertainment', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('school_fees_desc', models.CharField(
                    help_text='Are you schooling yourself or someone? Tell us how this expense applies to you.',
                    max_length=500)),
                ('school_fees', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('others', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Guarantor',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('other_names', models.CharField(max_length=50)),
                ('id_number', models.IntegerField(primary_key=True, serialize=False)),
                ('passport', models.BooleanField(default=False)),
                ('passport_no', models.IntegerField(blank=True)),
                ('pin_no', models.IntegerField(max_length=7)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Addresse')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_application_number',
                 models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('new_customer', models.BooleanField(default=True)),
                ('loan_tyoe', models.CharField(
                    choices=[('Instant', 'Instant'), ('Mjengo', 'Mjengo'), ('Mkulima', 'Mkulima'),
                             ('Salary Advance', 'Salary Advance'), ('School Fees', 'School Fees'),
                             ('Funeral', 'Funeral')], max_length=50)),
                ('loan_period', models.IntegerField(max_length=2)),
                (
                'loan_status', models.CharField(choices=[('Awarded', 'Awarded'), ('Denied', 'Denied')], max_length=20)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('participanting',
                 models.CharField(choices=[('Only me', 'Only me'), ('Group', 'Group')], default='Only me',
                                  max_length=20)),
                ('participant_no', models.IntegerField(blank=True, max_length=2)),
                ('loan_purpose', models.TextField(max_length=1000)),
                ('criminal_offence', models.BooleanField(default=False)),
                ('bankruptcy', models.BooleanField(default=False)),
                ('defaults_payments', models.BooleanField(default=False)),
                ('defaults_description', models.CharField(blank=True, max_length=1000)),
                ('child_support', models.BooleanField(default=False)),
                ('child_support_description', models.CharField(blank=True, max_length=1000)),
                ('guarantee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Guarantor')),
            ],
        ),
        migrations.CreateModel(
            name='Other_Borrower',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('other_names', models.CharField(max_length=50)),
                ('id_number', models.IntegerField(primary_key=True, serialize=False)),
                ('passport', models.BooleanField(default=False)),
                ('passport_no', models.IntegerField(blank=True)),
                ('pin_no', models.IntegerField(max_length=7)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Addresse')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Information',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('other_names', models.CharField(max_length=50)),
                ('id_number', models.IntegerField(primary_key=True, serialize=False)),
                ('passport', models.BooleanField(default=False)),
                ('passport_no', models.IntegerField(blank=True)),
                ('pin_no', models.IntegerField(max_length=7)),
                ('register_atm', models.BooleanField(default=True)),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Addresse')),
                ('atm_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.ATMCard')),
                (
                'current_ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.CurrentAccount')),
                ('economic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Economic')),
                ('loan_ac', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='loan.Loan')),
            ],
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savings_plan', models.BooleanField(default=True)),
                ('saving_detail', models.TextField(max_length=1000)),
                ('monthly_saving', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='SavingAccount',
            fields=[
                ('account_number',
                 models.IntegerField(auto_created=True, editable=False, max_length=7, primary_key=True,
                                     serialize=False)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='personal_information',
            name='saving_ac',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='loan.SavingAccount'),
        ),
        migrations.AddField(
            model_name='loan',
            name='participant_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Other_Borrower'),
        ),
        migrations.AddField(
            model_name='economic',
            name='monthly_expenses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Expenses'),
        ),
        migrations.AddField(
            model_name='economic',
            name='savings',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='loan.Saving'),
        ),
        migrations.AddField(
            model_name='atmcard',
            name='atm_current',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.CurrentAccount'),
        ),
        migrations.AddField(
            model_name='atmcard',
            name='atm_saving',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='loan.SavingAccount'),
        ),
    ]
