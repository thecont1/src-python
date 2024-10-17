import csv
import json

json_file = "/Users/home/Downloads/Haryana.json"

with open(json_file, 'r') as f_read:
    table = f_read.readlines()[0][2:-2].replace(', {"source_url":', '\n{"source_url":').split('\n')
    csv_file = json_file.replace('.json', '.csv')
    with open(csv_file, 'w') as f_write:
        fieldnames = ['state', 'constituency', 'serial_no', 'candidate', 'party', 'evm_votes', 'postal_votes']
        writer = csv.DictWriter(f_write, fieldnames=fieldnames)
        writer.writeheader()
        for row in table:
            for candidate in sorted(json.loads(row)['voting_data']['voting_tally']):
                candidate['state'] = 'Haryana'
                candidate['constituency'] = json.loads(row)['voting_data']['assembly_constituency']
                writer.writerow(candidate)

