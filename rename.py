# Эта утилита предназначена для автоматического удаления из названий файлов и папок, лежащих в некоторой корневой,
# повторяющейся части. Например, в папке "[s1.eground.org] PHP.Laravel.Ч1" лежат файлы, названия многих из которых
# (а может даже и всех) также начинаются с шаблона "[s1.eground.org] " (или содержат его в себе в качестве подстроки,
# в начале, середине или конце). После запуска данной программы из названия папки и всех таких файлов будет удалена
# подстрока "[s1.eground.org] " (подстрока для удаления и корневая папка задаются в начале программы).

import os
import time


# Включать ли режим DEBUG
# в режиме отладки все реальные переименования файлов/папок осуществляться не будут, вместо этого будет
#  иметь место простой вывод в консоль измененных имен файлов/папок
DEBUG = False

# В следующей переменной задаем подлежащий удалению шаблон, например f"[s1.eground.org] "
tmPlate = f"[s1.eground.org] "

# в следующей переменной задаем корневую папку, с которой начинается обработка всех вложенных в нее подпапок и файлов
# например f"D:\\Downloads\\PHP.Laravel.Ч6\\15 - Create Scroll To Top"
# rootdir = os.path.dirname(__file__)
rootdir = f"D:\\Downloads\\PHP.Laravel.Ч6"

os.chdir(rootdir)
StartTime = time.time()
for (p, d, f) in os.walk(rootdir, False):
    for curF in f:
        if tmPlate in curF:
            newF = curF.replace(tmPlate, "")
            if DEBUG:
                print(curF)
                # вывод теста зеленым ярким цветом с помощью esc-последовательностей
                print(f'\033[1;32;40m{newF}\033[0m')
            else:
                os.rename(os.path.join(p, curF), os.path.join(p, newF))
    if DEBUG:
        print("End_________________" + p)
    for curDir in d:
        if tmPlate in curDir:
            newDir = curDir.replace(tmPlate, "")
            if DEBUG:
                print(curDir)
                # вывод теста синим ярким цветом с помощью esc-последовательностей
                print(f'\033[1;34;40m{newDir}\033[0m')
            else:
                os.rename(curDir, newDir)
    if DEBUG:
        print("End_________________" + p)

if tmPlate in rootdir:
    newRootDir = rootdir.replace(tmPlate, "")
    #print(newRootDir)
    os.chdir(os.pardir)
    os.rename(rootdir, newRootDir)

print("Скрипт выполнен за %d секунд." % (time.time() - StartTime))