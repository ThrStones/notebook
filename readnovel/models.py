from django.db import models


# Create your models here.

class BaseInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'名称')
    createtime = models.DateTimeField(auto_now_add=True, verbose_name=u'数据创建时间')
    modifytime = models.DateTimeField(auto_now=True, verbose_name=u'数据最后修改时间')
    remark = models.TextField(verbose_name=u'备注')

    class Meta:
        abstract = True  # 声明为抽象基类

    def __str__(self):
        """ 返回模型的字符串表示 """
        return self.name


class NovelInfo(BaseInfo):
    """ 小说简要信息 """
    avatar = models.CharField(max_length=200, verbose_name=u'小说图片链接')
    author = models.CharField(max_length=20, verbose_name=u'小说作者')
    category = models.CharField(max_length=20, verbose_name=u'小说分类')
    state = models.CharField(max_length=10, verbose_name=u'更新状态')
    words = models.IntegerField(verbose_name=u'字数')
    latest_updatetime = models.CharField(max_length=20, verbose_name=u'最后更新时间')
    latest_chapter = models.CharField(max_length=200, verbose_name=u'最新章节名')
    website = models.CharField(max_length=200, verbose_name=u'小说网站')
    novelId = models.CharField(max_length=200, verbose_name=u'小说ID')
    intro = models.TextField(verbose_name=u'小说简介')
    # user = models.ForeignKey(User, verbose_name=u'所属用户')

    class Meta:
        verbose_name = 'Novel'
        verbose_name_plural = 'Novels'


class Chapter(BaseInfo):
    """ 小说章节信息 """
    href = models.CharField(max_length=200, verbose_name=u'小说具体链接')
    content = models.TextField(verbose_name=u'章节具体内容')
    serial_number = models.IntegerField(verbose_name=u'章节序号')
    novelInfo = models.ForeignKey(NovelInfo, verbose_name=u'所属小说')

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'
