from django.shortcuts import render, get_object_or_404
from .models import C_type
# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    test = C_type()
    #A유형
    if(request.POST.get('q2')=='2'):
        if(request.POST.get('q5')=='1'):
            if(request.POST.get('q8')=='1'):
                return render(request, 'result.html', {'title':'함께하는 여행은 내 삶의 일부', 'result':'함께하는 여행을 선호하시는군요! 다양한 액티비티가 있어 함께 놀 수 있는 가평은 어떠신가요?'})
            else:
                return render(request, 'result.html', {'title':'혼자하는 여행은 내 삶의 일부', 'result':'혼자하는 즉흥적인 여행을 선호하시는군요! 조용하지만 볼거리가 많은 단양은 어떠신가요?'})
    #B유형
    if(request.POST.get('q3')=='1'):
        if(request.POST.get('q5')=='1'):
            if(request.POST.get('q8')=='1'):
                if(request.POST.get('q2')=='1'):
                    return render(request, 'result.html', {'title':'즉흥적이지만 여행은 알차게', 'result':'전주에서 친구, 가족과 함께 핫플, 맛집 탐방과 인생샷을 남기기 위한 여행을 하는건 어떠신가요?'})
                else:
                    return render(request, 'result.html', {'title':'여행을 계획적으로 알차게', 'result':'계획을 세워 알차레 여행하는 것을 좋아하시는군요! 관광할 것이 많은 제주도는 어떠신가요?'})
    #C유형
    if(request.POST.get('q2')=='2'):
        if(request.POST.get('q3')=='1'):
            if(request.POST.get('q5')=='1'):
                return render(request, 'result.html', {'title':'여행은 또 다른 배움터', 'result':'조용한 곳에서 여행을 즐기며 새로운 걸 배우는 것을 좋아하시나요? 천년의 역사가 담긴 경주를 추천합니다!'})

    #D유형
    if(request.POST.get('q4')=='1'):
        if(request.POST.get('q7')=='1'):
            if(request.POST.get('q8')=='2'):
                return render(request, 'result.html', {'title':'조용한 힐링이 필요해', 'result':'이번 휴가엔 좋은 숙소에서 야경을 보며 혼자 힐링하는 것은 어떠신가요? 바다가 예쁜 속초를 추천합니다!'})
            else:
                return render(request, 'result.html', {'title':'함께하는 힐링이 필요해', 'result':'여수에서 밤바다를 보며 힐링하는건 어떠신가요? 새로운 인연을 만나게 될지도 몰라요!'})
    #E유형
    if(request.POST.get('q1')=='2'):
        if(request.POST.get('q4')=='1'):
            if(request.POST.get('q7')=='1'):
                if(request.POST.get('q5')=='1'):
                    return render(request, 'result.html', {'title':'좋은 풍경을 좋아하는 사람과 함께', 'result':'오션뷰가 멋있는 강릉에서 내가 좋아하는 사람과 함께 여행 하는건 어떠신가요?'})
                else:
                    return render(request, 'result.html', {'title':'좋은 볼거리을 좋아하는 사람과 함께', 'result':'볼거리와 맛집이 많은 서울에서 내가 좋아하는 사람과 호캉스를 하는건 어떠신가요?'})

    return render(request, 'result.html', {'title':'여행자의 파라다이스', 'result':'힐링, 액티비티, 멋진 뷰 모든걸 만족할 수 있는 다양한 여행지를 찾고계신가요? 여행자의 파라다이스 부산을 추천합니다!'})

