d={
    "student1":{
    "name":"sarath",
      "age":23,
      "marks":{
          "english":70,
          "maths":69,
      }
    },
    "student2":{
    "name":"abey",
      "age":23,
      "marks":{
        "english":70,
        "maths":69,
    }
    #concatination of dictionary
}
}
d["student2"]="studenttwo"#changing the dictionary
d["student1"]="ssss"
print(d.get('student1'))
#or
print(d['student2'])