from metrics.prompt_template_provider import get_prompt_for_accurancy


class AccurancyTest:
    def __init__(self, conversational_model):
        self.conversational_model = conversational_model

    def _construct_prompt(self, question,context):
        prompt = get_prompt_for_accurancy(question, context)
        return prompt
    
    def test_case(self, case):
        question = case['question']
        context = case ['context']
        final_prompt = self._construct_prompt(question, context)
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