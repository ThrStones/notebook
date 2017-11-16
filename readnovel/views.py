import re
from urllib.request import urlopen

from bs4 import BeautifulSoup
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from readnovel.models import NovelInfo, Chapter


def index(request):
    """主页"""
    return render(request, 'readnovel/index.html')


def novelList(request):
    """view all novels"""
    novelList = NovelInfo.objects.order_by('-modifytime')
    context = {'novelList': novelList}
    return render(request, 'readnovel/novellist.html', context)


def chapterList(request, novel_id):
    """ Chapter List"""
    novelInfo = NovelInfo.objects.get(id=novel_id)
    chapterList = novelInfo.chapter_set.order_by('-serial_number')
    context = {'novelInfo': novelInfo, "chapterList": chapterList}
    return render(request, 'readnovel/chapterlist.html', context)


def chapterDetails(request, novel_id, serial_number, flag):
    """Chapter Details"""
    chapter_serial_number = int(serial_number) + int(flag)

    chapter = Chapter.objects.get(serial_number=chapter_serial_number, novelInfo_id=novel_id)

    if chapter.content is "":
        html = urlopen(chapter.novelInfo.website + chapter.href)
        bsObj = BeautifulSoup(html, "lxml")
        showtxt = bsObj.find("div", {"class": "showtxt"})

        chapter.content = showtxt.get_text('\n\n', 'br/')
        chapter.save()

    try:
        next_chapter_serial_number = int(chapter_serial_number) + int(1)
        next_chapter = Chapter.objects.get(serial_number=next_chapter_serial_number, novelInfo_id=novel_id)
        context = {'chapter': chapter, 'novelInfo': chapter.novelInfo, 'next_flag': 'true'}
    except:
        context = {'chapter': chapter, 'novelInfo': chapter.novelInfo, 'next_flag': 'false'}

    return render(request, 'readnovel/chapterdetails.html', context)


def add_novel(request):
    """add novel"""
    if request.POST:
        novelInfo = NovelInfo()
        novelInfo.website = request.POST['website']
        novelInfo.novelId = request.POST['novelId']
        saveNovelInfo(novelInfo)
        novelInfo.save()

    return HttpResponseRedirect(reverse('readnovel:novelList'))


def update_novel(request, novel_id):
    novelInfo = NovelInfo.objects.get(id=novel_id)
    saveNovelInfo(novelInfo)
    novelInfo.save()
    messages.success(request, '更新成功！')

    return HttpResponseRedirect(reverse('readnovel:novelList'))


def saveNovelInfo(novelInfo):
    html = urlopen(novelInfo.website + novelInfo.novelId)
    bsObj = BeautifulSoup(html, "lxml")
    novelInfo.name = bsObj.h2.get_text()
    cover = bsObj.find("div", {"class": "cover"})
    novelInfo.avatar = cover.find("img").attrs['src']
    small = bsObj.find("div", {"class": "small"})
    for child in small.children:
        label = child.get_text().split("：")[0]
        value = child.get_text().split("：")[1]
        if label == "作者":
            novelInfo.author = value
        elif label == "分类":
            novelInfo.category = value
        elif label == "状态":
            novelInfo.state = value
        elif label == "字数":
            novelInfo.words = value
        elif label == "更新时间":
            novelInfo.latest_updatetime = value
        elif label == "最新章节":
            novelInfo.latest_chapter = value
    intro = bsObj.find("div", {"class": "intro"})
    introArray = intro.get_text().split("：")
    novelInfo.intro = introArray[1].replace("\u3000", "")


def update_chapter(request, novel_id):
    novelInfo = NovelInfo.objects.get(id=novel_id)
    chapters = novelInfo.chapter_set.order_by('-createtime')

    html = urlopen(novelInfo.website + novelInfo.novelId)
    bsObj = BeautifulSoup(html, "lxml")

    chapterList = bsObj.findAll("a", {"href": re.compile(novelInfo.novelId + "\/-?[1-9]\d*\.html")})

    update_count = len(chapterList[13:]) - len(chapters)

    chapterListToDB = chapterList[-update_count:]

    if update_count > 0:
        for index in range(len(chapterListToDB)):
            chapter = Chapter()
            chapter.novelInfo = novelInfo
            chapter.href = chapterListToDB[index]['href']
            chapter.name = chapterListToDB[index].get_text()
            if len(chapters) == 0:
                chapter.serial_number = index
            else:
                chapter.serial_number = len(chapters) + int(index)
            chapter.save()
        messages.success(request, '更新成功！')
    else:
        messages.success(request, '没有新章节！')

    return HttpResponseRedirect(reverse('readnovel:novelList'))
