from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import (
    Project, Skill, Experience, Blog, ProjectImage, Feature, Learning, FAQ, ContactMessage, Resume
)
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("file", "uploaded_at")

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1

class LearningInline(admin.TabularInline):
    model = Learning
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "categories", "publication_date", "slug")
    inlines = [ProjectImageInline, FeatureInline, LearningInline]  

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "image")

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "project")

@admin.register(Learning)
class LearningAdmin(admin.ModelAdmin):
    list_display = ("paragraph", "project")

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
    list_display = ("title", "publication_date", "slug")  

# ✅ Check if Blog is registered before unregistering
if admin.site.is_registered(Blog):
    admin.site.unregister(Blog)

admin.site.register(Blog, BlogAdmin)

# Register remaining models
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(FAQ)
admin.site.register(ContactMessage)
