import boto3
import hmac
import hashlib
import base64
from botocore.exceptions import ClientError
from auth_interface import AuthInterface

class CognitoAuthService(AuthInterface):
    def __init__(self, user_pool_id, client_id, client_secret=None, region='us-east-1'):
        self.user_pool_id = user_pool_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.region = region
        self.client = boto3.client('cognito-idp', region_name=region)

    def get_secret_hash(self, username):
        """Generate secret hash for requests if client secret exists"""
        if not self.client_secret:
            return None
        message = bytes(username + self.client_id, 'utf-8')
        secret = bytes(self.client_secret, 'utf-8')
        dig = hmac.new(secret, message, hashlib.sha256).digest()
        return base64.b64encode(dig).decode()

    def sign_up(self, username, password, email):
        """Register a new user"""
        try:
            kwargs = {
                'ClientId': self.client_id,
                'Username': username,
                'Password': password,
                'UserAttributes': [{'Name': 'email', 'Value': email}]
            }
            if self.client_secret:
                kwargs['SecretHash'] = self.get_secret_hash(username)
            
            response = self.client.sign_up(**kwargs)
            return {'success': True, 'user_sub': response['UserSub']}
        except ClientError as e:
            return {'success': False, 'error': str(e)}

    def authenticate(self, username, password):
        """Authenticate user and return tokens"""
        try:
            kwargs = {
                'ClientId': self.client_id,
                'AuthFlow': 'USER_PASSWORD_AUTH',
                'AuthParameters': {
                    'USERNAME': username,
                    'PASSWORD': password
                }
            }
            if self.client_secret:
                kwargs['AuthParameters']['SECRET_HASH'] = self.get_secret_hash(username)
            
            response = self.client.initiate_auth(**kwargs)
            return {
                'success': True,
                'access_token': response['AuthenticationResult']['AccessToken'],
                'id_token': response['AuthenticationResult']['IdToken'],
                'refresh_token': response['AuthenticationResult']['RefreshToken']
            }
        except ClientError as e:
            return {'success': False, 'error': str(e)}

    def refresh_token(self, refresh_token):
        """Refresh access token"""
        try:
            kwargs = {
                'ClientId': self.client_id,
                'AuthFlow': 'REFRESH_TOKEN_AUTH',
                'AuthParameters': {'REFRESH_TOKEN': refresh_token}
            }
            if self.client_secret:
                kwargs['AuthParameters']['SECRET_HASH'] = self.get_secret_hash('')
            
            response = self.client.initiate_auth(**kwargs)
            return {
                'success': True,
                'access_token': response['AuthenticationResult']['AccessToken'],
                'id_token': response['AuthenticationResult']['IdToken']
            }
        except ClientError as e:
            return {'success': False, 'error': str(e)}

    def confirm_sign_up(self, username, confirmation_code):
        """Confirm user sign up with verification code"""
        try:
            kwargs = {
                'ClientId': self.client_id,
                'Username': username,
                'ConfirmationCode': confirmation_code
            }
            if self.client_secret:
                kwargs['SecretHash'] = self.get_secret_hash(username)
            
            self.client.confirm_sign_up(**kwargs)
            return {'success': True}
        except ClientError as e:
            return {'success': False, 'error': str(e)}