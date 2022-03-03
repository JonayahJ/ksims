from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.utils.timezone import now

months = [
    ("JAN", "1"),
    ("FEB", "2"),
    ("MAR", "3"),
    ("APR", "4"),
    ("MAY", "5"),
    ("JUN", "6"),
    ("JUL", "7"),
    ("AUG", "8"),
    ("SEP", "9"),
    ("OCT", "10"),
    ("NOV", "11"), 
    ("DEC", "12")
]

# Article
class Article(models.Model):
    title = models.CharField(max_length=255)
    post_date = models.DateField(default=now, editable=True)
    month = models.CharField(choices=months, max_length=3, default="DEC")
    category = models.CharField(max_length=100, default='research')
    
    featuredImage = models.ImageField(upload_to="photos/publications", null=True, blank=True)
    featDesc = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")

    excerpt = models.CharField(max_length=400, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.")

    body = RichTextField(blank=True, null=True)

    innerImage = models.ImageField(upload_to="photos/publications", null=True, blank=True)
    imgDesc = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")

    body2 = RichTextField(blank=True, null=True)


    # Adding in the slugs for URLs and SEO
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Setting the slug to a keyword in the object (in this case, the title)
        return reverse('articles', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # if not a slug, slugify the title of the object
            self.slug = slugify(self.title)
        # return the new slug on save (?)
        return super().save(*args, **kwargs)
