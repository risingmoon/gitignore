#!/usr/bin/env python3
import argparse
import pathlib


def parse(snippet):
    parts = snippet.split(':')
    path = pathlib.Path(__file__).parent / 'snippets'

    folder = parts.pop(0)
    folder_path = path / folder
    assert folder_path.exists() is True, '%s is not supported' % folder
    paths = [path / folder / 'default.txt']

    for part in parts:
        file = '%s.txt' % part
        file_path = path / folder / file
        assert file_path.exists() is True, '%s submodule is not supported' % part
        paths.append(file_path)
    return paths


def generate(file_paths):
    content = []
    for path in file_paths:
        with open(path, 'r') as f:
            content.append(f.read())
    return content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('snippets', type=str, nargs='+')
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()

    file_paths = []
    for snippet in args.snippets:
        file_paths.extend(parse(snippet))
    content = generate(file_paths)
    lines = '\n\n'.join(content)

    if args.write:
        with open('.gitignore', 'w') as f:
            f.writelines(lines)
    else:
        print(lines)


if __name__ == '__main__':
    main()
