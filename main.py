#!/usr/bin/env python
"""
Hooks Generator for Git
This tool simplifies creating Git hooks from a template.

Copyright (C) 2024  worstprgr  github.com/worstprgr  p-trace.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys
import os
import argparse
from dataclasses import dataclass, asdict
from argparse import RawTextHelpFormatter
from pathlib import Path

from prereceive import TemplatePreReceive


@dataclass
class Hooks:
    # APPLYPATCH_MSG: str = 'applypatch-msg'
    # COMMIT_MSG: str = 'commit-msg'
    # FSMONITOR_WATCHMAN: str = 'fsmonitor-watchman'
    # POST_UPDATE: str = 'post-update'
    # PRE_APPLYPATCH: str = 'pre-applypatch'
    # PRE_COMMIT: str = 'pre-commit'
    # PRE_MERGE_COMMIT: str = 'pre-merge-commit'
    # PRE_PUSH: str = 'pre-push'
    # PRE_REBASE: str = 'pre-rebase'
    PRE_RECEIVE: str = 'pre-receive'
    # PREPARE_COMMIT_MSG: str = 'prepare-commit-msg'
    # PUSH_TO_CHECKOUT: str = 'push-to-checkout'
    # SENDEMAIL_VALIDATE: str = 'sendemail-validate'
    # UPDATE: str = 'update'


class ArgParser:
    def __init__(self) -> None:
        self.programm_file_name = os.path.basename(__file__)

        self.__hooks = asdict(Hooks())

        self.__description = ''
        self.__epilog = f'Type `{self.programm_file_name} help hooks` to display all supported hooks.'
        self.__help_hook = ''
        self.__help_repo_path = ''
        self.__help_target_branch = ''

        self.__parser = argparse.ArgumentParser(description=self.__description, epilog=self.__epilog,
                                                formatter_class=RawTextHelpFormatter)
        self.__parser.add_argument('hook', type=str, help=self.__help_hook)
        self.__parser.add_argument('repository_path', type=str, help=self.__help_repo_path)
        self.__parser.add_argument('--target-branch', '--tb', type=str, help=self.__help_target_branch)

        self.__args = self.__parser.parse_args()
        self.hook = self.__args.hook
        self.repository_path = self.__args.repository_path
        self.target_branch = self.__args.target_branch

        if self.hook == 'help' and self.repository_path == 'hooks':
            print('Displaying all supported Git hooks:')
            for v in self.__hooks.values():
                print('    ', v)
            sys.exit(0)


class Generator:
    def __init__(self) -> None:
        self.hooks = Hooks()
        self.argx = ArgParser()

        self.hooks_fp: Path = Path(self.argx.repository_path) / 'hooks'

    def generate(self) -> None:
        if not self.hooks_fp.exists():
            print(f'[ERROR]: Directory is missing -> {self.argx.repository_path}')
            sys.exit(1)

        hook = self.argx.hook

        if not hook:
            raise Exception('Hook Param empty')

        content: list[str] = []
        hook = hook.lower()

        if hook == self.hooks.PRE_RECEIVE:
            content = TemplatePreReceive(self.argx.target_branch).build()
        else:
            print(f'[Error]: Unkown argument. Type `python {self.programm_file_name} help hooks` for all possible options')
            sys.exit(1)

        if not content:
            raise Exception('Template content empty')

        with open(self.hooks_fp / hook, 'w+', encoding='utf8') as f:
            f.writelines(content)


if __name__ == "__main__":
    Generator().generate()

