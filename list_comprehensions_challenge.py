def run():
    naturals_sqr=[i**2 for i in range(1,101) if i % 3 !=0]
    
    print(naturals_sqr)

if __name__ == "__main__":
    run()
