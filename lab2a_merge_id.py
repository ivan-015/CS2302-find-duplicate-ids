# Ivan Vigliante
# CS2302 TR 10:20am-11:50am
# Lab 2A
# Professor Aguirre, Diego
# TA Saha, Manoj
# Date of last modification: 10/16/2018
# The purpose of this program is to read from a file of IDs, store them
# in a linked list, and through various sorting algorithms and techniques
# determine if any of the IDs are repeated.
from timeit import default_timer as timer
import sys

class Node(object):

    def __init__(self, item=-1, next=None):
        self.item = item
        self.next = next

    def insert(self, insert_item):
        curr = self
        if curr.item is -1:
            curr.item = insert_item
            return
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(insert_item)

# This method prompts the user for two files containing activision and vivendi
# ID's, adds them to a linked list, and returns the head node.
def get_ids():
    while True:
        try:
            id_list = Node()
            #Ask user for the paths that contain activision and vivendi ID's
            activision_file = input("Provide path of file with Activision ID's including filename(input ""e"" to exit the program): ")
            if activision_file == "e":
                sys.exit()
            vivendi_file = input("Provide path of file with Vivendi ID's including filename(input ""e"" to exit the program): ")
            if vivendi_file == "e":
                sys.exit()
            #Try to open the files
            activision_file = open(activision_file, "r")
            vivendi_file = open(vivendi_file, "r")

            #Read each line in the activision id file
            for line in activision_file:
                #If any of the ID's are outside of range, throw error message and terminate the program
                if int(line)<0 or int(line)>6000:
                    print("ID: ", int(line), "is out of range. Skipping.")
                    continue
                #Otherwise, insert ID into the linked list
                else:
                    id_list.insert(int(line))
            activision_file.close()

            #Read each line in the vivendi file
            for line in vivendi_file:
                #If any of the ID's are outside the range, throw error message and terminate the program
                if int(line)<0 or int(line)>5000:
                    print("ID: ", int(line), "is out of range. Skipping.")
                    continue
                #Otherwise, insert ID into linked list
                else:
                    id_list.insert(int(line))
            vivendi_file.close()
            break
        except FileNotFoundError:
            print("Error: File not found. Please try again.")
            continue
        except ValueError:
            print("Error: Make sure the file has only integers.")
            continue
        except Exception as ee:
            print(ee)
    return id_list

def main():

    head_node = get_ids()

    #Loop used to prompt the user for which solution they would like to implement
    while True:
        operation = input("\nInput one of the following:\n[1]: Get repeats by comparing every ID.\n[2]: Get repeats using bubble sort implementation.\n"
              "[3]: Get repeats using merge sort implementation.\n[4]: Get repeats using boolean array seen.\n[p]: print linked list\n[e]: Exit.\n")
        #exit operation
        if operation.lower() == "e":
            return
        #Print the linked list
        elif operation.lower() == "p":
            curr = head_node
            while curr is not None:
                print(curr.item, end=" ", flush=True)
                curr = curr.next
            print()
        #Find duplicate IDs using solution one(nested loops)
        elif operation == "1":
            start = timer()
            repeat_set = solution_one(head_node)
            runtime = timer() - start
            print("Runtime:", round(runtime*1000, 3), "milliseconds.")
            print("Found", len(repeat_set), "repeats")
            prompt = input("Print repeats set? [Y/N]")
            if prompt.lower() == "y":
                print(repeat_set)
        #Find duplicate IDs using solution two(bubble sort)
        elif operation == "2":
            clone = clone_list(head_node)
            start = timer()
            repeat_set = solution_two(clone)
            runtime = timer() - start
            print("Runtime:", round(runtime * 1000, 3), "milliseconds.")
            print("Found", len(repeat_set), "repeats")
            prompt = input("Print repeats set? [Y/N]")
            if prompt.lower() == "y":
                print(repeat_set)
        #Find duplicate IDs using solution 3(merge sort)
        elif operation == "3":
            clone = clone_list(head_node)
            start = timer()
            repeat_set = solution_three(clone)
            runtime = timer() - start
            print("Runtime:", round(runtime * 1000, 3), "milliseconds.")
            print("Found", len(repeat_set), "repeats")
            prompt = input("Print repeats set? [Y/N]")
            if prompt.lower() == "y":
                print(repeat_set)
        #Find duplicate IDs using solution 4(Boolean array)
        elif operation == "4":
            start = timer()
            repeat_set = solution_four(head_node)
            runtime = timer() - start
            print("Runtime:", round(runtime * 1000, 3), "milliseconds.")
            print("Found", len(repeat_set), "repeats")
            prompt = input("Print repeats set? [Y/N]")
            if prompt.lower() == "y":
                print(repeat_set)
        else:
            print("Not a valid command, try again.")
    # The following code is for testing solutions one through four. Each runs the solution
    # 100 times and calculates the average runtime of each solution in milliseconds.
    '''sum = 0
    for i in range(100):
        start = timer()
        repeat_set_one = solution_one(head_node)
        runtime = timer() - start
        sum += runtime
        print("     ", runtime, "seconds")
    average = (sum / 100) * 1000
    print("\naverage runtime of solution one: ", average, "milliseconds\n")'''

    '''sum = 0
    for i in range(100):
        clone = clone_list(head_node)
        start = timer()
        repeat_set_two = solution_two(clone)
        runtime = timer() - start
        sum += runtime
        print("     ", runtime, "seconds")
    average = (sum / 100) * 1000
    print("\naverage runtime of solution two: ", average, "milliseconds\n")'''

    '''sum = 0
    for i in range(100):
        clone = clone_list(head_node)
        start = timer()
        repeat_set_three = solution_three(clone)
        runtime = timer() - start
        sum += runtime
        print("     ", runtime, "seconds")
    average = (sum / 100) * 1000
    print("\naverage runtime of solution three: ", average, "milliseconds\n")'''

    '''sum = 0
    for i in range(100):
        start = timer()
        repeat_set_four = solution_four(head_node)
        runtime = timer() - start
        sum += runtime
        print("     ", runtime, "seconds")
    average = (sum / 100) * 1000
    print("\naverage runtime of solution four: ", average, "milliseconds\n")'''

# Finds duplicates in a linked list through nested loops
def solution_one(node):
    curr = node
    repeats_set = set()
    while curr is not None:
        every_other = curr.next
        while every_other is not None:
            #if two items match, add to repeats list
            if curr.item == every_other.item:
                repeats_set.add(curr.item)
            every_other = every_other.next
        curr = curr.next
    return repeats_set

#sort linked list using bubble sort, then look for duplicates
def solution_two(node):
    #call bubble sort method on node
    curr = bubble_sort(node)
    repeats_set = set()

    while curr.next is not None:
        #If the current item is the same as the next, add to repeats
        if curr.item == curr.next.item:
            repeats_set.add(curr.item)
        curr = curr.next
    return repeats_set


#sort linked list using merge sort, then look for duplicates
def solution_three(node):
    curr = merge_sort(node)

    repeats_list = set()
    while curr.next is not None:
        #If the current item is the same as the next item, add to duplicate list
        if curr.item == curr.next.item:
            repeats_list.add(curr.item)
        curr = curr.next

    return repeats_list

#Find duplicate ID's by using a boolean array to know if the item has been seen before
def solution_four(node):
    #Create a boolean array with 6001 spaces (max range is [0,6000])
    seen = [False] * 6001
    repeats_set = set()
    curr = node
    while curr is not None:
        #If the item has been seen, add to repeats set
        if seen[curr.item]:
            repeats_set.add(curr.item)
        #Otherwise, set the seen value at that index to True
        else:
            seen[curr.item] = True
        curr = curr.next
    return repeats_set

#Helper method that applies bubble sort on a linked list
def bubble_sort(node):
    curr = node
    while curr is not None:
        every_other = curr.next
        while every_other is not None:
            #If the current is greater than every_other, swap
            if curr.item > every_other.item:
                curr.item, every_other.item = every_other.item, curr.item

            every_other = every_other.next

        curr = curr.next
    return node

#Helper method that performs merge sort on a linked list
def merge_sort(node):
    if node is None or node.next is None:
        return node

    #Split the list into two halves
    first_half, second_half = split_list(node)

    # Recursively call merge sort on the two halves and merge them
    # once the two halves are each sorted
    return merge_lists(merge_sort(first_half),merge_sort(second_half))

#helper method that merges two lists
def merge_lists(first_half, second_half):
    #holder node to not lose the pointer of the newly organized list
    holder = Node()
    #curr node used to traverse holder
    curr = holder

    while first_half is not None and second_half is not None:
        # If the item in the first list is less than the item in second, add node to list
        # and move to the next item in the first list (to keep comparing)
        if first_half.item <= second_half.item:
            curr.next = first_half
            first_half = first_half.next
        # Otherwise, the item in the second list is less, so add node to list
        # and move to the next item in second list
        else:
            curr.next = second_half
            second_half = second_half.next
        #Once a node has been added to curr, go to next element in curr to not replace it
        curr = curr.next

    #if all the items on the first list have been added, add the rest of the second list to curr
    if first_half is None:
        curr.next = second_half
    #if all the items on the second list have been added, add the rest of the first list to curr
    elif second_half is None:
        curr.next = first_half
    #Return newly created list
    return holder.next

#Helper method for merge sort, splits a list in half and returns both halves
def split_list(node):
    if node is None or node.next is None:
        return node, None

    curr = node
    ahead = node.next #Node ahead used to stop curr in the middle index
    while ahead is not None and ahead.next is not None:
        # For each step curr takes, ahead takes two, by the time ahead
        # or ahead.next is none, curr will be in the middle index
        curr = curr.next
        ahead = ahead.next.next
    #Define second half
    second_half = curr.next
    #cut off the first half
    curr.next = None

    return node, second_half

# Method used before merge sort and bubble sort
# to avoid affecting the original linked list.
def clone_list(node):
    clone = Node()
    iter = node
    while iter is not None:
        clone.insert(iter.item)
        iter = iter.next
    return clone

main()
