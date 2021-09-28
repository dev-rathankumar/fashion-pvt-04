import os
from django.core.exceptions import ValidationError


def validate_video_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.avi', '.mp4', '.mkv']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Supports .avi, .mp4 and .mkv files.')