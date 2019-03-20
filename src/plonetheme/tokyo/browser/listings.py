# -*- coding: utf-8 -*-

from Products.Five import BrowserView


class ListingBase(BrowserView):

    def get_items(self):
        return self.context.getFolderContents(self.config, full_objects=True)


class ListingNewsView(ListingBase):

    config = {
        'sort_order': 'reverse',
        'sort_on': 'Date',
        'portal_type': 'News Item',
    }
