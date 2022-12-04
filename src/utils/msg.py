#!/usr/bin/python
import re


def clean_message(msg):
    """
    Function to clean the input discord message and return a lowercase ascii string
    :return: processed string
    """
    # Step 1: Remove non-english words in the text
    pattern = r"[^\x00-\x7f]"
    ret = ""
    for _, element in enumerate(msg):
        if not re.search(pattern, element):
            ret += element
    # Step 2: convert everything to lowercase
    return ret.lower()


def get_msg_template(user_id, reason, warning=False):
    """
    Utility Function to generate output message template
    :return: message template
    """
    # reason_dict = {"profane": "using profane words"}
    ret = ""
    reason_str = ",".join(reason) if isinstance(reason, list) else str(reason)
    if warning:
        ret = """ Warning user:<@{0}> for {1}.\n Another attempt will result in a ban!""".format(
            user_id, reason_str
        )
    else:
        ret = """ User:<@{0}> has been banned for {1}.""".format(user_id, reason_str)
    return ret


def get_help_message():
    """
    Utility Function to generate help options
    :return: message template
    """
    return """
                Inorder to report a word as profane use the below command:
                !report profane <word>
                Inorder to report a word as profane use the command:
                !report word <word>
                Inorder to apologize
                !apology <message>
           """
