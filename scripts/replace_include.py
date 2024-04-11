#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

def replace_includes(file_path):
    # 正则表达式匹配 .. include:: 指令
    include_pattern = re.compile(r'^\.\. include::\s*(.*)$')

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            match = include_pattern.match(line.strip())
            if match:
                # 获取包含的文件路径
                include_file = match.group(1).strip()
                include_path = (Path(file_path).parent / include_file).resolve()

                if include_path.exists() and include_path.is_file():
                    included_content = replace_includes(include_path)
                    new_lines.extend(included_content)
                else:
                    print(f"Warning: Included file not found: {include_path}", file=sys.stderr)
            else:
                new_lines.append(line)

        return new_lines
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    # 遍历 git 暂存区中的所有 .rst 文件
    readme_file = "../docs/README.rst"

    if readme_file.endswith('.rst'):
        updated_content = replace_includes(readme_file)
        with open("../README.rst", 'w') as file:
            file.writelines(updated_content)

        # 重新加入 git 暂存区
        os.system(f'git add {readme_file}')

if __name__ == "__main__":
    main()
