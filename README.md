# String API

### GET REQUEST FOR GET ALL STRING  || BASE_URL +"/string/" || http://127.0.0.1:8000/string/ || return all saved string

### POST REQUEST TO ADD NEW STRING || BASE_URL +/string/ || http://127.0.0.1:8000/string/  || return created String Id
##### post request example : { "name": "How are you?" }


### POST REQUEST TO PERFORM OPERATION ON STRING  || BASE_URL + "/operation/" || http://127.0.0.1:8000/operation/ 
##### post request example : {"id":7, "operation" : "reverse" }
##### post request example : {"id":7, "operation" : "reverse_word" }
##### post request example : {"id":7, "operation" : "flip_break" }
##### post request example : {"id":7, "operation" : "sort_char" }


### TO KNOW ALL OPERATION PERFORM ON STRING || BASE_URL + "/operation_info/" ||http://127.0.0.1:8000/operation_info/
#####  post request example : { "id":7 }
