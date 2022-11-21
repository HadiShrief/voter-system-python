voter = open("voter.txt", "r")
candidates = open("candidates.txt", "r")
voter_dict = {}
candidate_dict = {}
for line in voter:
    s, g, governate, key,value= line.split(",", maxsplit=5)
    value=int(value[1:4])#remove first space and "\n"
    voter_dict[key]=[value,governate]
Lines = candidates.readlines()
for line in Lines:
    id=line[0:7]
    new_text=line[9:]
    name, governate, count=new_text.split(",")
    count=count[0:2]
    count=int(count)
    candidate_dict[id]=[ name, governate, count]
list=[]
# O(nlogn)
def quicksort_by_score(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    # Select your `pivot` element
    pivot = array[1][3]
    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item[3] < pivot:
            low.append(item)
        elif item[3] == pivot:
            same.append(item)
        elif item[3] > pivot:
            high.append(item)
    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort_by_score(low) + same + quicksort_by_score(high)
# O(nlogn)
#  from https://realpython.com/sorting-algorithms-python/
def quicksort_by_governate(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    # Select your `pivot` element
    pivot = array[1][2]
    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item[2] < pivot:
            low.append(item)
        elif item[2] == pivot:
            same.append(item)
        elif item[2] > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort_by_governate(low) + same + quicksort_by_governate(high)
def Display_Statistics():
    print(quicksort_by_score(list))
def Display_Winner():
    list_governate=[]
    # for i in range (len(list)):
    #     list_governate.append([i][2])
    # for i in list:
    #     if i in
def Display_Candidates():
    cand_by_gov=[]
    cand_by_gov = quicksort_by_governate(list)
    for i in cand_by_gov:
        print(i[1], end=" ")
# O(n)
def add_candidate():
    list_of_keys=[]
    for key in candidate_dict:
        list_of_keys.append(key)
    length=len(list_of_keys)
    id=list_of_keys[length-1]
    Cand=id[0:4]
    num=id[4:7]
    num=int(num)
    num+=1
    name=input("enter the candidate name :")
    governorate=input("enter the candidate governorate")
    score=0
    candidate_dict[id]=[Cand+str(num),governorate,score]
    print(candidate_dict)
# O(n)
def add_voter():
    list_of_username=[]
    for i in voter_dict.values():
        list_of_username.append(i)
    check_username=input("enter the username you want to add :")
    if check_username in list_of_username:
        print("The entered username is not allowed")
    else:
        new_pass=input("enter password :")
        new_governarate=input("enter governorate")
        voter_dict[check_username]=[new_pass,new_governarate]
        print("new dictionary:",voter_dict)
# O(1)
def  remove_candidate():
    rem=input("enter the id you want to remove :")
    candidate_dict.pop(rem)
    print("new dictionary :",candidate_dict)
# O(1)
def remove_voter():
    rem = input("enter the username you want to remove :")
    voter_dict.pop(rem)
    print("new dictionary : ",voter_dict)
def  system_exit():
    list_voters_save=[]
    list_candidate_save=[]
    save_choice=input("Do you want to save yes/n0 :")
    for (key1,val1), (key2,val2) in zip(voter_dict.items(), candidate_dict.items()):
        list_voters_save.append([ key1,val1[0],val1[1]])
        list_candidate_save.append([key2, val2[0], val2[1],val2[2]])
    if save_choice == "yes":
        # from https://pynative.com/python-write-list-to-file/
        with open("voter.txt", 'w') as fp:
            for item in list_voters_save:
                # write each item on a new line
                fp.write("%s\n" % item)
            print('voters save done ')
        with open("candidates.txt", 'w') as fp:
            for item in list_candidate_save:
                # write each item on a new line
                fp.write("%s\n" % item)
            print('candidates save done')
    elif save_choice == "no":
        return
def admin_menu():
    global list
    print("1. Display Statistics")
    print("2. Display Winner")
    print("3. Display Candidates")
    print("4. Add Candidate")
    print("5. Add Voter")
    print("6. Remove Candidate")
    print("7. Remove Voter")
    print("8. Exit")
    choice = int(input("choose :"))
    if choice == 1:
        Display_Statistics()
        print(list)
    if choice == 2:
        Display_Winner()
    if choice == 3:
        Display_Candidates()
    if choice == 4:
        add_candidate()
    if choice == 5:
        add_voter()
    if choice == 6:
        remove_candidate()
    if choice == 7:
        remove_voter()
    if choice == 8:
        system_exit()
# the worst case is O(n power 2)
def voter_menu():
    global candidate_dict
    global voter_dict
    global list
    for i, v in candidate_dict.items():
        cand = v[0].replace("_", " ")# remove "_" from candidates
        gover = v[1]
        count = v[2]
        candidate_dict[i] = [cand, gover, count]
    print("Welcome", username)
    print("1. Vote")
    print("2. Exit")
    menu_choice = int(input())
    counter=0
    if menu_choice == 1:
        gov=voter_dict[username]
        gov=gov[1]# extract the governate of login user
        for key, val in candidate_dict.items():
            if val[1] in gov:
                print("Do you want to vote for :")
                print(val[0])
        voted_for=input("your vote is for :")
        for key, val in candidate_dict.items():
            if voted_for in val[0]:# check if the user enter correct name
                for i in range (len(list)):
                    if key == list[i][0]:# check if the id of candidate was added previously
                     list[i][3]+=1
                     return
                list.append([key, val[0], val[1], val[2] + 1])
                print(candidate_dict)
                print(voter_dict)
                print(list)
    if menu_choice == 2:
        candidate_save = []
        for key,val in candidate_dict.items():
            candidate_save.append([key, val[0], val[1],val[2]])
        with open("candidates.txt", 'w') as fp:
            for item in candidate_save:
                # write each item on a new line
                fp.write("%s\n" % item)
            print('new score is saved')
print(candidate_dict)
print(voter_dict)
login_counter=0
while login_counter<5:
    username = input("enter login user_name :")
    password = input("enter login password :")
    for key,val in voter_dict.items():
        if username == "admin" and password == "admin123123":
            admin_menu()
        elif username == key and int(password) == val[0]:
            voter_menu()
        # it makes some error so I didn't use it
        # else:
        #     print("Incorrect Username and/or Password")
        #     login_counter+=1
        #     break

# Note that their is some functions work but it return error at it's end even I achieved what I want from this function 
