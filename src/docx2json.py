import json
import docx
from simplify_docx import simplify

# 标记标题
def mark_titles(doc):
    for para in doc.paragraphs:
        if para.style.name.startswith('Heading'):
            level = para.style.name.split(' ')[-1]  # 获取标题级别
            para.add_run(f' [Title{level}]')  # 添加标记以便后续识别


# 二次处理-将标记的标题进行分级，并保留自然段落
def process_json_structure(data):
    result = {}
    stack = [result]

    for item in data['VALUE'][0]['VALUE']:
        if item['TYPE'] == 'paragraph':
            text = item['VALUE'][0]['VALUE']
            if '[Title' in text:
                # 提取标题级别和标题内容
                level = int(text.split('[Title')[-1][0])
                title = text.split('[Title')[0].strip()

                # 构建嵌套结构
                while len(stack) > level:
                    stack.pop()

                current_section = {"paragraphs": []}  # 保留自然段落
                stack[-1][title] = current_section
                stack.append(current_section)
            else:
                # 添加当前自然段落到当前标题下
                if 'paragraphs' in stack[-1]:
                    stack[-1]['paragraphs'].append(text.strip())
                else:
                    stack[-1]['paragraphs'] = [text.strip()]

    return result


# 读取
my_doc = docx.Document("../files/doctest.docx")

# 预处理-标记标题
mark_titles(my_doc)

# 将 docx 转换为 JSON
my_doc_as_json = simplify(my_doc)

# # 将初步生成的 JSON 数据写入中间文件
# with open("../output/intermediate_docx.json", "w", encoding="utf-8") as intermediate_json_file:
#     json.dump(my_doc_as_json, intermediate_json_file, ensure_ascii=False, indent=4)

# 二次处理-将 JSON 数据结构化为多级标题并保留自然段落
processed_json = process_json_structure(my_doc_as_json)

# final JSON
with open("../output/docx.json", "w", encoding="utf-8") as final_json_file:
    json.dump(processed_json, final_json_file, ensure_ascii=False, indent=4)

