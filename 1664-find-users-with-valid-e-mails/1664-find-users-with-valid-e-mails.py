import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    def validate_email(email):
        email = email.split('@')
        if 'leetcode.com' not in email or len(email) != 2 or not email[0][0].isalpha():
            return False
        elif not email[0].replace('-', '').replace('_', '').replace('.', '').isalnum():
            return False
        return True
        
    return users[users['mail'].apply(validate_email)]
        