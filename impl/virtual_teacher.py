from skill_sdk import skill, Response, tell, ask, context, ask_freetext, ssml
from skill_sdk.requests import CircuitBreakerSession
from skill_sdk.services.persistence import PersistenceService
import logging
import uuid

@skill.intent_handler('TEAM_35_START_VIRTUAL_TEACHER')
def virtual_teacher_handler(answer: str):
    logger = logging.getLogger(__name__)
    logger.info("**** Context2 = " + str(context))
    session_id = PersistenceService().get()['session_id']
    if not session_id:
        session_id = str(uuid.uuid4())
        PersistenceService().set(dict(session_id=session_id))
    
    return ask_freetext("Was möchtest du heute machen? Algebra oder Geometrie? Ich kann dir auch einige Fitness Übungen zeigen.")

@skill.intent_handler('CVI_INTERNAL_ASK_FREETEXT')
def handler(stt: str):
    try:
        if stt.lower() == 'exit':
            return tell("Auf Wiedersehen. bis bald")
        logger = logging.getLogger(__name__)
        logger.info("**** Test Context = "+ str(context)) 
        #session_id = PersistenceService().get()['session_id']
        session_id = '12345'
        with CircuitBreakerSession() as session:
            logger.info("**** session_id = "+ str(session_id))
            response = session.get('https://hi4m6llff6.execute-api.eu-west-1.amazonaws.com/prod/a?id='+session_id+'&stt='+ stt)
        return ask_freetext(response.text)
    except Exception as e:
        logger.info("**** Exception = " + str(e))
        return ask_freetext("Es ist ein Fehler aufgetreten!")
