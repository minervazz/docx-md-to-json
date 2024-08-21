import json
import os

def parse_headings_and_content(lines):
    result = {}
    stack = [result]  # 保留根节点
    current_section = None

    for line in lines:
        line = line.strip()

        if line.startswith('#'):
            level = line.count('#')
            title = line.lstrip('#').strip()

            while len(stack) > level:
                stack.pop()

            current_section = {}
            stack[-1][title] = current_section
            stack.append(current_section)

        elif line and not line.startswith('|'):
            if current_section is None:
                # 如果没有标题，直接添加内容
                stack[-1] = stack[-1].get("", "") + line
            else:
                # 添加到当前标题对应的内容
                stack[-1]["content"] = stack[-1].get("content", "") + line

    return result, stack

def parse_table(lines, start_index):
    columns = []
    data = []
    for i in range(start_index, len(lines)):
        line = lines[i].strip()
        if line.startswith('|'):
            if not columns:
                # 解析表头
                columns = [col.strip() for col in line.split('|') if col.strip()]
            else:
                # 过滤掉表头标识符行
                stripped_line = line.replace('|', '').strip()
                if not all(c == '-' or c == ':' or c == ' ' for c in stripped_line):
                    # 解析表格数据行
                    data.append([cell.strip() for cell in line.split('|') if cell.strip()])
        else:
            break  # 表格结束

    return {"columns": columns, "data": data}, i



def main():
    input_markdown_path = "../files/Python基础.md"
    output_json_path = os.path.join("../output", f"{os.path.splitext(os.path.basename(input_markdown_path))[0]}-md.json")

    with open(input_markdown_path, "r", encoding="utf-8") as markdown_file:
        markdown_content = markdown_file.read()

    lines = markdown_content.splitlines()
    result, stack = parse_headings_and_content(lines)

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('|'):
            table, i = parse_table(lines, i)

            current_section = stack[-1]
            if "tables" not in current_section:
                current_section["tables"] = []
            current_section["tables"].append(table)
        elif line.startswith('#'):  # 遇到新标题，更新 current_section
            level = line.count('#')
            title = line.lstrip('#').strip()

            while len(stack) > level:
                stack.pop()

            current_section = {}
            stack[-1][title] = current_section
            stack.append(current_section)
        else:
            if "content" in stack[-1]:
                stack[-1]["content"] += line
            else:
                stack[-1]["content"] = line
        i += 1

    # 将结果保存为 JSON 文件
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
