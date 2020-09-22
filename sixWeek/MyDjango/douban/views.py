from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here
from .models import T1
from django.db.models import Avg


def books_short(request):
    ### 从models取数据传给template，models中的数据可能依据存在
    shorts = T1.objects.all()

    # 评论数量
    counter = shorts.count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = f"{T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f}"  # 查看高级文档，返回的是一个字典，默认key是“字段_avg”
    # 情感分析
    sent_avg = f"{T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"

    # 正向数量
    queryset = T1.objects.values('sentiment')
    condition = {'sentiment__gte': 0.5}  # table中字段 + 比较符：greate than or equal
    plus = queryset.filter(**condition).count()

    # 逆向数量
    queryset = T1.objects.values('sentiment')
    condition = {'sentiment__lt': 0.5}  # less than
    minus = queryset.filter(**condition).count()

    return render(request, 'result.html', locals())
