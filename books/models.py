import os
from PIL import Image, ImageDraw, ImageFont
from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default=None)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='static/uploads/', null=True, blank=True)
    follow_author = models.CharField(max_length=2083, blank=True)
    book_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Call the save method of the parent class
        super().save(*args, **kwargs)

        # Add watermark to the uploaded image
        if self.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
            image = Image.open(image_path)

            # You can customize the watermark text, font, size, color, etc.
            watermark_text = "StoreBooks"
            font = ImageFont.load_default()
            draw = ImageDraw.Draw(image)
            draw.text((10, 10), watermark_text, fill="white", font=font)

            # Save the image with the watermark
            image.save(image_path)


class Order(models.Model):
	product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.title
