def solve_theater_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = f.read()
    except FileNotFoundError:
        return f"Ошибка: Файл '{file_path}' не найден."
    except Exception as e:
        return f"Произошла ошибка при чтении файла: {e}"

    lines = raw_data.splitlines()

    roles_list = []
    script_lines = []
    is_script = False
    for raw_line in lines:
        current_line = raw_line
        line_lstrip = current_line.lstrip()
        if line_lstrip.startswith('['):
            end_bracket_index = line_lstrip.find(']')
            if end_bracket_index != -1 and line_lstrip[1:].startswith('source:'):
                current_line = line_lstrip[end_bracket_index + 1:].lstrip()
            else:
                current_line = raw_line

        line_stripped = current_line.strip()
        if not line_stripped:
            continue
        if line_stripped == "roles:":
            continue
        if line_stripped == "textLines:":
            is_script = True
            continue

        if not is_script:
            roles_list.append(line_stripped)
        else:
            script_lines.append(current_line)
    roles_dict = {role: [] for role in roles_list}
    roles_sorted = sorted(roles_list, key=len, reverse=True)
    current_active_role = None
    for i, line in enumerate(script_lines, 1):
        line_content = line
        role_found_in_this_line = False
        for role in roles_sorted:
            prefix = role + ":"
            if line_content.lstrip().startswith(prefix):
                current_active_role = role
                content_after_strip = line_content.lstrip()
                text_part = content_after_strip[len(prefix):].lstrip()
                roles_dict[role].append((i, text_part.rstrip()))
                role_found_in_this_line = True
                break
        if not role_found_in_this_line:
            if current_active_role:
                roles_dict[current_active_role].append((i, line_content.strip()))
    output = []
    for role in roles_list:
        output.append(f"{role}:")
        for num, text in roles_dict[role]:
            output.append(f"{num}) {text}")
        output.append("")
    return "\n".join(output).strip()
file_to_process = "roles.txt"

result = solve_theater_from_file(file_to_process)
print(result)