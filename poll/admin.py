from django.contrib import admin
from .models import Poll, Option, Response

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class ResponseInline(admin.TabularInline):
    model = Response
    extra = 0
    readonly_fields = ['response_time']

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ['title', 'question', 'active_until', 'status']
    list_filter = ['status', 'active_until']
    search_fields = ['title', 'question']
    inlines = [OptionInline]

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'poll']
    list_filter = ['poll']
    search_fields = ['title', 'poll__title']

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['name', 'option', 'response_time', 'get_poll']
    list_filter = ['response_time', 'option__poll']
    search_fields = ['name', 'option__title']
    
    def get_poll(self, obj):
        return obj.option.poll
    get_poll.short_description = 'Poll'