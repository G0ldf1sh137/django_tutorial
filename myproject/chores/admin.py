from django.contrib import admin

from .models import ChoreDefinition, ChoreInstance

# class ChoreDefinitionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["title", "description"]}),
#     ]
    
#     list_display = ["title", "description"]
    
    
admin.site.register(ChoreDefinition)
admin.site.register(ChoreInstance)