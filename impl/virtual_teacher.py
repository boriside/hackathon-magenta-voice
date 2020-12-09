from skill_sdk import skill, Response, tell, ask, context, ask_freetext, ssml
from skill_sdk.requests import CircuitBreakerSession
from skill_sdk.services.persistence import PersistenceService
import logging


@skill.intent_handler('TEAM_35_START_VIRTUAL_TEACHER')
def virtual_teacher_handler(answer: str):
    logger = logging.getLogger(__name__)
    logger.info("**** Context2 = " + str(context))
    return ask_freetext("Was möchtest du heute machen? Algebra oder Geometrie? Ich kann dir auch einige Fitness Übungen zeigen.")

@skill.intent_handler('CVI_INTERNAL_ASK_FREETEXT')
def handler(stt: str):
    try:
        logger = logging.getLogger(__name__)
        logger.info("**** Test Context = "+ str(context))
        #session_id = PersistenceService().get()['session_id']
        #if not session_id:
            #PersistenceService().set(dict(session_id=context.session.session_id))
        with CircuitBreakerSession() as session:
            print("**** Test Context = "+ str(context))
            response = session.get('https://hi4m6llff6.execute-api.eu-west-1.amazonaws.com/prod/a?id=new_id2&answer='+ stt)
            #response = session.get('https://hi4m6llff6.execute-api.eu-west-1.amazonaws.com/prod/a?id=' + session_id +'&answer=' + stt)
        return ask_freetext(response.text)
    except Exception as e:
        logger.info("**** Exception = " + str(e))
        return ask("Es ist ein Fehler aufgetreten!")