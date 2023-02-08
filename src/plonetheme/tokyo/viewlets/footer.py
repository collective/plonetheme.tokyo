# -*- coding: utf-8 -*-

from datetime import date
from plone.app.layout.viewlets import ViewletBase


class Footer(ViewletBase):
    """
    Footer Viewlet
    """

    def update(self):
        self.year = self.get_year()

    def get_year(self):
        year = date.today().year
        return year

    def index(self):
        return super(Footer, self).render()
