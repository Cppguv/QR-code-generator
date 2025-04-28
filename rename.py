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
tmPlate = f"[Boominfo.ORG] "

# в следующей переменной задаем корневую папку, с которой начинается обработка всех вложенных в нее подпапок и файлов
# например f"D:\\Downloads\\PHP.Laravel.Ч6\\15 - Create Scroll To Top"
# rootdir = os.path.dirname(__file__)
rootdir = f"D:\\Downloads\\Архивы курсов\\Skillbox Дизайнер сайтов на Tilda (2020)"

# список названий файлов (может быть пустым), которые мы хотим удалить из каждой просматриваемой папки
listfilestoremove = (
    'Открой сокровищницу.url',
    'Рабочий Адрес сайта.url',
    'Курсы от Skillbox ЗДЕСЬ - skillbox.shop.url',
    'Информация.pdf',
)

os.chdir(rootdir)
StartTime = time.time()
# p - текущий обрабатываемый каталог, начинаем с самого нижнего каталога и затем вверх к rootdir, так как в следующей
# функции os.walk указан параметр False
# f - список всех файлов в текущей директории p
# d - список всех директорий в текущем обрабатываемом каталоге p
for (p, d, f) in os.walk(rootdir, False):
    for curF in f:
        if curF in listfilestoremove:
            os.remove(os.path.join(p, curF))
        if tmPlate in curF:
            newF = curF.replace(tmPlate, "")
            if DEBUG:
                print(curF)
                # вывод теста зеленым ярким цветом с помощью esc-последовательностей
                print(f'\033[1;32;40m{newF}\033[0m')
            else:
                try:
                    if not os.path.exists(os.path.join(p, newF)):
                        os.rename(os.path.join(p, curF), os.path.join(p, newF))
                    else:
                        print(f'Не могу переименовать, такой файл {newF} уже существует!')
                except OSError as e:
                    print(f"Ошибка при попытке переименовать файл {curF}: {e}")
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
                try:
                    if not os.path.exists(os.path.dirname(newDir)):
                        os.rename(os.path.join(p, curDir), os.path.join(p, newDir))
                    else:
                        print(f'Не могу переименовать, такой каталог {newDir} уже существует!')
                except OSError as e:
                    print(f"Ошибка при попытке переименовать каталог {curDir}: {e}")
    if DEBUG:
        print("End______" + p)

if tmPlate in rootdir:
    newRootDir = rootdir.replace(tmPlate, "")
    os.chdir(os.pardir)
    try:
        if not os.path.exists(newRootDir):
            os.rename(rootdir, newRootDir)
        else:
            print(f'Не могу переименовать корневой каталог, уже есть директория с таким названием!')
    except OSError as e:
        print(f"Ошибка при попытке переименовать корневой каталог: {e}")

print("Скрипт выполнен за %d секунд." % (time.time() - StartTime))