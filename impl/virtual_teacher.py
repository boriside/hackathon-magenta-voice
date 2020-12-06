from skill_sdk import skill, Response, tell
from skill_sdk.requests import CircuitBreakerSession

@skill.intent_handler('VIRTUAL_TEACHER_NUMBER')
def handler(answer: str):
    try:
        with CircuitBreakerSession() as session:
            response = session.get('https://hi4m6llff6.execute-api.eu-west-1.amazonaws.com/prod/a?id=new_id2&answer='+ answer)
        return tell(response.text)
    except:
        return tell("Sorry. I didn't understand that. Can you please repeat ?")

"""
1) CVI_INTERNAL_ASK_FREETEXT
"""
