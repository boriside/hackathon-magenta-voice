from skill_sdk import skill, Response, tell, ask, context, ask_freetext, ssml
from skill_sdk.requests import CircuitBreakerSession
from skill_sdk.services.persistence import PersistenceService
import logging
import uuid


@skill.intent_handler('TEAM_35_START_VIRTUAL_TEACHER')
def virtual_teacher_handler(answer: str):
    logger = logging.getLogger(__name__)
    logger.info("**** Start Context = " + str(context))
    return ask_freetext("Hallo, Irena! Was möchtest du heute machen? Ich kann dir Algebra oder Geometrie Aufgaben anbieten oder einige Fitness Übungen zeigen.")


@skill.intent_handler('CVI_INTERNAL_ASK_FREETEXT')
def handler(stt: str, user_id: str):
    try:
        if stt.lower() == 'spiel beenden':
            with CircuitBreakerSession() as session:
                session.delete('https://n3i39w6xtc.execute-api.eu-west-1.amazonaws.com/prod/delsession?id=' + user_id)
            return tell("Auf Wiedersehen. bis bald")
        logger = logging.getLogger(__name__)
        logger.info("**** CVI Context = " + str(context))
        with CircuitBreakerSession() as session:
            logger.info("**** user_hash = " + str(user_id))
            response = session.get(
                'https://hi4m6llff6.execute-api.eu-west-1.amazonaws.com/prod/a?id=' + user_id + '&stt=' + stt)
        return ask_freetext(response.text)
    except Exception as e:
        logger.info("**** Exception = " + str(e))
        return ask_freetext("Es ist ein Fehler aufgetreten!")
