import os
from dotenv import load_dotenv

from PyInquirer import style_from_dict, Token

load_dotenv()

command_style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
MAX_RESULTS = 10
