def __init__():
    lesson_name = input('What is the name of your lesson?: ')
    num_files = int(input('How many files are needed for this lesson? :))
    for num in range(num_files):
        f = open(lesson_name + '_' + num + '.py', a)
        f.close()
    print('Files Created, Good luck')
