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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCommentFlags(models.Model):
    flag = models.CharField(max_length=30)
    flag_date = models.DateTimeField()
    comment = models.ForeignKey('DjangoComments', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_comment_flags'
        unique_together = (('user', 'comment', 'flag'),)


class DjangoComments(models.Model):
    object_pk = models.CharField(max_length=64)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=254)
    user_url = models.CharField(max_length=200)
    comment = models.TextField()
    submit_date = models.DateTimeField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    is_public = models.BooleanField()
    is_removed = models.BooleanField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_comments'


class DjangoCommentsXtdBlacklisteddomain(models.Model):
    domain = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'django_comments_xtd_blacklisteddomain'


class DjangoCommentsXtdXtdcomment(models.Model):
    comment_ptr = models.OneToOneField(DjangoComments, models.DO_NOTHING, primary_key=True)
    thread_id = models.IntegerField()
    parent_id = models.IntegerField()
    level = models.SmallIntegerField()
    order = models.IntegerField()
    followup = models.BooleanField()
    nested_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_comments_xtd_xtdcomment'


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


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class MobilestoreBrand(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    nationality = models.CharField(max_length=32)
    description = models.TextField()
    publish = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mobilestore_brand'


class MobilestoreCart(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mobilestore_cart'


class MobilestoreCartitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey('MobilestoreMobile', models.DO_NOTHING)
    quantity = models.IntegerField()
    cart = models.ForeignKey(MobilestoreCart, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mobilestore_cartitem'


class MobilestoreComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    body = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    active = models.BooleanField()
    mobile = models.ForeignKey('MobilestoreMobile', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mobilestore_comment'


class MobilestoreMobile(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.CharField(unique=True, max_length=32)
    price = models.IntegerField()
    color = models.CharField(max_length=16)
    display_size = models.CharField(max_length=50)
    is_available = models.BooleanField()
    country = models.CharField(max_length=90, blank=True, null=True)
    photo = models.CharField(max_length=100)
    brand = models.ForeignKey(MobilestoreBrand, models.DO_NOTHING, blank=True, null=True)
    publish = models.DateTimeField()
    camera = models.CharField(max_length=50, blank=True, null=True)
    card = models.BooleanField(blank=True, null=True)
    memory = models.CharField(max_length=20, blank=True, null=True)
    dimensions = models.CharField(db_column='Dimensions', max_length=35, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    have_warranty = models.BooleanField(blank=True, null=True)
    warranty = models.CharField(max_length=50)
    register = models.BooleanField(blank=True, null=True)
    description = models.TextField()
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mobilestore_mobile'


class MobilestoreProcessor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mobilestore_processor'


class MobilestoreReview(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mobilestore_review'


class TwoFactorPhonedevice(models.Model):
    name = models.CharField(max_length=64)
    confirmed = models.BooleanField()
    throttling_failure_timestamp = models.DateTimeField(blank=True, null=True)
    throttling_failure_count = models.IntegerField()
    number = models.CharField(max_length=128)
    key = models.CharField(max_length=40)
    method = models.CharField(max_length=4)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'two_factor_phonedevice'
