import json
import os

def parse_headings_and_content(lines):
    result = {}
    stack = [result]  # 保留根节点
    current_section = None
    previous_level = 0  # 用于跟踪上一个标题的层级
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()

        if line.startswith('```'):
            # 处理代码块
            code_block, i = parse_code_block(lines, i)
            if current_section is not None:
                if "code_blocks" not in current_section:
                    current_section["code_blocks"] = []
                current_section["code_blocks"].append(code_block)
        elif line.startswith('#'):
            level = line.count('#')
            title = line.lstrip('#').strip()

            # 如果当前标题是n+2级，而没有n+1级标题，自动补充n+1级为null
            if level > previous_level + 1:
                for l in range(previous_level + 1, level):
                    placeholder = {"content": None}
                    stack[-1][f"Level_{l}"] = placeholder
                    stack.append(placeholder)

            while len(stack) > level:
                stack.pop()

            current_section = {}
            stack[-1][title] = current_section
            stack.append(current_section)
            previous_level = level

        elif line.startswith('|'): # 处理表格
            table, i = parse_table(lines, i)
            if current_section is not None:
                if "tables" not in current_section:
                    current_section["tables"] = []
                current_section["tables"].append(table)
        elif line and not line.startswith('|'):
            if current_section is None:
                stack[-1]["content"] = stack[-1].get("content", "") + line
            else:
                current_section["content"] = current_section.get("content", "") + line
        i += 1

    return result, stack


def parse_code_block(lines, start_index):
    code_block = {"language": None, "code": ""}
    line = lines[start_index].rstrip()

    # 提取代码块语言
    if len(line) > 3:
        code_block["language"] = line[3:].strip()

    i = start_index + 1
    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith('```'):
            break
        code_block["code"] += line + "\n"
        i += 1

    return code_block, i

def parse_table(lines, start_index):
    columns = []
    data = []
    for i in range(start_index, len(lines)):
        line = lines[i].strip()
        if line.startswith('|'):
            if not columns:
                columns = [col.strip() for col in line.split('|') if col.strip()]
            else:
                stripped_line = line.replace('|', '').strip()
                if not all(c == '-' or c == ':' or c == ' ' for c in stripped_line):
                    data.append([cell.strip() for cell in line.split('|') if cell.strip()])
        else:
            break

    return {"columns": columns, "data": data}, i

def main():
    input_markdown_path = "../files/web api.md"
    output_json_path = os.path.join("../output", f"{os.path.splitext(os.path.basename(input_markdown_path))[0]}-md.json")

    with open(input_markdown_path, "r", encoding="utf-8") as markdown_file:
        markdown_content = markdown_file.read()

    lines = markdown_content.splitlines()
    result, _ = parse_headings_and_content(lines)

    # 将结果保存为 JSON 文件
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
