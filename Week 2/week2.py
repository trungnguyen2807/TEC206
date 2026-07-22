# def print_details(name, age, country='Viet Nam'):
#   print(f"My name is {name}, I am {age} years old, and I live in {country}")

# print_details('Nguyen', age = '19')

# def count_occurrences(*lists):
#   freq = {}
#   for i in lists:
#     if i not in freq: freq[i] = 1
#     else: freq[i] += 1
#   return freq

# print(count_occurrences(1,2,4,5,6,7,4,2,2,4,5,6,7,8,3,4,5,6,7,1))

# def analyze_kwargs(a, **kwargs):
#   print("Type of kwargs:", type(kwargs))
#   print("Keyword arguments:", kwargs)
#   print("Value of 'example_kwarg':", kwargs.get('example_kwarg'))
#   print(a)
# analyze_kwargs(42, first_arg='Hello')

# def query_database(query, *filters, **options):
#   print(f"Running query: {query}")
#   print("Applying filters:")
#   for filter in filters:
#     print(f"- {filter}")
#   print("Options:")
#   for key, value in options.items():
#     print(f"- {key}: {value}")
# query_database("SELECT * FROM users", "Active Users", "Age > 30", limit=10, sort_by="name")

# def calculate_average(*lists):
#   return sum(lists) / len(lists)
# print(calculate_average(1,2,5,6,7,8,9,5,4,3,2,4,5,6,7,8,9))

# data = {'num1': 3, 'num2': 6, 'num3': 9}
# def calculate_total(num3, num2, num1):
#   print(num1 + num2 + num3)
# calculate_total(**data)
# def createTask(title, status, notes=None):
#   if notes is None:
#     notes = []
#   return {
#   'title': title,
#   'status': status,
#   'notes': notes
# }
# task1 = createTask('Task 1', 'Incomplete')
# task2 = createTask('Task 2', 'Complete')
# def addNote(task, note):
#   task['notes'].append(note)
#   print(task['notes'])
# addNote(task1, 'Note 1')
# addNote(task2, 'Note 2')
# Function with a mutable default argument
def create_student(name, age, grades=[]):
  student = {
  'name': name,
  'age': age,
  'grades': grades
  }
  return student
# Create two students using the create_student function
student1 = create_student('John', 18)
student2 = create_student('Alice', 19)
# Add grades to the students
student1['grades'].append(80)
student2['grades'].append(90)
# Print the students' details
print("Student 1:", student1)
print("Student 2:", student2)
