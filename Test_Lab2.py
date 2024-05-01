import Lab2

def test_find_max_min():
    input_temp = [25, 18, 30, 22, 27]
    test_max = 30
    test_min = 18

    result = Lab2.find_min_max(input_temp)
    
    assert (result == (test_min, test_max))

def test_calc_average():
    input_temp = [25, 18, 30, 22, 27]
    test_avg = 24.4

    result = Lab2.calc_average(input_temp)

    assert (result == test_avg)

def test_calc_median_temp():
    input_temp = [25, 18, 30, 22, 27]
    test_median = 25

    result = Lab2.calc_median_temperature(input_temp)

    assert (result == test_median)
