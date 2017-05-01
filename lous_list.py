# Christopher Geier (cpg3rb)
import urllib.request


def instructors(department):
    instructors_list = []
    classes = urllib.request.urlopen(url='http://cs1110.cs.virginia.edu/files/louslist/' + department).read().decode('utf-8').split('\n')
    for cls in classes:
        cls = cls.split('|')
        if department == cls[0]:
            instructor = cls[4].strip('+4+1+2+3')
            if instructor not in instructors_list:
                instructors_list.append(instructor)
    return sorted(instructors_list)


def level_check(level, cls):
    if level is None:
        return True
    else:
        return str(cls[1])[0] == str(level)[0]


def seats(has_seats_available,cls):
    if has_seats_available:
        return cls[15] < cls[16]
    else:
        return True


def time_before(not_before,cls):
    start = int(cls[12])
    if not_before is None:
        return True
    else:
        return start >= not_before


def time_after(not_after,cls):
    start = int(cls[12])
    if not_after is None:
        return True
    else:
        return start <= not_after


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    classes = urllib.request.urlopen(url='http://cs1110.cs.virginia.edu/files/louslist/' + dept_name).read().decode('utf-8').split('\n')
    matched_classes = []
    for cls in classes:
        cls = cls.split('|')
        if len(cls) > 1:
            if seats(has_seats_available, cls) and time_before(not_before, cls) and time_after(not_after, cls) and level_check(level, cls):
                matched_classes.append(cls)
    return matched_classes
