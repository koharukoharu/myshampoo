from django.contrib import admin
from cms.models import Shampoo, Impression

# Register your models here.

#admin.site.register(Shampoo)
#admin.site.register(Impression)

class ShampooAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'price',)
    list_display_links = ('id', 'name',)


admin.site.register(Shampoo, ShampooAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('shampoo',)


admin.site.register(Impression, ImpressionAdmin)

