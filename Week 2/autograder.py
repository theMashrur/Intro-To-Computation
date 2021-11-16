import numpy.testing as npt
print("Autograder loaded successfully!")
print("Remember to always restart and run all from the Kernel menu before submitting!")


def question1_i_a(_globals):
    score = 0
    number_of_tests = 3
    try:
        assert(isinstance(_globals["int1"], int))
        assert(_globals["int1"] == 123)
    except:
        print("int1 case failed!")
        pass
    else:
        score += 1
    
    try:
        assert(isinstance(_globals["int2"], int))
        assert(_globals["int2"] == 456)
    except:
        print("int2 case failed!")
        pass
    else:
        score += 1
        
    try:
        assert(isinstance(_globals["int3"], int))
        assert(_globals["int3"] == 789)
    except:
        print("int3 case failed!")
        pass
    else:
        score += 1

    print(f'{score} out of {number_of_tests} tests passed')
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')    

        
# def question1_i_a(lst):
#     answers   = [123, 456, 789]
#     questions = len(lst)
#     result    = [(isinstance(lst[i], int) and lst[i] == answers[i]) for i in range(questions)]
#     if sum(result) == questions:
#         print(f'{questions} out of {questions} tests passed')
#         return sum(result)
#     else:
#         print(f'{sum(result)} out of {questions} tests passed')
#         return sum(result)
                
        
        
def question1_i_b(_globals):
    score = 0
    number_of_tests = 3
    try:
        assert(isinstance(_globals["float1"], float))
        assert(_globals["float1"] == 123.0)
    except:
        print("float1 case failed!")
        pass
    else:
        score += 1
    
    try:
        assert(isinstance(_globals["float2"], float))
        assert(_globals["float2"] == 456.0)
    except:
        print("float2 case failed!")
        pass
    else:
        score += 1
        
    try:
        assert(isinstance(_globals["float3"], float))
        assert(_globals["float3"] == 789.0)
    except:
        print("float3 case failed!")
        pass
    else:
        score += 1

    print(f'{score} out of {number_of_tests} tests passed')
    if score > 0:
        return score
    else: 
        raise AssertionError('All tests failed!!')    

        
def question1_i_c():        
        return 3

def question1_i_d():        
        return 2
    
def question1_i_e():        
        return 1
    
def question1_i_f():        
        return 2
    
def question1_i_g():        
        return 3

    
def question1_ii_check(sol, ans, typ):
    score = 0
    if sol == ans:
        score += 1
        try:
            assert(isinstance(sol, typ))
            score += 1
        except:
            pass
    else:
        try:
            assert(isinstance(sol, typ))
            score += 1
        except:
            pass
    return score

def question1_ii_a(_globals):
    complex1 = _globals["complex1"]
    complex2 = _globals["complex2"]
    complex3 = _globals["complex3"]
    complex4 = _globals["complex4"]
    complex5 = _globals["complex5"]
    sols = [complex1, complex2, complex3, complex4, complex5] 
    ans  = [123 + 0j, 456 + 0j, 789 + 0j, 123+456j, 123+456j]
    test = [question1_ii_check(sols[i], ans[i], complex) for i in range(len(sols))]
    score = sum(test)
    if score == 10:
        print("All solutions and object types correct!")
    else:        
        print("Ensure the type of your solutions are correct and complex!")
        print('The following cases were failed:')
        failed = [i+1 for i, e in enumerate(test) if e != 2]
        for k in failed:
            print('complex{} is incorrect'.format(k))
    return score
        
    
    
def question1_ii_b():        
    return 3
    
    
def question1_ii_c():        
    return 3


def question1_ii_d():        
    return 2


def question1_ii_e():        
    return 2


def question1_ii_f():        
    return 2


def question1_ii_g():        
    return 2


def question1_ii_h():        
    return 5

def question2_i(_globals):
    q2ia_answer = _globals["q2ia_answer"]
    q2ib_answer = _globals["q2ib_answer"]
    q2ic_answer = _globals["q2ic_answer"]
    q2id_answer = _globals["q2id_answer"]
    score = 0
    try:
        assert q2ia_answer == "The quick brown"
        score += 1
    except:
        print("Question 2(a) failed!")
        pass
    try:
        assert q2ib_answer == "Teqikbon"
        score += 1
    except:
        print("Question 2(b) failed!")
        pass
    try:
        assert q2ic_answer == "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
        score += 1
    except:
        print("Question 2(c) failed!")
        pass
    try:
        assert q2id_answer == "The quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dog"
        score += 1
    except:
        print("Question 2(d) failed!")
        pass
    if score == 4:
        print("All tests passed!!")
    return score


def question2_ii(_globals):
    q2iia_answer = _globals["q2iia_answer"]
    q2iib_answer = _globals["q2iib_answer"]
    q2iic_answer = _globals["q2iic_answer"]
    score = 0
    try:
        assert q2iia_answer == [0j, 'one', 2, 3.0, (4+0j), 'five', 6, 7.0, (8+0j), 'nine', 10]
        score += 1
    except:
        print("Question 2(a) failed!")
        pass
    try:
        assert q2iib_answer == [0j, 2, (4+0j), 6, (8+0j), 10]
        score += 1
    except:
        print("Question 2(b) failed!")
        pass
    try:
        assert q2iic_answer == [0j, 'one', 2, 3.0, (4+0j), 'five', 6, 7.0, (8+0j), 'nine', 10, 11.0, (12+0j), 'thirteen', 14, 15.0, 0j, 'one', 2, 3.0, (4+0j), 'five', 6, 7.0, (8+0j), 'nine', 10, 11.0, (12+0j), 'thirteen', 14, 15.0, 0j, 'one', 2, 3.0, (4+0j), 'five', 6, 7.0, (8+0j), 'nine', 10, 11.0, (12+0j), 'thirteen', 14, 15.0]
        score += 1
    except:
        print("Question 2(c) failed!")
        pass
    if score == 3:
        print("All tests passed!!")
    return score   
    
    
def question2_iii(_globals):
    q2iiia_answer = _globals["q2iiia_answer"]
    q2iiib_answer = _globals["q2iiib_answer"]
    q2iiic_answer = _globals["q2iiic_answer"]
    score = 0
    try:
        assert q2iiia_answer == (0j, 'one', 2, 3.0, (4+0j), 'five', 6, 7.0, (8+0j), 'nine', 10)
        score += 1
    except:
        print("Question 2(a) failed!")
        pass
    try:
        assert q2iiib_answer == (0j, 2, (4+0j), 6, (8+0j), 10)
        score += 1
    except:
        print("Question 2(b) failed!")
        pass
    try:
        assert q2iiic_answer == (0j, 'one', 2, 3.0, (4+0j), 'five', 6, 7.0, (8+0j), 'nine', 10, 11.0, (12+0j), 'thirteen', 14, 15.0, 0j, 'one', 2, 3.0, (4+0j), 'five', 6, 7.0, (8+0j), 'nine', 10, 11.0, (12+0j), 'thirteen', 14, 15.0, 0j, 'one', 2, 3.0, (4+0j), 'five', 6, 7.0, (8+0j), 'nine', 10, 11.0, (12+0j), 'thirteen', 14, 15.0)
        score += 1
    except:
        print("Question 2(c) failed!")
        pass
    if score == 3:
        print("All tests passed!!")
    return score     
    
    
def question2_iv_a():
    return [0j, 'one', 2, 3.0, (4+0j), 'five', 6, 7.0, (8+0j), 'nine', 10, 11.0, (12+0j), 'thirteen', 14, 15.0, (16+0j), 'seventeen', 18, 19.0]
    
    
def question2_iv_b():
    return [0j, 'uno', 2, 3.0, (4+0j), 'cinco', 6, 7.0, (8+0j), 'nueve', 10, 11.0, (12+0j), 'trece', 14, 15.0, (16+0j), 'diecisiete', 18, 19.0]
    
    
def question2_iv_c():
    return (0j, 'one', 2, 3.0, (4+0j), 'five', 6, 7.0, (8+0j), 'nine', 10, 11.0, (12+0j), 'thirteen', 14, 15.0, (16+0j), 'seventeen', 18, 19.0)     
    

def question2_iv_d():
    return (0j, 'uno', 2, 3.0, (4+0j), 'cinco', 6, 7.0, (8+0j), 'nueve', 10, 11.0, (12+0j), 'trece', 14, 15.0, (16+0j), 'diecisiete', 18, 19.0)
    
    
def question3_a():
    return ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    
def question3_b():
    return "The quick brown fox jumps over the lazy dog"

def question3_c():
    return "brown, dog, fox, jumps, lazy, over, quick, the, the"
    
def question3_d():
    return "The quick brown fox jumps over the lazy cat"
    
def question3_e():
    return "The quick brown dog jumps over the lazy fox"
        

def question4_a(_globals):
    score = 0
    try:
        assert(_globals["polyhedron2"] == "The regular solid known as the cube has 6 square faces, 12 edges and 8 vertices.")
        score += 1
    except:
        pass
    try:
        assert(_globals["polyhedron3"] == "The regular solid known as the octahedron has 8 triangular faces, 12 edges and 6 vertices.")
        score += 1
    except:
        pass
    print(f"{score} tests passed!")
    return score


def question4_b():
    return 'The regular solid known as the cube has 6 square faces, 12 edges and 8 vertices.'
    
    
def question4_c():
    return 'The regular solid known as the cube has 6 square faces, 12 edges and 8 vertices.'
   
    