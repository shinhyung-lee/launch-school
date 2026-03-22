def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    elif not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters"
    else:
        return None
    
def find_list_by_id(list_id, lists):
    return next((lst for lst in lists if lst['id'] == list_id), None)

def find_todo_by_id(todo_id, todos):
    return next((todo for todo in todos if todo['id'] == todo_id), None)

def delete_todo_by_id(todo_id, lst):
    lst['todos'] = [todo for todo in lst['todos'] if todo['id'] != todo_id]
    return None

def mark_all_completed(lst):
    for todo in lst['todos']:
        todo['completed'] = True 
        
    return None 

# for '@app.route("/lists/<list_id>/delete")' route
def delete_list_by_id(list_id, lst):
    lst = [todo_list for todo_list in lst if todo_list['id'] != list_id]
    return lst

def error_for_todo(title):
    if not 1 <= len(title) <= 100:
        return "Todo title must be between 1 and 100 characters"

    return None

def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed'])

def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0


def is_todo_completed(todo):
    return todo['completed']

def sort_items(items, select_completed):
    sorted_todos = sorted(items, key=lambda t: t['title'])
    incomplete_todos = [todo for todo in sorted_todos
                        if not select_completed(todo)]
    complete_todos = [todo for todo in sorted_todos
                      if select_completed(todo)]

    return incomplete_todos + complete_todos
    
    
    
    
    
    
    
    