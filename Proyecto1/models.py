from django.db import models


class T2TCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't2_t_category'


class T2TConsulanteducation(models.Model):
    professional = models.OneToOneField('T2TProfesionprofile', models.DO_NOTHING, primary_key=True)
    education = models.ForeignKey('T2TEducation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't2_t_consulanteducation'
        unique_together = (('professional', 'education'),)


class T2TConsultant(models.Model):
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
    professional = models.ForeignKey('T2TProfesionprofile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't2_t_consultant'
        unique_together = (('phone', 'email'),)


class T2TConsultantreference(models.Model):
    professional = models.OneToOneField('T2TProfesionprofile', models.DO_NOTHING, primary_key=True)
    skill = models.ForeignKey('T2TReference', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't2_t_consultantreference'
        unique_together = (('professional', 'skill'),)


class T2TConsultantskill(models.Model):
    professional = models.OneToOneField('T2TProfesionprofile', models.DO_NOTHING, primary_key=True)
    skill = models.ForeignKey('T2TSkill', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't2_t_consultantskill'
        unique_together = (('professional', 'skill'),)


class T2TEducation(models.Model):
    education_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    institution = models.ForeignKey('T2TEducationinstitution', models.DO_NOTHING, db_column='institution', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't2_t_education'


class T2TEducationinstitution(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't2_t_educationinstitution'


class T2TProfesionprofile(models.Model):
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
        db_table = 't2_t_profesionprofile'


class T2TReference(models.Model):
    reference_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=80, blank=True, null=True)
    lastname = models.CharField(max_length=80, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't2_t_reference'


class T2TSkill(models.Model):
    skill_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    domain_level = models.CharField(max_length=40, blank=True, null=True)
    category = models.ForeignKey(T2TCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't2_t_skill'


class T2TWorkexperience(models.Model):
    work_id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=60, blank=True, null=True)
    company = models.CharField(max_length=60, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    professional = models.ForeignKey(T2TProfesionprofile, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't2_t_workexperience'
