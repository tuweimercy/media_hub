from django.contrib import admin
from .models import MediaAssets
# Register your models here.
@admin.register(MediaAssets)
class MediaAssetAmin(admin.ModelAdmin):
    list_display = ('title','category','uploaded_by','is_public',
    'views_count','created_at')
    list_filter = ('category','is_public','created_at')
    search_fields =('title','description','uploaded_by_username')
    '''admin can only view read only fields can never edit'''
    readonly_fields=('created_by','uploaded_at','views_count')
    date_hierarchy='created_at'#data ordering
    