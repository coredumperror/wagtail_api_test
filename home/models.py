from django.db import models

from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField



class MixedMediaBlock(blocks.StructBlock):

    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(**kwargs)
        self.min_width = kwargs.get('min_width', None)
        self.min_height = kwargs.get('min_height', None)

    image = ImageChooserBlock(required=False)
    video = EmbedBlock(
        label="Video URL",
        help_text="Paste the video URL from YouTube or Vimeo."
                  " e.g. https://www.youtube.com/watch?v=l3Pz_xQZVDg or https://vimeo.com/207076450.",
        required=False
    )
    caption = blocks.CharBlock(
        required=False,
        help_text="Adds a caption to the Video, or overrides any caption on the Image."
    )
    # This is called "photo_credit" so it will match the CaltechImage model, which is what our templates expect.
    photo_credit = blocks.CharBlock(
        label="Credit",
        required=False,
        help_text="Adds a credit to the Video, or overrides any credit on the Image."
    )


class MixedMediaCarouselBlock(blocks.StructBlock):

    items = blocks.ListBlock(
        MixedMediaBlock(),
        label="Media Assets"
    )

    class Meta:
        label = 'Mixed Media Carousel'
        template = 'mixed-media-carousel-block.html'
        form_classname = 'mixed-media-carousel-block struct-block'
        icon = 'image'


class HomePage(Page):
    
    body = StreamField([
        ('carousel', MixedMediaCarouselBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    api_fields = [
        APIField('body'),
    ]
