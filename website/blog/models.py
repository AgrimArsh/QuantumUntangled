from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.forms import CheckboxSelectMultiple

# Wagtail
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.search import index
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# Wagtail tagging
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

# Wagtail snippets
from wagtail.snippets.models import register_snippet

#################### Wagtail models ####################
# Home page
class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

# Show all published posts
class PostIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        postpages = self.get_children().live().order_by('-first_published_at')
        context['postpages'] = postpages
        return context

# Tag model for tagging posts. Authors can add tags to their posts.
class PostPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'PostPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

# Show posts by tag 
class PostTagIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        if request.GET.get('tag'):
            # Filter by tag
            tag = request.GET.get('tag')
            postpages = PostPage.objects.live().filter(tags__name=tag)

            # Update template context
            context = super().get_context(request)
            context['postpages'] = postpages
        else: 
            tags = []
            post_pages = PostPage.objects.live()
            for page in post_pages:
                tags += page.tags.all()
            tags = sorted(set(tags))

            # Update template context
            context = super().get_context(request)
            context['tags'] = tags
        
        return context

# Show post
class PostPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    tags = ClusterTaggableManager(through=PostPageTag, blank=True)
    categories = ParentalManyToManyField('blog.PostCategory', blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('html', blocks.RawHTMLBlock()),
        ('rich_text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=CheckboxSelectMultiple),
        ], heading="Post information"),
        FieldPanel('intro'),
        StreamFieldPanel('body', classname="full"),
    ]

# Categorize posts
@register_snippet
class PostCategory(models.Model):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'post categories'

# Show posts by category 
class PostCategoryIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        if request.GET.get('category'):
            # Filter by category
            category = request.GET.get('category')
            postpages = PostPage.objects.live().filter(categories__name=category)

            # Update template context
            context = super().get_context(request)
            context['postpages'] = postpages
        else: 
            categories = []
            post_pages = PostPage.objects.live()
            for page in post_pages:
                categories += page.categories.all()
            categories = sorted(set(categories))

            # Update template context
            context = super().get_context(request)
            context['categories'] = categories
        
        return context

#################### Native Django models ####################
# Create Profile when creating user (https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#disqus_thread)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save Profile when creating User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Tag(models.Model):
    db_name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.display_name}'

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title} by {self.author.username}'