# Generated by Django 5.0.6 on 2024-06-23 02:59

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id_car', models.AutoField(primary_key=True, serialize=False)),
                ('auc_link', models.TextField(null=True)),
                ('title', models.TextField(null=True)),
                ('auc_name', models.TextField(null=True)),
                ('auc_number', models.TextField(null=True)),
                ('auc_date', models.DateField(null=True)),
                ('year_car', models.TextField(null=True)),
                ('mileage', models.TextField(null=True)),
                ('color', models.TextField(null=True)),
                ('options', models.TextField(null=True)),
                ('the_body', models.TextField(null=True)),
                ('volume', models.TextField(null=True)),
                ('cpp', models.TextField(null=True)),
                ('estimation', models.TextField(null=True)),
                ('cooling', models.TextField(null=True)),
                ('set', models.TextField(null=True)),
                ('result', models.TextField(null=True)),
                ('start_price', models.TextField(null=True)),
                ('transmission', models.TextField(null=True)),
                ('location_auction', models.TextField(null=True)),
                ('year', models.TextField(null=True)),
                ('alt_color', models.TextField(null=True)),
                ('condition', models.TextField(null=True)),
                ('fuel', models.TextField(null=True)),
                ('equipment', models.TextField(null=True)),
                ('deadline_for_the_price_offer', models.TextField(null=True)),
                ('day_of_the_event', models.TextField(null=True)),
                ('number_of_sessions', models.TextField(null=True)),
                ('auc_list', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id_customer', models.AutoField(primary_key=True, serialize=False)),
                ('first_name_client', models.TextField()),
                ('last_name_client', models.TextField()),
                ('patronymic_client', models.TextField()),
                ('date_of_birth', models.TextField()),
                ('place_of_birth', models.TextField()),
                ('passport_series', models.TextField()),
                ('passport_number', models.TextField()),
                ('passport_department_code', models.TextField()),
                ('passport_department_name', models.TextField()),
                ('telephone', models.TextField()),
                ('address', models.TextField()),
                ('date_of_issue', models.TextField()),
                ('inn', models.FileField(blank=True, null=True, upload_to='inn/')),
                ('passport', models.FileField(blank=True, null=True, upload_to='passport/')),
                ('registration', models.FileField(blank=True, null=True, upload_to='registration/')),
            ],
        ),
        migrations.CreateModel(
            name='CustomsDuty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_action', models.DateField(blank=True, null=True)),
                ('type', models.TextField(choices=[('От 0 до 3 лет', 'От 0 до 3 лет'), ('От 3 до 5 лет', 'От 3 до 5 лет'), ('От 5 лет', 'От 5 лет')])),
                ('value_first', models.IntegerField(blank=True, null=True)),
                ('value_last', models.IntegerField(blank=True, null=True)),
                ('bet', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_action', models.DateField(blank=True, null=True)),
                ('volume_first', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('volume_last', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('coefficient_less_3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('coefficient_more_3', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Excise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_action', models.DateField(blank=True, null=True)),
                ('power_first_car', models.IntegerField(blank=True, null=True)),
                ('power_last_car', models.IntegerField(blank=True, null=True)),
                ('bet', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id_invoice', models.AutoField(primary_key=True, serialize=False)),
                ('payer', models.TextField()),
                ('seller', models.TextField()),
                ('date_form', models.TextField()),
                ('date_pay', models.TextField()),
                ('sum', models.IntegerField()),
                ('check_document', models.TextField()),
                ('assigning', models.TextField()),
                ('scan', models.TextField()),
                ('type', models.TextField(choices=[('Оплата авто в Японии', 'Оплата авто в Японии'), ('Оплата услуг ТК', 'Оплата услуг ТК'), ('Оплата таможенного взноса(ПТД)', 'Оплата таможенного взноса(ПТД)'), ('Оплата услуг лаборатории(СБТС)', 'Оплата услуг лаборатории(СБТС)'), ('Оплата услуг компании', 'Оплата услуг компании')])),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_first_car', models.IntegerField(blank=True, null=True)),
                ('price_last_car', models.IntegerField(blank=True, null=True)),
                ('price_transportation', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransportCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('number_contract', models.TextField(blank=True, null=True)),
                ('contract', models.FileField(blank=True, null=True, upload_to='transport_contract/')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.TextField()),
                ('job_title', models.TextField(choices=[('Менеджер', 'Менеджер'), ('Логист', 'Логист'), ('HR', 'HR'), ('Бухгалтер', 'Бухгалтер'), ('Оперативник', 'Оперативник'), ('Клиент', 'Клиент')])),
                ('phone_number', models.TextField()),
                ('passport', models.TextField(unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.TextField(blank=True, null=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(blank=True, null=True)),
                ('comment', models.TextField(null=True)),
                ('sbts', models.FileField(blank=True, null=True, upload_to='sbts/')),
                ('ptd', models.FileField(blank=True, null=True, upload_to='ptd/')),
                ('contract', models.FileField(blank=True, null=True, upload_to='client_contract/')),
                ('defective_statement', models.FileField(blank=True, null=True, upload_to='defective_statement/')),
                ('export_certificate', models.FileField(blank=True, null=True, upload_to='export_certificate/')),
                ('consignment', models.FileField(blank=True, null=True, upload_to='consignment/')),
                ('received_ptd', models.FileField(blank=True, null=True, upload_to='received_ptd/')),
                ('invoice', models.FileField(blank=True, null=True, upload_to='invoice/')),
                ('payment_order', models.FileField(blank=True, null=True, upload_to='payment_order/')),
                ('price', models.TextField(blank=True, max_length=5, null=True)),
                ('export_certificate_number', models.TextField(blank=True, max_length=5, null=True)),
                ('price_customer', models.TextField(blank=True, max_length=5, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('delivery', models.TextField(choices=[('Нужна доставка', 'Нужна доставка'), ('Доставка не требуется', 'Доставка не требуется')])),
                ('order_status', models.TextField(choices=[('В работе', 'В работе'), ('Не предоплачен', 'Не предоплачен'), ('Предоплачен', 'Предоплачен'), ('Выкуплен', 'Выкуплен'), ('Не выкуплен', 'Не выкуплен'), ('Оплачен', 'Оплачен'), ('Не оплачен', 'Не оплачен'), ('В пути до РФ', 'В пути до РФ'), ('В РФ', 'В РФ'), ('Ожидает отправки', 'Ожидает отправки'), ('В пути по РФ', 'В пути по РФ'), ('Выполнен', 'Выполнен')])),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.car')),
                ('id_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.customer')),
                ('id_worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoCar',
            fields=[
                ('id_photo', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.TextField()),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.car')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='order_photos/')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='auction.order')),
            ],
        ),
        migrations.CreateModel(
            name='Trans',
            fields=[
                ('id_trans', models.AutoField(primary_key=True, serialize=False)),
                ('trans_comp', models.TextField()),
                ('departure_point', models.TextField()),
                ('destination_point', models.TextField()),
                ('date_form', models.DateField()),
                ('date_shipment', models.DateField()),
                ('date_receive', models.DateField()),
                ('id_invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='TransportCompanyPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('id_transport_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.transportcompany')),
            ],
        ),
    ]