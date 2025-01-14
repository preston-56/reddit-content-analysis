from django.db import models

class Analysis(models.Model):
    subreddit = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()

    class Meta:
        app_label = 'reddit'

    def __str__(self):
        return f"Analysis of {self.subreddit} at {self.timestamp}"
