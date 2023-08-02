# L207-Course_Schedule


def can_finish(numCourses, prerequisites):
    adj_list, in_degrees = {}, {}

    for course, prereq in prerequisites:
        if prereq not in adj_list:
            adj_list[prereq] = [course]
        else:
            adj_list[prereq].append(course)
        in_degrees[course] = in_degrees.get(course, 0) + 1

    course_queue = []
    courses_taken = set()
    for course in range(numCourses):
        if course not in in_degrees:
            course_queue.append(course)
            courses_taken.add(course)

    while course_queue:
        new_course_queue = []
        for course in course_queue:
            if course in adj_list:
                for next_course in adj_list[course]:
                    in_degrees[next_course] -= 1
                    if in_degrees[next_course] == 0:
                        new_course_queue.append(next_course)
                        courses_taken.add(next_course)
        course_queue = new_course_queue

    return len(courses_taken) == numCourses


print(can_finish(2, [[1, 0]]))


# 0 to numCourses-1 courses you must take
# prereq list is [x,y] where y is the prereq
