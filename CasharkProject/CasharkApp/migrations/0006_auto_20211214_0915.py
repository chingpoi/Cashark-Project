# Generated by Django 3.2.6 on 2021-12-14 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CasharkApp', '0005_auto_20211117_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminList',
            fields=[
                ('Admin_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Last_Accessed', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('Bank_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Account_Number', models.CharField(max_length=50)),
                ('Balance', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('Bank_Info_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CasharkApp.bankinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('Feedback_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('Request_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Request_Description', models.CharField(max_length=50)),
                ('Status', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='gcash',
            name='Bank_Info_ID',
        ),
        migrations.RemoveField(
            model_name='message',
            name='Sender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Address_ID',
        ),
        migrations.AddField(
            model_name='message',
            name='Sender_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mSender', to='CasharkApp.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='Date_Paid',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Address_City',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Address_Province',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Address_Street',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='Message',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Status',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='Balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Credit_Score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Mobile_Number',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='GCash',
        ),
        migrations.AddField(
            model_name='request',
            name='Receiver_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rReceiver', to='CasharkApp.user'),
        ),
        migrations.AddField(
            model_name='request',
            name='Sender_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rSender', to='CasharkApp.user'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Receiver_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fReceiver', to='CasharkApp.user'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='Sender_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fSender', to='CasharkApp.user'),
        ),
        migrations.AddField(
            model_name='adminlist',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CasharkApp.user'),
        ),
    ]
