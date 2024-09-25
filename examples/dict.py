# json_data = {
#     "glossary": {
#         "title": "example glossary",
# 		"GlossDiv": {
#             "title": "S",
# 			"GlossList": {
#                 "GlossEntry": {
#                     "ID": "SGML",
# 					"SortAs": "SGML",
# 					"GlossTerm": "Standard Generalized Markup Language",
# 					"Acronym": "SGML",
# 					"Abbrev": "ISO 8879:1986",
# 					"GlossDef": {
#                         "para": "A meta-markup language, used to create markup languages such as DocBook.",
# 						"GlossSeeAlso": ["GML", "XML"]
#                     },
# 					"GlossSee": "markup"
#                 }
#             }
#         }
#     }
# }

# print(json_data["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["GlossDef"]["GlossSeeAlso"][1])





students_grades = [
    {"name": "Alice", "marks": [{"social": 80, "maths": 60, "science": 20, "tamil": 99, "english": 66}]},
    {"name": "Bob", "marks": [{"social": 70, "maths": 65, "science": 75, "tamil": 85, "english": 78}]},
    {"name": "Charlie", "marks": [{"social": 90, "maths": 85, "science": 95, "tamil": 88, "english": 92}]},
    {"name": "Diana", "marks": [{"social": 82, "maths": 79, "science": 85, "tamil": 90, "english": 87}]},
    {"name": "Eve", "marks": [{"social": 88, "maths": 90, "science": 92, "tamil": 94, "english": 89}]},
    {"name": "Frank", "marks": [{"social": 75, "maths": 80, "science": 23, "tamil": 60, "english": 65}]},
    {"name": "Grace", "marks": [{"social": 95, "maths": 90, "science": 85, "tamil": 80, "english": 88}]},
    {"name": "Hank", "marks": [{"social": 60, "maths": 70, "science": 65, "tamil": 75, "english": 70}]},
    {"name": "Ivy", "marks": [{"social": 85, "maths": 15, "science": 80, "tamil": 85, "english": 82}]},
    {"name": "Jack", "marks": [{"social": 78, "maths": 85, "science": 88, "tamil": 90, "english": 84}]}
]

print(students_grades[0]["marks"][0]["tamil"])