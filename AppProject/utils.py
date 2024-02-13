from django.core.exceptions import ValidationError

def validate_image_file_extension(value):
    if not value.name.endswith(('.png', '.jpg', '.jpeg')):
        raise ValidationError('Invalid file extension. Only PNG, JPG, and JPEG files are allowed.')

def max_file_size(value):
    limit = 2 * 1024 * 1024  # 2 megabytes
    if value.size > limit:
        raise ValidationError('File size cannot exceed 2 MB.')