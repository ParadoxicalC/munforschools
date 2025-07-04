from django.contrib import admin
from .models import (
    SecretariatMember, ExecutiveBoardMember, Committee, CommitteeMember,
    ItineraryEvent, GalleryImage, ResourceLink, Signup
)

class CommitteeMemberInline(admin.TabularInline):
    model = CommitteeMember
    extra = 1

@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    inlines = [CommitteeMemberInline]
    list_display = ('name', 'agenda', 'venue')
    search_fields = ('name', 'agenda')

@admin.register(ItineraryEvent)
class ItineraryEventAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time', 'title')
    list_filter = ('day',)
    search_fields = ('title',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('chapter', 'caption')
    list_filter = ('chapter',)

@admin.register(ResourceLink)
class ResourceLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'pdf')
    search_fields = ('title',)

admin.site.register(SecretariatMember)
admin.site.register(ExecutiveBoardMember)
admin.site.register(Signup)
