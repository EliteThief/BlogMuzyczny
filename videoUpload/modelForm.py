from django.forms import ModelForm
from content.models import Video


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['views', 'upvotes', 'downvotes', 'video_info', 'channel', 'file']
