from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Image


class ImagePlugin(CMSPluginBase):
    model = Image
    render_template = 'plugins/image.html'

    def render(self, context, instance, placeholder):
        context['image'] = instance
        return context


plugin_pool.register_plugin(ImagePlugin)