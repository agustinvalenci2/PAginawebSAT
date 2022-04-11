# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Consulanteducation(models.Model):
    professional = models.OneToOneField('Profesionprofile', models.DO_NOTHING, primary_key=True)
    education = models.ForeignKey('Education', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'consulanteducation'
        unique_together = (('professional', 'education'),)


class Consultant(models.Model):
    phone = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    firstname = models.CharField(max_length=60, blank=True, null=True)
    lastname = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    citizenship = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    skype = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(db_column='linkedIn', max_length=255, blank=True, null=True)  # Field name made lowercase.
    twitter = models.CharField(max_length=255, blank=True, null=True)
    about_us = models.CharField(max_length=60, blank=True, null=True)
    professional = models.ForeignKey('Profesionprofile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultant'
        unique_together = (('phone', 'email'),)


class Consultantreference(models.Model):
    professional = models.OneToOneField('Profesionprofile', models.DO_NOTHING, primary_key=True)
    skill = models.ForeignKey('Reference', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'consultantreference'
        unique_together = (('professional', 'skill'),)


class Consultantskill(models.Model):
    professional = models.OneToOneField('Profesionprofile', models.DO_NOTHING, primary_key=True)
    skill = models.ForeignKey('Skill', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'consultantskill'
        unique_together = (('professional', 'skill'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Education(models.Model):
    education_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    institution = models.ForeignKey('Educationinstitution', models.DO_NOTHING, db_column='institution', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'education'


class Educationinstitution(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'educationinstitution'


class Profesionprofile(models.Model):
    professional_id = models.IntegerField(primary_key=True)
    industry = models.CharField(max_length=90, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    experience_years = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    type_of_job = models.CharField(max_length=20, blank=True, null=True)
    remote_experience = models.IntegerField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesionprofile'


class Reference(models.Model):
    reference_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=80, blank=True, null=True)
    lastname = models.CharField(max_length=80, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference'


class Skill(models.Model):
    skill_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    domain_level = models.CharField(max_length=40, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill'


class Workexperience(models.Model):
    work_id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=60, blank=True, null=True)
    company = models.CharField(max_length=60, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    professional = models.ForeignKey(Profesionprofile, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workexperience'
