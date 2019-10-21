from django.shortcuts import render, get_object_or_404
from mng.models import task,progress
from .form import taskForm, progressForm
from django.utils import timezone


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

    # タスク一覧を取得
    tasks = task.objects.all().order_by("-id")[0:display_task_number]

    dic = {}
    # タスクの進捗度を取得
    for t in tasks:
        progresses = progress.objects.filter(task=t)
        temp_progress = 0
        for p in progresses:
            temp_progress = temp_progress + p.level

        #進捗度を辞書に格納
        progress_d = temp_progress / t.level
        dic[t.id] = progress_d * 100
    return render(request, 'mng/mypage.html', {"tasks": tasks, "dic": dic})


def add(request):

    return render(request, 'mng/add.html')


def task_edit(request, task_id):

    if request.method == 'POST':
        form = progressForm(request.POST)
        if form.is_valid():
            t = task.ovjects.filter(id=task_id)
            date = request.POST['date']
            level = request.POST['progress']
            content = request.POST['content']

            p = progress(task=t, date=date, level=level, content=content)
            p.save()

    t = get_object_or_404(task,id=task_id)
    ps = progress.objects.filter(task=t)
    t_p = 0
    for p in ps:
        t_p = t_p + p.level

    t_p_d = t_p / t.level * 100

    #状態を更新
    if t_p_d > 0.0:
        #着手状態
        t.condition = 2
    elif t_p_d == 100.0:
        #完了状態
        t.condition = 3
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
        current_level = p.level

    return render(request, 'mng/add_progress.html',
                  {"task": t, "current_level":current_level})



