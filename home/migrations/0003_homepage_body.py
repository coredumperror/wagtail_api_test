# Generated by Django 4.1.8 on 2023-04-18 20:09

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('carousel', wagtail.blocks.StructBlock([('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='Paste the video URL from YouTube or Vimeo. e.g. https://www.youtube.com/watch?v=l3Pz_xQZVDg or https://vimeo.com/207076450.', label='Video URL', required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Adds a caption to the Video, or overrides any caption on the Image.', required=False)), ('photo_credit', wagtail.blocks.CharBlock(help_text='Adds a credit to the Video, or overrides any credit on the Image.', label='Credit', required=False))]), label='Media Assets'))])), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], default='', use_json_field=True),
            preserve_default=False,
        ),
    ]