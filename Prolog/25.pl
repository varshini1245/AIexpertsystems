% Knowledge Base
student(john, math).
student(lisa, biology).
student(mike, history).

teacher(mr_smith, math).
teacher(mrs_jones, biology).
teacher(mr_doe, history).

subject(math, 'MTH101').
subject(biology, 'BIO202').
subject(history, 'HIS303').

% Generate questions
generate_question(Question) :-
    random_student(Student),
    random_teacher(Teacher),
    random_subject(Subject),
    format(atom(Question), 'Which student studies ~w with teacher ~w for subject ~w?', [Student, Teacher, Subject]).

% Rules to get random student, teacher, and subject
random_student(Student) :-
    findall(S, student(S, _), Students),
    random_member(Student, Students).

random_teacher(Teacher) :-
    findall(T, teacher(T, _), Teachers),
    random_member(Teacher, Teachers).

random_subject(Subject) :-
    findall(Sub, subject(Sub, _), Subjects),
    random_member(Subject, Subjects).
