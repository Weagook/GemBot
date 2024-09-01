def parse_arguments(args: str):
    """Функция для парсинга аргументов."""
    inviter_id = None
    tag = None
    
    if args:
        parts = args.split('and')
        for part in parts:
            if part.startswith('inviter_id'):
                inviter_id = part.replace('inviter_id', '')
            elif part.startswith('tag_'):
                tag = part.replace('tag_', '')
    
    return inviter_id, tag