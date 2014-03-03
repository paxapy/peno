# coding=utf-8
from django.core.urlresolvers import reverse

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class PollToolbar(CMSToolbar):
    def populate(self):
        if self.is_current_app:
            menu = self.toolbar.get_or_create_menu('news', u'Новости')
            url = reverse('admin:app_post_changelist')
            menu.add_sideframe_item(u'Добавить новости', url=url)


class PostApp(CMSApp):
    name = u'Новости'
    urls = ['app.urls']


apphook_pool.register(PostApp)