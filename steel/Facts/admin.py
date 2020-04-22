from django.contrib import admin
from .models import Link,Voters,UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Link)
admin.site.register(Voters)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(),UserProfileAdmin)


