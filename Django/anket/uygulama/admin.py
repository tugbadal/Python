from django.contrib import admin
from uygulama.models import Poll
from uygulama.models import Choice,Poll

#admin.site.register(Poll)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll,PollAdmin)

# Register your models here.
