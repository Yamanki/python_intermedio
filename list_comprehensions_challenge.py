def run():
    naturals_sqr=[]

    for i in range(1,101):
        if i %3 !=0:
            sqr=i**2
            naturals_sqr.append(sqr)
    
    print(naturals_sqr)

if __name__ == "__main__":
    run()
