from teacher import Teacher
from student import Student

#client

def main():
    teacher = Teacher('Sam', 'Data Analytics')
    teacher_clone = teacher.clone()
    teacher_clone.display()

if __name__ == '__main__':
    main()