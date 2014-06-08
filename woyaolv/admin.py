from django.contrib import admin
from woyaolv.models import user_traveler,user_driver,planfix,planfix_pictures,travel_propose,travel_propose_traveler,from_airport,to_airport,user_driver_comments,user_traveler_comments,planfix_comments
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date','publisher')    
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher', 'publication_date')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher','authors')
"""
"""
class userTravelerAdmin(admin.ModelAdmin):   
	list_filter = ('score',)
	ordering = ('score',)

class userDriverAdmin(admin.ModelAdmin):
	list_filter = ('score',)
	ordering = ('score',)

class planfixAdmin(admin.ModelAdmin):	
	list_filter = ('region',)
	ordering = ('region',)

#class planfixPicturesAdmin(admin.ModelAdmin):
	
class travelProposeAdmin(admin.ModelAdmin):	
	list_filter = ('datetime_create','state','num_want','num_now','start_date','end_date')
	ordering = ('-datetime_create',)

class travelProposeTravelerAdmin(admin.ModelAdmin):
	list_filter = ('travel_propose',)
	ordering = ('travel_propose',)

class fromAirportAdmin(admin.ModelAdmin):
	list_filter = ('datetime_create','datetime')
	ordering = ('-datetime_create',)

class toAirportAdmin(admin.ModelAdmin):
	list_filter = ('datetime_create','datetime')	
	ordering = ('-datetime_create',)	

class userDriverCommentsAdmin(admin.ModelAdmin):
	list_filter = ('datetime','user_driver')
	ordering = ('-datetime',)

class userTravelerCommentsAdmin(admin.ModelAdmin):
	list_filter = ('datetime','user_traveler')
	ordering = ('-datetime',)

class planfixCommentsAdmin(admin.ModelAdmin):
	list_filter = ('datetime','planfix')
	ordering = ('-datetime',)



admin.site.register(user_traveler,userTravelerAdmin)
admin.site.register(user_driver,userDriverAdmin)
admin.site.register(planfix,planfixAdmin)
admin.site.register(planfix_pictures)
admin.site.register(travel_propose,travelProposeAdmin)
admin.site.register(travel_propose_traveler,travelProposeTravelerAdmin)
admin.site.register(from_airport,fromAirportAdmin)
admin.site.register(to_airport,toAirportAdmin)
admin.site.register(user_driver_comments,userDriverCommentsAdmin)
admin.site.register(user_traveler_comments,userTravelerCommentsAdmin)
admin.site.register(planfix_comments,planfixCommentsAdmin)
