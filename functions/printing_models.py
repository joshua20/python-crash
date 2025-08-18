#demonstrating how a function can modify a list

#start with design that need to be printed

unprinted_design=['phone-case','robot pedant','dodecahhedron']
completed_models=[]
while unprinted_design:
    current_design=unprinted_design.pop()
    print(f"printing model : {current_design}")
    completed_models.append(current_design)

#display all completed models

print("the following are the completed models")
for model in completed_models:
    print(model)

def printed_models(unprinted_models, completed_models):
    '''use functions to print list of models'''
    while unprinted_models:
        current_model=unprinted_models.pop()
        print(f"printing, {current_model}")
        completed_models.append(current_model)

def show_printed(completed_models):
    '''show completed models'''
    print("the following the are the printed models")
    for model in completed_models:
        print(model)

unprinted_models=['kimbo','taifa','harambee']
completed_models=[]
printed_models(unprinted_models,completed_models)
show_printed(completed_models)
