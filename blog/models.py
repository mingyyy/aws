from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import localtime, now


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # can't change it if we use auto_now_add
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})


class Event(models.Model):
    location = models.CharField(max_length=200)
    details = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.location

    @property
    def get_html_url(self):
        url = reverse('blog:event_edit', args=(self.id,))
        return f'<a href="{url}">{self.location}</a>'

    def event_duration(self):
        delta = self.end_time - self.start_time
        if delta.days >= 0:
            return delta.days
        else:
            return False
    #
    # def days_left(self):
    #     today = localtime(now())
    #     delta = (self.start_time - today)
    #     if delta.days > 0:
    #         return f"{delta.days} days to {self.location}"
    #     elif delta.days == 0:
    #         return "Arriving today!"
    #     else:
    #         delta2 = self.end_time - today
    #         if delta2.days > 0:
    #             return f"{delta2.days} days left"
    #         elif delta2.days == 0:
    #             return "Leaving today."


