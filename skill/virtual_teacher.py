from skill_sdk import skill, Response, tell, ask, context, ask_freetext
from skill_sdk.requests import CircuitBreakerSession
import logging


@skill.intent_handler('TEAM_35_START_VIRTUAL_TEACHER')
def handler(answer: str):
    try:
        logger = logging.getLogger(__name__)
        logger.info("**** Test Context = "+ str(context))
        with CircuitBreakerSession() as session:

            answer = "number"
            print("**** Test Context = "+ str(context))
            response = session.get('https://hi4m6llff6.execute-api.eu-west-1.amazonaws.com/prod/a?id=new_id2&answer='+ answer)
        return ask_freetext(response.text)
    except Exception as e:
        logger.info("**** Exception = " + str(e))
        return ask("Sorry. I didn't understand that. Can you please repeat ?")


INTENT_NAME = "CVI_INTERNAL_ASK_FREETEXT"

@skill.intent_handler(INTENT_NAME)
def handler():
    logger = logging.getLogger(__name__)
    logger.info("**** Context2 = " + str(context))
    ask_freetext("What do you want to play")
