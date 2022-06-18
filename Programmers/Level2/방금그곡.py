def solution(m, musicinfos):
    answers = []
    m_list = []
    new_music_infos = []

    for i in range(len(m) - 1):
        if m[i+1] == '#':
            m_list.append(m[i] + '#')
        elif m[i] == '#':
            if i+1 == len(m) - 1:
                m_list.append(m[i+1])
            else:
                continue
        elif m[i+1] != '#' and i+1 == len(m) - 1:
            m_list.append(m[i])
            m_list.append(m[i+1])
        else:
            m_list.append(m[i])

    for n in range(len(musicinfos)):
        musicinfo = musicinfos[n].split(',')
        music_sheet = []
        total_music = []

        hour1, hour2 = musicinfo[0][0:2], musicinfo[1][0:2]
        min1, min2 = musicinfo[0][3:], musicinfo[1][3:]
        play_hour, play_minute = int(hour2) - int(hour1), int(min2) - int(min1)

        if play_minute < 0:
            play_hour -= 1
            play_minute += 60
        for h in range(play_hour):
            play_minute += 60

        for i in range(len(musicinfo[3]) - 1):
            if musicinfo[3][i+1] == '#':
                music_sheet.append(musicinfo[3][i] + '#')
            elif musicinfo[3][i] == '#':
                if i+1 == len(musicinfo[3]) - 1:
                    music_sheet.append(musicinfo[3][i+1])
                else:
                    continue
            elif musicinfo[3][i+1] != '#' and i+1 == len(musicinfo[3]) - 1:
                music_sheet.append(musicinfo[3][i])
                music_sheet.append(musicinfo[3][i+1])
            else:
                music_sheet.append(musicinfo[3][i])

        repeat_count = play_minute // len(music_sheet)
        repeat_remain = play_minute % len(music_sheet)

        for i in range(repeat_count):
            total_music += music_sheet

        for i in range(repeat_remain):
            total_music.append(music_sheet[i])

        new_music_infos.append([musicinfo[2], total_music, play_minute, n])

    for i in range(len(new_music_infos)):
        tmp_list = []
        index = 0
        for j in range(len(new_music_infos[i][1])):
            if index >= len(m_list):
                break
            if m_list[index] == new_music_infos[i][1][j]:
                tmp_list.append(m_list[index])
                index += 1
            else:
                tmp_list.clear()
                index = 0
                if m_list[index] == new_music_infos[i][1][j]:
                    tmp_list.append(m_list[index])
                    index += 1

        if m_list == tmp_list:
            answers.append(
                [new_music_infos[i][0], new_music_infos[i][2], new_music_infos[i][3]])

    if len(answers) == 0:
        return "(None)"
    else:
        answers.sort(key=lambda x: (-x[1], x[2]))
        return answers[0][0]
