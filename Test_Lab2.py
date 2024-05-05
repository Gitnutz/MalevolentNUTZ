import Lab2

print("Test_Lab2")

def test_find_min_max_temperature():
    input_arr=[83,27,47,56,22]
    test_arr=[22,83]
    result =Lab2.find_min_max_temperature(input_arr)
    
    assert(result==test_arr)

def test_calc_average_temperature():
    input_arr=[22,44]
    test_ans=33.0

    result=Lab2.calc_average_temperature(input_arr)

    assert(result==test_ans)

def test_calc_median_temperature():
    input_arr=[22,33,44]
    test_ans=33.0

    result=Lab2.calc_average_temperature(input_arr)

    assert(result==test_ans)

def test_calc_median_temperature2():
    input_arr=[2,3,4,5,6]
    test_ans=4.0

    result=Lab2.calc_average_temperature(input_arr)

    assert(result==test_ans)