import json


def run(args):
    print(generate_diff(args.first_file, args.second_file, format='string'))


def generate_diff(first_path, second_path, format=''):
    diff = []

    data_before = json.load(open(first_path))
    data_after = json.load(open(second_path))

    keys_before = data_before.keys()
    keys_after = data_after.keys()
    all_keys = list(set(list(keys_before) + list(keys_after)))
    all_keys.sort()

    added_keys = keys_after - keys_before
    deleted_keys = keys_before - keys_after
    common_keys = keys_before & keys_after

    for key in all_keys:
        template = '  {symbol} {key}: {value}'

        if key in added_keys:
            diff.append(template.format(
                symbol='+', key=key, value=data_after[key]
                )
            )
        elif key in deleted_keys:
            diff.append(template.format(
                symbol='-', key=key, value=data_before[key]
                )
            )
        elif key in common_keys and (data_before[key] == data_after[key]):
            diff.append(template.format(
                symbol=' ', key=key, value=data_before[key]
                )
            )
        else:
            diff.append(template.format(
                symbol='-', key=key, value=data_before[key]
                )
            )
            diff.append(template.format(
                symbol='+', key=key, value=data_after[key]
                )
            )

    return '{\n' + '\n'.join(diff) + '\n}'
