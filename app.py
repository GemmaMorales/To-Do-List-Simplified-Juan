import csv
import os

todos = []
stop = False
def load_todos():
  global todos
  try:
    with open("todos.csv", newline='') as myFile:
      reader = csv.reader(myFile)
      for row in reader:
        todos = row
  except:
    open("todos.csv", "w+")
    load_todos()
def add_one_task(title):
    todos.append(title)
    save_todos() 
def print_list():
    print ("\nTO DO LIST:\n")
    for i in range (0,(len(todos))):
      print(str(i+1)+")"+ " "+ todos[i])
def delete_task(number_to_delete):
  del todos[(int(number_to_delete)-1)]
  save_todos()
def save_todos():
  myfile = open("todos.csv", "w+")     
  wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
  wr.writerow(todos)
if __name__ == '__main__':
    load_todos()
    while stop == False:
        os.system("clear")
        # print(todos) 
        print_list()
        print("""
      Options: 
        del: Delete a task
        stop: Exit the application
    """)
        print("Select an option or enter task")
        response = input("_")
        if response == "stop":
          print("Application stopped by user")
          stop = True
        elif response == "del":
            print("What task number you want to delete?")
            del_resp = input()
            if del_resp.isdigit() == False:
              print("Is not a number")
              try:
                input("Press enter to continue and input 'del' to delete")
              except SyntaxError:
                pass
            elif int(del_resp) > len(todos):
              print ("The selection is not in the list")
              try:
                input("Press enter to continue and input 'del' to delete")
              except SyntaxError:
                pass
            else:
              delete_task(del_resp)
        else:
          add_one_task(response)
