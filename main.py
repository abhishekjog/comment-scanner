import os
import sys
from http import HTTPStatus
from typing import Optional, Tuple

import requests

GITHUB_API_BASE_URL = 'https://api.github.com'

def get_action_input(name: str, required: bool = False, default: Optional[str] = None) -> str:
    v = os.environ.get(f'INPUT_{name.upper()}', '')
    if v == '' and default:
        v = default
    if required and v == '':
        print_action_error(f'input required and not supplied: {name}')
        exit(1)
    return v

def delete(token, repo, comment_id) -> Tuple[str, str]:
    headers = {
        'Authorization': f'token {token}',
    }
    resp = requests.delete(
        f'{GITHUB_API_BASE_URL}/repos/{repo}/issues/comments/{comment_id}',
        headers=headers,
    )
    if resp.status_code != HTTPStatus.NO_CONTENT:
        print_action_error(f'cannot delete comment')
        print_action_debug(f'status code: {resp.status_code}')
        print_action_debug(f'response body: {resp.text}')
        exit(1)

def main():
    repo = os.environ['GITHUB_REPOSITORY']
    action_type = get_action_input('type', required=True)
    token = get_action_input('token', required=True)
    body = get_action_input('body', required=True)
    bad_text = get_action_input('bad_text', required=True)
    comment_id = get_action_input('comment_id')
    issue_number = get_action_input('issue_number')

    if bad_text in body:
        print_action_error(f"Found {bad_text} in comment. Disallowed!")
        _id, _body = delete(token, repo, comment_id)
        exit(1)
        
if __name__ == '__main__':
    main()
