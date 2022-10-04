import re
from .db import DbConnector


def cleanMessage(msg):
    """
    Function to clean the input discord message and return a lowercase ascii string
    :return: processed string
    """
    # Step 1: Remove non-english words in the text
    pattern = r'[^\x00-\x7f]'
    ret = ''
    for _, element in enumerate(msg):
        if not re.search(pattern, element):
            ret += element
    # Step 2: convert everything to lowercase
    return ret.lower()


def getMsgTemplate(user_id, reason="profane", warning=False):
    """
    Utility Function to generate output Message Template
    :return: message template
    """
    reason_dict = {"profane": "using profane words"}
    ret = ""
    if warning:
        ret = """ Warning user:<@{0}> for {1}.\n Another attempt will result in a Ban!""".format(user_id,
                                                                                                 reason_dict[reason])
    else:
        ret = """ User:<@{0}> has been banned for {1}.""".format(user_id, reason_dict[reason])
    return ret


def checkOffenseCount(user_id, reason):
    dbconnect = DbConnector()
    sql_query = "SELECT offense_count FROM user_activity where user_id = %s"
    dbconnect.connect()
    result = dbconnect.executequery(sql_query, (user_id,))
    if result == 1:
        getMsgTemplate(user_id, reason, True)
    else:
        ##Ban User
        sql_query = "DELETE FROM user where user_id = %s"
        result = dbconnect.executequery(sql_query, (user_id,))
        getMsgTemplate(user_id, reason, False)
    return True
