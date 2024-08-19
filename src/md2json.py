import json

def parse_markdown_to_json(markdown_content):
    lines = markdown_content.splitlines()
    result = {}
    stack = [result]  # 保留根节点
    current_section = None

    for line in lines:
        line = line.strip()

        if line.startswith('#'):
            # 计算标题的层级
            level = line.count('#')
            title = line.lstrip('#').strip()

            # 构建嵌套结构
            while len(stack) > level:
                stack.pop()

            current_section = {}
            stack[-1][title] = current_section
            stack.append(current_section)

        elif line:  # 当前行是正文内容
            if current_section is None:
                # 如果没有标题，直接添加内容
                stack[-1] = stack[-1].get("", "") + line + "\n"
            else:
                # 添加到当前标题对应的内容
                stack[-1]["content"] = stack[-1].get("content", "") + line + "\n"

    # 去除每个段落末尾的换行符
    def clean_content(d):
        for key, value in d.items():
            if isinstance(value, dict):
                clean_content(value)
            elif isinstance(value, str):
                d[key] = value.rstrip()

    clean_content(result)
    return result


# 文件路径
input_markdown_path = "../files/mdtest.md"
output_json_path = "../output/md.json"

# 从文件中读取 Markdown 内容
with open(input_markdown_path, "r", encoding="utf-8") as markdown_file:
    markdown_content = markdown_file.read()

# 解析 Markdown 并转换为 JSON
parsed_json = parse_markdown_to_json(markdown_content)

# 将结果保存为 JSON 文件
with open(output_json_path, "w", encoding="utf-8") as json_file:
    json.dump(parsed_json, json_file, ensure_ascii=False, indent=4)


