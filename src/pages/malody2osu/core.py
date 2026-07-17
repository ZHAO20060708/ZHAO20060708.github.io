import os
import json
import zipfile
import shutil
import io
import traceback

def convert(i, bgtmp, soundtmp):
    try:
        with open(i, encoding='utf-8') as mc:
            mcFile = json.loads(mc.read())
    except:
        return 1

    if not mcFile['meta']['mode'] == 0:
        return 1

    ms = lambda beats, bpm, offset: 1000*(60/bpm)*beats+offset
    beat = lambda beat: beat[0] + beat[1]/beat[2]
    col = lambda column, keys: int(512*(2*column+1)/(2*keys))

    line = mcFile['time']
    meta = mcFile['meta']
    note = mcFile['note']
    
    soundnote = {}
    keys = meta["mode_ext"]["column"]
    for x in note:
        if x.get('type',0):
            soundnote = x

    bpm = [line[0]['bpm']]
    bpmoffset = [-soundnote.get('offset',0)]

    if len(line)>1:
        j=0
        lastbeat=line[0]['beat']
        for x in line[1:]:
            bpm.append(x['bpm'])
            bpmoffset.append(ms(beat(x['beat'])-beat(lastbeat),line[j]['bpm'],bpmoffset[j]))
            j+=1
            lastbeat=x['beat']

    title = meta["song"]["title"]
    artist = meta["song"]["artist"]
    preview = meta.get('preview',-1)
    titleorg = meta['song'].get('titleorg',title)
    artistorg = meta['song'].get('artistorg',artist)
    background = meta["background"]
    if not background=="": bgtmp.append(os.path.join(os.path.dirname(i), background))
    sound = soundnote.get("sound", "")
    if not sound=="": soundtmp.append(os.path.join(os.path.dirname(i), sound))
    creator = meta["creator"]
    version = meta["version"]

    with open(f'{os.path.splitext(i)[0]}.osu',mode='w',encoding='utf-8-sig') as osu:
        osuformat = ['osu file format v14','','[General]',f'AudioFilename: {sound}',
                     'AudioLeadIn: 0',f'PreviewTime: {preview}','Countdown: 0','SampleSet: Soft',
                     'StackLeniency: 0.7','Mode: 3','LetterboxInBreaks: 0','SpecialStyle: 0',
                     'WidescreenStoryboard: 0','','[Editor]','DistanceSpacing: 1.2','BeatDivisor: 4',
                     'GridSize: 8','TimelineZoom: 2.4','','[Metadata]',f'Title:{title}',
                     f'TitleUnicode:{titleorg}',f'Artist:{artist}',f'ArtistUnicode:{artistorg}',
                     f'Creator:{creator}',f'Version:{version}','Source:Malody','Tags:Malody Convert by Jakads Web',
                     'BeatmapID:0','BeatmapSetID:-1','','[Difficulty]','HPDrainRate:8',f'CircleSize:{keys}',
                     'OverallDifficulty:8','ApproachRate:5','SliderMultiplier:1.4','SliderTickRate:1','',
                     '[Events]','//Background and Video events',f'0,0,"{background}",0,0','','[TimingPoints]\n']
        osu.write('\n'.join(osuformat))

        bpmcount = len(bpm)
        for x in range(bpmcount):
            osu.write(f'{bpmoffset[x]},{60000/bpm[x]},{int(line[x].get("sign",4))},1,0,0,1,0\n')

        osu.write('\n\n[HitObjects]')

        for n in note:
            if not n.get('type',0) == 0: continue
            j, k = 0, 0
            for b in line:
                if beat(b['beat']) > beat(n['beat']): j+=1
                else: continue
            if not n.get('endbeat') == None:
                for b in line:
                    if beat(b['beat']) > beat(n['endbeat']): k+=1
                    else: continue
            j=bpmcount-j-1
            k=bpmcount-k-1

            if int(ms(beat(n["beat"]), bpm[j], bpmoffset[j])) >= 0:
                osu.write(f'\n{col(n["column"], keys)},192,{int(ms(beat(n["beat"])-beat(line[j]["beat"]), bpm[j], bpmoffset[j]))}')
                if n.get('endbeat') == None:
                    osu.write(',1,0,0:0:0:')
                else:
                    osu.write(f',128,0,{int(ms(beat(n["endbeat"])-beat(line[k]["beat"]), bpm[k], bpmoffset[k]))}:0:0:0:')
                if n.get('sound') == None:
                    osu.write('0:')
                else:
                    osu.write('{0}:{1}'.format(n['vol'],n['sound'].replace('"','')))
    return 0, title, artist

def process_file_bytes(file_bytes, original_filename):
    try:
        if hasattr(file_bytes, 'to_py'):
            file_bytes = bytes(file_bytes.to_py())
        else:
            file_bytes = bytes(file_bytes)
            
        work_dir = '/workspace'
        if os.path.exists(work_dir):
            shutil.rmtree(work_dir)
        os.makedirs(work_dir)
        
        zip_path = os.path.join(work_dir, original_filename)
        with open(zip_path, 'wb') as f:
            f.write(file_bytes)
        
        extract_dir = os.path.join(work_dir, 'extracted')
        os.makedirs(extract_dir)
        
        with zipfile.ZipFile(zip_path, 'r') as mcz:
            for zipinfo in mcz.infolist():
                if zipinfo.flag_bits & 0x800 == 0:
                    try:
                        raw_bytes = zipinfo.filename.encode('cp437')
                        for enc in ['utf-8', 'gbk', 'shift_jis', 'big5']:
                            try:
                                zipinfo.filename = raw_bytes.decode(enc)
                                break
                            except UnicodeDecodeError: pass
                    except: pass
                mcz.extract(zipinfo, extract_dir)
                
        bgtmp = []
        soundtmp = []
        mc_files = []
        mctitle = "Unknown"
        mcartist = "Unknown"
        
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                if file.endswith('.mc'):
                    full_path = os.path.join(root, file)
                    res = convert(full_path, bgtmp, soundtmp)
                    if type(res) is tuple:
                        mctitle = res[1]
                        mcartist = res[2]
                        mc_files.append(full_path)
                        
        if not mc_files:
            return "ERROR", "压缩包内没有找到支持的 .mc 谱面文件", b""
            
        osz_name = f"{mcartist} - {mctitle}.osz"
        osz_path = os.path.join(work_dir, osz_name)
        
        with zipfile.ZipFile(osz_path, 'w') as osz:
            for mc in mc_files:
                osu_file = os.path.splitext(mc)[0] + '.osu'
                osz.write(osu_file, os.path.basename(osu_file))
            for bg in set(bgtmp):
                if os.path.exists(bg): osz.write(bg, os.path.basename(bg))
            for snd in set(soundtmp):
                if os.path.exists(snd): osz.write(snd, os.path.basename(snd))
                
        with open(osz_path, 'rb') as f:
            final_bytes = f.read()
            
        return "SUCCESS", osz_name, final_bytes
    except Exception as e:
        return "ERROR", str(traceback.format_exc()), b""
