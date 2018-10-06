from datetime import datetime
from django.db import models

STRMAX = 300

# Create your models here.
class Rally(models.Model):
    # rally_id = models.IntegerField(unique=True,auto_created=True)
    rally_name = models.CharField(max_length=STRMAX)
    rally_no = models.IntegerField()
    added_date = models.DateTimeField('date added', default=datetime.now, editable=False)
    updated_date = models.DateTimeField('date added', default=datetime.now, editable=False)
    added_by_name = models.CharField(max_length=STRMAX, blank=True, editable=False)
    num_pitches_total = models.IntegerField(default=1)
    num_powered_pitches = models.IntegerField(default=0)
    start_date = models.DateField('first night')
    end_date = models.DateField('last night')
    leave_time = models.TimeField('time to leave site', default='16:00')

    site_name = models.CharField(max_length=STRMAX, default='')

    #Options
    dogs_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.rally_name

    def is_published(self):
        return self.pub_date is not None

    def save(self):
        if not self.id:
            self.added_date = datetime.today()
            #TODO: use session.logged_in_users
            added_by_name = ''
        self.updated_date = datetime.today()
        if self.end_date > self.start_date:
            #TODO: lookup how to do this
            return False
        super(Rally, self).save()

class RallyBooking(models.Model):
    booked_name = models.CharField(max_length=STRMAX, default='')

    def __str__(self):
        return self.booked_name


#
# class CCMember(models.Model):
#     pass
#
# class DCMember(models.Model):
#     pass

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)