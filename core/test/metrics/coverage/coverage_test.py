def test_case(case):
    contexts = case['context']
    expected_contexts = case ['expected_context']
    i = 0
    count = 0
    for expected_context in expected_contexts:
        i+=1
        for context in contexts:
            if expected_context in context:
                count +=1
                break
    return count/i
     
def test_mutiple_case(cases):
    ans = []
    for case in cases:
        ans.append(test_case(case))
    return ans