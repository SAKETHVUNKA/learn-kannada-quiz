import time

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from gtts import gTTS
from pathlib import Path
from .tr_mod import translate
from .q_gen import questionset
from time import time

name = "NONE"
qno = 0
score = 0
ans = ''
res = () 
audio_urls = []
highscores = {'Noob': 0, 'Pro': 0, 'Gamer': 0, 'Ninja': 0, 'Legend': 0}


def generate_audio(text, index):
    audio_dir = Path(settings.BASE_DIR) / "static" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    # Create unique filename using timestamp
    timestamp = int(time())
    file_name = f"option{index}_{timestamp}.mp3"
    file_path = audio_dir / file_name

    # Save new audio
    tts = gTTS(text=text, lang='kn')
    tts.save(str(file_path))

    return f"/static/audio/{file_name}"

def clear_all_audio_files():
    audio_root = Path(settings.BASE_DIR) / "static" / "audio"

    if audio_root.exists() and audio_root.is_dir():
        for item in audio_root.iterdir():
            if item.is_file():
                item.unlink()  # delete file
            elif item.is_dir():
                # Delete all files in subfolder
                for sub_item in item.glob("**/*"):
                    if sub_item.is_file():
                        sub_item.unlink()
                # Finally remove the empty subfolder
                item.rmdir()

def start(request):
    global score
    score = 0
    return render(request, "start.html")


# def home_submit(request):
#     global name
#     name = request.GET.get('name')
#     print(name)
#     # return HttpResponse("Success")
#     return render(request, "quest.html")


def quest(request):
    name_l = request.GET.get('name', 'None')
    if name_l != 'None':
        global name
        name = name_l
        print(name)
    global res
    res = questionset()
    global ans
    ans = str(res[2].index(res[1].text))
    global audio_urls
    clear_all_audio_files()
    for idx, opt in enumerate(res[2]):
        url = generate_audio(opt, idx)
        audio_urls.append(url)
    params = {'question': res[0], 'o0': res[2][0], 'o1': res[2][1], 'o2': res[2][2], 'o3': res[2][3], 'audio0': audio_urls[0], 'audio1': audio_urls[1], 'audio2': audio_urls[2], 'audio3': audio_urls[3], 'score': score}
    return render(request, "quest.html", params)


def answer(request):
    global score
    params = {'question': res[0], 'o0': res[2][0], 'o1': res[2][1], 'o2': res[2][2], 'o3': res[2][3], 'audio0': audio_urls[0], 'audio1': audio_urls[1], 'audio2': audio_urls[2], 'audio3': audio_urls[3], 'score': score}
    user_ans = request.GET.get('choice', '0')
    if user_ans == ans:
        score += 1
        params[f"o{ans}"] = params[f"o{ans}"] + "✅"
        params['score'] = score
    else:
        params[f"o{ans}"] = params[f"o{ans}"] + "✅"
        params[f"o{user_ans}"] = params[f"o{user_ans}"] + "❌"
    return render(request, "answer.html", params)


def results(request):
    # ans = request.GET.get('choice', 'None')
    global qno
    qno += 1
    # print(ans)
    if qno < 5:
        global res
        res = questionset()
        global ans
        ans = str(res[2].index(res[1].text))
        global audio_urls
        clear_all_audio_files()
        audio_urls = []
        for idx, opt in enumerate(res[2]):
            url = generate_audio(opt, idx)
            audio_urls.append(url)
        params = {'question': res[0], 'o0': res[2][0], 'o1': res[2][1], 'o2': res[2][2], 'o3': res[2][3], 'audio0': audio_urls[0], 'audio1': audio_urls[1], 'audio2': audio_urls[2], 'audio3': audio_urls[3], 'score': score}
        return render(request, "quest.html", params)
    else:
        qno = 0
        global highscores
        if name in highscores:
            if score > highscores[name]:
                highscores[name] = score
        else:
            highscores[name] = score
        return render(request, "results.html", {'score': score, 'name': name})


def high_score(request):
    h_lst = [[k, v] for k, v in highscores.items()]
    h_lst.sort(key=lambda x: x[1], reverse=True)
    params = {'n1': h_lst[0][0], 's1': h_lst[0][1], 'n2': h_lst[1][0], 's2': h_lst[1][1], 'n3': h_lst[2][0],
              's3': h_lst[2][1], 'n4': h_lst[3][0], 's4': h_lst[3][1], 'n5': h_lst[4][0], 's5': h_lst[4][1]}
    return render(request, "high_score.html", params)


def end(request):
    return render(request, "start.html")