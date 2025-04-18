# Read the data from the files
with open("cs.txt", "r") as cs_file:
    cs_majors = set(cs_file.read().splitlines())

with open("math.txt", "r") as math_file:
    math_majors = set(math_file.read().splitlines())

student_year = {}
with open("studentYear.txt", "r") as year_file:
    for line in year_file:
        name, year = line.strip().split()
        student_year[name] = int(year)
# a. Find all sophomore level CS majors
sophomore_cs = {name for name in cs_majors if student_year.get(name) == 2}
print("a. Sophomore CS majors:", sophomore_cs)

# b. Find all Freshmen who are not majoring in math or CS
freshmen_not_math_cs = {name for name, year in student_year.items() if year == 1 and name not in cs_majors and name not in math_majors}
print("b. Freshmen not majoring in math or CS:", freshmen_not_math_cs)

# c. Find all the Senior Math and CS majors
senior_math_cs = {name for name in math_majors.union(cs_majors) if student_year.get(name) == 4}
print("c. Senior Math and CS majors:", senior_math_cs)


