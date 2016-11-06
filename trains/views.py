#coding=utf-8
from django.shortcuts import render,HttpResponse
import random
import json
# Create your views here.

def trains_search(request):
    if request.method == "POST":
        checi = request.POST["checiIn"].encode("utf-8")
        # label = "+checi+"
        res_dict = {
            "status": True,
            "message":["Test success!"],
            "trains":checi,
            "data":{
                                "labels": ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"],
                                "datasets": [
                                    {
                                        "label": "列车"+checi+"晚点情况",
                                        "fill": False,
                                        "lineTension": 0.1,
                                        "backgroundColor": "rgba(75,192,192,0.4)",
                                        "borderColor": "rgba(75,192,192,1)",
                                        "borderCapStyle": 'butt',
                                        "borderDash": [],
                                        "borderDashOffset": 0.0,
                                        "borderJoinStyle": 'miter',
                                        "pointBorderColor": "rgba(75,192,192,1)",
                                        "pointBackgroundColor": "#fff",
                                        "pointBorderWidth": 1,
                                        "pointBorderWidth": 1,
                                        "pointHoverRadius": 4,
                                        "pointHoverBackgroundColor": "rgba(75,192,192,1)",
                                        "pointHoverBorderColor": "rgba(220,220,220,1)",
                                        "pointHoverBorderWidth": 2,
                                        "pointRadius": 8,
                                        "pointHitRadius": 10,
                                        "data": [random.randint(29,60),
                                                  random.randint(29,60),
                                                  random.randint(29,60),
                                                  random.randint(29,60),
                                                  random.randint(29,60),
                                                  random.randint(29,60),
                                                  random.randint(29,60)],
                                        "spanGaps": False,
                                    }
                                ]
                            }
        }
        return HttpResponse(json.dumps(res_dict))
    return render(request, 'search.html')