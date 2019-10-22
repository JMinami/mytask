from mng.models import task, progress


def get_progress_degree(tasks):
    dic = {}
    for t in tasks:
        progresses = progress.objects.filter(task=t)
        temp_progress = 0
        for p in progresses:
            temp_progress = temp_progress + p.progress
        progress_d = temp_progress / t.level
        dic[t.id] = progress_d * 100

    return dic
