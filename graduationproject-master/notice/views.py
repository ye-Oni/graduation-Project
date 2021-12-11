from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Notice
from .form import NoticePost


def index(request):
    return render(request, 'recommend_index.html')


def detail(request, notice_id):
    details = get_object_or_404(Notice, pk=notice_id)  # 첫번째 인자는 어떤 클래스로부터 객체를 받을지, 두번째는 검색조건(pk)
    return render(request, 'notice_detail.html', {'details': details})


# new.html 띄워주는 함수
def new(request):
    return render(request, 'new.html')


# 입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    notice = Notice()
    notice.title = request.GET['title']
    notice.body = request.GET['body']
    notice.pub_date = timezone.datetime.now()
    notice.save()  # 쿼리셋 메소드 중 하나. 위의 객체를 데이터베이스에 저장해라. ex) 객체.delete : ~?
    return redirect('/notice/' + str(notice.id))


def noticepost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = NoticePost(request.POST)
        if form.is_valid():  # 잘 입력되었는지 확인
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('notice')

    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = NoticePost()
        return render(request, 'new.html', {'form': form})


def notice(request):
    notices = Notice.objects  # 쿼리셋
    # 블로그 모든 글들을 대상으로
    notice_list = Notice.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(notice_list, 7)
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해준다.
    posts = paginator.get_page(page)
    return render(request, 'notice.html', {'notices': notices, 'posts': posts})


def result(request):
    posts = Notice.objects.all()
    query = request.GET.get('query')
    if query:
        posts = posts.filter(title__icontains=query)
    return render(request, 'notice_result.html', {'posts': posts})