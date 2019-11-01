from django.shortcuts import render, get_object_or_404
from mng.models import task,progress
from .form import taskForm, progressForm
from django.utils import timezone
from mng.functions import get_progress_degree
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
display_task_number = 4

def mypage(request):

    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            level = request.POST['level']
            overview = request.POST['overview']
            add_date = timezone.now()
            condition = 1
            t = task(name=name, level=level, overview=overview,
                     condition=condition, add_date=add_date)
            t.save()

    # 最近のタスク一覧を取得
    latest_tasks = task.objects.all().order_by("-id")[0:display_task_number]
    latest_dic = get_progress_degree(latest_tasks)

    # 未完了のタスク一覧を取得
    nocomplate_tasks = task.objects.filter(Q(condition=1) | Q(condition=2)).order_by("-id")[0:display_task_number]
    nocomplate_dic = get_progress_degree(nocomplate_tasks)

    # 完了したタスク一覧を取得
    complate_tasks = task.objects.filter(condition=3).order_by("-id")[0:display_task_number]
    complate_dic = get_progress_degree(complate_tasks)



    return render(request, 'mng/mypage.html',
                  {"latest_tasks": latest_tasks, "latest_dic": latest_dic,
                   "nocomplate_tasks": nocomplate_tasks, "nocomplate_dic": nocomplate_dic,
                   "complate_tasks": complate_tasks, "complate_dic": complate_dic}
                  )


def add(request):

    return render(request, 'mng/add.html')


def task_edit(request, task_id):

    if request.method == 'POST':

        form = progressForm(request.POST)
        if form.is_valid():
            t = task.objects.get(id=task_id)
            date = request.POST['date']
            pr = request.POST['progress']
            content = request.POST['content']

            p = progress(task=t, date=date, progress=pr, content=content)
            p.save()

    t = get_object_or_404(task, id=task_id)
    ps = progress.objects.filter(task=t)
    t_p = 0
    for p in ps:
        t_p = t_p + p.progress

    t_p_d = t_p / t.level * 100

    #状態を更新
    if t_p_d == 100.0:
        #完了状態
        t.condition = 3
        #終了日を更新
        p = progress.objects.filter(task=t).latest('date')
        t.end_date = p.date
    elif t_p_d > 0.0:
        #着手状態
        t.condition = 2
    else:
        #未着手
        t.condition = 1
    t.save()

    return render(request, 'mng/task_edit.html',
                  {"task": t, "progresses": ps, "progress": t_p_d})


def add_progress(request, task_id):

    t = get_object_or_404(task, id=task_id)
    ps = progress.objects.filter(task=t)
    current_level = 0
    for p in ps:
        current_level = current_level + p.progress

    return render(request, 'mng/add_progress.html',
                  {"task": t, "current_level":current_level})


def all_tasks(request):

    ts = task.objects.all()
    return render(request, 'mng/all_tasks.html', {"all_tasks": ts})


def testing(request):

    return render(request, 'mng/testing.html')


