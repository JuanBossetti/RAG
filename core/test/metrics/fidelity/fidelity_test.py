from metrics.prompt_template_provider import get_prompt_for_fidelity


class FidelityTest:
    def __init__(self, conversational_model):
        self.conversational_model = conversational_model

    def _construct_prompt(self, context, actual_answer):
        prompt = get_prompt_for_fidelity(context, actual_answer)
        return prompt
    
    def test_case(self, case):
        context = case['context']
        actual_answer = case ['actual_answer']
        final_prompt = self._construct_prompt(context, actual_answer)
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