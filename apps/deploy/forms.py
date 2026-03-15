from django import forms
from django.core.exceptions import ValidationError

from .models import Deployment


MAX_IMAGE_SIZE_BYTES = 5 * 1024 * 1024
ALLOWED_IMAGE_CONTENT_TYPES = {
    'image/jpeg',
    'image/png',
    'image/gif',
    'image/webp',
}
ALLOWED_IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}


class DeploymentForm(forms.ModelForm):
    class Meta:
        model = Deployment
        fields = ['name', 'image', 'description']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            return image

        if image.size > MAX_IMAGE_SIZE_BYTES:
            raise ValidationError('Image file size must be 5MB or smaller.')

        file_name = getattr(image, 'name', '')
        lower_name = file_name.lower()
        has_allowed_extension = any(
            lower_name.endswith(ext) for ext in ALLOWED_IMAGE_EXTENSIONS
        )
        if not has_allowed_extension:
            raise ValidationError('Only JPG, PNG, GIF, and WEBP image formats are allowed.')

        content_type = getattr(image, 'content_type', None)
        if content_type and content_type not in ALLOWED_IMAGE_CONTENT_TYPES:
            raise ValidationError('Only JPG, PNG, GIF, and WEBP image formats are allowed.')

        return image
