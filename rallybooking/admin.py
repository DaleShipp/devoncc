from django.contrib import admin

# Register your models here.
from .models import Rally, RallyBooking

# rally_name = models.CharField(max_length=STRMAX)
# rally_no = models.IntegerField()
# added_date = models.DateTimeField('date added', default=datetime.now, editable=False)
# updated_date = models.DateTimeField('date added', default=datetime.now, editable=False)
# added_by_name = models.CharField(max_length=STRMAX, blank=True, editable=False)
# num_pitches_total = models.IntegerField(default=1)
# num_powered_pitches = models.IntegerField(default=0)
# start_date = models.DateField('first night')
# end_date = models.DateField('last night')
# leave_time = models.TimeField('time to leave site', default='16:00')

# Options
# dogs_allowed = models.BooleanField(default=False)


# Rally.ra
class RallyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['rally_name', 'rally_no']}),
        ('Date information', {'fields': ['start_date', 'end_date']}),
        ('Pitches', {'fields': ['num_pitches_total','num_powered_pitches']}),
        ('Site', {'fields': ['site_name', 'leave_time']})
    ]
    list_display = ('rally_name', 'start_date','end_date')
    list_filter = ['start_date']
    search_fields = ['rally_name']
admin.site.register(Rally, RallyAdmin)
admin.site.register(RallyBooking)

