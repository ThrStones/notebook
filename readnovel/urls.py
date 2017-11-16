"""readnovel URL Configuration
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # novel list
    url(r'^novelList/$', views.novelList, name='novelList'),

    # chapter list
    url(r'^chapterList/(?P<novel_id>\d+)/$', views.chapterList, name='chapterList'),

    # chapter Detail
    url(r'^chapterDetails/(?P<novel_id>\d+)/(?P<serial_number>\d+)/(?P<flag>[-1，0，1]\d*)/$', views.chapterDetails, name='chapterDetails'),

    # new novels
    url(r'^add_novel/$', views.add_novel, name='add_novel'),

    # update novel
    url(r'^update_novel/(?P<novel_id>\d+)/$', views.update_novel, name='update_novel'),

    # update chapter
    url(r'^update_chapter/(?P<novel_id>\d+)/$', views.update_chapter, name='update_chapter'),
]
