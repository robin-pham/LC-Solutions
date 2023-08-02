# L210-Course_Schedule_2


def findOrder(numCourses, prerequisites):
    adj_list, in_degrees, course_queue, course_order = {}, {}, [], []
    for course, prereq in prerequisites:
        if prereq not in adj_list:
            adj_list[prereq] = [course]
        else:
            adj_list[prereq].append(course)
        in_degrees[course] = in_degrees.get(course, 0) + 1

    for course in range(numCourses):
        if course not in in_degrees:
            course_queue.append(course)
            course_order.append(course)

    while course_queue:
        new_queue = []
        for course in course_queue:
            if course in adj_list:
                for next_course in adj_list[course]:
                    in_degrees[next_course] -= 1
                    if in_degrees[next_course] == 0:
                        new_queue.append(next_course)
                        course_order.append(next_course)

        course_queue = new_queue

    return course_order if len(course_order) == numCourses else []


print(findOrder(1, []))
