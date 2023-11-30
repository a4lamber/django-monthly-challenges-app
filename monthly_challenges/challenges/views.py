from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# 创造你的视图, 你的视图是一个python函数, 它接受一个请求对象作为参数, 并返回一个响应对象
# dynamic path segments, month对应着<month>

monthly_challenges = {
    "january": "don's skip leg days",
    "february": "walk for at least 20 mins every day!",
    "march": "try a new type of exercise each week",
    "april": "practice mindfulness meditation for 10 minutes daily",
    "may": "drink at least 8 glasses of water every day",
    "june": "cut out processed foods from your diet",
    "july": "get at least 7 hours of sleep every night",
    "august": "take the stairs instead of the elevator whenever possible",
    "september": "learn a new skill or hobby",
    "october": "eat a serving of fruits and vegetables with every meal",
    "november": "do a daily act of kindness for others",
    "december": None,
}


def index(request):
    """_summary_
    index page for localhost/challenges/, 创建一个
    - Janurary
    - Feburary
    - March
    ...
    - December

    :param _type_ request: _description_
    :return _type_: _description_
    """

    return render(
        request=request,
        template_name="challenges/index.html",
        context={
            "monthly_challenges": monthly_challenges,
        },
    )


def monthly_challenge_by_number(request, month):
    """
    处理redirection, 解决如何redirect 如下URL:
    From: localhost:8000/challenges/1

    To: localhost:8000/challenges/january

    :param _type_ request: _description_
    :param _type_ month: _description_
    :return _type_: _description_
    """
    # python获得ordered keys
    months = list(monthly_challenges.keys())
    # 判定month是否在1-12之间
    if month > len(months):
        return HttpResponseNotFound("invalid month")

    # shift by 1. 月份1 - 12,对应的index from 0 - 11
    redirect_month = months[month - 1]

    # 用reverse()来动态的定义path
    redirect_path = reverse("month-challenges", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    """
    sending back http response, 可以传输的格式有:
    - string
    - html

    :param _type_ request: _description_
    :param _type_ month: _description_
    :return _type_: _description_
    """
    try:
        # extract string
        challenge_text = monthly_challenges[month]
        # grab the template html and convert it to string
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

        return render(
            request=request,
            template_name="challenges/challenge.html",
            context={
                "text": challenge_text,
                "month": month,
            },
        )
    except Exception as e:
        # automatically look for templates/404.html
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
