from metrics.prompt_template_provider import get_prompt_for_relevancy


class RelevancyTest:
    def __init__(self, conversational_model):
        self.conversational_model = conversational_model

    def _construct_prompt(self, question, actual_answer):
        prompt = get_prompt_for_relevancy(question, actual_answer)
        return prompt
    
    def test_case(self, case):
        question = case['question']
        actual_answer = case ['actual_answer']
        final_prompt = self._construct_prompt(question, actual_answer)
        string_ans = self.conversational_model.get_answer(final_prompt)
        try:
            dict_ans = eval(string_ans)
            ans = dict_ans['value']
        except:
            print("no se ha devuelto un json")
            return
        return ans

    def test_mutiple_case(self, cases):
        ans = []
        for case in cases:
            ans.append(self.test_case(case))
        return ans