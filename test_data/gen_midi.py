# 安装依赖
# pip install midiutil

from midiutil import MIDIFile

# 创建MIDI对象
midi = MIDIFile(1)
track = 0
time = 0
midi.addTrackName(track, time, "Lyrical Piano")
midi.addTempo(track, time, 100)  # 中速

# 音高映射
note_map = {
    "C4": 60, "D4": 62, "E4": 64, "F4": 65, "G4": 67, "A4": 69, "B4": 71,
    "C5": 72, "D5": 74, "E5": 76, "F5": 77, "G5": 79, "A5": 81, "B5": 83
}

# 主旋律音符（四分音符为1拍）
melody = [
    "C5","C5","C5","B4","A4","B4","B4",
    "G4","G4","G4","A4","B4","A4","E4",
    "C5","C5","C5","E5","D5","E5","B4",
    "B4","C5","D5","D5","C5","A4"
]

durations = [1,1,1,0.5,0.5,1,1, 1,1,1,0.5,0.5,1,1, 1,1,1,0.5,0.5,1,1, 1,1,1,1,1,2]

# 添加旋律
channel = 0
volume = 90
time = 0
for note, dur in zip(melody, durations):
    midi.addNote(track, channel, note_map[note], time, dur, volume)
    time += dur

# 添加伴奏和弦（每4拍一个和弦）
chords = [
    ("C4","E4","G4"), ("A3","C4","E4"), ("F3","A3","C4"), ("G3","B3","D4"), ("A3","C4","E4"), ("F3","A3","C4")
]
chord_duration = 4
time = 0
for chord in chords:
    for note in chord:
        midi.addNote(track, 1, note_map[note.replace("3","4")]-12, time, chord_duration, 70)
    time += chord_duration

# 保存文件
with open("demo.mid", "wb") as f:
    midi.writeFile(f)

print("✅ 已生成文件：demo.mid")
