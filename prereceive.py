from basetemplate import BaseTemplate


class TemplatePreReceive(BaseTemplate):
    def __init__(self, protect_branch: str) -> None:
        super().__init__()
        self.branch_to_protect = protect_branch

    def build(self) -> list[str]:
        return self.add_line_sep(self.protect_branch())

    def protect_branch(self) -> list[str]:
        ERR_CANNOT_PUSH = 'Cannot push to a protected branch!'
        return [
            '#!/bin/bash',
            '',
            '# Hook: pre-receive',
            '',
            f'protected_branch="{self.branch_to_protect}"',
            '',
            'while read oldrev newrev refname; do',
            '    if [[ "$refname" =~ ^refs/heads/ ]]; then',
            '        branch_name=${refname#refs/heads/}',
            '        if [[ "$branch_name" == "$protected_branch" ]]; then',
            f'            echo "{self.error_message(ERR_CANNOT_PUSH)}"',
            '            exit 1',
            '        fi',
            '    fi',
            'done',
            '',
            'exit 0'
        ]


