def scramble_string(s):
    n=len(s)
    mid=(n+1)//2
    return s[0:mid]+s[n:mid-1:-1]
# f.write(scramble_string("abcdefg"))

def sort_courses(course_list):
    return sorted(course_list,key=lambda x: x[1],reverse=True)
# courses = [('CS101', 50), ('MA202', 35), ('EE301', 45), ('PY451', 30)]
# sorted_courses = sort_courses(courses)
# f.write(sorted_courses)
    

def main():
    with open("results.txt", "w") as f:
        f.write("--- SCRABBLED STRING ---\n")
        f.write(scramble_string("AUTOMATION")+"\n")
        f.write("--- SORTED COURSES ---\n")
        f.write(str(sort_courses([('CS101', 50), ('MA202', 35), ('EE301', 45), ('PY451', 30)]))+"\n")
        f.write("--- SET OPERATIONS ---\n")
        # --- Part 1: Set Operations ---
        ai_club =  ["Priya", "Sameer", "Aditi", "Neha", "Rohan"]
        robotics_club =  ["Kunal", "Aditi", "Rohan", "Priya", "Vikram"]

        ai_club_s=set(ai_club)
        robotics_club_s=set(robotics_club)
        # 1.intersection
        both_clubs = ai_club_s & robotics_club_s

        # 2.union
        all_students = ai_club_s | robotics_club_s

        # 3.difference
        only_robotics = robotics_club_s - ai_club_s

        f.write("Intersection: "+str(both_clubs)+"\n")
        f.write("Union: "+str(all_students)+"\n")
        f.write("Difference: "+str(only_robotics)+"\n")


        # Part 2: Dictionary Creation 
        student_clubs = {}

        for student in robotics_club:
            student_clubs.setdefault(student, []).append("Robotics")

        for student in ai_club:
            student_clubs.setdefault(student, []).append("AI")
        # Sort each student's club list alphabetically
        for clubs in student_clubs.values():
            clubs.sort()
        f.write("--- STUDENT DICTIONARY ---\n")
        f.write(str(student_clubs))

if __name__=='__main__':
    main()