def print_play(lines):
    roles = []
    text_lines = []
    section = None
    
    for line in lines:
        stripped = line.strip()
        if stripped == "roles:":
            section = "roles"
        elif stripped == "textLines:":
            section = "text"
        else:
            if section == "roles" and stripped:
                roles.append(stripped)
            elif section == "text" and stripped:
                text_lines.append(line)
    
    sorted_roles = sorted(roles, key=len, reverse=True)
    role_dict = {role: [] for role in roles}
    
    for i, line in enumerate(text_lines, 1):
        for role in sorted_roles:
            if line.startswith(role + ":"):
                text = line[len(role) + 1:].lstrip()
                role_dict[role].append((i, text))
                break
    
    result = []
    for role in roles:
        if role_dict[role]:
            block = [f"{role}:"]
            for num, text in role_dict[role]:
                block.append(f"{num}) {text}")
            result.append("\n".join(block))
        else:
            result.append(f"{role}:")
    
    return "\n\n".join(result)

print(print_play("roles.txt"))