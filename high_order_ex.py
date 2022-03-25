def run():
    # get the sqrt of a number form a list of them
    my_list=[1,2,4,5,6,9,13,19,21]
    sqr=[i**2 for i in my_list]
    ### by applying  map
    sqr_map= list(map(lambda x: x**2, my_list))
    print(sqr, " vs", sqr_map)

    #Miltiply all 
    my_list = [2,2,2,2,2]
    all_multiplied = 1

    for i in my_list:
        all_multiplied= all_multiplied * i

    ### by applying reduce
    from functools import reduce

    all_multiplied_red = reduce(lambda a,b: a* b, my_list)
    print(all_multiplied, 'vs', all_multiplied_red)


if __name__ == '__main__':
    run()
