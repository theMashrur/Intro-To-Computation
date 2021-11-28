import numpy.testing as npt
from time import time
from numpy import isclose, allclose, linspace, cos, exp, sin, pi, array, poly1d
print("Autograder loaded successfully!")
print("Remember to always restart and run all from the Kernel menu before submitting!")
def question1a(_globals):
    score = 0
    score0, score1 = 0, 0
    number_of_tests = 2
    print('Testing: typical case')
    try:
        this_list = [3, 5, 2, 7, 1, 2, 3, 1, 9]
        this_min = _globals["pop_min"](this_list)
        assert(this_min == 1)
        assert(this_list == [3, 5, 2, 7, 2, 3, 1, 9])
        print('Test passed!')
    except:
        print('Test failed!')
    else:
        score0 += 1
    print('\nTesting: edge case')
    try:
        this_list = [3]
        this_min = _globals["pop_min"](this_list)
        assert(this_min == 3)
        assert(this_list == [])
        print('Test passed!')
    except:
        print('Test failed!')
    else:
        score1 += 1
    score = score1 + score0
    if score > 0:
        print("\n{} out of {}".format(score,2))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question1b(_globals):
    score = 0
    score0, score1 = 0, 0
    number_of_tests = 2
    print('Testing: typical case')
    try:
        this_list = [3, 5, 2, 7, 1, 2, 3, 1, 9]
        this_sorted = _globals["simple_sort"](this_list)
        assert(this_sorted == [1, 1, 2, 2, 3, 3, 5, 7, 9])
        print('Test passed!')
    except:
        print('Test failed!')
    else:
        score0 += 1
    print('\nTesting: edge case')
    try:
        this_list = [3]
        this_sorted = _globals["simple_sort"](this_list)
        assert(this_sorted == [3])
        print('Test passed!')
    except:
        print('Test failed!')
    else:
        score1 += 1
    score = score1 + score0
    if score > 0:
        print("\n{} out of {}".format(score,2))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question1c(_globals):
    score = 0
    score0, score1 = 0, 0
    score00, score01, score10, score11 = 0, 0, 0, 0
    number_of_tests = 2
    print('Testing: typical case')
    try:
        this_list = [3, 5, 2, 7, 1, 2, 3, 1, 9]
        this_sorted = _globals["simple_sort"](this_list)
        assert(this_sorted == [1, 1, 2, 2, 3, 3, 5, 7, 9])
    except:
        print('Sorted list not returned correctly')
    else:       
        print('Sorted list returned correctly')
        score00 += 1
    try:
        assert(this_list == [1, 1, 2, 2, 3, 3, 5, 7, 9])
    except:
        print('List not sorted correctly in place')
    else:       
        print('List sorted correctly in place')
        score01 += 1
    score0 = score00*score01
    print('\nTesting: edge case')
    try:
        this_list = [3]
        this_sorted = _globals["simple_sort"](this_list)
        assert(this_sorted == [3])
    except:
        print('Sorted list not returned correctly')
    else:       
        print('Sorted list returned correctly')
        score10 += 1
    try:
        assert(this_list == [3])
    except:
        print('List not sorted correctly in place')
    else:       
        print('List sorted correctly in place')
        score11 += 1
    score1 = score10*score11
    score = score1 + score0
    if score > 0:
        print("\n{} out of {}".format(score,2))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question1d(_globals):
    score = 0
    score0, score1 = 0, 0
    score00, score01, score02, score10, score11, score12 = 0, 0, 0, 0, 0, 0
    number_of_tests = 2
    print('Testing: typical case')
    try:
        comparison_count = 0
        this_list = [3, 5, 2, 7, 1, 2, 3, 1, 9]
        this_sorted = _globals["simple_sort"](this_list)
        assert(this_sorted == [1, 1, 2, 2, 3, 3, 5, 7, 9])
    except:
        print('Sorted list not returned correctly')
    else:       
        print('Sorted list returned correctly')
        score00 += 1
    try:
        assert(this_list == [1, 1, 2, 2, 3, 3, 5, 7, 9])
    except:
        print('List not sorted correctly in place')
    else:       
        print('List sorted correctly in place')
        score01 += 1
    try:
        assert(_globals["comparison_count"] == 45)
    except:
        print('Incorrect comparison count')
    else:       
        print('Correct comparison count')
        score02 += 1
    score0 = score00*score01*score02
    print('\nTesting: edge case')
    try:
        this_list = [3]
        this_sorted = _globals["simple_sort"](this_list)
        assert(this_sorted == [3])
    except:
        print('Sorted list not returned correctly')
    else:       
        print('Sorted list returned correctly')
        score10 += 1
    try:
        assert(this_list == [3])
    except:
        print('List not sorted correctly in place')
    else:       
        print('List sorted correctly in place')
        score11 += 1
    try:
        assert(_globals["comparison_count"] == 46)
    except:
        print('Incorrect comparison count')
    else:       
        print('Correct comparison count')
        score12 += 1
    score1 = score10*score11*score11
    score = score1 + score0
    if score > 0:
        print("\n{} out of {}".format(score,2))
        return score
    else: 
        raise AssertionError('Test failed overall!') 

def question2_ia():   
    return 1

def question2_ib():   
    return 2

def question2_ic():   
    return 2

def question2_iia():   
    return 3

def question2_iib():   
    return 4

def question3_ia():   
    return 2

def question3_ib():   
    return 2

def question3_ic():   
    return 2

def question3_iia():   
    return 2

def question3_iib():   
    return 3

def question3_iiia():   
    return 2

def question3_iiib():   
    return 3 

def question3_iiic():   
    return 1

def question3_iiid():   
    return 2

def question3_iva():   
    return 2

def question3_ivb():   
    return True

def question4_a():   
    return 2

def question4_b():   
    return 1

def question4c(_globals):
    score = 0
    number_of_tests = 3
    try:
        assert(allclose(_globals['theta_array'], linspace(0,2*pi,401)))
    except:
        print('Incorrect value for theta_array')
    else:
        print('Correct value for theta_array')
        score += 1
    try:
        assert(allclose(_globals['x_array'], cos(3*_globals['theta_array'])))
    except:
        print('Incorrect value for x_array')
    else:
        print('Correct value for x_array')
        score += 1
    try:
        assert(allclose(_globals['y_array'], sin(5*_globals['theta_array'])))
    except:
        print('Incorrect value for y_array')
    else:
        print('Correct value for y_array')
        score += 1
    print('{} out of {}'.format(score,3))
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question5_ia():   
    return 3

def question5_ib():   
    return {1, 2, 4}

def question5_ic():   
    return 2

def question5_id():   
    return 4

def question5iia(_globals):
    score = 0
    number_of_tests = 2
    try:
        assert(allclose(_globals["A"],array([[1,-3,2,2],[0,1,0,-1],[1,3,1,-2],[-2,0,-3,-2]])))
    except:
        print('Incorrect value for A')
    else:
        print('Correct value for A')
        score += 1
    try:
        assert(allclose(_globals["v"], array([0, -2, -5, -1])))
    except:
        print('Incorrect value for v')
    else:
        print('Correct value for v')
        score += 1
    print('{} out of {}'.format(score,2))
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question5iib(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(isclose(_globals["normv"],5.477225575051661))
    except:
        print('Incorrect value for normv')
    else:
        print('Correct value for normv')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question5iic(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(isclose(_globals["norm1v"],8.0))
    except:
        print('Incorrect value for norm1v')
    else:
        print('Correct value for norm1v')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question5iid(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(isclose(_globals["norminfv"],5.0))
    except:
        print('Incorrect value for norminfv')
    else:
        print('Correct value for norminfv')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question5iie(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(isclose(_globals["detA"],2.0))
    except:
        print('Incorrect value for detA')
    else:
        print('Correct value for detA')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question5iif(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(allclose(_globals["invA"],array([[ 0.5, -9. ,  3.5,  1.5],[-0.5,  1. , -0.5, -0.5],[ 0. ,  6. , -2. , -1. ],[-0.5, -0. , -0.5, -0.5]])))
    except:
        print('Incorrect value for invA')
    else:
        print('Correct value for invA')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question5iig(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(allclose(_globals["eigA"],array([[ 3.02385899, -2.28250615, -0.42429781, 0.68294497]])))
    except:
        print('Incorrect value for eigA')
    else:
        print('Correct value for eigA')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!')  

def question5iih(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(allclose(_globals["Apow5"],array([[  13,  -12,   22,   41],[  34,   31,   47,  -31],[ 130,   99,  183,  -75],[-109,  -39, -161,  -36]])))
    except:
        print('Incorrect value for Apow5')
    else:
        print('Correct value for Apow5')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question5iij(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(allclose(_globals["solution1"],array([-1.,  1., -1.,  3.])))
    except:
        print('Incorrect value for solution1')
    else:
        print('Correct value for solution1')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question5iik(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(allclose(_globals["solution2"],array([ 1., -3.,  2.,  1.])))
    except:
        print('Incorrect value for solution2')
    else:
        print('Correct value for solution2')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question6a(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(_globals["mypoly"]==poly1d([   1,   -8,  -26,  168, -135]))
    except:
        print('Incorrect value for mypoly')
    else:
        print('Correct value for mypoly')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question6b(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(_globals["mypoly"]==poly1d([   1,   -8,  -26,  168, -135]))
    except:
        print('Incorrect value for mypoly')
    else:
        print('Correct value for mypoly')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question6b(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(allclose(_globals["mypolyvalues"],array([ 945.,    0., -455., -576., -495. ,-320., -135.,    0.,   49.,    0., -135., -320., -495., -576., -455.,    0.,  945.])))
    except:
        print('Incorrect value for mypolyvalues')
    else:
        print('Correct value for mypolyvalues')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question6c(_globals):
    score = 0
    number_of_tests = 1
    try:
        assert(allclose(_globals["mypolyroots"],array([ 9., -5.,  3.,  1.])))
    except:
        print('Incorrect value for mypolyroots')
    else:
        print('Correct value for mypolyroots')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 

def question6d(_globals):
    score = 0
    number_of_tests = 2
    try:
        assert(allclose(_globals["spx"],array([7., -3.,  2.])))
    except:
        print('Incorrect value for spx')
    else:
        print('Correct value for spx')
        score += 1
    try:
        assert(allclose(_globals["spy"],array([-576., -576.,   49.])))
    except:
        print('Incorrect value for spy')
    else:
        print('Correct value for spy')
        score += 1
    if score > 0:
        return score
    else: 
        raise AssertionError('Test failed!') 